# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup
import urllib2
import requests
import os
import sys
import re
jnuUrl = 'http://sanskrit.jnu.ac.in/sandhi/viccheda.jsp?itext='
inriaUrl = 'http://sanskrit.inria.fr/cgi-bin/SKT/sktreader?t=VH;lex=SH;cache=f;st=t;us=f;cp=t;text='
samasnidhiUrl = 'http://52.25.246.194/cgi-bin/scl/sandhi_splitter/sandhi_splitter.cgi?encoding=Unicode&sandhi_type=s&word='

def getHTMLData(name, url, type):
    out = open(name+'_'+type+'.html','w')
    #print url+word
    resp = requests.get(url)
    #print resp.text
    out.write(resp.text.encode("utf-8"))
    out.close()
    return resp.text

def writeToFile(merged, split, san, out, result, rule, id):
    out.write(id+':'+merged+':')
    for sa in split:
        out.write(sa+',')
    out.write(':')
    for sa in san:
        out.write(sa+',')
    out.write(':'+rule+':'+result+'\n')

def jnuParse(data, merged, split, out, rule, id):
    if data != None and split != None:
        split = split.strip().strip(',').split('+')
        soup = BeautifulSoup(data)
        if soup != None:
            for result in  soup.findAll('a', {"name": "results"}):
                sandhi = result.getText().encode("utf-8")
                sandhi = sandhi.replace("Results","").strip().split(')')
                for san in sandhi:
                    san = san.split('(')[0].split()
                
                    if split == san:
                        writeToFile(merged, split, san, out, '1', rule, id)
                    else:
                        writeToFile(merged, split, san, out, '0', rule, id)
						
def inriaParse(data, merged, split, out, rule, id):
    if data != None and split != None:
        sandhi = [];
        split = split.strip().strip(',').split('+')
        soup = BeautifulSoup(data)
        if soup != None:
            for result in  soup.findAll('span'):
                for attr in result.attrs:
                    if 'title' in attr:
                        if attr[1].encode("utf-8") == 0 or attr[1].encode("utf-8") == '0' and len(sandhi) != 0:
                            if split == sandhi:
                                writeToFile(merged, split, sandhi, out, '1', rule, id)
                            else:
                                writeToFile(merged, split, sandhi, out, '0', rule, id)
                            sandhi = [];
                        sandhi.append(str(BeautifulStoneSoup(result.getText().decode("latin-1").encode("utf-8"), convertEntities=BeautifulStoneSoup.ALL_ENTITIES))) 
        if len(sandhi) != 0:
            if split == sandhi:
                writeToFile(merged, split, sandhi, out, '1', rule, id)
            else:
                writeToFile(merged, split, sandhi, out, '0', rule, id)  
                        #print attr[0].encode("utf-8"), attr[1].encode("utf-8")
                        #print result.getText().decode("latin-1").encode("utf-8")
						
def samasnidhiParse(data, merged, split, out, rule, id):
    if data != None and split != None:
        split = split.strip().strip(',').split('+')
        data = re.sub(r'title = "(.+?)"', r'', data)
        soup = BeautifulSoup(data)
        if soup != None:
            if(len(soup.findAll('div')) > 0):
                sandhi = []
                #out.write(str(soup.findAll('div', {"id": "finalout"})[0]));
                sandhis = str(soup.findAll('div', {"id": "finalout"})[0].getText().encode("utf-8")).strip().split('true;')[2].replace('}','').strip()
                for result in  sandhis.split('/'):
                    if result != "" or result != " ": 
                        if '>' in result and len(result.strip().split('">')) > 1:
                            result = result.strip().split('">')[1]
                        sandhi = result.strip().split('+')
                        if split == sandhi:
                            writeToFile(merged, split, sandhi, out, '1', rule, id)
                        else:
                            writeToFile(merged, split, sandhi, out, '0', rule, id)

def samasnidhiFilParse(data, merged, split, out, rule, id):
    if data != None and split != None:
        split = split.strip().strip(',').split('+')
        data = re.sub(r'title = "(.+?)"', r'', data)
        soup = BeautifulSoup(data)
        if soup != None:
            if(len(soup.findAll('div')) > 0):
                sandhi = []
                #out.write(str(soup.findAll('div', {"id": "finalout"})[0]));
                sandhis = str(soup.findAll('div', {"id": "finalout"})[0].getText().encode("utf-8")).strip().split('true;')[0].split('function')[0].replace('}','').strip()
                for result in  sandhis.split('/'):
                    if result != "" or result != " ": 
                        if '>' in result and len(result.strip().split('">')) > 1:
                            result = result.strip().split('">')[1]
                        sandhi = result.strip().split('+')
                        if split == sandhi:
                            writeToFile(merged, split, sandhi, out, '1', rule, id)
                        else:
                            writeToFile(merged, split, sandhi, out, '0', rule, id)

def processFile(filePath):
    if os.path.isfile(filePath):
        parentDir = os.path.dirname(os.path.abspath(filePath))
        parentDir = os.path.join(parentDir,'output')
        if not os.path.exists(parentDir):
            os.makedirs(parentDir)
        jnuOut = open(filePath+'.jnu','w')
        samOut = open(filePath+'.sam','w')
        samFilOut = open(filePath+'.sam.fil','w')
        inrOut = open(filePath+'.inria','w')
        inrFilOut = open(filePath+'.inria.fil','w')
        for word in open(filePath).readlines():
            word = word.strip().split(',')
            jnuData = getHTMLData(os.path.join(parentDir, word[0]),jnuUrl+word[1].replace(',',''), 'jnu')
            samData = getHTMLData(os.path.join(parentDir,word[0]),samasnidhiUrl+word[1].replace(',',''), 'sam')
            if jnuData != None:
                jnuParse(jnuData, word[1].replace(',',''), word[2].replace('"', ''), jnuOut, word[3].strip(), word[0].strip())
            if samData != None:
                samasnidhiParse(samData, word[1].replace(',',''), word[2].replace('"',''), samOut, word[3].strip(), word[0].strip())
                samasnidhiFilParse(samData, word[1].replace(',',''), word[2].replace('"',''), samFilOut, word[3].strip(), word[0].strip())
        for word in open(filePath+'.vel').readlines():
            word = word.strip().split(',')
            inrData = getHTMLData(os.path.join(parentDir,word[0]),inriaUrl+word[1].replace(',','')+';topic=;abs=f;allSol=2;mode=t;cpts=','inr')
            inrFilData = getHTMLData(os.path.join(parentDir,word[0]),inriaUrl+word[1].replace(',','')+';topic=;abs=f;allSol=2;mode=p;cpts=','inr')
            if inrData != None:
                inriaParse(inrData, word[1].replace(',',''), word[2].replace('"',''), inrOut, word[3].strip(),word[0].strip())
            if inrFilData != None:
                inriaParse(inrFilData, word[1].replace(',',''), word[2].replace('"',''), inrFilOut, word[3].strip(),word[0].strip())
        jnuOut.close()
        samOut.close()
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

