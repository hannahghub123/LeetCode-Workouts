'''2864. Maximum Odd Binary Number

You are given a binary string s that contains at least one '1'.

You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can be created from this combination.

Return a string representing the maximum odd binary number that can be created from the given combination.

Note that the resulting string can have leading zeros.

Example 1:

Input: s = "010"
Output: "001"
Explanation: Because there is just one '1', it must be in the last position. So the answer is "001".
Example 2:

Input: s = "0101"
Output: "1001"
Explanation: One of the '1's must be in the last position. The maximum number that can be made with the remaining digits is "100". So the answer is "1001".
'''

# solution 1:
def max_odd_num(s):

    s=sorted(list(s))
    s=s[::-1]

    for i in range(len(s)):
        if s[i]=='1':
            index=i

    if s[-1]=='0':
        s[-1],s[index]=s[index],s[-1]

    s=''.join(s)
    return s


# solution 2:
def max_odd_binary_num(s):
    s=sorted(list(s))
    s=s[::-1]

    temp=s.pop(0)
    s.append(temp)

    s=''.join(s)

    return s


s="1011"
print(max_odd_num(s))
print(max_odd_binary_num(s))