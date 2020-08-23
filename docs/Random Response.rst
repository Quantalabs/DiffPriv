
.. toctree::
    :max-depth: 1

    What is the Random Response Mechanism
    How to use it


Random Response
###############

What it is
**********
The random response mechanism only uses zeros and ones. It flips a coin, and if it
lands on heads, it returns the truth. If it's tails, then it flips it again. If it's
heads this time, it returns 1, otherwise, it returns 0.

How to Use It
*************

The random response mechaism can be called using the `random()` mechansim.

.. code-block:: python

   randresponse(response_list)

The parameter `response_list` is a list of responses. These can only be zeros and
ones.