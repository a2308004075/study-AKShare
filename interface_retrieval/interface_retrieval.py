import akshare as ak


# AKShare 接口检索
class InterfaceRetrieval:
    """
    AKShare 接口检索
    说明：提供 ak.search、ak.interface_info、ak.list_categories 三个函数
    特性：完全离线，接口元数据随安装包分发（akshare/data/interfaces.json），调用不发起网络请求，无需 token
    边界：
        1. 关键词匹配而非语义检索，基于接口名、描述、类目与输出字段名做子串比对，不理解同义词
        2. 传入完整接口名时该接口一定排在第一位，尾随标点不影响该保证
        3. 匹配分只能在同一次查询内比较，不可作为跨查询的置信度阈值
        4. 未收录接口的描述、输入参数等字段为空，有无文档为 False
        5. 元数据是构建时的快照，升级 AKShare 即可获得更新后的元数据
    """

    @staticmethod
    def search():
        """
        描述：按关键词检索 AKShare 接口，返回按匹配度降序排列的结果
        限量：单次返回不超过 limit 条记录，默认 20 条
        :param
            query | str | query="可转债 实时行情"；关键词以空格或逗号分隔；传入完整接口名时该接口置顶
            limit | int | limit=20；返回条数上限；不可为负数
            category | str | category=None；默认返回全部类目，可用 ak.list_categories() 查询可选值
            documented_only | bool  documented_only=False；默认返回全部接口，设为 True 时仅返回本文档中已收录的接口
        :return
            接口名 | object | 可直接用于 getattr(ak，接口名) 调用
            类目 | object | -
            描述 | object | 取自本文档的接口描述，未收录的接口该字段为 None
            有无文档 | bool | 该接口是否已被本文档收录
            匹配分 | float64 | 仅供同一次查询内比较相对排序，不可跨查询比较，详见下方"能力边界"
        """

        search_df = ak.search("可转债 实时行情", limit=5)
        print(search_df)

    @staticmethod
    def interface_info():
        """
        描述：返回单个接口的完整元数据，含输入参数，输出字段与调用示例
        限量：单次返回一个接口的元数据
        :param
            name | str | name="energy_carbon_bj"；接口名；传入未知接口名时抛出异常并在消息中给出最接近的候选
        :return
            返回一个 dict，含以下键：
            name | str | 接口名
            module | str | 该接口所在的模块路径
            category | str | 所属类目
            documented | bool | 是否已被本文档收录
            desc | str | 接口描述，未收录时为 None
            url | str | 数据源地址，未收录时为 None
            limit_desc | str | 单次返回的数据量说明，无此说明时为 None
            params | list | 输入参数列表，每项含 name/type/desc 三个键
            outputs | list | 输出字段列表，每项含 name/type/desc 三个键
            example | str | 调用示例代码，未收录时为 None
        """

        interface_info_dict = ak.interface_info("energy_carbon_bj")
        print(interface_info_dict)

    @staticmethod
    def list_categories():
        """
        描述：列出全部类目及其接口数量，可用于确定 ak.search 的 category 取值
        限量：单次返回全部类目
        :param
            无
        :return
            类目 | object | -
            接口数 | int64 | -
        """

        list_categories_df = ak.list_categories()
        print(list_categories_df)

