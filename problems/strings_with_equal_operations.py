'''2839. Check if Strings Can be Made Equal With Operations I

You are given two strings s1 and s2, both of length 4, consisting of lowercase English letters.

You can apply the following operation on any of the two strings any number of times:

Choose any two indices i and j such that j - i = 2, then swap the two characters at those indices in the string.
Return true if you can make the strings s1 and s2 equal, and false otherwise.

Example 1:

Input: s1 = "abcd", s2 = "cdab"
Output: true
Explanation: We can do the following operations on s1:
- Choose the indices i = 0, j = 2. The resulting string is s1 = "cbad".
- Choose the indices i = 1, j = 3. The resulting string is s1 = "cdab" = s2.

Example 2:

Input: s1 = "abcd", s2 = "dacb"
Output: false
Explanation: It is not possible to make the two strings equal.
'''

def strings_with_equal_operations(s1,s2):
    n=len(s1)
    s1=list(s1)
    demo_s1=list(s1)
    if s1==s2:
        return True
    else:


        for i in range(n//2):
            j=2+i
            if j<len(s1):
                s1[i],s1[j]=s1[j],s1[i]

            if ''.join(s1)==s2:
                return True
        
        s1=demo_s1

        for i in range(n-1,n//2,-1):
            j=i-2
            if j<len(s1):
                s1[i],s1[j]=s1[j],s1[i]

            if ''.join(s1)==s2:
                return True
    
    return False



s1 = "abcd"
s2 = "dacb"

print(strings_with_equal_operations(s1,s2))
