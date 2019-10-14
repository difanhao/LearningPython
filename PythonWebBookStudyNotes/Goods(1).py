#coding:utf-8

class Goods:
    "购买商品的活动"

    def buyGoods(self):
        "是否参与该活动"

        print "调用buyGoods"
        # 判断是否执行购买商品的活动
        if __name__ == "__main__":
            # 提示是否购买商品
            goods = raw_input("您是否购买商品? N:不买，Y:买，请输入：")
            if goods == "Y":
                # 提示输入商品的名称和数量
                goodsName = raw_input("请输入商品名称：")
                goodsnum = int(raw_input("请输入该商品数量："))
                print "您购买的商品是：" + goodsName + " 数量：" + str(goodsnum)
                print "商品单价5元，总价：" + str(5 * goodsnum)
            if goods == "N":
                print "您没有购买商品！"
        else:
            print "您放弃了参与活动"

print Goods.__doc__
print Goods.buyGoods.__doc__

goods = Goods()
print goods.buyGoods() # 没有return的方法，默认返回None


