# Find the first repeated character in a string
def firstRepeatedChar(str):
         
        h = {} # Create empty hash
        #strin = lower(str)
         
            # Traverse each characters in string
            # in lower case order
        for ch in str.lower():
         
                # If character is already present
                # in hash, return char
            if ch in h:
                return ch;
         
                # Add ch to hash
            else:
                h[ch] = 1
                #print(h)
         
        return 'No common letter is found'
        
print(firstRepeatedChar("saiS"))
