'''1002. Find Common Characters

Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]'''

from collections import Counter

def common_chars(words):
    temp_list=Counter(list(words[0]))

    for i in range(1,len(words)):
        temp_list&=Counter(list(words[i]))

        
    return list(temp_list.elements())



words =["bella","label","roller"]
print(common_chars(words))