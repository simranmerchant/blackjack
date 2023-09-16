from p1_random import P1Random

rng = P1Random()

# print(rng.next_int(13) + 1)

game_continue = True
game_num = 0
player_wins = 0
dealer_wins = 0
tie_games = 0

# Control the number of games player will play
while game_continue:
    game_num += 1
    print(f"START GAME #{game_num}\n")
    player_hand = 0
    dealer_hand = 0
    card = (rng.next_int(13) + 1)
    if card == 1:
        print("Your card is a ACE!")
        card = 1
    elif 2 <= card <= 10:
        print(f"Your card is a {card}!")
    elif card == 11:
        print("Your card is a JACK!")
        card = 10
    elif card == 12:
        print("Your card is a QUEEN!")
        card = 10
    elif card == 13:
        print("Your card is a KING!")
        card = 10

    player_hand += card
    print(f"Your hand is: {player_hand}")


    no_winner = True
    while no_winner:
        print("\n1. Get another card")
        print("2. Hold hand")
        print("3. Print statistics")
        print("4. Exit\n")
        menu_option = int(input("Choose an option: "))
        if menu_option == 1:
            # while game_continue:
                card = (rng.next_int(13) + 1)
                if card == 1:
                    print("\nYour card is a ACE!")
                    card = 1
                elif 2 <= card <= 10:
                    print(f"\nYour card is a {card}!")
                elif card == 11:
                    print("\nYour card is a JACK!")
                    card = 10
                elif card == 12:
                    print("\nYour card is a QUEEN!")
                    card = 10
                elif card == 13:
                    print("\nYour card is a KING!")
                    card = 10
                player_hand += card
                print(f"Your hand is: {player_hand}")
                if player_hand == 21:
                    print("BLACKJACK! You win!\n")
                    player_wins += 1
                    no_winner = False
                    break
                elif player_hand > 21:
                    print("\nYou exceeded 21! You lose.\n")
                    dealer_wins += 1
                    no_winner = False
                    break
                else:
                    no_winner = True
                    break
        elif menu_option == 2:
            card = (rng.next_int(11) + 16)
            dealer_hand += card
            print(f"\nDealer's hand: {dealer_hand}")
            print(f"Your hand is: {player_hand}")
            if dealer_hand == 21:
                dealer_wins += 1
                print("Dealer wins!\n")
                no_winner = False
            elif dealer_hand > 21:
                print("You win!\n")
                player_wins += 1
                no_winner = False
            elif dealer_hand > player_hand:
                dealer_wins += 1
                print("Dealer wins!\n")
                no_winner = False
            elif dealer_hand == player_hand:
                tie_games += 1
                print("It's a tie! No one wins!\n")
                no_winner = False
            else:
                no_winner = True
        elif menu_option == 3:
            games_played = (player_wins + dealer_wins + tie_games)
            percent = (player_wins / games_played) * 100
            print(f"Number of Player wins: {player_wins}")
            print(f"Number of Dealer wins: {dealer_wins}")
            print(f"Number of tie games: {tie_games}")
            print(f"Total # of games played is: {games_played}")
            print(f"Percentage of Player wins: {percent:.1f}%")
        elif menu_option == 4:
            no_winner = False
            game_continue = False
        else:
            print("\nInvalid input!" 
                  "\nPlease enter an integer value between 1 and 4.")

