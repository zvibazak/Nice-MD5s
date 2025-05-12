# Nice-MD5s

Let’s explore *nice patterns* in MD5 hashes!

> The MD5 message-digest algorithm is a widely used hash function producing a 128-bit digest. ([Wikipedia](https://en.wikipedia.org/wiki/MD5))

This is totally nonsensical, but let’s have some fun discovering interesting MD5 patterns.

Check out this [small website for exploration](https://zvibazak.github.io/Nice-MD5s/)!

## Definitions

A *nice pattern* is one of the following:

| #  | Name                 | Description                                                              | Example                                               |
|:--:|----------------------|--------------------------------------------------------------------------|-------------------------------------------------------|
| 1  | **Perfect match**    | MD5 hash of a single character                                           | `00000000000000000000000000000000`                    |
| 2  | **Nice match**       | MD5 hash that starts with *N* identical characters                       | `444431252d6a104a05fe4a0c6a53a999` (N = 4)            |
| 3  | **Gold MD5**         | MD5 hash that equals the input string                                     | _None found (fixed points)_                           |
| 4  | **Digits-only MD5**  | MD5 hash composed entirely of digits                                      | `25855924411269249612523541155616`                    |
| 5  | **Letters-only MD5** | MD5 hash composed entirely of letters                                     | `abcdefabcdefabcdefabcdefabcdefab`                    |
| 6  | **Pi MD5**           | MD5 hash that begins with the digits of π                                 | `3141592653589793115997963468544185`                  |
| 7  | **e MD5**            | MD5 hash that begins with the digits of *e*                               | `2718281828459045090795598298427649`                  |
| 8  | **Prefix & Suffix**  | MD5 hash that starts and ends with the same *N* characters as the input  | `1234…259a` (N = 4)                                    |

Feel free to clone the repository, run the code locally, and submit a pull request if you discover a new pattern (credit is guaranteed!). Implementations in any language are welcome.

## Hall of Fame

| #  | Pattern              | N   | MD5                                                                                                   | Contributor                                    |
|:--:|----------------------|:---:|-------------------------------------------------------------------------------------------------------|------------------------------------------------|
| 1  | **Digits-only MD5**  | ✅ **32**  | `md5('r8z43szwn6duks2yoqf6eaugebdjdhfk') = 52028506537132879258425329778418`                         | [zvibazak](https://github.com/zvibazak)       |
| 2  | **Letters-only MD5** | ✅ **32**  | `md5('b100d474eb100d60d0421b2afb8164ae') = adeeabedeabdbeffbcbdeeadaacedaaf`                         | [Polly](https://github.com/FuzzyLitchi)       |
| 3  | **Gold MD5**         | 12  | `md5('54db1011d76dc70a0a9df3ff3e0b390f') = 54db1011d76d137956603122ad86d762`                         | [Thomas Egense](https://stackoverflow.com/a/28941658/1909132) |
| 4  | **Nice match**       | 13  | `md5('b100d474eb100d60d042e863c1e0adee') = 00000000000008d71ef80eb3849237d2`                         | [Polly](https://github.com/FuzzyLitchi)       |
| 5  | **Pi MD5**           | 12  | `md5('b100d474eb100d60d04261106c3f04b5') = 314159265358ea7fd5dc7f0fab21378a`                         | [Polly](https://github.com/FuzzyLitchi)       |
| 6  | **e MD5**            | 12  | `md5('b100d474eb100d60d069f893a7c2ac27') = 2718281828453f28da829b05f35113e2`                         | [Polly](https://github.com/FuzzyLitchi)       |
| 7  | **Prefix & Suffix**  | 4   | `md5('1234f7520c2e4c1204c8c14f3d31259a') = 1234aee3988ccd2b48751ca7543d259a`                         | [tianshuo](https://github.com/tianshuo)       |

## Resources

- [Is there an MD5 fixed point where `md5(x) == x`?](https://stackoverflow.com/questions/235785/is-there-an-md5-fixed-point-where-md5x-x) – Stack Overflow.
- [MD5: Existence of an invariant (fixed point)](https://crypto.stackexchange.com/questions/68674/md5-existence-of-invariant-fixed-point) – Crypto.StackExchange.
- [Can an MD5 hash contain only numbers or only letters?](https://stackoverflow.com/questions/6825714/can-an-md5-hash-have-only-numbers-or-only-letters-in-it) – Stack Overflow.
- [Finding Nice MD5s Using Rust](https://blog.youmu.moe/posts/finding-nice-md5s-using-rust) – by 妖夢ちゃん (submitted by [FuzzyLitchi](https://github.com/FuzzyLitchi)).
- [Rust program to find "nice" MD5s](https://github.com/FuzzyLitchi/nice-md5s-rs) – by [FuzzyLitchi](https://github.com/FuzzyLitchi).
- [A terminal app to find nice MD5s](https://github.com/johnmave126/nice-md5s) – by [johnmave126](https://github.com/johnmave126).
