Exponential Mechaism
********************

The exponential mechanism is not so easy like the random response mechanism. Call
the `expmech()` function to use it.

.. code-block:: python

   expmech(data, file_name, epsilon, f, r, sample_size=10, delta_f=None)

Data
====

This is quite simple. You should pass in something like this:

.. code-block:: python

   open('data.csv', 'r')

Make sure that it has reading permissions.

file_name
=========

This is the name of the file that the privatized data will go into. It doesn't have
to be created for this to work.


epsilon
=======

This is one of the most important parameters in the entire algorithm. Unlike the
random response mechanism, epsilon allows us to quantify privacy loss. This number
should be a positive float like 3.14 or 2.71. Play around with different values to
find which one works best but remember that smaller values will cause significant
data changes while larger values may compromise privacy. Find the value that best
works for your survey!

f
=

f should be a function that takes in an array (all
the elements in a certain column of the data) and produce an output (like the
average, standard deviation, etc.). This should be a valid python function!

r
=

r is any valid python range. You could pass in:

.. code-block:: python

   range(0, 10)

Optional Parameters
===================

delta_f
=======

delta_f is the sensitivity of f. Remeber that this is an optional parameter

sample_size
===========

sample_size is also optional. It gives the program an idea of what delta_f should
be. It will default to 10 if left empty.
