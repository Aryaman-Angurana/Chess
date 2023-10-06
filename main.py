from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.config import Config

from dchess import inputPos, gameover

Config.set('graphics', 'width', 700)
Config.set('graphics', 'height', 700)
Builder.load_file("layout.kv")

prev_command = ""
prev_coor = ()

board =[["Rk", "Kt", "Bs", "Kn", "Qn", "Bs", "Kt", "Rk"],
        ["Pn", "Pn", "Pn", "Pn", "Pn", "Pn", "Pn", "Pn"],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["pn", "pn", "pn", "pn", "pn", "pn", "pn", "pn"],
        ["rk", "kt", "bs", "kn", "qn", "bs", "kt", "rk"]]

player = 1
element = 0


class MyLayout(Widget):

    def start(self):
        id = self.ids["start"]
        id.disabled = True
        id = self.ids["draw"]
        id.disabled = False
        for i in range(0,8):
            for j in (range(0,8)):
                string = self.ids[chr(i+65)+str(j+1)]
                string.disabled = False

    def draw(self):
        ele = self.ids['box']
        ele.size_hint = (1,1)
        id = self.ids["draw"]
        id.disabled = True
        for i in range(0,8):
            for j in (range(0,8)):
                string = self.ids[chr(i+65)+str(j+1)]
                string.disabled = True
        label = self.ids['go']
        label.font_size = 45
        label.text= "-------Draw-------"


    def click(self,a):
        global prev_command
        global player
        global board
        if prev_command == "":
            prev_command = a
            id=self.ids[a]
            id.disabled = True

        else:
            id=self.ids[prev_command]
            id.disabled = False
            board1 = [["", "", "", "", "", "", "", ""],["", "", "", "", "", "", "", ""],["", "", "", "", "", "", "", ""],["", "", "", "", "", "", "", ""],["", "", "", "", "", "", "", ""],["", "", "", "", "", "", "", ""],["", "", "", "", "", "", "", ""],["", "", "", "", "", "", "", ""]]
            for i in range(0,8):
                for j in range(0,8):
                    board1[i][j] = board[i][j]
            board = inputPos(prev_command,a,board,player)

            if (board1 != board):
                if (player == 1):
                    player = 2
                else:
                    player = 1            
            prev_command = ""



class ChessGame(App):
    def draw(self):
        for i in range(0,8):
            for j in (range(0,8)):
                string = self.root.ids[chr(i+65)+str(j+1)]
                if (board[i][j] == "kt"):
                    string.text= "n"
                elif (board[i][j] == "Kt"):
                    string.text= "N"
                elif (board[i][j] != ""):
                    string.text= board[i][j][0]
                else:
                    string.text= ""


    def gameOver(self):
        if (gameover(board)):
            ele = self.root.ids['box']
            ele.size_hint = (1,1)
            
            for i in range(0,8):
                for j in (range(0,8)):
                    string = self.root.ids[chr(i+65)+str(j+1)]
                    string.disabled = True
            
            string = self.root.ids["draw"]
            string.disabled = True

            label = self.root.ids['go']
            label.font_size = 45
            if (player == 1):
                label.text = "----Game Over--------Player 2 wins"
            else:
                label.text = "----Game Over--------Player 1 wins"

    a = (0,0)

    def pawns(self):
        global element
        if (element == 0):
            self.root.ids.layout.remove_widget(self.root.ids.pawns)
            element = 1
        for i in range (0,8):
            if (board[0][i] == "pn" or board[7][i] == "Pn"):
                global a
                self.root.ids.layout.add_widget(self.root.ids.pawns)
                if (board[0][i] == "pn"):
                    a = (0,i)
                else:
                    a = (7,i)
                for i in range(0,8):
                    for j in (range(0,8)):
                        string = self.root.ids[chr(i+65)+str(j+1)]
                        string.disabled = True
                break
    

    def pawn_promotion(self,var):
        if (board[a[0]][a[1]][0].islower()):
            board[a[0]][a[1]] = var[0].lower() + var[1]
        else:
            board[a[0]][a[1]] = var
        for i in range(0,8):
            for j in (range(0,8)):
                string = self.root.ids[chr(i+65)+str(j+1)]
                string.disabled = False
        self.root.ids.layout.remove_widget(self.root.ids.pawns)

    def build(self):
        Window.size = (640,640)

        return MyLayout()
    
if __name__ == "__main__":
    ChessGame().run()