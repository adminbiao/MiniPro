import utils, logging
from Api.apifactory import ApiFactory


class TestProduct:
    """商品"""
    def test_product_classify(self):
        # 请求返回数据
        res = ApiFactory.get_product_api().product_classify_api()
        # 打印 请求地址 打印请求参数 打印请求响应数据
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言状态码
        utils.common_assert_code(res)
        # 断言商品数量大于0
        assert len(res.json()) > 0
        # 断言关键字 id name topic_img_id
        assert "id" in res.text and "name" in res.text and "topic_img_id" in res.text

    def test_classify_product(self):
        # 请求返回数据
        res = ApiFactory.get_product_api().classify_product_api()
        # 打印 请求地址 打印请求参数 打印请求响应数据
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言状态码
        utils.common_assert_code(res)
        # 断言商品数量大于0
        assert len(res.json()) > 0
        # 断言关键字 id name  price stock
        assert False not in [i in res.text for i in ['id', 'name', 'price', 'stock']]

    def test_product_detail(self):
        # 请求返回数据
        res = ApiFactory.get_product_api().product_detail_api()
        # 打印 请求地址 打印请求参数 打印请求响应数据
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言状态码
        utils.common_assert_code(res)
        # 断言id
        assert res.json().get("id") == 2
        # 断言name
        assert res.json().get('name') == "梨花带雨 3个"
        # 断言 price
        assert res.json().get("price") == "0.01"
