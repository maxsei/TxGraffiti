import pandas as pd
from sympy import divisors, totient, mobius, primefactors

def prod(iterable):
    p = 1
    for n in iterable:
        p *= n
    return p


# Define our functions
def number_of_divisors(n):
    return len(divisors(n))

def sum_of_divisors(n):
    return sum(divisors(n))

def euler_totient(n):
    return totient(n)

def mobius_function(n):
    return mobius(n)

def sum_of_proper_divisors(n):
    return sum(divisors(n)) - n

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def product_of_digits(n):
    return prod(int(digit) for digit in str(n))

def number_of_prime_factors(n):
    return len(primefactors(n))

def number_of_distinct_prime_factors(n):
    return len(set(primefactors(n)))

# Create a dataframe to store our results
df = pd.DataFrame(index=range(1, 101), columns=[
    'Number of Divisors',
    'Sum of Divisors',
    'Euler Totient',
    'Mobius Function',
    'Sum of Proper Divisors',
    'Sum of Digits',
    'Product of Digits',
    'Number of Prime Factors',
    'Number of Distinct Prime Factors'
])

# Compute our functions for each integer
for n in range(1, 101):
    df.loc[n, 'name'] = f"{n}"
    df.loc[n, 'Number of Divisors'] = number_of_divisors(n)
    df.loc[n, 'Sum of Divisors'] = sum_of_divisors(n)
    df.loc[n, 'Euler Totient'] = euler_totient(n)
    df.loc[n, 'Mobius Function'] = mobius_function(n)
    df.loc[n, 'Sum of Proper Divisors'] = sum_of_proper_divisors(n)
    df.loc[n, 'Sum of Digits'] = sum_of_digits(n)
    df.loc[n, 'Product of Digits'] = product_of_digits(n)
    df.loc[n, 'Number of Prime Factors'] = number_of_prime_factors(n)
    df.loc[n, 'Number of Distinct Prime Factors'] = number_of_distinct_prime_factors(n)

# Save to a CSV file
df.to_csv('math_data/data/integers.csv')