# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup
import urllib2
import requests
import os
import sys
import re
import codecs

def htmlTodev(text):
    def fixup(m):
        text = m.group(0)
        if text[:2] == "&#":
            # character reference
            try:
                if text[:3] == "&#x":
                    return unichr(int(text[3:-1], 16))
                else:
                    return unichr(int(text[2:-1]))
            except ValueError:
                pass
        else:
            # named entity
            try:
                text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
            except KeyError:
                pass
        return text # leave as is
    return re.sub("&#?\w+;", fixup, text)


def devToVel(value):
    inHex = [ "05", "06", "07", "08", "09", "0a", "0b", "60", "0c", "0f", "10", "13", "14", "02", "01", "03", "3d", "4d" ]
    outVH = [ "a", "aa", "i", "ii", "u", "uu", ".r", ".rr", ".l", "e", "ai", "o", "au", ".m", "~l", ".h", "'", "" ]
    matIn = [ "3e", "3f", "40", "41", "42", "43", "44", "62", "47", "48", "4b", "4c" ]
    consIn = [ "15", "16", "17", "18", "19", "1a", "1b", "1c", "1d", "1e", "1f", "20", "21", "22", "23", "24", "25", "26", "27", "28", "2a", "2b", "2c", "2d", "2e", "2f", "30", "32", "35", "36", "37", "38", "39", "00" ]
    orig = value.strip().decode("utf-8")
    output = ""
    wasCons = False
    for i in range(len(orig)):
    
        origC = orig[i]
        l = "{0:04x}".format(ord(origC))
        
        lenL = len(l)
        if lenL == 0:
            l = "0000"
        if lenL == 1:
            l = "000" + l
        if lenL == 2:
            l = "00" + l
        if lenL == 3:
            l = "0" + l
        check = l[2:]
        init = l[0:2]
        
        if not init == "09":
            check = "00"

        consOut = [ "k", "kh", "g", "gh", "f", "c", "ch", "j", "jh", "~n", ".t", ".th", ".d", ".dh", ".n", "t", "th", "d", "dh", "n", "p", "ph", "b", "bh", "m", "y", "r", "l", "v", "z", ".s", "s", "h", origC + "" ]
        for j in range (len(inHex)):
            if check == inHex[j]:
                if check == "03" or check == "01" or check == "02" or check == "3d":
                    if wasCons:
                        output = output+"a" + outVH[j]
                    else:
                        output = output+outVH[j]
                else:
                    output = output+outVH[j]
                wasCons = False
        for j in range (len(consIn)):
            if check == consIn[j]:
                if wasCons:
                    output = output+"a" + consOut[j]
                else:
                    output = output+consOut[j]
                if not check == "00":
                    wasCons = True
                else:
                    wasCons = False
                if i == len(orig) - 1:
                    output = output+"a"
        for j in range (len(matIn)):
            if check == matIn[j]:
                output = output+outVH[j + 1]
                wasCons = False
    return output

def getHTMLData(name, url, type):
    out = open(name+'_'+type+'.html','w')
    #print url+word
    resp = requests.get(url)
    #print resp.text
    out.write('url: '+url.encode('utf-8'))
    out.write(resp.text.encode('utf-8'))
    out.close()
    return resp.text

def writeToFile(merged, split, san, out, result, rule, id):
    out.write(id+':'+merged+':')
    for sa in split:
        out.write(sa+',')
    out.write(':')
    out.write(san+',')
    out.write(':'+rule+':'+result+'\n')

def inriaParse(data, merged, split, out, rule, id):
    if data != None and split != None:
        sandhi = [];
        split = split.strip().strip(',').split('+')
        soup = BeautifulSoup(data)
        if soup != None and len(soup.findAll('span', {"class": "devared", "lang": "sa"})) == 3:
            #result = soup.findAll('span', {"class": "red"})[2].getText()
            result = htmlTodev(soup.findAll('span', {"class": "devared", "lang": "sa"})[2].getText()).encode('utf-8')
            #result = str(BeautifulStoneSoup(result.decode("latin-1").encode("utf-8"), convertEntities=BeautifulStoneSoup.ALL_ENTITIES))
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
        inrOut = open(filePath+'.ext.inria','w')
        inrFilOut = open(filePath+'.int.inria','w')
        for word in open(filePath).readlines():
            word = word.strip().split(',')
            print word[0]
            inrFilData = getHTMLData(os.path.join(parentDir,word[0]),'http://sanskrit.inria.fr/cgi-bin/SKT/sktsandhier?lex=SH&l='+devToVel(word[2].replace('"','').split('+')[0].strip())+'&r='+devToVel(word[2].replace('"','').split('+')[1].strip())+'&t=VH&k=internal','int.inr')
            inrData = getHTMLData(os.path.join(parentDir,word[0]),'http://sanskrit.inria.fr/cgi-bin/SKT/sktsandhier?lex=SH&l='+devToVel(word[2].replace('"','').split('+')[0].strip())+'&r='+devToVel(word[2].replace('"','').split('+')[1].strip())+'&t=VH&k=external','ext.inr')
            if inrData != None:
                inriaParse(inrData, word[1].replace(',',''), word[2].replace('"',''), inrOut, word[3].strip(),word[0].strip())
            if inrFilData != None:
                inriaParse(inrFilData, word[1].replace(',',''), word[2].replace('"',''), inrFilOut, word[3].strip(),word[0].strip())
        inrOut.close()

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

