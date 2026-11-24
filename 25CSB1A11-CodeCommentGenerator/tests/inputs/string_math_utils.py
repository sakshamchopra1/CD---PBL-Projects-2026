"""
String & Math Utility Sample.
Tests simple scalar arguments, return types, and algorithmic loops.
"""

def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9 / 5) + 32


def is_palindrome(text: str) -> bool:
    cleaned = "".join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]


def find_primes(n: int) -> list:
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]
