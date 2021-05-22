import os
import sys
import csv

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import DiffPriv

class Testlfl:
    def test_lfl_noutput(self): # Test the lfl without giving an output file.
        with open('text.txt', 'w') as testfile:
            testfile.write('Text')
        
        key = [['t', 'h'], ['e', 'i'], ['x', 'g'], ['T', 'H']]
        with open('key.csv', 'w', newline='') as keyfile:
            csvreader = csv.writer(keyfile)
            csvreader.writerows(key)
        
        DiffPriv.cli.run(['diffpriv', 'lfl', 'text.txt', 'key.csv'])
    
    def test_lfl_woutput(self): # Test the cli's lfl function with a output file.
        with open('text.txt', 'w') as testfile:
            testfile.write('Text')
        
        key = [['t', 'h'], ['e', 'i'], ['x', 'g'], ['T', 'H']]
        with open('key.csv', 'w', newline='') as keyfile:
            csvreader = csv.writer(keyfile)
            csvreader.writerows(key)
            keyfile.close() 
        
        DiffPriv.cli.run(['diffpriv', 'lfl', 'text.txt', 'key.csv', 'output.txt'])

class TestRciph:
    def test_rciph_wouput(self):
        with open('rciphtext.txt', 'w') as text:
            text.write('Text')
        
        DiffPriv.cli.run(['diffpriv', 'rcipher', 'rciphtext.txt', 'routput.txt'])
    
    def test_rciph_nouput(self):
        with open('rciphtext.txt', 'w') as text:
            text.write('Text')
        
        DiffPriv.cli.run(['diffpriv', 'rcipher', 'rciphtext.txt'])

class TestDlfl:
    def test_dlfl_woutput(self):
        key = [['t', 'h'], ['e', 'i'], ['x', 'g'], ['T', 'H']]
        with open('key.csv', 'w', newline='') as keyfile:
            csvreader = csv.writer(keyfile)
            csvreader.writerows(key)
        
        with open('text.txt', 'w') as testfile:
            testfile.write('High')
        
        DiffPriv.cli.run(['diffpriv', 'dlfl', 'text.txt', 'key.csv', 'output.txt'])
    
    def test_lfl_output(self):
        key = [['t', 'h'], ['e', 'i'], ['x', 'g'], ['T', 'H']]
        with open('key.csv', 'w', newline='') as keyfile:
            csvreader = csv.writer(keyfile)
            csvreader.writerows(key)
        
        with open('text.txt', 'w') as testfile:
            testfile.write('Text')
        
        DiffPriv.cli.run(['diffpriv', 'dlfl', 'text.txt', 'key.csv'])

class TestPorta:
    def test_enc(self):
        with open('porta_test.txt', 'w') as test_file:
            test_file.write('Test String')
            
        DiffPriv.cli.run(['diffpriv', 'porta', 'porta_test.txt', 'porta_test.txt', 'key'])
    
    def test_dec(self):
        DiffPriv.cli.run(['diffpriv', 'portadec', 'porta_test.txt', 'porta_test.txt', 'key'])

class TestHelp:
    def test_base_help(self):
        DiffPriv.cli.run(['diffpriv', '--help'])
    
    def test_command_help(self):
        DiffPriv.cli.run(['diffpriv', '--help', 'porta'])

class TestDocs:
    def test_docs(self):
        DiffPriv.cli.run(['diffpriv', '--docs'])
    
    def test_docs_submodule(self):
        DiffPriv.cli.run(['diffpriv', '--docs', 'cli'])

def test_changelog():
    DiffPriv.cli.run(['diffpriv', '--changelog'])

def test_command_error():
    try:
        DiffPriv.cli.run(['diffpriv', 'not-a-command'])
        raise RuntimeError('Command "not-a-command" doesn\'t output an error despite not existing in the command library.')
    except ValueError:
        print('All good. No Error.')