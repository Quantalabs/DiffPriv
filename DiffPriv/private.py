from . import np
from . import random

def random(response_list):
    """
    Random
    Random uses the Random Response mechanism. Random Response is a simple differential privacy algorithm. To use random pass one parameter:

        random(response_list)

    response_list is the list of responses.

    """

    for i in response_list:
        b = np.random.randint(2)
        if b == 0:
            response_list[i] = 0

        if b == 1:
            b1 = np.random.randint(2)

            if b1 == 0:
                response_list[i] = 0

            if b1 == 1:
                response_list[i] = 1
                
def laplace(data, file_name, epsilon, f, sample_size=10, delta_f=None):

    """
      For an explanation of how to use the laplace mechanism, go to https://github.com/quantum9Innovation/Differential-Privacy/wiki/Doing-Complex-Stuff-...
      The ... is part of the URL
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
            samples = [int(rows * random.random()) for i in range(sample_size)]
            delta_f.append(0.01)

            for i in samples:

                x_prime = [x for x in data_draft[-1]]
                x_prime[i] += 1
                delta_f[-1] = max(delta_f[-1], abs(f(data_draft[-1])-f(x_prime)))

    for r in range(rows):

        line = []
        for c in range(columns):

            b = delta_f[c]/epsilon
            coin_flip = round(random.random())
            if coin_flip == 0: line.append(float(raw_data[r].split(',')[c]) + random.expovariate(1 / (2 * b)))
            if coin_flip == 1: line.append(float(raw_data[r].split(',')[c]) - random.expovariate(1 / (2 * b)))

        new_data.writelines(str(line)+'\n')

    return new_data

               
