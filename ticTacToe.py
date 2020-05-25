
import random

def chose_first():
	flip=random.randint(0,1)
	
	if flip==0:
		return 'player1'
	else:
		return 'player2'
		
def space_check(board,position):
	return board[position]==' '

def full_board_check(board):
	for i in range(1,10):
		if space_check(board,i):
			return False
		
	return True
def player_choice(board):
	position=0
	while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
		position=int(input('Chose a position:(1-9) '))
	return position
		
def display_board(board):        
	
	print(board[7]+'|'+board[8]+'|'+board[9])
	print("-|-|-")
	print(board[4]+'|'+board[5]+'|'+board[6])
	print("-|-|-")
	print(board[1]+'|'+board[2]+'|'+board[3])
	 
test_board=['0','1','2','3','4','5','6','7','8','9']     	 

def place_marker(board,marker,position):
	board[position]=marker
 

def win_check(board,mark):
	return ((board[1]==mark and board[2]==mark and board[3]==mark) or 
	(board[4]==mark and board[5]==mark and board[6]==mark) or
	(board[7]==mark and board[8]==mark and board[9]==mark) or
	(board[1]==mark and board[4]==mark and board[7]==mark) or
	(board[2]==mark and board[5]==mark and board[8]==mark) or
	(board[3]==mark and board[6]==mark and board[9]==mark) or
	(board[1]==mark and board[5]==mark and board[9]==mark) or
	(board[3]==mark and board[5]==mark and board[7]==mark)  )
	
	
	
def player_input():				
	marker=''
	
	while marker !='x' and marker !='o':
		marker=input("Player 1,chose x or o ")
		
	player1=marker
	if player1=='x':
		player2='o'
	else:
		player2='x'
		
	return (player1,player2)
 
def replay():
		choice=input("Play again? Enter Y Or N :")
		c=choice.lower()
		return c[0]=='y'
print("WelCome to Tic Tac Toe\nThis is sample position")	
display_board(test_board)

while True:
	test_board=[' ']*10  
	playerMarker1,playerMarker2=player_input() 
	turn=chose_first()
	print(turn+" will go fast")
	
	play_game=input("Ready to play? y or n : ")
	
	if play_game.lower()[0]=='y':
		game_on=True
	else:
		game_on=False
		
	while game_on:
		if turn=='player1':
			display_board(test_board)
			position=player_choice(test_board)
			place_marker(test_board,playerMarker1,position)
			
			if win_check(test_board,playerMarker1):
				display_board(test_board)
				print("Player 1 Win")
				game_on=False
			else:
				if full_board_check(test_board):
					display_board(test_board)
					print("Tie Game")
					break
					
				else:
					turn='player2';
		else:
			display_board(test_board)
			position=player_choice(test_board)
			place_marker(test_board,playerMarker2,position)
			
			if win_check(test_board,playerMarker2):
				display_board(test_board)
				print("player 2 win")
				game_on=False
			else:
				if full_board_check(test_board):
					display_board(test_board)
					print("Draw")
					break
				else:
					turn='player1'
								
			
	if not replay():
		break   






