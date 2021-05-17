"""
The cli can be accessed through the help command. Use `--help` to get a command list, and `--help [command]` for help on a specfic command.

The documentation below is best accessed through the `--help` command or through the built-in python attribute `__doc__`
"""

from . import enc
from pathlib import Path
from . import csv
from . import sys
from . import webbrowser

def lfl(enc_file, key_file, output):
    """lfl

    \33[1mdiffpriv lfl input_file key_file outputfile\33[9m[optional]

The lfl command will encrypt the given input file with the given key and put the output in the given output file, or,
if there is none, will automatically put the output in the input file, replacing the content.
    """
    txt = Path(enc_file).read_text().replace('/n', '')
    with open(key_file, 'r') as key:
        keyvar = csv.reader(key)
        keyvar = list(keyvar)

    with open(output, 'w') as opt:
        opt.write(enc.lfl(txt, keyvar))

def dlfl(denc_file, key_file, output):
    """dlfl

    \33[1mdiffpriv dlfl input_file key_file outputfile\33[0m[optional]

The dlfl command decrypts the given input file with the given key and put the output in the given output file, or,
if there is none, will automatically put the output in the input file, replacing the content.
    """
    txt = Path(denc_file).read_text().replace('/n', '')
    with open(key_file, 'r') as key:
        keyvar = csv.reader(key)
        keyvar = list(keyvar)
    
    with open(output, 'w') as opt:
        opt.write(enc.dec_lfl(txt, keyvar))

def rcipher(file, output):
    """rcipher
    
    \33[1mdiffpriv rcipher file outputfile\33[0m[optional]

The rcipher command will run the reverse cipher on a given file and put the output in the given output file, or,
if there is none, will automatically put the output in the input file, replacing the content.
    """
    txt = Path(file).read_text().replace('/n', '')

    with open(output, 'w') as opt:
        opt.write(enc.reverse_cipher(txt))
    
def porta(ifile, ofile, key):
    """porta

    \33[1mdiffpriv porta input_file output_file key\33[0m

The porta commmand will encrypt the message in the given input file using the given key and put the output in the given output file.\33[31m
NOTE\33[0m: The key should not be part of a file, but passed in as text in the CLI. Use quotes for a multi-word key, ex \33[1m"This is a multi-word key"\33[0m
or otherwise just \33[1mkey\33[0m for a single word key.
"""
    cipher = enc.Porta()

    with open(ifile, 'r') as enctext:
        text = enctext.readlines()
    
    output = []

    for x in text:
        output.append(cipher.encrypt(x, key)+'\n')
    
    with open(ofile, 'w') as ofilewrite:
        output = ''.join(output)
        ofilewrite.write(output)

def portadec(ifile, ofile, key):
    """portadec

    \33[1mdiffpriv portadec input_file output_file key\33[0m

The portadec command will decrypt a message in the input file using the given key and put the output in the given output file. \33[31m 
NOTE\33[0m: The key should not be part of a file, but passed in as text in the CLI. Use quotes for a multi-word key, ex. \33[1m"This is a multi-word key"\33[0m
or otherwise just \33[1mkey\33[0m for a single word key.
"""
    cipher = enc.Porta()

    with open(ifile, 'r') as enctext:
        text = enctext.readlines()
    
    output = []

    for x in text:
        output.append(cipher.decrypt(x, key)+'\n')
    
    with open(ofile, 'w') as ofilewrite:
        output = ''.join(output)
        ofilewrite.write(output)
    
def help(command=None):
    if command is None:
        print('\33[1mDiffPriv CLI Help\n\33[0m')
        print('The DiffPriv CLI provides an easy way to encrypt files or use differential privacy on data quickly and easily. See documentation for more detailed help - https://diffpriv.rtfd.io')
        print('\n \nCOMMANDS')
        print('---------------------------------------\n')
        print('\33[31m--help \33[0m')
        print('This command. Outputs help for the CLI. Add the name of a command after it for easy \n')
        print('\33[31mlfl\33[0m')
        print('Uses letter for letter encryption on a file. Format is \33[1mdiffpriv lfl input_file key_file outputfile\33[0m[optional] If last option is left blank, replaces the encryption file content with the new content\n')
        print('\33[31mdlfl\33[0m')
        print('Decrypts a file with letter for letter encryption. Format is \33[1mdiffpriv dlfl input_file key_file outputfile\33[0m[optional] If last option is left blank, replaces the decryption file content with the new content\n')
        print('\33[31mrcipher\33[0m')
        print('Reverse cipher. Format is \33[1mdiffpriv rcipher input_file output_fle\33[0m[optional] If last option is left blank, replaces the content of the input file with the encrypted text')
        print('\n\33[31mporta\33[0m')
        print('Encrypts file with the porta cipher. Format is \33[1mdiffpriv porta input_file output_file key\33[0m Last option is passed in as text not a file. Ex. \33[1mdiffpriv porta file.txt output.txt thisisthekey\33[0m')
        print('\n\33[31mportadec\33[0m')
        print('Decrypts file with the porta cipher. Format is \33[1mdiffpriv portadec input_file output_file key\33[0m Last option is passed in as text not a file. Ex. \33[1mdiffpriv portadec file.txt output.txt thisisthekey\33[0m')
        print('\n\33[31m--docs\33[0m')
        print('Shows diffpriv documentation for package or submodule.')
        print('\n\33[31m--changelog\33[0m')
        print('Shows the changelog.')
    else:
        eval('print('+command+'.__doc__)') # skipcq: PYL-W0123

def docs(submodule=None):
    """docs
    
    \33[1mdiffpriv docs submodule\33[0moptional

The `--docs` command will open up the diffpriv documentation. If you pass in a submodule it will open up the docs for that submodule, eg. `--docs diff` will open up docs
for the `diff` submodule.
    """
    base_url = 'https://quantalabs.github.io/DiffPriv/docs/'
    if submodule is None:
        webbrowser.open(base_url+'DiffPriv.html')
    else:
        webbrowser.open('DiffPriv/'+base_url+submodule+'.html')

def changelog():
    """--changelog
Shows the changelog
"""
    webbrowser.open('https://quantalabs.github.io/DiffPriv/CHANGELOG')

def run(args=sys.argv):
    if args[1] == 'lfl':
        if len(args) < 5:
            lfl(args[2], args[3], args[2])
        else:
            lfl(args[2], args[3], args[4])
    elif args[1] == 'dlfl':
        if len(args) < 5:
            dlfl(args[2], args[3], args[2])
        else:
            dlfl(args[2], args[3], args[4])
    elif args[1] == 'rcipher':
        if len(args) < 4:
            rcipher(args[2], args[2])
        else:
            rcipher(args[2], args[3])
    elif args[1] == 'porta':
        porta(args[2], args[3], args[4])
    elif args[1] == 'portadec':
        portadec(args[2], args[3], args[4])
    elif args[1] == '--help':
        if len(args) < 3:
            help()
        else:
            help(command=args[2])
    elif args[1] == '--changelog':
        changelog()
    elif args[1] == '--docs':
        if len(args) < 3:
            docs()
        else:
            docs(submodule=args[2])
    else:
        raise ValueError('Command '+ args[1] + ' not found. Use --help for list of commands.')

if __name__ == "__main__":
    run(sys.argv) # pragma: no cover