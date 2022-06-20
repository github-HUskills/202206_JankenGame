# 出し手の入力チェック関数
def validate(hand):
    if hand < 0 or 2 < hand:
        return False
    return True

# 出し手の出力関数
def print_hand(hand,name="gest"):
    hands = ["グー", "チョキ", "パー"]
    print(name+"は"+hands[int(hand)]+"を出しました")

# じゃんけん結果判定
def judge(player, computer):
    if player == computer:
        return "あいこ"
    elif player == 0 and computer == 1:
        return "勝ち"
    elif player == 1 and computer == 2:
        return "勝ち"
    elif player == 2 and computer == 0:
        return "勝ち"
    else:
        return "負け"