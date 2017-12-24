# Name: Sabrina Warner
# vigenere.py
#Problem: Create a window with a message and key input window that takes the
    #information entered and creates a new encripted message.
#Certification of Authenticity:
    #I certify that this lab is entirely my own work, but I discussed it with
    #Matthew from CS tutoring lab.

from graphics import *
def vigenereGraphics():
    #graphic window
    width = 400
    height = 300
    win = GraphWin("Vigenere", width, height)
    #encode graphic box
    encodeBox = Rectangle(Point(170,150),Point(230,190))
    encodeBox.draw(win)
    encodeText = Text(Point(width/2,170),"Encode")
    encodeText.draw(win)
    #message input box
    messageText = Text(Point(70,50),"Message to code")
    messageText.draw(win)
    messageEntry = Entry(Point(220,50), 30)
    messageEntry.draw(win)
    #keyword input box
    keyText = Text(Point(64,90),"Enter Keyword")
    keyText.draw(win)
    keyEntry = Entry(Point(175,90), 15)
    keyEntry.draw(win)

    
    #gets inputed values when mouse is clicked
    win.getMouse()
    message=(messageEntry.getText())
    keyword=(keyEntry.getText())
    letter=code(message,keyword)
    
    
    #removes the encode box
    encodeBox.undraw()
    encodeText.undraw()
    #resulting message
    resultMessage = Text(Point(width/2,170),"Resulting Message")
    resultMessage.draw(win)
    endMessage = Text(Point(width/2, 190), letter)
    endMessage.draw(win)

    #click to close
    closeMessage = Text(Point(width/2,280),"Click Anywhere to Close Window")
    closeMessage.draw(win)

    win.getMouse()
    win.close()


def code(message,keyword):
    #removes spaces and makes message uppercase
    message = message.replace(' ', '')
    message = message.upper()
    #makes keyword uppercase
    keyword=keyword.upper()
    #makes the a new key that spreads the length of the message
    newKey=keyword*len(message)



    letter=""
    for i in range(0,len(message)):
        #ensures the ord values stay in the range of the alphabet
        newNum = ord(message[i])-65 + ord(newKey[i])-65
        newNum = (newNum % 26) +65
        #accumulates the letters of the newNum
        letter += chr(newNum)
    return letter

    

def main():
    vigenereGraphics()
    
main()


##vigenereCipher()


