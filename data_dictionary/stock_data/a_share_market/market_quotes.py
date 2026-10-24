import akshare as ak


# 行情报价
class MarketQuotes:
    @staticmethod
    def stock_bid_ask_em():
        """
        描述：东方财富-行情报价
        限量：单次返回指定股票的行情报价数据
        :param
            symbol | str | symbol="000001"；股票代码
        :return
            item | object | -
            value | float64 | -
        """

        stock_bid_ask_em_df = ak.stock_bid_ask_em(symbol="000001")
        print(stock_bid_ask_em_df)
