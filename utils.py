def common_assert_code(res, code=200):
    """
    响应状态码
    :param res: 响应对象
    :param code: 响应状态码默认200
    :return:
    """
    assert res.status_code == code
