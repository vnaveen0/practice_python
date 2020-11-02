class Solution0(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        g_max=0
        last = None
        LR_stack = []
        is_push = True
        
        def update_status(val, g_max, last, LR_stack, is_push):
            
            if is_push:
                LR_stack.append(val)
                last = val
                print('push: {}'.format(val))
            else: 
                if LR_stack:
                    LR_stack.pop()
                    last = val 
                    print('pop: {}'.format(val))
                    
                    if not LR_stack:
                        g_max +=1
                        is_push = True 
                        last = None
                        print('g_max: {}'.format(g_max))
                        
                else: 
                    return g_max
            return g_max, last, LR_stack, is_push
            
        

        
        
        for val in s: 
            if val == last or last is None:
                g_max, last, LR_stack, is_push = update_status(val, g_max, last, LR_stack, is_push)
            else: 
                is_push = not is_push
                g_max, last, LR_stack, is_push = update_status(val, g_max, last, LR_stack, is_push)
            
            print(g_max)
        
        return g_max 
