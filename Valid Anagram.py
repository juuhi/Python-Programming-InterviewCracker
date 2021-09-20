Valid Anagram
Easy

Given two strings s and t, return true if t is an anagram of s, and false otherwise.


Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

############################################################ Solution ############################################

    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        
        for j in t:
            if j not in dic:
                return False
            else:
                dic[j] -= 1
        
        for val in dic.values():
            if val != 0:
                return False
        return True
      
   
  
  ################################################## Another effective way to solve the probleem, but both are coorect for interview ##########################
  
    def isAnagram(self, s: str, t: str) -> bool:
        dic1, dic2 = {}, {}
        for item in s:
            dic1[item] = dic1.get(item, 0) + 1
        for item in t:
            dic2[item] = dic2.get(item, 0) + 1
        return dic1 == dic2
      
 # In this case get function, use to get the key and then we initilize it with 0 for the increments.


