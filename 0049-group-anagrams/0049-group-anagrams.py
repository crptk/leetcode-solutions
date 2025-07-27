from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # This allows us to use a dictionary where missing keys automatically create empty lists
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a ... z

            # Adds 1 to the array of 26 zeros
            for c in s:
                count[ord(c) - ord("a")] += 1

            # Creates an entry for this letter count key, if it exists just append it
            res[tuple(count)].append(s) # We're only converting to tuple cuz python doesn't accept otherwise
        
        # Return the values (all the group anagrams)
        return list(res.values())

'''
In order to solve this we use a hashmap with a default value of []. We create unique ids/indexes for each word
by creating a list of 26 zeros (26 letters of alphabet) then we add 1 to the index that corresponds to the character
for the word that we're on. This will produce a unique id for that anagram. If the anagram is one that we haven't seen before
(i.e, a unique anagram id), then create a new pair of key and value. If the key already exists, then append the value to the key.
This has a time complexity of O(n * m) where n is the program iterating through the whole list, and m is the program itertating through
each character of each word.

Final solution becomes like this:

    (1,0,0,0,1,0,...1...): ['tea', 'eat', 'ate'],  # Group 1
    (1,0,0,0,0,0,...1,1): ['tan', 'nat'],         # Group 2
    (1,1,0,...): ['bat']                          # Group 3
'''