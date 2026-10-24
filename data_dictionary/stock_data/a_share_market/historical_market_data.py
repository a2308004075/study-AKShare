import akshare as ak


# 历史行情数据
class HistoricalMarketData:
    @staticmethod
    def stock_zh_a_hist():
        """
        描述：东方财富-沪深京 A 股日频率数据；历史行情数据按日频率更新，当日收盘价请在收盘后获取
        限量：单次返回指定沪深京 A 股上市公司、指定周期和指定日期间的历史行情日频率数据
        :param
            symbol | str | symbol='603777'；股票代码可以在 ak.stock_zh_a_spot_em() 中获取
            period | str | period='daily'; choice of {'daily', 'weekly', 'monthly'}
            start_date | str | start_date='20210301'；开始查询的日期
            end_date | str | end_date='20210616'；结束查询的日期
            adjust | str | 默认返回不复权的数据；qfq: 返回前复权后的数据；hfq: 返回后复权后的数据
            timeout | float | timeout=None；默认不设置超时参数
        :return
            日期 | object | 交易日
            股票代码 | object | 不带市场标识的股票代码
            开盘 | float64 | 开盘价
            收盘 | float64 | 收盘价
            最高 | float64 | 最高价
            最低 | float64 | 最低价
            成交量 | int64 | 注意单位：手
            成交额 | float64 | 注意单位：元
            振幅 | float64 | 注意单位：%
            涨跌幅 | float64 | 注意单位：%
            涨跌额 | float64 | 注意单位：元
            换手率 | float64 | 注意单位：%
        """

        stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20170301", end_date='20240528', adjust="")
        print(stock_zh_a_hist_df)

    @staticmethod
    def stock_zh_a_daily():
        """
        描述：新浪财经-沪深京 A 股的数据，历史数据按日频率更新；注意其中的 sh689009 为 CDR，请 通过 ak.stock_zh_a_cdr_daily 接口获取
        限量：单次返回指定沪深京 A 股上市公司指定日期间的历史行情日频率数据，多次获取容易封禁 IP
        说明：P.S. 建议切换为 stock_zh_a_hist 接口使用（该接口数据质量高，访问无限制）
        :param
            symbol | str | symbol='sh600000'；股票代码可以在 ak.stock_zh_a_spot() 中获取
            start_date | str | start_date='20201103'；开始查询的日期
            end_date | str | end_date='20201116'；结束查询的日期
            adjust | str | 默认返回不复权的数据；qfq: 返回前复权后的数据；hfq: 返回后复权后的数据；hfq-factor: 返回后复权因子；qfq-factor: 返回前复权因子
        :return
            date | object | 交易日
            open | float64 | 开盘价
            high | float64 | 最高价
            low | float64 | 最低价
            close | float64 | 收盘价
            volume | float64 | 成交量；注意单位：股
            amount | float64 | 成交额；注意单位：元
            outstanding_share | float64 | 流动股本；注意单位：股
            turnover | float64 | 换手率=成交量/流动股本
        """

        stock_zh_a_daily_qfq_df = ak.stock_zh_a_daily(symbol="sz000001", start_date="19910403", end_date="20231027", adjust="qfq")
        print(stock_zh_a_daily_qfq_df)

    @staticmethod
    def stock_zh_a_hist_tx():
        """
        描述：腾讯证券-日频-股票历史数据；历史数据按日频率更新，当日收盘价请在收盘后获取
        限量：单次返回指定沪深京 A 股上市公司、指定周期和指定日期间的历史行情日频率数据
        说明：symbol 支持传入带市场前缀的代码，如 sz000001；symbol 也支持传入纯 6 位 A 股代码，如 000001，接口内部会自动补全市场前缀；volume 已统一为股，amount 已统一为元
        :param
            symbol | str | symbol='sz000001'；带市场标识
            start_date | str | start_date='19000101'；开始查询的日期
            end_date | str | end_date='20500101'；结束查询的日期
            adjust | str | 默认返回不复权的数据；qfq: 返回前复权后的数据；hfq: 返回后复权后的数据
            timeout | float | timeout=None；默认不设置超时参数
        :return
            date | object | 交易日
            open | float64 | 开盘价
            close | float64 | 收盘价
            high | float64 | 最高价
            low | float64 | 最低价
            volume | float64 | 成交量；单位：股
            turnover | float64 | 换手率；小数表示
            amount | float64 | 成交额；单位：元
        """

        stock_zh_a_hist_tx_df = ak.stock_zh_a_hist_tx(symbol="sz000001", start_date="20200101", end_date="20231027", adjust="")
        print(stock_zh_a_hist_tx_df)

    @staticmethod
    def stock_zh_a_minute():
        """
        描述：新浪财经-沪深京 A 股股票或者指数的分时数据，目前可以获取 1, 5, 15, 30, 60 分钟的数据频率，可以指定是否复权
        限量：单次返回指定股票或指数的指定频率的最近交易日的历史分时行情数据；注意调用频率
        :param
            symbol | str | symbol='sh000300'；同日频率数据接口
            period | str | period='1'；获取 1, 5, 15, 30, 60 分钟的数据频率
            adjust | str | adjust=""；默认为空：返回不复权的数据；qfq: 返回前复权后的数据；hfq: 返回后复权后的数据；
        :return
            day | object | -
            open | float64 | -
            high | float64 | -
            low | float64 | -
            close | float64 | -
            volume | float64 | -
            amount | float64 | -
        """

        stock_zh_a_minute_df = ak.stock_zh_a_minute(symbol='sh600751', period='1', adjust="qfq")
        print(stock_zh_a_minute_df)

    @staticmethod
    def stock_zh_a_hist_min_em():
        """
        描述：东方财富网-行情首页-沪深京 A 股-每日分时行情；该接口只能获取近期的分时数据，注意时间周期的设置
        限量：单次返回指定股票、频率、复权调整和时间区间的分时数据，其中 1 分钟数据只返回近 5 个交易日数据且不复权
        说明：period='1' 时返回 1 分钟数据字段，含均价，无涨跌幅、涨跌额、振幅、换手率；period 取 5/15/30/60 时返回行情字段，含涨跌幅、涨跌额、振幅、换手率，无均价
        :param
            symbol | str | symbol='000300'；股票代码
            start_date | str | start_date="1979-09-01 09:32:00"；日期时间；默认返回所有数据
            end_date | str | end_date="2222-01-01 09:32:00"；日期时间；默认返回所有数据
            period | str | period='5'; choice of {'1', '5', '15', '30', '60'}；其中 1 分钟数据返回近 5 个交易日数据且不复权
            adjust | str | adjust=''; choice of {'', 'qfq', 'hfq'}; '': 不复权，'qfq': 前复权，'hfq': 后复权，其中 1 分钟数据返回近 5 个交易日数据且不复权
        :return
            时间 | object | -
            开盘 | float64 | -
            收盘 | float64 | -
            最高 | float64 | -
            最低 | float64 | -
            成交量 | float64 | 注意单位：手
            成交额 | float64 | -
            均价 | float64 | -
            涨跌幅 | float64 | 注意单位：%
            涨跌额 | float64 | -
            振幅 | float64 | 注意单位：%
            换手率 | float64 | 注意单位：%
        """

        # 注意：该接口返回的数据只有最近一个交易日的有开盘价，其他日期开盘价为 0
        stock_zh_a_hist_min_em_df = ak.stock_zh_a_hist_min_em(symbol="000001", start_date="2024-03-20 09:30:00", end_date="2024-03-20 15:00:00", period="1", adjust="")
        print(stock_zh_a_hist_min_em_df)

    @staticmethod
    def stock_intraday_em():
        """
        描述：东方财富-分时数据
        限量：单次返回指定股票最近一个交易日的分时数据，包含盘前数据
        :param
            symbol | str | symbol="000001"；股票代码
        :return
            时间 | object | -
            成交价 | float64 | -
            手数 | int64 | -
            买卖盘性质 | object | -
        """

        stock_intraday_em_df = ak.stock_intraday_em(symbol="000001")
        print(stock_intraday_em_df)

    @staticmethod
    def stock_intraday_sina():
        """
        描述：新浪财经-日内分时数据
        限量：单次返回指定交易日的分时数据；只能获取近期的数据，此处仅返回大单数据（成交量大于等于：400手）
        :param
            symbol | str | symbol="sz000001"；带市场标识的股票代码
            date | str | date="20240321"；交易日
        :return
            symbol | object | -
            name | object | -
            ticktime | object | -
            price | float64 | -
            volume | int64 | 注意单位：股
            prev_price | float64 | -
            kind | object | D 表示卖盘，表示 是买盘
        """

        stock_intraday_sina_df = ak.stock_intraday_sina(symbol="sz000001", date="20240321")
        print(stock_intraday_sina_df)

    @staticmethod
    def stock_zh_a_hist_pre_min_em():
        """
        描述：东方财富-股票行情-盘前数据
        限量：单次返回指定 symbol 的最近一个交易日的股票分钟数据，包含盘前分钟数据
        :param
            symbol | str | symbol="000001"；股票代码
            start_time | str | start_time="09:00:00"；时间；默认返回所有数据
            end_time | str | end_time="15:40:00"；时间；默认返回所有数据
        :return
            时间 | object | -
            开盘 | float64 | -
            收盘 | float64 | -
            最高 | float64 | -
            最低 | float64 | -
            成交量 | float64 | 注意单位：手
            成交额 | float64 | -
            最新价 | float64 | -
        """

        stock_zh_a_hist_pre_min_em_df = ak.stock_zh_a_hist_pre_min_em(symbol="000001", start_time="09:00:00", end_time="15:40:00")
        print(stock_zh_a_hist_pre_min_em_df)
