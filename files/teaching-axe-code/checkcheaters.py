import hashlib
import os
from time import sleep

def check():
    h = hashlib.sha256()
    with open("comp.py", "rb", buffering=0) as f:
        for b in iter(lambda : f.read(128*1024), b''):
            h.update(b)

    hexValue = h.hexdigest()
    result = "707e123ed40df9502c0fec50bfb97cca78ebe60f0ce3522f8360debee0d2f2de" == hexValue

    if(result == False):
        print("Cheater -_-, don't change the comp.py file")
        sleep(1)
        print("Reverting the comp.py file", end="")
        for i in range(5):
            print(".",end="", flush=True)
            sleep(0.25)
        print("")
        os.system("cat copycomp.py > comp.py")
        sleep(1)
