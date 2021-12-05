# v2a2
## What's Changed
* Initial Restructuring of the package, as detailed in #33 (The other functions still are avaliable, but will be removed and deprecated in the future.)

# v1.0.3
Patch Update

## Bug Fixes
 - Fix out-of-date url from diffpriv.rtfd.io to quantalabs.github.io/docs/
 - Fix laplace and exponential mechanism formatting error.

---

# v1.0.2
Patch Update
## Bug Fixes
- Fix a formatting error in the CLI with the `--help` command. 

---
# v1.0.1
Patch update
- Fix another bug with the version warning

---
# v1.0.0

## Bug Fixes
- Fix version warnings

---

# v1.0.0rc
## Bug Fixes
- Security Fix with commit 46f3363.
    With the diff and enc modules, parameters were stored in python memory, and never removed. This commit deletes these parameters and helps prevent attackers from gaining access to these parameters, which can help them gain access to the original text and/or data.

## New Features
None.


---

# v1.0.0-beta _pre release_
## Bug Fixes
- Fix version error
- Fix a CLI error
- Fix a circular import error

## New Features
- Add a `--docs` command to view the documentation for DiffPriv
- Add a `--changelog` command to view the changelog

---
# v1.0.0-alpha _pre release_
The first beta release of the first version of diffpriv. Includes:
- Differential Privacy
  - Laplace Mechanism
  - Exponential Mechanism
  - Random Response
- Encryption Schemes
  - ROT13 Cipher (a letter for letter substitution cipher)
  - Reverse Cipher
  - Porta Cipher

---

# v0.1.1
## New Functions

v0.1.1 now includes the exponential mechanism. you can view how to use it in the `README.md`.

## Fixes

None

## Collaborators

@quantum9Innovation 
@Quantalabs 

---
# **v0.0.2**
## New Functions

Added the new Laplace Mechanism. A new method which allows for much more capability. This allows you to import .csv files and deferentially privatize the data and keep the original data too.  It will create a new file for the deferentially privatized data. It also allows for any float value instead of just 0 or 1 like it is with random response. But here are all the advantages of the Laplace Mechanism function in DiffPriv.

| :+1: |
| :----: |
| More Flexibility in your data and values | 
| Allows for .csv files to be used |
| Allows for _both_ datasets to be kept (the original and privatized data) |
| Flexibility on how privatized your data can be and how much it can be altered by using the epsilon parameter |

## Fixes

None

## Uploading from PyPI

     python3 -m pip install DiffPriv==0.0.2

## Collaborators

- @quantum9Innovation 
- @Quantalabs 

---
# **v0.0.1**

This version only includes one function 😞. The function is random. It runs the random response mechanism.

     random(response_list)

v0.0.2 might include:

- Random Response
- Laplace Mechanism
- Exponential Mechanism
