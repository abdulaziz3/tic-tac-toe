# Abdulaziz Alothaim 
# D13125638
import numpy
import itertools

class board:
    _board = None
    _dimension = None
    _number_of_player = 3
    _active_player =  0

    def __init__(self, n):
        self._dimension = n
        self._board = numpy.arange(1,self._dimension*self._dimension+1,dtype=numpy.int).reshape(self._dimension,self._dimension)
	# this for array of numbers and group it by user number input such as 5 , will be 5 x 5 . 

    def move(self, loc1, loc2): 
        if(self._board[loc1][loc2]>0): # this function cooardnate the move and print ' X', 'O' AND 'Z'
            self._board[loc1][loc2] = -1* (self._active_player+1) 
            self._active_player = (self._active_player + 1) % self._number_of_player
            print('value',self._board[loc1][loc2])
        else:
            print('Illegal Move')
            return None

    def check_win(self):
        for i in range(0,len(self._board)):
            for x, y in itertools.groupby(self._board[i,:]): # check the winning by rowwise
                if len(list(y)) >= 3:
                    return x

            for x, y in itertools.groupby(self._board[:,i]): # check winning by columnswize 
                if len(list(y)) >= 3:
                    return x

            for x, y in itertools.groupby(self._board.diagonal(i)): # check winning from left upper corner forward 
               if len(list(y)) >= 3:
                   return x

            for x, y in itertools.groupby(numpy.fliplr(self._board).diagonal(i)): # check winning from right upper corner forward 
                if len(list(y)) >= 3:
                   return x

        return 0

    def convert(self, value): # assign letters for players instead of the numbers. 
        if(value == -1):
            return ' X '
        if(value == -2):
            return ' O '
        if(value == -3): 
            return ' Z '
        return '{0:03d}'.format(value)  # format the numbers printed in the grid 

    def print_board(self):
        i = 0
        print()
        for row in range(0,len(self._board)):

            print('\t\t',''.join(['=' for i in range(0,(self._dimension* 5) + self._dimension + 1)]))  # print the board rows
            print('\t\t','| ',end='') # end last row wall
            print(' | '.join([self.convert(self._board[row][col]) for col in range(0, len(self._board[row]))]),end='')  #  print columns 
            print(' |')
            i += 1

        print('\t\t',''.join(['=' for i in range(0, (self._dimension *  5 ) + self._dimension + 1)]))  # print the board underneath the board.
        print()

def run_game():
    size = 0
    print(" # Welcom to the tic tac toe game, this game is slightly different than the game you know.... \n    when game starts will ask  to enter a number that will determine the borad size.... \n    For example, when enter 5 the game board will be 5 x 5 will have 25 boxs...\n     also its 3 player-game !!")
	
    while (size < 5 or size > 10):
        size = int(input('\n\n  # Enter Board size between 5 - 10 : '))
        if (size < 5):
           print('\n\n  # Enter a value more than 5 ')
        elif (size > 10):
           print('\n\n  # Enter a value less than 10 ')
           

    b = board(size)
    b.print_board()

    while(b.check_win() == 0):
        print('Turn for player :  ' + str(b._active_player +1) + '\n')
        line = input(' # Enter the location :  ')
        loc1 = int(line) / len(b._board[0]) -1 / len(b._board[0])  # calculate the cooardnate on rows from the number of box
        loc2 = int(line) % len(b._board[0]) -1 # calculate the cooardnte on column from the numnber of box
        b.move(loc1,loc2) # pass the location by cooardnate
        b.print_board()

    print('\n\n*******************************\n')
    print('CONGRATULATION !! -- PLAYER = ' + str(b._active_player))
    print('\n *******************************\n\n')

run_game()