# Nice-MD5s
Let's find nice patterns of MD5!!

> The MD5 message-digest algorithm is a widely used hash function producing a 128-bit hash value. ([Wikipedia](https://en.wikipedia.org/wiki/MD5))

This is totaly a nonsence but let's find nice patterns of MD5s.


## Definitions

A `nice pattern` considers as one of the below:

1. **Perfect match** - `00000000000000000000000000000000` etc.

   Example - not found yet...
  
2. **Nice match** - start with N-same letter:

   Example of `N=4`:
   
   `md5('AGN04QP3DP74') = 444431252d6a104a05fe4a0c6a53a999`
   
   Example of `N=3`:
   
   `md5('CNFIVNSBBM86') = 555161f9f70ee828da527a6934596f61`

3. **Gold MD5** - md5 of it - equal to itself. 

   Example - not found yet...

 
Please see the attached Python code to run on your computer, and add a `pull request` if you find new one (a credit is promised!).

Feel free to add your language version of the code!

## Results

**Perfect match** - N/A.
 
**Nice match** of 5 - Zvi Bazak: `md5('UPSCLU4P1EW7') = 7777759f258245119a1fe75ad393d91c`
