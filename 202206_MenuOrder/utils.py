# メニュー番号がインスタンスリスト要素数内であるかチェックする関数
def validate(val, max):
    if 0 <= val <= max:
        return False
    return True

# Foodクラス、Drinkクラスのインスタンスリストを受け取り、メニュー表示を行う関数
def view_menu_items(menu_items):
    # メニュー表示番号(初期値)
    index = 0

    # インスタンスのリストをfor文で繰り返してメニュー表示
    for item in menu_items:
        print("　" + str(index) + "." + item.info())
        index += 1