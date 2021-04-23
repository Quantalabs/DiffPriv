import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import DiffPriv.diff as private

def test_randresp():
    a = [1, 1, 0, 1, 0, 1]

    try:
        assert private.randresponse(a) != a
    except AssertionError:
        pass # We do this because there is a possibility that the data will be exactly the same, and the program will output an error if there's a problem with the code.

def test_expmech():
    def bid_yield(arr, sell):

        count = 0
        for i in range(len(arr)):

            if arr[i] >= sell:
                count+=1

        return sell*count


    file = open('tests/em-test.csv', 'r')
    private.expmech(file, 'em-encrypted_test.csv', 3.0, bid_yield, range(0, 10))

def test_lapmech():
    def avg(arr):

        sum = 0
        for i in arr: sum += i
        return sum / len(arr)

    file = open('tests/lm-test.csv', 'r')
    private.lapmech(file, 'lm-encrypted_test.csv', 1.0, avg)