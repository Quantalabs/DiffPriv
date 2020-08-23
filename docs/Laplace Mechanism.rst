Laplace Mechanism
******************

The laplace mechaism is another great mechanism for differential privacy. To use,
call the `lapmech` function

.. code-block:: python

   lapmech(data, file_name, epsilon, f, sample_size=10, delta_f=None)

The laplace mechansim has all of the parameters as the exponential mechanism
does other than r.