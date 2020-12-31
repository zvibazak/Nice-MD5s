# Nice-MD5s
Let's find nice patterns of MD5!!

> The MD5 message-digest algorithm is a widely used hash function producing a 128-bit hash value. ([Wikipedia](https://en.wikipedia.org/wiki/MD5))

This is totaly a nonsence but let's find nice patterns of MD5s.


## Definitions

A `nice pattern` considers as one of the below:
| # | Name | Example | 
|:--|:------------- |:-------------| 
| 1 | **Perfect match** - md5 of one letter\digit | `00000000000000000000000000000000` | 
| 2 | **Nice match** - md5 starts with N-same letter | `444431252d6a104a05fe4a0c6a53a999` (N=4)| 
| 3 | **Gold MD5** - md5 of it - equal to itself | `N/A` | 
| 4 | **Limit char** - md5 contains only N letters | `12345612345612345612345612345612` (N=6)| 
| 5 | **MD5 of digits** - md5 contains only digits | `12345612345612345612345612345612` | 
| 6 | **MD5 of letters** - md5 contains only letters | `abcdefabcdefabcdefabcdefabcdefab` |
| 7 | **Pi MD5** - md5 contains pi digits | `3141592653589793115997963468544185` |
| 8 | **e MD5** - md5 contains contant e digits | `2718281828459045090795598298427649` |

Please see the attached Python code to run on your computer, and add a `pull request` if you find new one (a credit is promised!).

Feel free to add your language version of the code!

## Results

| # | Name | N | MD5 | Founder | 
|:--|:------------- |:---|:-------------|:-------------| 
| 1 | **Nice match** | 5 |`md5('UPSCLU4P1EW7') = 7777759f258245119a1fe75ad393d91c` |zvibazak |
| 2 | **Limit char** | 8 |`md5(y7y8piinvbwca5kllokqkk16gk7mjy4g) = c1be414b7effcb4e881e74e4e181ceb1`|zvibazak |
