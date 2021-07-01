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

    diffpriv lfl input_file key_file outputfile[optional]

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

    diffpriv dlfl input_file key_file outputfile[optional]

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
    
    diffpriv rcipher file outputfile[optional]

The rcipher command will run the reverse cipher on a given file and put the output in the given output file, or,
if there is none, will automatically put the output in the input file, replacing the content.
    """
    txt = Path(file).read_text().replace('/n', '')

    with open(output, 'w') as opt:
        opt.write(enc.reverse_cipher(txt))
    
def porta(ifile, ofile, key):
    """porta

    diffpriv porta input_file output_file key

The porta commmand will encrypt the message in the given input file using the given key and put the output in the given output file.
NOTE: The key should not be part of a file, but passed in as text in the CLI. Use quotes for a multi-word key, ex "This is a multi-word key"
or otherwise just key for a single word key.
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

    diffpriv portadec input_file output_file key

The portadec command will decrypt a message in the input file using the given key and put the output in the given output file.  
NOTE: The key should not be part of a file, but passed in as text in the CLI. Use quotes for a multi-word key, ex. "This is a multi-word key"
or otherwise just key for a single word key.
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
        print('DiffPriv CLI Help\n')
        print('The DiffPriv CLI provides an easy way to encrypt files or use differential privacy on data quickly and easily. See documentation for more detailed help - https://quantalabs.github.io/DiffPriv/docs/DiffPriv/cli.html')
        print('\n \nCOMMANDS')
        print('---------------------------------------\n')
        print('--help ')
        print('This command. Outputs help for the CLI. Add the name of a command after it for easy \n')
        print('lfl')
        print('Uses letter for letter encryption on a file. Format is \ndiffpriv lfl input_file key_file outputfile[optional] \nIf last option is left blank, replaces the encryption file content with the new content\n')
        print('dlfl')
        print('Decrypts a file with letter for letter encryption. Format is \ndiffpriv dlfl input_file key_file outputfile[optional]\n If last option is left blank, replaces the decryption file content with the new content\n')
        print('rcipher')
        print('Reverse cipher. Format is \ndiffpriv rcipher input_file output_fle[optional]  \nIf last option is left blank, replaces the content of the input file with the encrypted text')
        print('\nporta')
        print('Encrypts file with the porta cipher. Format is \ndiffpriv porta input_file output_file key\n Last option is passed in as text not a file. Ex. diffpriv porta file.txt output.txt thisisthekey')
        print('\nportadec')
        print('Decrypts file with the porta cipher. Format is \ndiffpriv portadec input_file output_file key\n Last option is passed in as text not a file. Ex. diffpriv portadec file.txt output.txt thisisthekey')
        print('\n--docs')
        print('Shows diffpriv documentation for package or submodule.')
        print('\n--changelog')
        print('Shows the changelog.')
    else:
        eval('print('+command+'.__doc__)') # skipcq: PYL-W0123

def docs(submodule=None):
    """docs
    
    diffpriv docs submodule[optional]

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