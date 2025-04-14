# Challenge 1: Large Power
def large_power(base, exponent):
    result = base ** exponent
    if result > 5000:
        return True
    else:
        return False

# Test cases for large_power
print("Testing large_power:")
print(large_power(2, 13))  # Should return True (2^13 = 8192)
print(large_power(2, 12))  # Should return False (2^12 = 4096)
print(large_power(10, 3))  # Should return False (10^3 = 1000)
print(large_power(10, 4))  # Should return True (10^4 = 10000)

# Challenge 2: Divisible By Ten
def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False

# Test cases for divisible_by_ten
print("\nTesting divisible_by_ten:")
print(divisible_by_ten(20))  # Should return True
print(divisible_by_ten(25))  # Should return False
print(divisible_by_ten(100))  # Should return True
print(divisible_by_ten(101))  # Should return False