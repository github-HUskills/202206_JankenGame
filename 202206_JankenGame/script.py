# 自作モジュール
import utils
# Python標準モジュール
import random

print("---じゃんけんを始めます---")

# プレイヤー名を取得
player_name = input("◆名前を入力してください：")

# プレイヤーの出し手を取得
print("◆何をだしますか？（0:グー, 1:チョキ, 2:パー）")
player_hand = int(input("　数字を入力してください："))
print("----------")

# 出し手の入力チェック関数の呼び出し
if utils.validate(player_hand):
    # 標準モジュールを利用してコンピューターの出し手を取得
    computer_hand = random.randint(0, 2)

    # プレイヤー名の入力可否によって処理分岐
    if player_name:
        # 自作モジュールを利用して出し手を出力
        utils.print_hand(player_hand, player_name)
    else:
        utils.print_hand(player_hand)

    utils.print_hand(computer_hand, "コンピューター")

    # プレイヤーとコンピューターのじゃんけん結果判定
    result = utils.judge(player_hand, computer_hand)

    # 結果出力
    print("----------")
    print("結果は"+result+"です")
else:
    # 出し手の入力チェックエラー
    print("error：正しい数値(0～2)を入力してください")

print("---じゃんけんを終了します---")