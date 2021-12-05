"""
This is a very basic test intended to ensure that v2a2 is ready to ship.
This test should be run before releasing *all* v2 alpha releases.
"""

from DiffPriv import mech
import math, random

def test_v2a2_ready():
    """
    This test ensures that v2a2 is ready to ship.
    This test should be run before releasing *all* v2 alpha releases.
    """
    
    randresp = mech.pre.randresponse()

    print(randresp.about())
    print(randresp([0,1,0,1,0,0,1,0,1,1,1,0,1,0]))

    def random_response(data):
        out = []
        for x in data:
            coin = random.randint(0,1)
            if coin == 0:
                out.append(bool(x))
            else:
                coin2 = random.randint(0,1)
                out.append(bool(coin2))

        return out

    Random_Response = mech.Mechanism('Random Response Mechnaism', 
                                     'https://en.wikipedia.org/wiki/Randomized_response', 
                                     random_response,
                                     'rr', 
                                     epsilon=lambda data: math.log(3),
                                     delta=lambda data: 0.0)
    about = Random_Response.about()
    test_set = [True, True, False, 
                True, True, True, 
                True, False, False, 
                False, False, True, 
                True, False, True]
    result = Random_Response(test_set)
    index = Random_Response.index()
    Double_Random_Response = Random_Response + Random_Response
    Triple_Random_Response = Random_Response * 3

    print(f'Docs: {about}')

    print('======')

    print(f'Eval: {result}')
    print(f'{index[0]}-differentially private')
    print(f'Repr: {Random_Response.__repr__()}')
    print(f'String: {Random_Response}')

    print('======')

    assert Random_Response == Random_Response
    assert Random_Response != 'Random Response Mechnaism'
    
    print('Assertion tests passed!')
    print('======')

    print(f'Double eval: {Double_Random_Response(test_set)}')
    print(f'Triple eval: {Triple_Random_Response(test_set)}')
