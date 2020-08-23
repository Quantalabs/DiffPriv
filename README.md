![DiffPriv Logo](https://docs.google.com/drawings/d/e/2PACX-1vQ8A92uJpy4g09GFYxayNQXOvtl0wmXXkYFiteDFSaXVcfdbcm835wc_IjjlKHlM94rjdsM7H1Szzjq/pub?w=600)

[![PyPI Version](https://shields.mitmproxy.org/pypi/v/DIffPriv.svg)](https://pypi.org/project/DiffPriv)
[![Documentation Status](https://readthedocs.org/projects/diffpriv/badge/?version=latest)](https://diffpriv.readthedocs.io/en/latest/?badge=latest)
[![Language](https://img.shields.io/badge/language-python-blueviolet)](https://github.com/Quantalabs/DiffPriv)
# Welcome to DiffPriv v0.0.2

DiffPriv is a collection of different defferential privacy algorithms. From the Laplace Mechanism
to the simple Random Response mechanism, use differential privacy in your data easily with _DiffPriv_.

### Our world is full of data. Our world *is* data.
#### So let's protect it. Easily.

![photo of room with light up text saying, 'Data has a better idea'](https://images.unsplash.com/photo-1527474305487-b87b222841cc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60)

Photo by Franki Chamaki

## Downloading DIffPriv
To download, open up you command prompt and type

    python3 -m pip install DiffPriv


## How to Use

Now import DiffPriv.

    from DiffPriv import private

The first method we will use is the _Random Response Mechanism_. To use this, we use the `randresponse()` function.
You only need to pass *one* parameter. 

    randresponse(response_list)
    
Response list, the parameter, is the list of data or responses in a form. __Make sure you know how the random response mechansim works before you use it__.

The next method we can use is the _laplace mechanism_. To use the laplace function, we use the `lapmech()` function.

    lapmech(data, file_name, epsilon, f, sample_size=10, delta_f=None)
    
This will return a new dataset that is differentially privatized. @q9i's differential privacy wiki page on the laplace mechanism is a great explainer. You can view it [here](https://github.com/quantum9Innovation/Differential-Privacy/wiki/Doing-Complex-Stuff-...). You should also make sure you know how the laplace mechanism works.

The last method we will use is the _exponetial mechanism_. We will use the `expmech()` function.

    expmech(data, file_name, epsilon, f, r, sample_size=10, delta_f=None)

A lot of these are the same parameters from the `lapmech()` function, but `r` is new. r is any valid python range. So you can just use `range(0, 10)` or something like that. But again, make sure you know what the exponential mechansim is before you use it.

# People
- @quanatum9innovation - https://github.com/quantum9innovation
- @quantalabs -https://github.com/quantalabs

View on PyPI - https://pypi.org/project/DiffPriv

Homepage - https://quantalabs.github.io/DiffPriv
