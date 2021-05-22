![DiffPriv Logo](https://docs.google.com/drawings/d/e/2PACX-1vQ8A92uJpy4g09GFYxayNQXOvtl0wmXXkYFiteDFSaXVcfdbcm835wc_IjjlKHlM94rjdsM7H1Szzjq/pub?w=600)

[![Build Status](https://www.travis-ci.com/Quantalabs/DiffPriv.svg?branch=master)](https://www.travis-ci.com/Quantalabs/DiffPriv)
[![PyPI Version](https://shields.mitmproxy.org/pypi/v/DIffPriv.svg)](https://pypi.org/project/DiffPriv)
[![DeepSource](https://deepsource.io/gh/Quantalabs/DiffPriv.svg/?label=active+issues&show_trend=true)](https://deepsource.io/gh/Quantalabs/DiffPriv/?ref=repository-badge)
[![codecov](https://codecov.io/gh/Quantalabs/DiffPriv/branch/master/graph/badge.svg?token=wCz4qTJxEO)](https://codecov.io/gh/Quantalabs/DiffPriv)
[![License](https://img.shields.io/badge/License-GNU%20GPL%20v3.0-green)](https://github.com/Quantalabs/DiffPriv/blob/master/LICENSE)
[![Downloads](https://pepy.tech/badge/diffpriv)](https://pepy.tech/project/diffpriv)
[![Downloads](https://pepy.tech/badge/diffpriv/month)](https://pepy.tech/project/diffpriv/month)
[![Downloads](https://pepy.tech/badge/diffpriv/week)](https://pepy.tech/project/diffpriv/week) 
[![Chat on GitHub Discussions](https://img.shields.io/badge/Chat-on%20Discussions-green)](https://github.com/Quantalabs/DiffPriv/discussions)


> The truth is more important than ever—let's make sure easy privacy protection is available.

Differential privacy should be simple. Now that data defines our world, we need to look at the cost of privacy. Let's make protecting privacy easy.

<br><br>

## What is differential privacy?

Differential privacy allows for data to be preserved while making sure that attackers cannot gain access to an individual's data. Even if you publish summary statistics (like average age of participants, unlabeled addresses of participants, etc.), attackers can gain access to *individual* data (like age of *each* participant, *labeled* addresses of participants, etc.). In order to achieve this, differential privacy slightly changes the actual dataset to make sure that any uncovered data will not give away personal information. See below for how to get started!

<br>

## Downloading DiffPriv
To download, open up your command prompt and type
```sh
    pip install DiffPriv
```
or from the source repo:
```sh
    git clone https://github.com/Quantalabs/DiffPriv
    cd diffpriv
    python setup.py install
```
### Conda Envioronment

You can install it from conda through the command:
```sh
conda install -c conda-forge diffpriv
```