# MenuItemクラスの読み込み
from menu_item import MenuItem

# 自作モジュールの読み込み
import utils

# MenuItemクラスのインスタンス作成 ＆ インスタンス変数に値格納
menu_item1 = MenuItem("サンドウィッチ", 500)
menu_item2 = MenuItem("チョコケーキ", 400)
menu_item3 = MenuItem("コーヒー", 300)
menu_item4 = MenuItem("オレンジジュース", 200)

# MenuItemクラスのインスタンスのリスト作成
menu_items = [menu_item1, menu_item2, menu_item3, menu_item4]

# メニュー表示番号(初期値)
index = 0
# インスタンスのリストをfor文で繰り返してメニュー表示
for item in menu_items:
    print(str(index) + "." + item.info())
    index += 1

print("---------------")

# メニュー番号の取得（0～4の値）
oder = input("メニューの番号を入力してください：")

# メニュー番号が正常値かチェック
if utils.validate(int(oder), len(menu_items)):
    # メニュー番号をもとにMenuItemクラスのインスタンスを取得
    select_menu = menu_items[int(oder)]
    print("選択されたメニュー：" + select_menu.name)

    # 注文個数の取得
    count = input("個数を入力してください（3つ以上で1割引き）：")

    # 注文個数をもとに合計金額の計算
    result = select_menu.get_total_price(int(count))
    print("合計は" + str(result) + "円です")

else:
    print("error：正しい値を入力してください")
