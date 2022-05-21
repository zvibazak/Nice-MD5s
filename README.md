# Nice-MD5s
Let's find `nice patterns` of MD5!!

> The MD5 message-digest algorithm is a widely used hash function producing a 128-bit hash value. ([Wikipedia](https://en.wikipedia.org/wiki/MD5))

This is totaly a nonsence but let's find nice patterns of MD5s.


## Definitions

A `nice pattern` considers as one of the below:
| # | Name | Explanation | Example | 
|:--|:------------- |:------------- |:-------------| 
| 1 | **Perfect match** | md5 of one characters | `00000000000000000000000000000000` | 
| 2 | **Nice match** | md5 starts with N-same characters | `444431252d6a104a05fe4a0c6a53a999` (N=4)| 
| 3 | **Gold MD5** | md5 of it - equal to itself | `N/A` | 
| 4 | **Limit char** | md5 contains only N characters | `12345612345612345612345612345612` (N=6)| 
| 5 | **MD5 of digits** | md5 contains only digits | `25855924411269249612523541155616` | 
| 6 | **MD5 of letters** | md5 contains only letters | `abcdefabcdefabcdefabcdefabcdefab` |
| 7 | **Pi MD5** | md5 contains pi digits | `3141592653589793115997963468544185` |
| 8 | **e MD5** | md5 contains contant e digits | `2718281828459045090795598298427649` |

Please see the attached Python code to run on your computer, and add a `pull request` if you find new one (a credit is promised!).

Feel free to add your language version of the code!

## Hall of fame

| # | Name | N | MD5 | Founder | 
|:--|:------------- |:---|:-------------|:-------------| 
| 1 | **Nice match** | 7 |`md5('8jstmg2n317o7flqy5j8wzxkxb7698c0') = 666666633662d078567e1c5b196a821e` |zvibazak |
| 2 | **Limit char** | 7 |`md5('kkh8j1n5sle3vzb1v5f6ll7pc1x9ne7u') = 8aac28ffafe8aeccfaafa8ec8a6f82ce`|zvibazak |
| 3 | **MD5 of digits** | - |`md5('r8z43szwn6duks2yoqf6eaugebdjdhfk') = 52028506537132879258425329778418`|zvibazak |
| 4 | **Nice match** | 9 | `md5('8teyu1mjb014j2mlt8c527cejx6gyfat ') = 888888888ff2f2e45199d0ef65b7fea2` |marcdtheking |
