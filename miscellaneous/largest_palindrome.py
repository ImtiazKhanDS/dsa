def largest_palindromic_number(S):
    # Step 1: Count occurrences of each digit
    digit_counts = [0] * 10
    for digit in S:
        digit_counts[int(digit)] += 1
    
    # Step 2: Construct the largest palindromic number
    largest_palindrome = ""
    for i in range(9, -1, -1):  # Start from 9 and move downwards
        largest_palindrome += str(i) * digit_counts[i]
    
    # Step 3: Ensure no leading zeros
    largest_palindrome = largest_palindrome.lstrip("0")
    
    # Step 4: Return the largest palindromic number
    return largest_palindrome if largest_palindrome else "0"

# Example usage:
S = "8199"
result = largest_palindromic_number(S)
print("Largest palindromic number:", result)
