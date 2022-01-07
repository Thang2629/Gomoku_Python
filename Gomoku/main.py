from Tkinter import *
import tkMessageBox
 
class Application(Frame):
    def displayBoard(self):
        self.canvas = Canvas(self, width="280m", height="280m", bg='#F7DCB4')
        self.canvas.pack(side=LEFT)
 
        #black starts
        self.color = 'black'
 
        self.size = 50
        size = self.size
        for x in range(19):
            self.canvas.create_line(size+x*size,size,size+x*size,size+18*size)
        for y in range(19):
            self.canvas.create_line(size,size+y*size,size+18*size,size+size*y)
 
        # initialize the board (for checking the rules, wins etc.)
        self.board = [[-1 for col in range(19)] for row in range(19)]
 
        self.canvas.bind('', callback)
        self.pack()
 
    def __init__(self, master=None):
        Frame.__init__(self, master)
        Pack.config(self)
 
    def changeColor(self):
        if self.color == 'black':
            self.color = 'white'
        else:
            self.color = 'black'
 
    def updateBoard(self, x,y):
        offset = 7.5
        #we decided the size of the grid based on "self size"
        #now we calculate which row and column we should place things by
        #rounding to the nearest intersection
        #we do this by dividing the pixel by grid size and rounding
        row = int(round(float(x)/self.size))
        column = int(round(float(y)/self.size))
 
        new_x=row*50
        new_y=column*50
 
        self.canvas.create_oval(new_x-offset,new_y-offset,new_x+offset,
new_y+offset, width = 1, fill=self.color, outline ='black')
        #check if legal move
        #based on if space is already occupied
 
        if self.checkMove(row,column) == False:
            print 'illegal move'
            sys.exit()
        else:
 
            print 'next move by ' + self.color, [row, column]
 
        #ongoing tally of where pieces are
        #black -- zero entry
        #white -- 1 entry
        #nothing -- original negative one entry
        if self.color == 'black':
            self.board[row][column]=0
 
        elif self.color =='white':
            self.board[row][column]=1
 
        #check if last move results in win
        #if so: ask if new game
        if self.checkForWin(row, column) == True:
            print self.color + ' wins!'
 
            answer= tkMessageBox.askyesno('Game Over!', self.color + ' wins! -- New Game?')
            print answer
            if answer == True:
                print 'yes'
                self.resetBoard()
            else:
                print 'no'
                sys.exit()
 
        self.changeColor()
 
    def checkMove(self, x,y):
        if x < 0 or x > 18 or y < 0 or y > 18:
            print 'out of bounds'
            return False
        elif self.board[x][y] != -1:
            print self.board[x][y]
            print 'already occupied'
            return False
        else:
            return True
    def checkForWin(self,x,y):
        dirs = [(1,0), (0,1), (1,1), (1,-1)]
        for (dx,dy) in dirs:
            sum1 = self.checkLines(x,y,dx,dy)
            sum2 = self.checkLines(x,y,-dx,-dy)
            #print "length: ", anz1+anz2+1
 
            if sum1+sum2 >= 4:
                return True
 
        return False
 
    def checkLines(self, x,y,dx,dy):
        count = -1  # don't count x,y itself
        current = self.board[x][y]
        while x >= 0 and y >= 0 and x <= 18 and y <= 18 and self.board[x][y] == current:
            count = count + 1
            x = x + dx
            y = y + dy
        return count
    def resetBoard(self):
        self.canvas.destroy()
        self.displayBoard()
 
def callback(event):
    gmkgame.updateBoard(event.x,event.y)
 
gmkgame = Application()
gmkgame.displayBoard()
gmkgame.mainloop()