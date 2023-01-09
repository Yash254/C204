import socket
from tkinter import *
from  threading import Thread
from PIL import ImageTk, Image

screen_width = None
screen_height = None

SERVER = None
PORT = None
IP_ADDRESS = None


canvas1 = None

playerName = None
nameEntry = None
nameWindow = None

def saveName():
    global playerName
    global nameEntry
    global nameWindow
    global SERVER

    playerName=nameEntry.get()
    nameEntry.delete(0,END)
    nameWindow.destroy()
    SERVER.send(playerName.encode())
    

#Teacher write code here for askPlayerName()
def askPlayerName():
    global playerName
    global nameEntry
    global nameWindow
    global screen_height
    global screen_width
    global canvas1

    nameWindow=Tk()
    nameWindow.title('LUDO GAME')
    nameWindow.attributes('-fullscreen',True)

    screen_width=nameWindow.winfo_screenwidth()
    screen_height=nameWindow.winfo_screenheight()
    
    bg=ImageTk.PhotoImage(file='./assets/background.png')

    canvas1=Canvas(nameWindow,width=500, height=500)
    canvas1.pack(fill='both', expand=True)
    canvas1.create_text(screen_width/2, screen_height/4, text='Enter Your Name',
                        font=('Helvetica 14', 100), fill='white')
    
    nameEntry=Entry(nameWindow, width=15, justify='center', font=('Helvetica 14', 50),
                    bd=5,bg='white')
    nameEntry.place(x=screen_width/2-220,y=screen_height/4+100)

    button=Button(nameWindow,text='Save',width=15,height=2,command=saveName,
                    font=('Helvetica 13',50),bd=3,bg='cyan')
    button.place(x=screen_width/2-130,y=screen_height/2-30)

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    PORT  = 5000
    IP_ADDRESS = '127.0.0.1'

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))


    # Creating First Window
    askPlayerName()




setup()
