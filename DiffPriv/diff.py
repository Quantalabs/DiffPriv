from . import numpy as np
from . import random as rd
from . import math

def randresponse(response_list):
    """
    Random uses the Random Response mechanism. Random Response is a simple differential privacy algorithm. To use random pass one parameter:

    

        random(response_list)

    ## Parameters

    - response_list
        List with data.
    """

    for i in response_list:
        b = np.random.randint(2)
        if b == 0:
            response_list[i] = 0

        if b == 1:
            b1 = np.random.randint(2)

            if b1 == 0: # pragma: no cover
                response_list[i] = 0

            if b1 == 1: # pragma: no cover
                response_list[i] = 1

def lapmech(data, file_name, epsilon, f, sample_size=10, delta_f=None):
    """
    Preforms the laplace mechanism.

    

        lapmech(data, file_name, epsilon, f, sample_size=10, delta_f=None)
    
    ## Parameters

    - Data
        This is quite simple. You should pass in something like this:
            open('data.csv', 'r')
        Make sure that it has reading permissions.

    - file_name
        This is the name of the file that the privatized data will go into. It doesn’t have to be created for this to work.

    - epsilon
        This is one of the most important parameters in the entire algorithm. Unlike the random response mechanism, epsilon allows us to quantify privacy loss. This number should be a positive float like 3.14 or 2.71. Play around with different values to find which one works best but remember that smaller values will cause significant data changes while larger values may compromise privacy. Find the value that best works for your survey!

    - f
        f should be a function that takes in an array (all the elements in a certain column of the data) and produce an output (like the average, standard deviation, etc.). This should be a valid python function!

    
    ## Optional Parameters

    - delta_f
        delta_f is the sensitivity of f. Remeber that this is an optional parameter

    - sample_size
        sample_size is also optional. It gives the program an idea of what delta_f should be. It will default to 10 if left empty.
    """
    new_data = open(file_name, 'w+')
    raw_data = data.readlines()

    rows = len(raw_data)
    sample_size = min(rows, sample_size)
    columns = len(raw_data[0].split(','))

    if delta_f is None:

        delta_f = []
        data_draft = []

        for c in range(columns):

            data_draft.append([float(raw_data[r].split(',')[c]) for r in range(rows)])
            samples = [int(rows * rd.random()) for i in range(sample_size)]
            delta_f.append(0.01)

            for i in samples:

                x_prime = [x for x in data_draft[-1]]
                x_prime[i] += 1
                delta_f[-1] = max(delta_f[-1], abs(f(data_draft[-1])-f(x_prime)))

    for r in range(rows):

        line = []
        for c in range(columns):

            b = delta_f[c]/epsilon
            coin_flip = round(rd.random())
            if coin_flip == 0: line.append(float(raw_data[r].split(',')[c]) + rd.expovariate(1 / (2 * b)))
            if coin_flip == 1: line.append(float(raw_data[r].split(',')[c]) - rd.expovariate(1 / (2 * b)))

        new_data.writelines(str(line)+'\n')

    return new_data

def expmech(data, file_name, epsilon, u, r, sample_size=10, delta_u=None):
    '''
    Preforms the exponential mechanism.

    

        expmech(data, file_name, epsilon, u, r, sample_size=10, delta_f=None)
    
    ## Parameters

    - Data
        This is quite simple. You should pass in something like this:
            open('data.csv', 'r')
        Make sure that it has reading permissions.

    - file_name
        This is the name of the file that the privatized data will go into. It doesn’t have to be created for this to work.

    - epsilon
        This is one of the most important parameters in the entire algorithm. Unlike the random response mechanism, epsilon allows us to quantify privacy loss. This number should be a positive float like 3.14 or 2.71. Play around with different values to find which one works best but remember that smaller values will cause significant data changes while larger values may compromise privacy. Find the value that best works for your survey!

    - f
        f should be a function that takes in an array (all the elements in a certain column of the data) and produce an output (like the average, standard deviation, etc.). This should be a valid python function!

    - r
        r is any valid python range. You could pass in:
            range(0, 10)
    
    ## Optional Parameters

    - delta_f
        delta_f is the sensitivity of f. Remeber that this is an optional parameter

    - sample_size
        sample_size is also optional. It gives the program an idea of what delta_f should be. It will default to 10 if left empty.
    '''
    new_data = open(file_name, 'w+')
    raw_data = data.readlines()

    rows = len(raw_data)
    sample_size = min(rows, sample_size)
    columns = len(raw_data[0].split(','))

    if delta_u is None:

        delta_u = []
        data_draft = []

        for c in range(columns):

            data_draft.append([float(raw_data[ro].split(',')[c]) for ro in range(rows)])
            samples = [int(rows * rd.random()) for i in range(sample_size)]
            delta_u.append(0.01)

            for i in samples:

                for k in r:

                    x_prime = [x for x in data_draft[-1]]
                    x_prime[i] += 1
                    delta_u[-1] = max(delta_u[-1], abs(u(data_draft[-1], k)-u(x_prime, k)))

    line = []

    for c in range(columns):

        data = [float(raw_data[ro].split(',')[c]) for ro in range(rows)]
        probabilities = [math.exp(epsilon*u(data, k)/(2*delta_u[c])) for k in r]
        rand = sum(probabilities)*rd.random()

        r_choice = 0
        running_sum = 0

        for choice in r:

            if rand <= running_sum + probabilities[choice]:
                r_choice = choice
                break

            else:
                running_sum += probabilities[choice]

        line.append(r_choice)

    new_data.writelines(str(line)+'\n')

    return new_data
