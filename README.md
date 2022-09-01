# Nice-MD5s
Let's find `nice patterns` of MD5!!

> The MD5 message-digest algorithm is a widely used hash function producing a 128-bit hash value. ([Wikipedia](https://en.wikipedia.org/wiki/MD5))

This is **totaly a nonsence** but let's find nice patterns of MD5s.


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
| 1 | **MD5 of digits** | **32** |`md5('r8z43szwn6duks2yoqf6eaugebdjdhfk') =` **52028506537132879258425329778418** | zvibazak |
| 2 | **MD5 of letters** | 25 |`md5('8f980d694e5beefed4feb669a0c7de3a') =` **fdffbedbbfbadffaafbfadceb**51b30fe | zvibazak |
| 3 | **Gold MD5** | 12 |`md5('54db1011d76dc70a0a9df3ff3e0b390f') =` **54db1011d76d**137956603122ad86d762 | [Thomas Egense](https://stackoverflow.com/a/28941658/1909132) |
| 4 | **Nice match** | 9 |`md5('8teyu1mjb014j2mlt8c527cejx6gyfat') =` **888888888**ff2f2e45199d0ef65b7fea2 | marcdtheking |
| 5 | **e MD5** | 8 |`md5('us5rthcbjhhemvllo84dd78wrbt1gzu8') =` **27182818**8d69458862beb75e836ea2da | zvibazak |
| 6 | **Pi MD5** | 8 |`md5('y6y8fht4enu4fo2hq73d1othbaitzi5b') =` **31415926**b87f076e8d5d422c6be787d9 | zvibazak |
