# Goal
# Given a string, output the sum of each ASCII character value multiplied by its index in the string
# Input
# Line 1: A string S
# Output
# Line 1: The sum of each ASCII character value multiplied by its index.

# Example: ABC => 65*0 + 66*1 + 67*2 => 200
# Constraints
# The string contains no space.
# Example
# Input
# ABC
# Output
# 200

s = input()
a = 0
for i in range(len(s)):
    a+=ord(s[i])*i
print(a)

# Test Cases
# 1) Test 1
# Input
# ABC
# Expected output
# 200

# 2) Test 2
# Input
# ASCII
# Expected output
# 728

# 3) Test 3
# Input
# index
# Expected output
# 1093

# 4) Test 4
# Input
# CoDiNgAmE
# Expected output
# 3094

