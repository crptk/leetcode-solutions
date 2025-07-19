class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1
        for char in t:
            if char in t_dict:
                t_dict[char] += 1
            else:
                t_dict[char] = 1

        print(f"s_dict: {s_dict}")
        print(f"t_dict: {t_dict}")
        return s_dict == t_dict

'''
Solution by Edrees

My first approach was to check if the set of both dictionaries equaled each other, but the problem was that if a letter was repeated more times in one string compared to the other, it would still yield the results because it still aligns with the properties of a set. So I figured, how can I keep track of the presence of characters in both strings, AND the count of each character at the same time? The answer was dictionaries. So I put all the characters of both strings into a dictionary and kept track of the count of all their characters, which allowed me to hit both nails on the head and solve the problem. This solution has a time complexity of O(n) and a space complexity of O(1) since there can at most be 26 characters in a string.
'''