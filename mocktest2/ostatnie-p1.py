def f(player1,player2):
    card_values = {"A": 10, "K": 10, "Q": 10, "J": 10, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, 
                   "5":5, "4": 4, "3": 3, "2": 2 }
    
    player1_total = sum(card_values[cards] for cards in player1)
    player2_total = sum(card_values[cards] for cards in player2)

    if player1_total >= player2_total:
        return True
    else:
        return False
    
if __name__ == "__main__":
 print( f("AJ972","AQT72") )
 print( f("9532","K8") )