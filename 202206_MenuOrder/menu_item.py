class MenuItem:

    # インスタンス生成時に自動実行されるメソッド
    # インスタンス生成時に引数を受け取り、インスタンス変数に格納している
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # メニュー表示文言の設定
    def info(self):
        return self.name + "：￥" + str(self.price)

    # 注文数を引数で受け取り、合計金額を計算
    def get_total_price(self, count):
        total_price = self.price * count

        # 注文数が3個以上の場合は9割引き
        if count >= 3:
            total_price = total_price * 0.9

        # 四捨五入した値を返却
        return round(total_price)