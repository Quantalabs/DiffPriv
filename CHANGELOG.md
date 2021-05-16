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
