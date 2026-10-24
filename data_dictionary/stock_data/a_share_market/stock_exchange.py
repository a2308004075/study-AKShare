import akshare as ak


class StockExchange:
    # 上海证券交易所
    @staticmethod
    def stock_sse_summary():
        """
        描述：上海证券交易所-股票数据总貌
        限量：单次返回最近交易日的股票数据总貌（当前交易日的数据需要交易所收盘后统计）
        :param
            无
        :return
            项目 | object | -
            股票 | object | -
            科创板 | object | -
            主板 | object | -
        """

        stock_sse_summary_df = ak.stock_sse_summary()
        print(stock_sse_summary_df)

    @staticmethod
    def stock_sse_deal_daily():
        """
        描述：上海证券交易所-数据-股票数据-成交概况-股票成交概况-每日股票情况
        限量：单次返回指定日期的每日概况数据，当前交易日数据需要在收盘后获取；注意仅支持获取在 20211227（包含）之后的数据
        :param
            date | str | date="20250221"；当前交易日的数据需要交易所收盘后统计；注意仅支持获取在 20211227（包含）之后的数据
        :return
            单日情况 | object | 包含了网页所有字段
            股票 | float64 | -
            主板A | float64 | -
            主板B | float64 | -
            科创板 | float64 | -
            股票回购 | float64 | -
        """

        stock_sse_deal_daily_df = ak.stock_sse_deal_daily(date="20250221")
        print(stock_sse_deal_daily_df)

    # 深圳证券交易所
    @staticmethod
    def stock_szse_summary():
        """
        描述：深圳证券交易所-市场总貌-证券类别统计
        限量：单次返回指定 date 的市场总貌数据-证券类别统计（当前交易日的数据需要交易所收盘后统计）
        :param
            date | str | date="20200619"；当前交易日的数据需要交易所收盘后统计
        :return
            证券类别 | object | -
            数量 | int64 | 注意单位：只
            成交金额 | float64 | 注意单位：元
            总市值 | float64 | -
            流通市值 | float64 | -
        """

        stock_szse_summary_df = ak.stock_szse_summary(date="20200619")
        print(stock_szse_summary_df)

    @staticmethod
    def stock_szse_area_summary():
        """
        描述：深圳证券交易所-市场总貌-地区交易排序
        限量：单次返回指定 date 的市场总貌数据-地区交易排序数据
        说明：2025 年起输出新增优先股交易额与期权交易额两列
        :param
            date | str | date="202203"；年月
        :return
            序号 | int64 | -
            地区 | object | -
            总交易额 | float64 | 注意单位：元
            占市场 | float64 | 注意单位：%
            股票交易额 | float64 | 注意单位：元
            基金交易额 | float64 | 注意单位：元
            债券交易额 | float64 | 注意单位：元
            优先股交易额 | float64 | 注意单位：元
            期权交易额 | float64 | 注意单位：元
        """

        stock_szse_area_summary_df = ak.stock_szse_area_summary(date="202412")
        print(stock_szse_area_summary_df)

    @staticmethod
    def stock_szse_sector_summary():
        """
        描述：深圳证券交易所-统计资料-股票行业成交数据
        限量：单次返回指定 symbol 和 date 的统计资料-股票行业成交数据
        说明：仅支持查询深交所统计月报页面已发布的月份；若传入尚未发布的月份，接口会抛出明确的参数异常并提示当前最新可用月份
        :param
            symbol | str | symbol="当月"；choice of {"当月", "当年"}
            date | str | date="202501"；年月
        :return
            项目名称 | object | -
            项目名称-英文 | object | -
            交易天数 | int64 | -
            成交金额-人民币元 | int64 | -
            成交金额-占总计 | float64 | 注意单位：%
            成交股数-股数 | int64 | -
            成交股数-占总计 | float64 | 注意单位：%
            成交笔数-笔 | int64 | -
            成交笔数-占总计 | float64 | 注意单位：%
        """

        stock_szse_sector_summary_df = ak.stock_szse_sector_summary(symbol="当年", date="202501")
        print(stock_szse_sector_summary_df)
