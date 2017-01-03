from __future__ import absolute_import
from __future__ import print_function

import os, io, re, json
import random

import numpy as np
import theano

from keras.preprocessing import sequence, text
from keras.optimizers import SGD, RMSprop, Adagrad
from keras.utils import np_utils, generic_utils
from keras.models import Sequential
from keras.layers.embeddings import Embedding
from keras.layers.core import Reshape
from keras.layers.core import Merge
from keras.models import load_model

import six.moves.cPickle
from six.moves import range
from six.moves import zip

max_features = 159970  # vocabulary size most common words in data
second_max_features = 500
skip_top = 100  # ignore top 100 most common words
nb_epoch = 1
dim_proj = 256  # embedding space dimension

save = True
load_model_flag = False
load_tokenizer = False
train_model = True
save_dir = os.path.expanduser("~/.keras/models")

model_load_fname = "sankritSandhi_skipgram_model.pkl"
model_save_fname = "sankritSandhi_skipgram_model.pkl"
sandhiData_fname = "sankritSandhi_data.pkl"

trainTestData_fname = "sandhiTrainTestData.pkl"

raw_data_path = "./all.examples.txt.slp"


word_count = 2 
max_split = 0 
split_count = 0 
sandhiData_dict = {"rootWords":set(), "compoundWords":set(), "sandhi":{}, "index":{}}


# model management
if os.path.isfile(os.path.join(save_dir, sandhiData_fname)):
# if load_tokenizer:
    print('Loading sandhi data...')
    sandhiData = six.moves.cPickle.load(open(os.path.join(save_dir, sandhiData_fname), 'rb'))
    
else:
    print("Getting sandhi data from file...")

    rawData = io.open(raw_data_path,"r",encoding='utf8')
    for line in rawData.readlines():
        sandhiWords = line.strip().split(',')
        compoundWord = sandhiWords[0]
        rootWords = sandhiWords[1].split('+')
        sandhiData_dict["compoundWords"].add(compoundWord) 
        sandhiData_dict["sandhi"][compoundWord] = rootWords

        sandhiData_dict["index"][compoundWord] = word_count

        max_split = max(max_split,len(rootWords))
        word_count = word_count + 1
        split_count = split_count + len(rootWords) 

        if(word_count % 1000 == 0):
                    print("Word Count-", word_count,"  Max Split-", max_split )

        for rw in rootWords:
            sandhiData_dict["rootWords"].add(rw)
            if rw not in sandhiData_dict["index"].keys():
                sandhiData_dict["index"][rw] = word_count
                word_count = word_count + 1 
                if(word_count % 1000 == 0 ):
                    print("Word Count-", word_count,"  Max Split-", max_split )
    
    print("Total Word Count -", word_count)
    print("Max Split -", max_split)
    print("Average Split -", (split_count*1.0)/word_count)     

    sandhiData = sandhiData_dict
    if save:
        print("Save sandhi data...")
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        six.moves.cPickle.dump(sandhiData_dict, open(os.path.join(save_dir, sandhiData_fname), "wb"))



print("Root words -- ",len(sandhiData["rootWords"]))
print("Compound words -- ",len(sandhiData["compoundWords"]))
print("Sandhi words -- ",len(sandhiData["sandhi"]))
print("Index words -- ",len(sandhiData["index"])) 

training_sandhi = set()
validation_sandhi = set()
test_sandhi = set()

