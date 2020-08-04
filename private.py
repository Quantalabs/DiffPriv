from . import np

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