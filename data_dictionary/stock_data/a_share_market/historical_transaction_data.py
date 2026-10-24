import akshare as ak


# 历史分笔数据
class HistoricalTransactionData:
    @staticmethod
    def stock_zh_a_tick_tx_js():
        """
        描述：每个交易日 16:00 提供当日数据；如遇到数据缺失，请使用 ak.stock_zh_a_tick_163() 接口（注意数据会有一定差异）
        限量：单次返回最近交易日的历史分笔行情数据
        说明：文档标注的接口名为 stock_zh_a_tick_tx，akshare 实际导出为 stock_zh_a_tick_tx_js，当前版本仅此一个分笔接口，文档提到的备选 ak.stock_zh_a_tick_163() 并不存在
        :param
            symbol | str | symbol="sh600000"
        :return
            成交时间 | object | -
            成交价格 | float64 | 注意单位：元
            价格变动 | float64 | 注意单位：元
            成交量 | int32 | 注意单位：手
            成交额 | int32 | 注意单位：元
            性质 | object | 买卖盘标记
        """

        stock_zh_a_tick_tx_js_df = ak.stock_zh_a_tick_tx_js(symbol="sz000001")
        print(stock_zh_a_tick_tx_js_df)
