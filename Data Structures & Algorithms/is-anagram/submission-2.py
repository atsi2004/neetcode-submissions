class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)): # Not an anagram if lengths differ
            return False
        s_freq = {}
        t_freq = {}

        for char in s: # iterate through s string
            if char in s_freq: # if character already in dict
                s_freq[char] += 1 # add 1 to its freq
            else:
                s_freq[char] = 1 # otherwise set freq to 1
        for char in t:
            if char in t_freq:
                t_freq[char] += 1
            else:
                t_freq[char] = 1
    
        if(t_freq == s_freq): # if the frequencies of both are the same
            return True # strings are anagrams
        else:
            return False

