import akshare as ak


# 实时行情数据
class RealTimeMarketData:
    @staticmethod
    def stock_zh_a_spot_em():
        """
        描述：东方财富网-沪深京 A 股-实时行情数据
        限量：单次返回所有沪深京 A 股上市公司的实时行情数据
        :param
            无
        :return
            序号 | int64 | -
            代码 | object | -
            名称 | object | -
            最新价 | float64 | -
            涨跌幅 | float64 | 注意单位：%
            涨跌额 | float64 | -
            成交量 | float64 | 注意单位：手
            成交额 | float64 | 注意单位：元
            振幅 | float64 | 注意单位：%
            最高 | float64 | -
            最低 | float64 | -
            今开 | float64 | -
            昨收 | float64 | -
            量比 | float64 | -
            换手率 | float64 | 注意单位：%
            市盈率-动态 | float64 | -
            市净率 | float64 | -
            总市值 | float64 | 注意单位：元
            流通市值 | float64 | 注意单位：元
            涨速 | float64 | -
            5分钟涨跌 | float64 | 注意单位：%
            60日涨跌幅 | float64 | 注意单位：%
            年初至今涨跌幅 | float64 | 注意单位：%
        """

        stock_zh_a_spot_em_df = ak.stock_zh_a_spot_em()
        print(stock_zh_a_spot_em_df)

    @staticmethod
    def stock_sh_a_spot_em():
        """
        描述：东方财富网-沪 A 股-实时行情数据
        限量：单次返回所有沪 A 股上市公司的实时行情数据
        :param
            无
        :return
            序号 | int64 | -
            代码 | object | -
            名称 | object | -
            最新价 | float64 | -
            涨跌幅 | float64 | 注意单位：%
            涨跌额 | float64 | -
            成交量 | float64 | 注意单位：手
            成交额 | float64 | 注意单位：元
            振幅 | float64 | 注意单位：%
            最高 | float64 | -
            最低 | float64 | -
            今开 | float64 | -
            昨收 | float64 | -
            量比 | float64 | -
            换手率 | float64 | 注意单位：%
            市盈率-动态 | float64 | -
            市净率 | float64 | -
            总市值 | float64 | 注意单位：元
            流通市值 | float64 | 注意单位：元
            涨速 | float64 | -
            5分钟涨跌 | float64 | 注意单位：%
            60日涨跌幅 | float64 | 注意单位：%
            年初至今涨跌幅 | float64 | 注意单位：%
        """

        stock_sh_a_spot_em_df = ak.stock_sh_a_spot_em()
        print(stock_sh_a_spot_em_df)

    @staticmethod
    def stock_sz_a_spot_em():
        """
        描述：东方财富网-深 A 股-实时行情数据
        限量：单次返回所有深 A 股上市公司的实时行情数据
        :param
            无
        :return
            序号 | int64 | -
            代码 | object | -
            名称 | object | -
            最新价 | float64 | -
            涨跌幅 | float64 | 注意单位：%
            涨跌额 | float64 | -
            成交量 | float64 | 注意单位：手
            成交额 | float64 | 注意单位：元
            振幅 | float64 | 注意单位：%
            最高 | float64 | -
            最低 | float64 | -
            今开 | float64 | -
            昨收 | float64 | -
            量比 | float64 | -
            换手率 | float64 | 注意单位：%
            市盈率-动态 | float64 | -
            市净率 | float64 | -
            总市值 | float64 | 注意单位：元
            流通市值 | float64 | 注意单位：元
            涨速 | float64 | -
            5分钟涨跌 | float64 | 注意单位：%
            60日涨跌幅 | float64 | 注意单位：%
            年初至今涨跌幅 | float64 | 注意单位：%
        """

        stock_sz_a_spot_em_df = ak.stock_sz_a_spot_em()
        print(stock_sz_a_spot_em_df)

    @staticmethod
    def stock_bj_a_spot_em():
        """
        描述：东方财富网-京 A 股-实时行情数据
        限量：单次返回所有京 A 股上市公司的实时行情数据
        :param
            无
        :return
            序号 | int64 | -
            代码 | object | -
            名称 | object | -
            最新价 | float64 | -
            涨跌幅 | float64 | 注意单位：%
            涨跌额 | float64 | -
            成交量 | float64 | 注意单位：手
            成交额 | float64 | 注意单位：元
            振幅 | float64 | 注意单位：%
            最高 | float64 | -
            最低 | float64 | -
            今开 | float64 | -
            昨收 | float64 | -
            量比 | float64 | -
            换手率 | float64 | 注意单位：%
            市盈率-动态 | float64 | -
            市净率 | float64 | -
            总市值 | float64 | 注意单位：元
            流通市值 | float64 | 注意单位：元
            涨速 | float64 | -
            5分钟涨跌 | float64 | 注意单位：%
            60日涨跌幅 | float64 | 注意单位：%
            年初至今涨跌幅 | float64 | 注意单位：%
        """

        stock_bj_a_spot_em_df = ak.stock_bj_a_spot_em()
        print(stock_bj_a_spot_em_df)

    @staticmethod
    def stock_new_a_spot_em():
        """
        描述：东方财富网-新股-实时行情数据
        限量：单次返回所有新股上市公司的实时行情数据
        :param
            无
        :return
            序号 | int64 | -
            代码 | object | -
            名称 | object | -
            最新价 | float64 | -
            涨跌幅 | float64 | 注意单位：%
            涨跌额 | float64 | -
            成交量 | float64 | 注意单位：手
            成交额 | float64 | 注意单位：元
            振幅 | float64 | 注意单位：%
            最高 | float64 | -
            最低 | float64 | -
            今开 | float64 | -
            昨收 | float64 | -
            量比 | float64 | -
            换手率 | float64 | 注意单位：%
            市盈率-动态 | float64 | -
            市净率 | float64 | -
            上市时间 | object | -
            总市值 | float64 | 注意单位：元
            流通市值 | float64 | 注意单位：元
            涨速 | float64 | -
            5分钟涨跌 | float64 | 注意单位：%
            60日涨跌幅 | float64 | 注意单位：%
            年初至今涨跌幅 | float64 | 注意单位：%
        """

        stock_new_a_spot_em_df = ak.stock_new_a_spot_em()
        print(stock_new_a_spot_em_df)

    @staticmethod
    def stock_cy_a_spot_em():
        """
        描述：东方财富网-创业板-实时行情
        限量：单次返回所有创业板的实时行情数据
        :param
            无
        :return
            序号 | int64 | -
            代码 | object | -
            名称 | object | -
            最新价 | float64 | -
            涨跌幅 | float64 | 注意单位：%
            涨跌额 | float64 | -
            成交量 | float64 | 注意单位：手
            成交额 | float64 | 注意单位：元
            振幅 | float64 | 注意单位：%
            最高 | float64 | -
            最低 | float64 | -
            今开 | float64 | -
            昨收 | float64 | -
            量比 | float64 | -
            换手率 | float64 | 注意单位：%
            市盈率-动态 | float64 | -
            市净率 | float64 | -
            总市值 | float64 | 注意单位：元
            流通市值 | float64 | 注意单位：元
            涨速 | float64 | -
            5分钟涨跌 | float64 | 注意单位：%
            60日涨跌幅 | float64 | 注意单位：%
            年初至今涨跌幅 | float64 | 注意单位：%
        """

        stock_cy_a_spot_em_df = ak.stock_cy_a_spot_em()
        print(stock_cy_a_spot_em_df)

    @staticmethod
    def stock_kc_a_spot_em():
        """
        描述：东方财富网-科创板-实时行情
        限量：单次返回所有科创板的实时行情数据
        :param
            无
        :return
            序号 | int64 | -
            代码 | object | -
            名称 | object | -
            最新价 | float64 | -
            涨跌幅 | float64 | 注意单位：%
            涨跌额 | float64 | -
            成交量 | float64 | 注意单位：手
            成交额 | float64 | 注意单位：元
            振幅 | float64 | 注意单位：%
            最高 | float64 | -
            最低 | float64 | -
            今开 | float64 | -
            昨收 | float64 | -
            量比 | float64 | -
            换手率 | float64 | 注意单位：%
            市盈率-动态 | float64 | -
            市净率 | float64 | -
            总市值 | float64 | 注意单位：元
            流通市值 | float64 | 注意单位：元
            涨速 | float64 | -
            5分钟涨跌 | float64 | 注意单位：%
            60日涨跌幅 | float64 | 注意单位：%
            年初至今涨跌幅 | float64 | 注意单位：%
        """

        stock_kc_a_spot_em_df = ak.stock_kc_a_spot_em()
        print(stock_kc_a_spot_em_df)

    @staticmethod
    def stock_zh_ab_comparison_em():
        """
        描述：东方财富网-行情中心-沪深京个股-AB股比价-全部AB股比价
        限量：单次返回全部 AB 股比价的实时行情数据
        :param
            无
        :return
            序号 | int64 | -
            B股代码 | object | -
            B股名称 | object | -
            最新价B | float64 | -
            涨跌幅B | float64 | -
            A股代码 | object | -
            A股名称 | object | -
            最新价A | float64 | -
            涨跌幅A | float64 | -
            比价 | float64 | -
        """

        stock_zh_ab_comparison_em_df = ak.stock_zh_ab_comparison_em()
        print(stock_zh_ab_comparison_em_df)

    @staticmethod
    def stock_zh_a_spot():
        """
        描述：新浪财经-沪深京 A 股数据，重复运行本函数会被新浪暂时封 IP，建议增加时间间隔；接口请求当前内置 15 秒超时，避免上游长时间无响应时进程一直阻塞
        限量：单次返回沪深京 A 股上市公司的实时行情数据
        :param
            无
        :return
            代码 | object | -
            名称 | object | -
            最新价 | float64 | -
            涨跌额 | float64 | -
            涨跌幅 | float64 | 注意单位：%
            买入 | float64 | -
            卖出 | float64 | -
            昨收 | float64 | -
            今开 | float64 | -
            最高 | float64 | -
            最低 | float64 | -
            成交量 | float64 | 注意单位：股
            成交额 | float64 | 注意单位：元
            时间戳 | object | -
        """

        stock_zh_a_spot_df = ak.stock_zh_a_spot()
        print(stock_zh_a_spot_df)

    @staticmethod
    def stock_individual_spot_xq():
        """
        描述：雪球-行情中心-个股
        限量：单次获取指定 symbol 的最新行情数据
        :param
            symbol | str | symbol="SH600000"；证券代码，可以是 A 股个股代码，A 股场内基金代码，A 股指数，美股代码，美股指数
            token | str | token=None；雪球 xq_a_token
            timeout | float | timeout=None；默认不设置超时参数
        :return
            item | object | -
            value | object | -
        """

        stock_individual_spot_xq_df = ak.stock_individual_spot_xq(symbol="SH600000")
        print(stock_individual_spot_xq_df)
