import turtle

class Letter:
    def __init__(self, character, score_value, amt_remain):
        self.__character = character
        self.__score_value = score_value
        self.__amt_remain = amt_remain

    def getRemaining(self):
        return self.__amt_remain

    def setRemaining(self, letters_used):
        self.__amt_remain -= letters_used


class Player:
    def __init__(self):
        self.__score = 0

class Cell:
    def __init__(self, t, xmin, ymin, width, height, type):
        self.__t = t
        self.__xmin = xmin
        self.__ymin = ymin
        self.__xmax = xmin + width
        self.__ymax = ymin + height
        self.__occupied = False
        self.__type = type
        # self.__multiplier = getMultiplier(self)
        self.__letter = None
        self.__anchor_square = False

# If occupied don't decrease letter count when calculating score
    def setOccupied(self):
        self.__occupied = True

    def isOccupied(self):
        return self.__occupied

    def setLetter(self, letter):
        self.__letter = letter

    def getreadytodraw(self, xcor, ycor):
        self.__t.penup()
        self.__t.goto(xcor, ycor)
        self.__t.pendown()

# If letter != None, then write letter
    def draw(self):  # Draws a cell and fills it with a color depending on type
        if self.__type == 'triple_letter':
            self.__t.fillcolor("#003B6F")  # Tardis Blue
        elif self.__type == 'double_letter':
            self.__t.fillcolor("#3b85c6") # light blue
        elif self.__type == 'double_word':
            self.__t.fillcolor("#f977c1") # pink
        elif self.__type == 'triple_word':
            self.__t.fillcolor("#db0202")  # Blood Red
        else:
            self.__t.fillcolor("#989c9a")  # Earl Grey
        self.getreadytodraw(self.__xmin, self.__ymin)
        self.__t.begin_fill()
        for position in ((self.__xmax, self.__ymin), (self.__xmax, self.__ymax),
                         (self.__xmin, self.__ymax), (self.__xmin, self.__ymin)):
            self.__t.goto(position)
        self.__t.end_fill()

        if self.__letter != None:
            mid_cellx = (self.__xmin + self.__xmax)/2
            mid_celly = (self.__ymax + self.__ymin)/2
            self.getreadytodraw(mid_cellx + 2, mid_celly - 8)
            self.__t.write(self.__letter.upper(), False, align="center", font=("Gothic", 12, "normal"))

class LowestScrabble:
    triple_word = [(0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14)]
    double_word = [(1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10)]
    triple_letter = [(1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9)]
    double_letter = [(0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11)]

    def __init__(self, displayBoard=False):
        self.__turn_number = 0
        self.__game_over = False
        self.__bag = {
        '?':Letter('?', 0, 2),
        'e':Letter('e', 1, 12),
        'a':Letter('a', 1, 9),
        'i':Letter('i', 1, 9),
        'o':Letter('o', 1, 8),
        'n':Letter('n', 1, 6),
        'r':Letter('r', 1, 6),
        't':Letter('t', 1, 6),
        'l':Letter('l', 1, 4),
        's':Letter('s', 1, 4),
        'u':Letter('u', 1, 4),
        'd':Letter('d', 2, 4),
        'g':Letter('g', 2, 3),
        'b':Letter('b', 3, 2),
        'c':Letter('c', 3, 2),
        'm':Letter('m', 3, 2),
        'p':Letter('p', 3, 2),
        'f':Letter('f', 4, 2),
        'h':Letter('h', 4, 2),
        'v':Letter('v', 4, 2),
        'w':Letter('w', 4, 2),
        'y':Letter('y', 4, 2),
        'k':Letter('k', 5, 1),
        'j':Letter('j', 8, 1),
        'x':Letter('x', 8, 1),
        'q':Letter('q', 10, 1),
        'z':Letter('z', 10, 1),
        }
        if displayBoard:
            self.__t = turtle.Turtle()
            self.__t.hideturtle()
            self.__t.speed(0)
            self.__s = self.__t.getscreen()
            self.__s.title("Epic Scrabble Game of Epicness")
            self.__s.tracer(0)
            self.__grid = []

            xpos, ypos = -310, -310
            for row in range(15):
                if row > 0:
                    ypos += 44
                self.__grid.append([])
                for column in range(15):
                    self.__grid[row].append(Cell(self.__t, xpos, ypos, 40, 40, self.getType(row,column)))
                    self.__grid[row][column].draw()
                    xpos += 44
                xpos = -310
            self.__s.update()
            self.__s.mainloop()

    def getType(self, row, col):
        if (row,col) in self.triple_word:
            return 'triple_word'
        elif (row,col) in self.double_word:
            return 'double_word'
        elif (row,col) in self.triple_letter:
            return 'triple_letter'
        elif (row,col) in self.double_letter:
            return 'double_letter'
        else:
            return 'blank'

    def inBoard(self):
        if 0 <= row < 15 and 0 <= col < 15:
            return True
        return False

def compute_score(word):
    return sum([scores[letter.upper()] for letter in word])



def main():
    LowestScrabble(True)

if __name__ == '__main__':
    main()
