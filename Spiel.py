import unittest


 # takes player input for row between 1 and 3
def ask_row(x_o):
    while True:
        print('Player ' + x_o + ' set raw with digit between 1 and 3')

        user_row = int(input('Enter row: '))
 
        if user_row < 4 and user_row > 0:
            return user_row-1
        else:
            print ('please try again..')
            
            
 # takes player input for column between 1 and 3
def ask_col(x_o):            
    while True:
        print('Player ' + x_o + ' set collumn with digit between 1 and 3')

        user_col = int(input('Enter col: '))
 
        if user_col < 4 and user_col > 0:
            return user_col-1
        else:
            print ('please try again..')

            
 # combines the player inputs
def player_turn(x_o):
    while True:
        turn[0] = ask_row(x_o)
        turn[1] = ask_col(x_o)

        if spiel_matrix[turn[0]][turn[1]] != '-':
            print('please choose another field')
        else:
            return turn
 

 # checks if the condition to win has been met
def check_if_won():
    result = True
    for x in range(3):
        if spiel_matrix[x][0] != '-':
           # print('horizont pre' + str(x))
            if spiel_matrix[x][0] == spiel_matrix[x][1] == spiel_matrix[x][2]:
                return result #2

        if spiel_matrix[0][x] != '-':  
          #  print('vertical pre' + str(x))
            if spiel_matrix[0][x] == spiel_matrix[1][x] == spiel_matrix[2][x]:
                return result #1

        if spiel_matrix[1][1] != '-':
            if spiel_matrix[0][0] == spiel_matrix[1][1] == spiel_matrix[2][2] or spiel_matrix[0][2] == spiel_matrix[1][1] == spiel_matrix[2][0]:
                return result #3
        else:
            return False
            


#Game start
running = True
spieler_1 = True
game_over = False
new_round = True
turn = [1,1]

# run the game until end of the game and "no new game" condition
while running:
    
    # switch player 
    if spieler_1:
        x_o = 'X'
        spieler_1 = False
    else:
        x_o = 'O'
        spieler_1 = True
        
    # generate blank field if new game
    if new_round:
        rows, cols = (3, 3)
        spiel_matrix = [['-' for i in range(cols)] for j in range(rows)]
        new_round = False
        
    # show the field matrix
    for row in spiel_matrix:
        print(row)
        
    # player input
    turn = player_turn(x_o)

    spiel_matrix[turn[0]][turn[1]] = x_o

    result = check_if_won()    

    if result:
        print ('Player ' + x_o + ' won')
        again = input('wanna play again? y/n ')
        if again == 'y':
            new_round = True
        else:
            running = False
            break
    else:
        print('player ' + x_o)
    

    unittest.main()
