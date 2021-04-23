![DiffPriv Logo](https://docs.google.com/drawings/d/e/2PACX-1vQ8A92uJpy4g09GFYxayNQXOvtl0wmXXkYFiteDFSaXVcfdbcm835wc_IjjlKHlM94rjdsM7H1Szzjq/pub?w=600)

[![Build Status](https://www.travis-ci.com/Quantalabs/DiffPriv.svg?branch=master)](https://www.travis-ci.com/Quantalabs/DiffPriv)
[![Documentation Status](https://readthedocs.org/projects/diffpriv/badge/?version=latest)](https://diffpriv.readthedocs.io/en/latest/?badge=latest)
[![PyPI Version](https://shields.mitmproxy.org/pypi/v/DIffPriv.svg)](https://pypi.org/project/DiffPriv)
[![Maintainability](https://api.codeclimate.com/v1/badges/e8eefc6c39998b74f69a/maintainability)](https://codeclimate.com/github/Quantalabs/DiffPriv/maintainability)
[![codecov](https://codecov.io/gh/Quantalabs/DiffPriv/branch/master/graph/badge.svg?token=wCz4qTJxEO)](https://codecov.io/gh/Quantalabs/DiffPriv)
[![License](https://img.shields.io/badge/License-GNU%20GPL%20v3.0-green)](https://github.com/Quantalabs/DiffPriv/blob/master/LICENSE)
[![Downloads](https://pepy.tech/badge/diffpriv)](https://pepy.tech/project/diffpriv)
[![Downloads](https://pepy.tech/badge/diffpriv/month)](https://pepy.tech/project/diffpriv/month)
[![Downloads](https://pepy.tech/badge/diffpriv/week)](https://pepy.tech/project/diffpriv/week) 
[![Chat on GitHub Discussions](https://img.shields.io/badge/Chat-on%20Discussions-green)](https://github.com/Quantalabs/DiffPriv/discussions)


# The truth is more important than ever—let's make sure easy privacy protection is available.

Differential privacy should be simple. Now that data defines our world, we need to look at the cost of privacy. Let's make protecting privacy easy.

<br><br>

# What is differential privacy and how can I start protecting privacy?

Differential privacy allows for data to be preserved while making sure that attackers cannot gain access to an individual's data. Even if you publish summary statistics (like average age of participants, unlabeled addresses of participants, etc.), attackers can gain access to *individual* data (like age of *each* participant, *labeled* addresses of participants, etc.). In order to achieve this, differential privacy slightly changes the actual dataset to make sure that any uncovered data will not give away personal information. See below for how to get started!

<br>

# The world is data
![The world is data](https://live.staticflickr.com/5228/5679642883_24a2e905e0_b.jpg)

## Downloading DiffPriv
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
