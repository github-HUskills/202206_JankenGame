# MenuItemクラスの読み込み
from menu_item import MenuItem

# MenuItemクラスの子クラスとしてFoodクラスを定義
class Food(MenuItem):
    # MenuItemクラスのオーバーライドメソッド。calorieを追加している
    def __init__(self, name, price, calorie):
        super().__init__(name, price)
        self.calorie = calorie

    # MenuItemクラスのオーバーライドメソッド。calorieを追加している
    def info(self):
        return self.name + "：￥" + str(self.price) + " (" + str(self.calorie) + "kcal)"
