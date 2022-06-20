# メニュー番号がインスタンスリスト要素数内であるかチェックする関数
def validate(val, max):
    if 0 <= val <= max:
        return True
    return False