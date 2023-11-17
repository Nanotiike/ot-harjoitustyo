class sudoku:
    def __init__(self, board):
        self.board = board

    def print_board(self):
        c=0
        for i in range(len(self.board)):
            r=0
            for j in range(len(self.board[i])):
                print(self.board[i][j], end=" ")
                r+=1
                if r==3:
                    print("|",end=" ")
                    r=0
            print()
            c+=1
            if c==3:
                print("---------------------")
                c=0

    def check_number(self,x,y,number):
        for i in range(len(self.board)):
            if self.board[x][i]==number:
                return False
            
        for i in range(len(self.board)):
            if self.board[i][y]==number:
                return False
        
        x0=(x//3)*3
        y0=(y//3)*3
        for i in range(3):
            for j in range(3):
                if self.board[x0+i][y0+j]==number:
                    return False

        return True