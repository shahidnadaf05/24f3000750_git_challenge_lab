import prime
import even_odd
import factorial
number = int(input())
print(f"Is {number} prime? {prime.is_prime(number)}")
print(f"Is {number} even? {even_odd.is_even(number)}")
print(f"Factorial of {number} = {factorial.compute_factorial(number)}")