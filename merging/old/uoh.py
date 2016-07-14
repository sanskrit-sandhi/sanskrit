# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup
import requests
import os
import sys
import re
uohUrl = 'http://sanskrit.uohyd.ac.in/cgi-bin/scl/sandhi/sandhi.cgi?encoding=Unicode&text='

def getHTMLData(name, url, type):
    out = open(name+'_'+type+'.html','w')
    #print url+word
    resp = requests.get(url)
    #print resp.text
    out.write("url: "+url)
    out.write(resp.text.encode("utf-8"))
    out.close()
    return resp.text

def writeToFile(merged, split, san, out, result, rule, id):
    out.write(id+':'+merged+':')
    for sa in split:
        out.write(sa+',')
    out.write(':')
    out.write(san+',')
    out.write(':'+rule+':'+result+'\n')

def uohParse(data):
    if data != None:
        soup = BeautifulSoup(data)
        if soup != None:
            if(len(soup.findAll('table')) > 0):
                sandhi = soup.findAll('table')[0].findAll('tr')[1].findAll('td')[2].getText().encode("utf-8")
                return sandhi
    return ''					

def getMerged(id, word1, word2, parentDir):
    uohData = getHTMLData(os.path.join(parentDir,id),uohUrl+word1.strip()+'&text1='+word2.strip(),'uoh')
    if uohData != None:
        return uohParse(uohData)
    return ''

def getRecMerge(id, word, list, parentDir):
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
        uohOut = open(filePath+'.uoh','w')
        for word in open(filePath).readlines():
            word = word.strip().split(',')
            print word[0]
            wordSplit = word[2].replace('"','').split('+')
            merged = word[1].replace(',','')
            result = getRecMerge(word[0], wordSplit[0], wordSplit[1:], parentDir)

            compareResult(merged, wordSplit, result, uohOut,  word[3].strip(), word[0].strip())
                   
        uohOut.close()


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

