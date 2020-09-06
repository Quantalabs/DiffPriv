![DiffPriv](https://ibb.co/pz4WLH4)

[![PyPI Version](https://shields.mitmproxy.org/pypi/v/DIffPriv.svg)](https://pypi.org/project/DiffPriv)
[![Documentation Status](https://readthedocs.org/projects/diffpriv/badge/?version=latest)](https://diffpriv.readthedocs.io/en/latest/?badge=latest)
[![Language](https://img.shields.io/badge/language-python-blueviolet)](https://github.com/Quantalabs/DiffPriv)
[![License](https://img.shields.io/badge/License-GNU%20GPL%20v3.0-green)](https://github.com/Quantalabs/DiffPriv/blob/master/LICENSE)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/Quantalabs/DiffPriv.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Quantalabs/DiffPriv/context:python)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/Quantalabs/DiffPriv.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Quantalabs/DiffPriv/alerts/)
[![Downloads](https://pepy.tech/badge/diffpriv)](https://pepy.tech/project/diffpriv)
[![Downloads](https://pepy.tech/badge/diffpriv/month)](https://pepy.tech/project/diffpriv/month)
[![Downloads](https://pepy.tech/badge/diffpriv/week)](https://pepy.tech/project/diffpriv/week) 
[![Join the chat at https://gitter.im/Quantalabs/DiffPriv](https://badges.gitter.im/Quantalabs/DiffPriv.svg)](https://gitter.im/Quantalabs/DiffPriv?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Issue Tracking](https://img.shields.io/badge/issue_tracking-github-blue.svg)](https://github.com/Quantalabs/DiffPriv/issues)
[![PRs Welcome](https://img.shields.io/badge/PR-Welcome-%23FF8300.svg?)](https://git-scm.com/book/en/v2/GitHub-Contributing-to-a-Project)

# Welcome to DiffPriv v0.1.1

DiffPriv is a collection of different defferential privacy algorithms. From the Laplace Mechanism
to the simple Random Response mechanism, use differential privacy in your data easily with _DiffPriv_.

### Our world is full of data. Our world *is* data.
#### So let's protect it. Easily.

![photo of room with light up text saying, 'Data has a better idea'](https://images.unsplash.com/photo-1527474305487-b87b222841cc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60)

Photo by Franki Chamaki

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
