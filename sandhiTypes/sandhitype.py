
# -*- coding: utf-8 -*-

def isVowelChar(alphabet):
    if alphabet == u'अ' or alphabet == u'आ'  or alphabet ==  u'इ' or alphabet ==  u'ई'  or alphabet ==  u'उ' or alphabet ==  u'ऊ' or alphabet ==  u'ऋ' or alphabet ==  u'ॠ' or alphabet ==  u'ऌ' or alphabet ==  u'ॡ' or alphabet ==  u'ए' or alphabet ==  u'ऐ' or alphabet ==  u'ओ' or alphabet ==  u'औ' or alphabet ==  u'अं' or alphabet ==  u'अः' or alphabet ==  u'अँ':
        return True
    return False

def isEndsWithVowel(value):
    word = value.strip().decode("utf-8")
    last = len(word) - 1
    if isVowelChar(word[last]):
        return True
    return False


def isEndsWithVisarga(value):
    word = value.strip().decode("utf-8")
    last = len(word) - 1
    print word[last], type(word[last]), u'ः', type(u'ः')
    if word[last] == u'ः':
    	return True
    return False


def isVowelSandhi(word1, word2):
	if isEndsWithVowel(word1) and isStartsWithVowel(word2):
		return True

def isVisargaSandhi(word):
    if isEndsWithVisarga(word):
        return True

def isCumVowel(arr):
    result = True;
    if len(arr) > 0:
        for i in arr:
            result = result and i
        return result
    return False



def sandhiType(words):
    words = words.strip().split('+');
    isVowel = []
    isViserga = []
    print len(words)
    for i in range(len(words)):
        if i<len(words)-1:
            word1 = words[i].strip()
            word2 = words[i+1].strip()
            print word1, word2
            isVowel.append(isVowelSandhi(word1, word2))
            isViserga.append(isVisargaSandhi(word1))
    print isCumVowel(isVowel)
    print isCumVowel(isViserga)

print sandhiType('एव+इत्यादि')
