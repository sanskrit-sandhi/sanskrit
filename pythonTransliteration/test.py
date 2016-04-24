import chardet    
rawdata = open("input.txt", "r").read()
result = chardet.detect(rawdata)
charenc = result['encoding']
print charenc
print result