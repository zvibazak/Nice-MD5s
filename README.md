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
| 2 | **MD5 of letters** | 27 |`md5('86564eb130eaa1c997c71512973e93c0') =` **faefbbbeddcdabeebbfffdbdaeb**53a8c | [Polly](https://github.com/FuzzyLitchi) |
| 3 | **Gold MD5** | 12 |`md5('54db1011d76dc70a0a9df3ff3e0b390f') =` **54db1011d76d**137956603122ad86d762 | [Thomas Egense](https://stackoverflow.com/a/28941658/1909132) |
| 4 | **Nice match** | 10 |`md5('665d8e9f2d6a6c5cc54d97b1b9aaefe6') =` **2222222222**c237bb277df9573d27f13f  | zvibazak |
| 5 | **Pi MD5** | 11 |`md5(b100d474eb100d60d000b08822844917) =` **31415926535**f1ade4ad780c95815f2dc | [Polly](https://github.com/FuzzyLitchi) |
| 6 | **e MD5** | 9 |`md5('6a751b7229da6c73cb26144abc17ae7c') =` **271828182**eb107ef23900482d683ddc0 | [Polly](https://github.com/FuzzyLitchi) |

## Links
* [Is there an MD5 Fixed Point where md5(x) == x?](https://stackoverflow.com/questions/235785/is-there-an-md5-fixed-point-where-md5x-x) - A question on StackOverflow.
* [MD5: Existence of invariant (fixed point)](https://crypto.stackexchange.com/questions/68674/md5-existence-of-invariant-fixed-point) - A question on crypto.stackexchange.com.
* [Finding Nice MD5s Using Rust](https://blog.youmu.moe/posts/finding-nice-md5s-using-rust) - by 妖夢ちゃん (submitted by [FuzzyLitchi](https://github.com/FuzzyLitchi)).
* [Rust program to find "nice" md5s](https://github.com/FuzzyLitchi/nice-md5s-rs) - by [FuzzyLitchi](https://github.com/FuzzyLitchi).
* [A terminal app to find nice MD5s](https://github.com/johnmave126/nice-md5s) - by [johnmave126](https://github.com/johnmave126).
