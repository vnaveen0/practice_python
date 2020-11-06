class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        mem = {}
        i_mem = {}
        
        prev_long = 0 
        longest_so_far = 0 
        prev_start_idx = 0 
        for idx, char in enumerate(s):
            old_idx = None 
            if char in mem:
                old_idx = mem[char]
                longest_so_far = max(longest_so_far, prev_long)
                prev_long = idx - prev_start_idx
                print('c:{} o:{} n:{} pl:{}'.format(char, old_idx, idx, prev_long))
                # todo: del all keys from 0-- oldidx
                for i in range(prev_start_idx,old_idx+1):
                    # mem = {key:val for key, val in mem.items() if val != i}
                    toremove_char = i_mem[i]
                    del mem[toremove_char]
                    del i_mem[i]
                    
                prev_start_idx = old_idx + 1 
                    
                # store  idx again. 
                mem[char] = idx 
                i_mem[idx] = char
                print(mem)
                print(i_mem)
                
            else: 
                prev_long +=1
                mem[char] = idx
                i_mem[idx] = char 
                longest_so_far = max(longest_so_far, prev_long)
   
        longest_so_far = max(longest_so_far, prev_long)    
        return longest_so_far
            
            
