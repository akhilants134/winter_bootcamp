MOD = 10**9 + 7

# Recursive function to count good numbers
def count_good_numbers(index, n):
    # Base case: if we've reached the end of the string
    if index == n:
        return 1

    result = 0
    # Even index: Use even digits
    if index % 2 == 0:  
        even_digits = [0, 2, 4, 6, 8]
        for digit in even_digits:
            result = (result + count_good_numbers(index + 1, n)) % MOD
    # Odd index: Use prime digits        
    else:
        prime_digits = [2, 3, 5, 7]
        for digit in prime_digits:
            result = (result + count_good_numbers(index + 1, n)) % MOD
    return result

# Main function
if __name__ == "__main__":
    n = 1
    print(count_good_numbers(0, n))
