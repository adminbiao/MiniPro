from Api.apifactory import ApiFactory
import utils,logging


class TestHome:

    def test_home_api(self):
        """轮播图"""
        # 请求返回数据
        res = ApiFactory.get_home_api().banner_api()
        # 打印 请求地址 打印请求参数 打印请求响应数据
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言状态码
        utils.common_assert_code(res)
        # 断言id 和 name
        assert res.json().get("id") == 1 and res.json().get("name") == "首页置顶"
        # 断言items的长度大于0
        assert len(res.json().get("items")) > 0

    def test_theme_api(self):
        """专题栏"""
        # 请求返回数据
        res = ApiFactory.get_home_api().theme_api()
        # 打印 请求地址 打印请求参数 打印请求响应数据
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言状态码
        utils.common_assert_code(res)
        # 断言 三个id =1,2,3
        assert 'id":1' in res.text and 'id":2' in res.text and 'id":3' in res.text
        # 断言关键字段 name description topic_img head_img
        assert False not in [i in res.text for i in ['name', 'description', 'topic_img', 'head_img']]

    def test_recent_product_api(self):
        """最近新品"""
        # 请求返回数据
        res = ApiFactory.get_home_api().recent_product_api()
        # 打印 请求地址 打印请求参数 打印请求响应数据
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言状态码
        utils.common_assert_code(res)
        # 断言最近商品的数量大于0
        assert len(res.json()) > 0
        # 断言关键字段 name price main_img_url
        assert 'name' in res.text and "price" in res.text and "main_img_url" in res.text
