class Solution1(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if prices is None:
            return 0

        def update_profit(g_profit, c_profit):
            if g_profit < c_profit:
                g_profit = c_profit
            return g_profit

        N = len(prices)
        g_profit = 0
        for i in range(0, N):
            for j in range(i + 1, N):
                buy = prices[i]
                sell = prices[j]
                cur_profit = sell - buy
                g_profit = update_profit(g_profit, cur_profit)

        if g_profit < 0:
            return 0
        else:
            return g_profit


class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if prices is None:
            return 0

        def update_max_sell_price(mem, s_price, idx):
            if mem is None:
                mem = [None, None]
                mem[0] = idx
                mem[1] = s_price
            else:
                if mem[1] < s_price:
                    mem[0] = idx
                    mem[1] = s_price

            return mem

        def update_profit(g_profit, c_profit):
            if g_profit < c_profit:
                g_profit = c_profit
            return g_profit

        N = len(prices)
        g_profit = 0
        max_sprice_mem = None

        for i in range(0, N):
            buy = prices[i]
            if max_sprice_mem is None:
                for j in range(i + 1, N):
                    sell = prices[j]
                    update_max_sell_price(max_sprice_mem, sell, j)
                    cur_profit = sell - buy
                    g_profit = update_profit(g_profit, cur_profit)
            elif i < max_sprice_mem[0]:
                start_j, sell = max_sprice_mem
                cur_profit = sell - buy
                g_profit = update_profit(g_profit, cur_profit)
            else:
                max_sprice_mem = None
                for j in range(i + 1, N):
                    sell = prices[j]
                    update_max_sell_price(max_sprice_mem, sell, j)
                    cur_profit = sell - buy
                    g_profit = update_profit(g_profit, cur_profit)

        if g_profit < 0:
            return 0
        else:
            return g_profit


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        def update_profit(g_profit, c_profit):
            if g_profit < c_profit:
                g_profit = c_profit
            return g_profit

        minPrice = None
        maxPrice = None
        gProfit = 0
        for idx, c_price in enumerate(prices):
            if minPrice is None or c_price <= minPrice:
                # Keep updating minPrice
                minPrice = c_price

            else:
                # Update maxPrice
                if maxPrice is None or c_price > minPrice:
                    # Keep updating maxPrice
                    maxPrice = c_price
                    c_profit = maxPrice - minPrice
                    gProfit = update_profit(gProfit, c_profit)

                else:
                    # Reset
                    minPrice = c_price
                    maxPrice = None

        if gProfit <= 0:
            return 0
        else:
            return gProfit