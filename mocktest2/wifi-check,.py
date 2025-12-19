def f(player1,player2):
    card_value = {
        "A":10, "K":10, "Q":10, "J":10, "T":10, "9":9, "8":8, "7":7,
        "6":6, "5":5, "4":4, "3":3, "2":2
    }

    player1_total = sum(card_value[card] for card in player1)

    player2_total = sum(card_value[card] for card in player2)

    if player1_total > player2_total:
        return "player1"
    elif player1_total < player2_total:
        return "player2"
    else:
        return "Tie"

if __name__ == "__main__":
    print(f("AJ972", "AQT72"))  
    print(f("9532", "K8")) 
    print(f("AK", "QJ"))