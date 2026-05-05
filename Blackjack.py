import random 
def user_game():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10,10,10]
    card_1 = random.choice(cards)
    card_2 = random.choice(cards)
    dealer_card1 = random.choice(cards)
    dealer_card2 = random.choice(cards)
    hit_card =random.choice(cards)
    current_score = card_1+card_2 
    current_cards = [card_1,card_2]
    dealer_cards=[dealer_card1]
    dealer_score =dealer_card1+dealer_card2 
    print(f"your cards{current_cards} = {current_score}")
    print(f"dealers firs card{dealer_cards}={dealer_card1}")
    dealer_game=False 
    should_continue =True 
    while should_continue:
        user_chose =input("type hit to get one more card or type stand to pass:  ")   
        if current_score == 21:
             print("you win!")
             should_continue = False 
             dealer_game=True            
        elif user_chose == "hit":
            hit_card=random.choice(cards) 
            current_cards.append(hit_card)
            current_score+=hit_card
            print(f"{current_cards}={current_score}")
            if current_score ==22 or current_score>=22:
                should_continue =False 
                dealer_game=True 
                print("            【BUST】")
            else :    
                print(user_chose)
        elif user_chose == "stand":
            print(f"this is your final score {current_cards}={current_score}")
            should_continue = False
            dealer_game=True 
        else:
             print("you chosen in valid chice")
             print("try to get valid choice\n")  
       
    while dealer_game: 
         
         if current_score==22 or current_score>=22:
             dealer_cards.append(dealer_card2)
             dealer_game  = False           
             print(f"hear  is dealer score {dealer_cards}={dealer_score}")  
                
         elif current_score >21:
             print(dealer_score)
             dealer_game=False 
         elif dealer_score >=17:
             dealer_game= False
             dealer_cards.append(dealer_card2)
             print(f"hear is dealer score{dealer_cards}={dealer_score}")
             
         else :
             dealer_cards.append(hit_card)
             dealer_score+=hit_card
    if dealer_score ==21:
        print("            【DEALER WINS...!】") 
        dealer_game=False
    elif dealer_score == current_score:
        print("            【PUSH....!】")    
        game_continue=False  
    elif current_score<=22 and dealer_score<=22:
        if dealer_score>current_score:
            print("        【DEALER WIN'S...!】")
        else:
            print("        【YOU WINS】") 
    elif dealer_score > current_score:
        print("            【YOU WINS...!】") 
    elif dealer_score < current_score:
        print("            【DEALER WIN'S....!】")             
    else:
        print("            【sumthing went wrong in game】")
    print(1*"\n") 
    print("=============new game================")        
    user_game()         
user_game()   
   