# MenuItemクラスの読み込み
from menu_item import MenuItem

# MenuItemクラスの子クラスとしてDrinkクラスを定義
class Drink(MenuItem):
    # MenuItemクラスのオーバーライドメソッド。amountを追加している
    def __init__(self, name, price, amount):
        super().__init__(name, price)
        self.amount = amount

    # MenuItemクラスのオーバーライドメソッド。amountを追加している
    def info(self):
        return self.name + "：￥" + str(self.price) + " (" + str(self.amount) + "mL)"