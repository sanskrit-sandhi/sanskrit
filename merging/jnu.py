# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup
import requests
import os
import sys
import re
jnuUrl = 'http://sanskrit.jnu.ac.in/sandhi/gen.jsp#results'

def getHTMLData(name, url, type, words):
    out = open(name+'_'+type+'.html','w')
    #print url+word
    headers = { 'Accept-Charset': 'UTF-8'}
    data = {'itext':words,'itrans':'','lastChar':''}
    resp = requests.post(url, params=data, headers=headers)
    #print resp.text
    out.write("url: "+url)
    out.write("headers: "+str(data))
    out.write(resp.text.encode("utf-8"))
    out.close()
    return resp.text

def writeToFile(merged, split, san, out, result, rule, id):
    out.write(id+':'+merged+':')
    for sa in split:
        out.write(sa+',')
    out.write(':')
    if san != None:
        out.write(san+',')
    else:
        out.write(',')
    out.write(':'+rule+':'+result+'\n')

def jnuParse(data):
    if data != None:
        soup = BeautifulSoup(data)
        if soup != None:
            for result in  soup.findAll('a', {"name": "results"}):
                sandhi = result.getText().encode("utf-8")
                return sandhi
    return ''					

def getMerged(id, word1, word2, parentDir):
    jnuData = getHTMLData(os.path.join(parentDir,id),jnuUrl,'.jnu', word1+'+'+word2)
    if jnuData != None:
        return jnuParse(jnuData)
    return ''

def getRecMerge(id, word, list, parentDir):
    if list and len(list) > 0:
        result = getMerged(id, word, list[0], parentDir)
        i = 0;
        if(len(list[1:]) > 0):
            i=i+1
            result = getRecMerge(id+'_'+str(i), result, list[1:], parentDir)
        return result

def compareResult(merged, split, result, out, rule, id):
    if merged == result:
        writeToFile(merged, split, result, out, '1', rule, id)
    else:
        writeToFile(merged, split, result, out, '0', rule, id) 

def processFile(filePath):
    if os.path.isfile(filePath):
        parentDir = os.path.dirname(os.path.abspath(filePath))
        parentDir = os.path.join(parentDir,sys.argv[1]+'_output')
        if not os.path.exists(parentDir):
            os.makedirs(parentDir)
        jnuOut = open(filePath+'.jnu','w')
        for word in open(filePath).readlines():
            word = word.strip().split(',')
            print word[0]
            wordSplit = word[2].replace('"','').split('+')
            merged = word[1].replace(',','')
            result = getRecMerge(word[0], wordSplit[0], wordSplit[1:], parentDir)

            compareResult(merged, wordSplit, result, jnuOut,  word[3].strip(), word[0].strip())
                   
        jnuOut.close()


def processFolder(folderPath):
    if os.path.isdir(folderPath):
        for path in os.listdir(folderPath):
            print os.path.join(folderPath, path)
            processFolder(os.path.join(folderPath, path))
    else:
        processFile(folderPath)


def main():
    path = sys.argv[1]
    processFolder(path)

if __name__ =="__main__":
    main()

