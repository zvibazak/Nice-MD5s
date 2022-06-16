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
| 4 | **MD5 of digits** | md5 contains only digits | `25855924411269249612523541155616` | 
| 5 | **MD5 of letters** | md5 contains only letters | `abcdefabcdefabcdefabcdefabcdefab` |
| 6 | **Pi MD5** | md5 contains pi digits | `3141592653589793115997963468544185` |
| 7 | **e MD5** | md5 contains contant e digits | `2718281828459045090795598298427649` |

Please see the attached Python code to run on your computer, and add a `pull request` if you find new one (a credit is promised!).

Feel free to add your language version of the code!

## Hall of fame

| # | Name | N | MD5 | Founder | 
|:--|:------------- |:---|:-------------|:-------------| 
| 1 | **MD5 of digits** | 32! |`md5('r8z43szwn6duks2yoqf6eaugebdjdhfk') =` **52028506537132879258425329778418**|zvibazak |
| 2 | **MD5 of letters** | 21 |`md5('stngf63cv8gjzfss95hkcihqpatxam64') =` **ebdbaaefddcfdfcfdabff**4675d4b832c|zvibazak |
| 3 | **Nice match** | 9 |`md5('8teyu1mjb014j2mlt8c527cejx6gyfat') =` **888888888**ff2f2e45199d0ef65b7fea2 |marcdtheking |
| 4 | **Pi MD5** | 7 |`md5('hvm97m3cqx33kqsewub1cekqqawb1y16') =` **3141592**f6b8ccecc81f16843277bda04|zvibazak |
| 5 | **e MD5** | 7 |`md5('593890wfhxvwi9yo1s3cwqavmrhrojt6') =` **2718281**7b60a112000cdbae16cf00502|zvibazak |
| 6 | **Gold MD5** | 5 |md5('**23a63**qzw4q6f6l4ivvuusr48boqcm3ux') = **23a63**47131253d0e9bc123d5fe2d7de1|zvibazak |


