import akshare as ak


# 个股信息查询
class StockIndividualInfo:
    @staticmethod
    def stock_individual_info_em():
        """
        描述：东方财富-个股-股票信息
        限量：单次返回指定 symbol 的个股信息
        说明：接口已兼容东方财富返回体偶发新增的顶层元数据字段，如 dsc
        :param
            symbol | str | symbol="603777"；股票代码
            timeout | float | timeout=None；默认不设置超时参数
        :return
            item | object | -
            value | object | -
        """

        stock_individual_info_em_df = ak.stock_individual_info_em(symbol="000001")
        print(stock_individual_info_em_df)

    @staticmethod
    def stock_individual_basic_info_xq():
        """
        描述：雪球财经-个股-公司概况-公司简介
        限量：单次返回指定 symbol 的个股信息
        :param
            symbol | str | symbol="SH601127"；股票代码
            token | str | token=None；雪球 xq_a_token
            timeout | float | timeout=None；默认不设置超时参数
        :return
            item | object | -
            value | object | -
        """

        stock_individual_basic_info_xq_df = ak.stock_individual_basic_info_xq(symbol="SH601127")
        print(stock_individual_basic_info_xq_df)
