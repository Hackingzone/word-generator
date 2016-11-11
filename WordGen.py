# *- coding:UTF-8 -*
#WordGen
'''
__        __            _  ____            
\ \      / /__  _ __ __| |/ ___| ___ _ __  
 \ \ /\ / / _ \| '__/ _` | |  _ / _ \ '_ \ 
  \ V  V / (_) | | | (_| | |_| |  __/ | | |
   \_/\_/ \___/|_|  \__,_|\____|\___|_| |_|   
--------------------------------------------
Organization    : Offensive Deffensive Information Security
WebSite : https://OdInfoSec.blogspot.com
Author : Djamm Stap
'''
import itertools
import string
import sys
import time
def main():
    try:
        chrs = sys.argv[1]
        _min = int(sys.argv[2])
        _max = int(sys.argv[3])
        _out = sys.argv[4]
        _generator(chrs,_min,_max,_out)
    except IndexError:
        print("\n\033[91m[+]\033[0m Usage: python WordGen.py [CHARACTERS] [MINLENGTH] [MAXLENGTH] [OUTPUTFILE]\n")
def _generator(chrs,_min,_max,_out):
    try:
        _time = time.strftime('%H:%M:%S')
        print("\n\033[91m[+]\033[0m Started at %s\n" % _time)
        _output = open("wordlists/%s" % _out,"w")
        for n in range(_min, _max):
            for xs in itertools.product(chrs, repeat=n):
                _word = ''.join(xs)
                _output.write("%s\n" % _word)       
        _output.close()
        print("\n\033[91m[+]\033[0m Wordlist saved to %s\n" % _out)
    except Exception as error:
        print(error)
main()                                       
