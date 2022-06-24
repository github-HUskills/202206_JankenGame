# Foodクラス, Drinkクラスの読み込み
from food import Food
from drink import Drink

# 自作モジュールの読み込み
import utils

# Foodクラスのインスタンス作成 ＆ インスタンス変数に値格納
food1 = Food("サンドウィッチ", 500, 330)
food2 = Food("チョコケーキ", 400, 450)
food3 = Food("シュークリーム", 200, 180)

# Foodクラスのインスタンスのリスト作成
foods = [food1, food2, food3]

# Drinkクラスのインスタンス作成 ＆ インスタンス変数に値格納
drink1 = Drink("オレンジジュース", 200, 350)
drink2 = Drink("コーヒー", 300, 180)
drink3 = Drink("エスプレッソ", 300, 30)

# Drinkクラスのインスタンスのリスト作成
drinks = [drink1, drink2, drink3]

print("◆ 食べ物メニュー")
utils.view_menu_items(foods)

print("◆ 飲み物メニュー")
utils.view_menu_items(drinks)

print("---------------")

# 食べ物メニュー番号の取得（0～4の値）
food_oder = input("食べ物メニューの番号を入力してください：")

# 食べ物メニュー番号が正常値かチェック
if utils.validate(int(food_oder), len(foods)):
    # メニュー番号をもとにFoodクラスのインスタンスを取得
    select_food_menu = foods[int(food_oder)]
    print("選択されたメニュー：" + select_food_menu.name)

    # 注文個数の取得
    food_count = input("個数を入力してください（3つ以上で1割引き）：")

    print("---------------")

    # 飲み物メニュー番号の取得（0～4の値）
    drink_oder = input("飲み物メニューの番号を入力してください：")

    # メニュー番号が正常値かチェック
    if utils.validate(int(drink_oder), len(drinks)):
        # メニュー番号をもとにDrinkクラスのインスタンスを取得
        select_drink_menu = drinks[int(drink_oder)]
        print("選択されたメニュー：" + select_drink_menu.name)

        # 注文個数の取得
        drink_count = input("個数を入力してください（3つ以上で1割引き）：")

        print("---------------")

        # 注文個数をもとに合計金額の計算
        food_result = select_food_menu.get_total_price(int(food_count))
        drink_result = select_drink_menu.get_total_price(int(drink_count))
        print("合計は" + str(food_result + drink_result) + "円です")

    else:
        print("error：正しい値を入力してください")
else:
    print("error：正しい値を入力してください")
