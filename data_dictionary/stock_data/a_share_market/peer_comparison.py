import akshare as ak


# 同行比较
class PeerComparison:
    @staticmethod
    def stock_zh_growth_comparison_em():
        """
        描述：东方财富-行情中心-同行比较-成长性比较
        限量：单次返回全部数据
        :param
            symbol | str | symbol="SZ000895"
        :return
            代码 | object | -
            简称 | object | -
            基本每股收益增长率-3年复合 | float64 | -
            基本每股收益增长率-24A | float64 | -
            基本每股收益增长率-TTM | float64 | -
            基本每股收益增长率-25E | float64 | -
            基本每股收益增长率-26E | float64 | -
            基本每股收益增长率-27E | float64 | -
            营业收入增长率-3年复合 | float64 | -
            营业收入增长率-24A | float64 | -
            营业收入增长率-TTM | float64 | -
            营业收入增长率-25E | float64 | -
            营业收入增长率-26E | float64 | -
            营业收入增长率-27E | float64 | -
            净利润增长率-3年复合 | float64 | -
            净利润增长率-24A | float64 | -
            净利润增长率-TTM | float64 | -
            净利润增长率-25E | float64 | -
            净利润增长率-26E | float64 | -
            净利润增长率-27E | float64 | -
            基本每股收益增长率-3年复合排名 | float64 | -
        """

        stock_zh_growth_comparison_em_df = ak.stock_zh_growth_comparison_em(symbol="SZ000895")
        print(stock_zh_growth_comparison_em_df)

    @staticmethod
    def stock_zh_valuation_comparison_em():
        """
        描述：东方财富-行情中心-同行比较-估值比较
        限量：单次返回全部数据
        :param
            symbol | str | symbol="SZ000895"
        :return
            排名 | object | -
            代码 | object | -
            简称 | object | -
            PEG | float64 | -
            市盈率-24A | float64 | -
            市盈率-TTM | float64 | -
            市盈率-25E | float64 | -
            市盈率-26E | float64 | -
            市盈率-27E | float64 | -
            市销率-24A | float64 | -
            市销率-TTM | float64 | -
            市销率-25E | float64 | -
            市销率-26E | float64 | -
            市销率-27E | float64 | -
            市净率-24A | float64 | -
            市净率-MRQ | float64 | -
            市现率1-24A | float64 | -
            市现率1-TTM | float64 | -
            市现率2-24A | float64 | -
            市现率2-TTM | float64 | -
            EV/EBITDA-24A | float64 | -
        """

        stock_zh_valuation_comparison_em_df = ak.stock_zh_valuation_comparison_em(symbol="SZ000895")
        print(stock_zh_valuation_comparison_em_df)

    @staticmethod
    def stock_zh_dupont_comparison_em():
        """
        描述：东方财富-行情中心-同行比较-杜邦分析比较
        限量：单次返回全部数据
        :param
            symbol | str | symbol="SZ000895"
        :return
            代码 | object | -
            简称 | object | -
            ROE-3年平均 | float64 | -
            ROE-22A | float64 | -
            ROE-23A | float64 | -
            ROE-24A | float64 | -
            净利率-3年平均 | float64 | -
            净利率-22A | float64 | -
            净利率-23A | float64 | -
            净利率-24A | float64 | -
            总资产周转率-3年平均 | float64 | -
            总资产周转率-22A | float64 | -
            总资产周转率-23A | float64 | -
            总资产周转率-24A | float64 | -
            权益乘数-3年平均 | float64 | -
            权益乘数-22A | float64 | -
            权益乘数-23A | float64 | -
            权益乘数-24A | float64 | -
            ROE-3年平均排名 | float64 | -
        """

        stock_zh_dupont_comparison_em_df = ak.stock_zh_dupont_comparison_em(symbol="SZ000895")
        print(stock_zh_dupont_comparison_em_df)

    @staticmethod
    def stock_zh_scale_comparison_em():
        """
        描述：东方财富-行情中心-同行比较-公司规模
        限量：单次返回全部数据
        :param
            symbol | str | symbol="SZ000895"
        :return
            代码 | object | -
            简称 | object | -
            总市值 | float64 | -
            总市值排名 | int64 | -
            流通市值 | float64 | -
            流通市值排名 | int64 | -
            营业收入 | float64 | -
            营业收入排名 | int64 | -
            净利润 | float64 | -
            净利润排名 | int64 | -
        """

        stock_zh_scale_comparison_em_df = ak.stock_zh_scale_comparison_em(symbol="SZ000895")
        print(stock_zh_scale_comparison_em_df)
