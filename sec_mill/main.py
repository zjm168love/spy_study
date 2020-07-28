# 使用方法
# 1 设置url
# 2 设置天猫还是淘宝
# 3 设置开抢时间
# 4 运行程序
# 5 扫码登录
# 6 选中要购买商品以及相应种类等（必须选中！！！）
# 7 自动下单
#

if __name__ == "__main__":
    # 输入要购买物品 url
    # 如果是天猫超市的抢购 请先加入购物车 此处为购物车链接
    url = "https://cart.taobao.com/cart.htm"
    # 请选择商城（淘宝 1  天猫 2  3 通过购物车 输入数字：
    mall = '3'
    # 输入开售时间
    bt = "2020-03-01 15:00:00"
    server_time, tmp = get_server_time()
    time_dif = time.time() - server_time + tmp + tmp
    login(url, mall)
    buy(bt, mall, 2 * time_dif + 0.5)