# training process
model = None
if train_model:
    if os.path.isfile(os.path.join(save_dir, model_load_fname)):
        print('Load model...')
        model = load_model(os.path.join(save_dir, model_load_fname))
        print('Load dataset...')
        sandhiDataset = six.moves.cPickle.load(open(os.path.join(save_dir, trainTestData_fname), 'rb'))
        training_sandhi = sandhiDataset["training"]
        test_sandhi = sandhiDataset["test"]
        validation_sandhi = sandhiDataset["validation"]

    else:
        print('Build model...')
        sandhi_count = 0 
        for i in sandhiData["sandhi"].keys(): 
            sandhi_count = sandhi_count + 1 
            if(sandhi_count % 10 == 0):
                test_sandhi.add(i)
            else:
                training_sandhi.add(i)

        sandhi_count = 0 
        for i in training_sandhi:
            sandhi_count = sandhi_count + 1 
            if(sandhi_count % 5 == 0):
                validation_sandhi.add(i)

        sandhiDataset = {"training":training_sandhi, "test":test_sandhi, "validation":validation_sandhi}
        six.moves.cPickle.dump(sandhiDataset, open(os.path.join(save_dir, trainTestData_fname), "wb"))


        ### Model Intialization
        model = Sequential()

        # Models Array 
        models = []

        # Word vectors
        dims=[second_max_features]
        model_word = Sequential()
        
        model_word.add(Embedding(max_features, second_max_features, input_length=1))
        rs = Reshape(dims)
        model_word.add(rs)
        models.append(model_word)

        # Context vectors
        model_context = Sequential()

        model_context.add(Embedding(max_features, second_max_features, input_length=1))
        model_context.add(Reshape(dims))
        models.append(model_context)

        # Combined model
        model = Sequential()
        model.add(Merge(models, mode='dot'))
        
        model.compile(loss='mse', optimizer='rmsprop')

        for e in range(nb_epoch):
            print('-' * 40)
            print('Epoch', e)
            print('-' * 40)

            progbar = generic_utils.Progbar(max_features)
            samples_seen = 0
            losses = []

            input_vec = []
            output_vec = []
            context_vec = []
            sandhi_count = 0

            for i in training_sandhi:

                sandhi_count = sandhi_count + 1 

                for cw in sandhiData["sandhi"][i]:
                    input_vec.append(sandhiData["index"][i])
                    context_vec.append(sandhiData["index"][cw])
                    output_vec.append(1)

                negativeSamples = set(random.sample(sandhiData["rootWords"], 5))
                while len(negativeSamples.intersection(sandhiData["sandhi"][i])):
                    negativeSamples = set(random.sample(sandhiData["rootWords"], 5))

                for ncw in negativeSamples:
                    input_vec.append(sandhiData["index"][i])
                    context_vec.append(sandhiData["index"][ncw])
                    output_vec.append(0)

                if sandhi_count % 200 == 0:

                    ### one gradient update per 20 compound words
                    print( "Mini batch of 200", sandhi_count / 200)
                    X = np.array(input_vec, dtype="int32")
                    Y = np.array(context_vec, dtype="int32")
                    labels = output_vec 

                    loss = model.train_on_batch([X,Y], labels)
                    losses.append(loss)
                    samples_seen += len(labels)

                    input_vec = []
                    output_vec = []
                    context_vec = []

                if sandhi_count % 2000 == 0:
                    print( "Processed 10 batch of 200", sandhi_count / 2000 ,"Mean Loss --", np.mean(losses))
                    # progbar.update(i, values=[("loss", np.mean(losses))])
                    losses = []
                    break

            print('-' * 15,'Epoch', e, "completed", '-' * 15)
            print('Samples seen:', samples_seen)

            if sandhi_count % 200 != 0:
                print( "Last batch of 200")
                X = np.array(input_vec, dtype="int32")
                Y = np.array(context_vec, dtype="int32")
                labels = output_vec 

                loss = model.train_on_batch([X,Y], labels)
                losses.append(loss)
                samples_seen += len(labels)

                print( "Model Mean Loss--", np.mean(losses))
                losses = []

            # score = model.evaluate(X Y_test, verbose=0)
            # print('Test accuracy:', score[1])

        print("Training completed!")

        if save:
            print("Saving model...")
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
            model.save(os.path.join(save_dir, model_save_fname))


print("Length of training set", len(training_sandhi))
print("Length of testing set", len(test_sandhi))
print("It's test time!")

# recover the embedding weights trained with skipgram:
weights = model.layers[0].get_weights()

# # we no longer need this
# del model
model.compile(loss='mse', optimizer='rmsprop')

# weights[:skip_top] = np.zeros((skip_top, dim_proj))
norm_weights = np_utils.normalize(weights)

reverse_sandhi_index = dict([(v, k) for k, v in sandhiData["index"].items()])
word_index = sandhiData["index"]

def embed_word(w):
    i = word_index.get(w)
    if (not i) or (i >= max_features):
        return None
    return norm_weights[i]

def closest_to_point(point, nb_closest=10):
    proximities = np.dot(norm_weights, point)
    tups = list(zip(list(range(len(proximities))), proximities))
    tups.sort(key=lambda x: x[1], reverse=True)
    return [(reverse_sandhi_index.get(t[0]), t[1]) for t in tups[:nb_closest]]


def closest_to_word(w, nb_closest=10):
    i = word_index.get(w)
    if (not i) or (i >= max_features):
        return []
    return closest_to_point(norm_weights[i].T, nb_closest)

test_count = 0 
for test_word in test_sandhi:
    test_count = test_count + 1
    if(test_count == 2):
        break
    print(model.predict([sandhiData["index"][test_word]], batch_size=1))
    # res = closest_to_word(test_word)
    # print('====', test_word)
    # for r in res:
    #     print(r)


''' the resuls in comments below were for:
    5.8M HN comments
    dim_proj = 256
    nb_epoch = 2
    optimizer = rmsprop
    loss = mse
    max_features = 50000
    skip_top = 100
    negative_samples = 1.
    window_size = 4
    and frequency subsampling of factor 10e-5.
'''