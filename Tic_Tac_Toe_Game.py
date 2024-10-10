
#LIBRARIES NEEDED
import time
import colors as clr


def clear():
	ap =[]
	for i in range(len(board)):
			for j in range(len(board[0])):
				add = board[i][j]
				ap.append(add)
	if sum(ap) ==13 or sum(ap) == 14:	
				for index,rows in enumerate(board):
					print("\n    	 row =  ",index,rows,"\n	")	
				print(f"	{clr.color.BackgroundBrightYellow}   NO WINNER YET,       CLEARING GAME BOARD          {clr.color.reset}")
				time.sleep(3)
				for i in range(len(board)):
					for j in range(len(board[0])):
						board[i][j]=0
			
				

def my_game():
	# INFINITY LOOP
	run = True
	while run:
		# ERROR HANDLER
		try:
			print("\n		PRESENT BOARD	")
			print("		  Columns \n")
			print("	       	   0   1  2")
			# PRINTING THE ROWS IN THE GAME BOARD
			for index,rows in enumerate(board):
				
				print("\n    	 row =  ",index,rows,"\n	")
		
			
			print("\u001b[33m","\n		** PLAYER 1 , YOUR TURN** \n","\u001b[0m \n")
			
			# TAKING INPUT FROM PLAYER 1 USING WHILE LOOP
			while True:
				usr1r = int(input("	ENTER ROW :"))
				usr1c = int(input("	ENTER COLUMN :"))
				# CHECKING FOR CONDITIONS
				if board[usr1r][usr1c]<1: 
					board[usr1r][usr1c]=1
					break
						
				if board[usr1r][usr1c]>0:
					print("\u001b[31m","****  NO MORE SPACE TO PLAY THERE (( PLAYER 1 )), PLEASE PLAY AGAIN ","\u001b[0m \n")
					print("\u001b[33m","\n		***** PLAYER 1 , PLAY AGAIN  **** \n","\u001b[0m")
			clear()
					
			#LOOKING IF PLAYER 1 IS THE WINNER	
			if board[0][0] ==1 and  board[0][1] ==1 and  board[0][2] ==1 or  board[1][0] ==1 and  board[1][1] ==1 and  board[1][2] ==1 or  board[2][0] ==1 and  board[2][1] ==1  and  board[2][2] ==1:
				for vs in board:
					print("\n")
					print("	  ",vs)
				print(clr.color.yellow,"\n		PLAYER 1 WON IN ROWS ",clr.color.reset)
				play()
				break
				
			if board[0][0] ==1 and board[1][0] ==1 and board[2][0] ==1:
				for vs in board:
					print("\n")
					print("	  ",vs)
				print(clr.color.yellow,"\n		PLAYER 1 WON IN COLUMN ",clr.color.reset)
				play()
				break
				
			if board[0][1] ==1 and board[1][1] ==1 and board[2][1] ==1:
				for vs in board:
					print("\n")
					print("	  ",vs)
				print(clr.color.yellow,"\n		PLAYER 1 WON IN COLUMN ",clr.color.reset)
				play()
				break
				
			if board[0][2] ==1 and board[1][2] ==1 and board[2][2] ==1:
				for vs in board:
					print("\n")
					print("	  ",vs)
				print(clr.color.yellow,"\n		PLAYER 1 WON IN COLUMN ",clr.color.reset)
				play()
				break
				
				#CHECKING FOR DIAGONALS WIN
			if board[0][0] ==1 and board[1][1] ==1 and board[2][2] ==1 or board[0][2] ==1 and board[1][1] ==1 and board[2][0] ==1:
				for vs in board:
					print("\n")
					print("	  ",vs)
				print(clr.color.yellow,"\n		PLAYER 1 WON IN DIAGONAL ",clr.color.reset)
				play()
				break
				
			
			print("\n		 Columns")
			print("\n	       	   0   1  2")
			
			for index,rows in enumerate(board):
				
				print("\n    	 row =  ",index,rows,"\n	")
			
			
			print("\u001b[33m","\n		** PLAYER 2 , YOUR TURN** \n","\u001b[0m")
			
			while True:
				usr2r = int(input("	ENTER ROW :"))
				usr2c = int(input("	ENTER COLUMN :"))
				if board[usr2r][usr2c]<1: 
					board[usr2r][usr2c]=2
					break
					
					
				if board[usr2r][usr2c]>0:
					print("\u001b[31m","****  NO MORE SPACE TO PLAY THERE (( PLAYER 2 )), PLEASE PLAY AGAIN ","\u001b[0m \n")
					print("\u001b[33m","\n		***** PLAYER 2 , PLAY AGAIN  **** \n","\u001b[0m")
			clear()
					
					
			#LOOKING IF PLAYER 2 IS THE WINNER	
			if board[0][0] ==2 and  board[0][1] ==2 and  board[0][2] ==2 or  board[1][0] ==2 and  board[1][1] ==2 and  board[1][2] ==2 or  board[2][0] ==2 and  board[2][1] ==2  and  board[2][2] ==2:
				for vs in board:
					print("\n")
					print("	  ",vs)
				print(clr.color.yellow,"\n		PLAYER 2 WON IN ROWS ",clr.color.reset)
				play()
				break
				
			if board[0][0] ==2 and board[1][0] ==2 and board[2][0] ==2:
				for vs in board:
					print("\n")
					print("	  ",vs)
				print(clr.color.yellow,"\n		PLAYER 2 WON IN COLUMN ",clr.color.reset)
				play()
				break
				
			if board[0][1] ==2 and board[1][1] ==2 and board[2][1] ==2:
				for vs in board:
					print("\n")
					print("	  ",vs)
				print(clr.color.yellow,"\n		PLAYER 2 WON IN COLUMN ",clr.color.reset)
				play()
				break
				
			if board[0][2] ==2 and board[1][2] ==2 and board[2][2] ==2:
				for vs in board:
					print("\n")
					print("	  ",vs)
				print(clr.color.yellow,"\n		PLAYER 2 WON IN COLUMN ",clr.color.reset)
				play()
				break
				
				#CHECKING FOR DIAGONALS WIN
			if board[0][0] ==2 and board[1][1] ==2 and board[2][2] ==2 or board[0][2] ==2 and board[1][1] ==2 and board[2][0] == 2:
				for vs in board:
					print("\n")
					print("	  ",vs)
				print(clr.color.yellow,"\n		PLAYER 2 WON IN DIAGONAL ",clr.color.reset)
				play()
				break
				
					
			print("\n		 Columns")		
			print("\n	       	   0   1  2")
			for index,rows in enumerate(board):
				
				print("\n    	 row =  ",index,rows,"\n	")
				
				
		except (ValueError,IndexError)  as err1:
			print("\n	********",err1,", \n	 And An Error Occured **Player 1 Enter Again!!! ************ \n")
			print("	PLAYER 1 ENTER AGAIN Below  ↓↓↓↓↓ \n")
			print("\n	 \u001b[32m Waiting ...............\n\u001b[0m")
			time.sleep(3.5)
			print("\n")
			for i in range(len(board)):
				for j in range(len(board[0])):
					board[i][j]=0
					
					
# GAME BOARD
board = [[ 0, 0, 0],[ 0, 0, 0],[ 0, 0, 0]]		
		
		
		
def play():
	enter = input(f"\n \n	{clr.color.blue}{clr.color.BackgroundYellow}     DO YOU WANT TO PLAY (Yes or No)   :{clr.color.reset}")
	if enter.lower()== "yes" or enter.lower() =="y":
			my_game()
	else:
		print("\n\n		OK GOODBYE PLAYERS \n ")
		
		

if __name__=="__main__":
		play()