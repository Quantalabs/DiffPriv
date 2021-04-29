from . import enc
from pathlib import Path
import csv
import sys

def lfl_encrypt(enc_file, key_file, output):
    txt = Path(enc_file).read_text().replace('/n', '')
    with open(key_file, 'r') as key:
        keyvar = csv.reader(key)
        keyvar = list(keyvar)

    with open(output, 'w') as opt:
        opt.write(enc.lfl(txt, keyvar))

def lfl_decrypt(denc_file, key_file, output):
    txt = Path(denc_file).read_text().replace('/n', '')
    with open(key_file, 'r') as key:
        keyvar = csv.reader(key)
        keyvar = list(keyvar)
    
    with open(output, 'w') as opt:
        opt.write(enc.dec_lfl(txt, keyvar))

def rcipher(file, output):
    print(file + " " + output)
    txt = Path(file).read_text().replace('/n', '')

    with open(output, 'w') as opt:
        opt.write(enc.reverse_cipher(txt))

def run(args):
    if args[1] == 'lfl':
        if len(args) < 5:
            lfl_encrypt(args[2], args[3], args[2])
        else:
            lfl_encrypt(args[2], args[3], args[4])
    elif args[1] == 'dlfl':
        if len(args) < 5:
            lfl_decrypt(args[2], args[3], args[2])
        else:
            lfl_decrypt(args[2], args[3], args[4])
    elif args[1] == 'rcipher':
        if len(args) < 4:
            rcipher(args[2], args[2])
        else:
            rcipher(args[2], args[3])

if __name__ == "__main__":
    run(sys.argv)