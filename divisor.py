class Solution2(object):
    def __init__(self):
        print('Divisor Game')
        self.memory = {0:{}, 1:{}}
        # self.LOST=False
        # self.WIN=True

    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        depth = 1
        depth, iswin = self.check_future(depth, N)

        d = depth % 2
        # if d==0 => Bob's result
        if d == 0:
            print('*** for vals :{}, new num: {}, ans: {}'.format(d, N, iswin))
            return not iswin
        else: # ALis's result
            return iswin

    def check_future(self, depth, N):
        d = depth%2
        if N in self.memory[d]:
            iswin = self.memory[d][N]
            print('--* for vals :{}, new num: {}, ans: {}'.format(d, N, iswin))
            return depth, iswin

        # elif N < 0:
        #     depth += 1
        #     print('-- - for vals :{}, new num: {}, ans: {}'.format(d, N, ans))
        #     return depth, True
        elif N == 1:
            d = depth%2
            if d == 0:
                ans=True
            else:
                ans=False
            print('-- - for vals :{}, new num: {}, ans: {}'.format(d, N, ans))
            self.memory[d][N] = ans
            return depth, False
        elif N == 2:
            d = depth%2
            if d == 0:
                ans=False
            else:
                ans=True
            print('-- - for vals :{}, new num: {}, ans: {}'.format(d, N, ans))
            self.memory[d][N] = ans
            return depth, ans

        else:
            x = self.search_selected_numbers(N)
            print('sel num:{}'.format(x))

            orig_depth = depth
            for idx, selected_val in enumerate(x):
                # Alice's turn
                depth = orig_depth + 1
                new_num = N - selected_val
                # Bob's turn
                print('for vals :{}, new num: {}'.format(selected_val, new_num))
                _, is_win = self.check_future(depth, new_num)
                d= (depth)%2
                self.memory[d][new_num] = is_win

                if not is_win:
                    continue
                else:
                    return depth, is_win
            # end for
            d = orig_depth%2
            print('-- for vals :{}, new num: {}, ans: {}'.format(d, N, False))
            return orig_depth, False

    def search_selected_numbers(self, N):
        x = []
        for i in range(1, N):
            if N % i == 0:
                x.append(i)
        return x

class Solution(object):
    def __init__(self):
        print('Divisor Game')

    def divisorGame(self, N):
        memory = {}
        return self.canWin(N,memory)

    def canWin(self, N, memory):
        if N < 1:
            return True
        elif N == 1:
            return False
        if N in memory.keys():
            return memory[N]

        max_val = int(N/2 + 1 )
        for x in range(1,max_val):
            if N%x == 0:
                if not self.canWin(N-x, memory):
                    memory[N] = True
                    return True
        memory[N] = False
        return False


if __name__ == '__main__':
    soln = Solution()
    x=4
    ans = soln.divisorGame(x)
    print('Input: {} Output: {}'.format(x,ans))
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
