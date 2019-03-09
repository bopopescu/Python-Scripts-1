import os
import re

search_text="import"

print("Current directory", os.getcwd())
dir=os.getcwd()

'''
print(os.listdir(os.getcwd()))
for files in os.listdir(os.getcwd()):
    if os.path.isdir(files):
        print("\n %s is directory" %(files))
    else:
        with open(files, mode='r', encoding='utf-8') as f:
            print("\n Content of %s" % (files))
            for lines in f:
                if re.search(search_text, lines):
                    print(lines)

        f=open(files,mode='r',encoding='utf-8')
        print("\n Content of %s" % (files))
        print("\n", f.readlines())
        for lines in f:
            if re.search(search_text,lines):
                print(lines)
        f.close()
'''

for root,dirs,files in os.walk(dir, followlinks=False):
    for file in files:
#        path=os.path.join(root,file)
#        print(path)
        try:
            f=open(file, mode='r', encoding='utf-8')
        except Exception:
            print("\ncant' open file", file)
            continue
        print("\n Content of %s" % (file))
        print("\n", f.readlines())
        for lines in f:
            if re.search(search_text, lines):
                print(lines)
        f.close()





