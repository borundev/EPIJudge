from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    running_min_price=float('inf')
    running_max_profit=0.0

    for price in prices:
        running_max_profit=max(running_max_profit,price-running_min_price)
        running_min_price=min(running_min_price,price)

    return running_max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
