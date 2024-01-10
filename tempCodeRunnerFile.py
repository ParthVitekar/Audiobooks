
import gtts
import playsound
import os
from googletrans import Translator
from tkinter.filedialog import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import *
import PyPDF2
import pyttsx3
import json

from difflib import get_close_matches

data = json.load(open("dictdb.json"))

def translate(a):
    a = a.lower()
    b=a.capitalize()

    if a in data:
        return data[a]
    elif b in data:
        return data[b]



    elif len(get_close_matches(a, data.keys())) > 0:

        ans = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(a, data.keys())[0])


        if ans == "Y" or ans=="y":


            return data[get_close_matches(a, data.keys())[0]]



        elif ans == "N" or ans=="n":

            return "The given word does not exist."



        else:

            return "We didn't understand your entry."



    else:

        return "The given word does not exist"

root = Tk()
root.geometry('1255x944')


frame = Frame(root,bg ="Indianred1")
frame.place(relwidth =1,relheight =1)
scr1 = Canvas(root , bd = 2, relief = "raised",bg = "pink")
scr1.pack()
title = Label(root ,text = " AUDIOBOOK \nYOUR PERSONAL TEXT READER",bg="azure" ,fg = "DarkSlateBlue",justify ="center" ,padx= 4,pady = 4 ,relief ="raised")
title.config(font = ("Impact",22))
scr1.create_window(200,100,window= title,)



def open_offline():
    global book
    book = filedialog.askopenfilename()

    bookreader = PyPDF2.PdfFileReader(book)
    pages = bookreader.numPages
    reader = pyttsx3.init()

    num  =0
    sp = 1
    n = 0

    print("\nNumber of pages in the book : ",pages)
    sp = int(input("\nenter the page number to start from : "))
    n = int(input("\n select voice [0] for DAVID voice & [1] for ZIRA'S voice : "))

    for num in range(sp-1,pages+1) :

        # Set the pronunciation rate, the default value is 200
        rate = reader.getProperty('rate')
        reader.setProperty('rate', rate - 250)

        # Set the pronunciation size, the range is 0.0-1.0
        volume = reader.getProperty('volume')
        reader.setProperty('volume', 1.0)

        # Set the default voice: voices[0].id represents boys, voices[1].id represents girls
        voices = reader.getProperty('voices')
        reader.setProperty('voice', voices[n].id)

        print("current page number :",num+1)
        print("\n")
        text = bookreader.getPage(num).extractText()
        text = text.replace('\n', '  ')
        print(text)
        reader.say(text)
        reader.runAndWait()
        reader.stop()
        reader.runAndWait()

def open_online():
    global book
    book = askopenfilename()

    bookreader = PyPDF2.PdfFileReader(book)

    num = 0
    sp = 1
    n = 0

    pages = bookreader.numPages

    print("\nNumber of pages in the book : ", pages)
    sp = int(input("\nenter the page number to start from : "))
    dest_lang = str(
        input(" \nEnter The Language you want to translate the input \n(Enter the code of the language) : "))
    translator = Translator()
    for num in range(sp - 1, pages + 1):
        print("current page number :", num + 1)
        print("\n")
        text = bookreader.getPage(num).extractText()
        text = text.replace('\n', '  ')
        print(text)
        # output = gtts.gTTS(text)

        print(translator.detect((text)))
        translated = translator.translate(text, dest=dest_lang, slow=True)

        print("")
        print(translated.text)
        Output = gtts.gTTS(translated.text, lang=dest_lang)
        Output.save("audio.mp3")
        playsound.playsound("audio.mp3")
        os.remove("audio.mp3")

def word_translator():
    Quicky ="\nHello... \nQuicky the Translator is here to help you..... \nTell Quicky What to translate............\n"
    print(Quicky)
    Quickysay = gtts.gTTS(Quicky)

    Quickysay.save("audio1.mp3")
    playsound.playsound("audio1.mp3")
    os.remove("audio1.mp3")

    translator  = Translator()

    user_input = str(input( "PLEASE ENTER YOUR INPUT : "))

    while True:
        try :
            output = gtts.gTTS(user_input)



            dest_lang = str(input(" \nTell Quicky The Language you want to translate the input \n(Enter the code of the language) : "))

            print(translator.detect((user_input)))
            translated = translator.translate(user_input , dest = dest_lang , slow = True )

            print("")
            print(translated.text)
            Output = gtts.gTTS(translated.text , lang = dest_lang )


            Output.save("audio.mp3")
            playsound.playsound("audio.mp3")
            os.remove("audio.mp3")
        except (AssertionError):
            print("\nInvalid Input Please try again .")


def spell_word():
    line = str(input("\n Enter the word\line to listen : "))
    n = int(input(' select voice [0] for male & [1] for female : '))

    pronouncer = pyttsx3.init()

    # Set the pronunciation rate, the default value is 200

    rate = pronouncer.getProperty('rate')
    pronouncer.setProperty('rate', rate - 100)

    # Set the pronunciation size, the range is 0.0-1.0
    volume = pronouncer.getProperty('volume')
    pronouncer.setProperty('volume', 1.0)

    # Set the default voice: voices[0].id represents boys, voices[1].id represents girls
    voices = pronouncer.getProperty('voices')
    pronouncer.setProperty('voice', voices[n].id)

    print("\n listen carefully......\n")

    pronouncer.say(line)
    pronouncer.runAndWait()

def dictionary():
      global dictionary
      print("---------------------------WELCOME TO THE AUDIO BOOK DICTIONARY-------------------------------")
      iter = "y"
      while (iter == "y" or iter == "Y"):
          word = input("enter the word whose meaning you want to find: ")

          output = translate(word)

          if type(output) == list:

              for item in output:
                  print(item)



          else:

              print(output)

          iter = input("To continue browsing for more words,enter 'Y' or press the enter 'key' to exit:  ")
      print("---------------------THANKYOU FOR USING AUDIO BOOK DICTIONARY---------------------------------")

btn1 = Button(root, text='GO OFLINE', bg ="azure3",command=lambda: open_offline(),cursor = "hand2", width =20,height=1 ,font =("Arial",18),
              activebackground= "azure4")
btn2 = Button(root, text='GO ONLINE', bg ="azure3",command=lambda: open_online(),cursor = "hand2", width =20,height=1 ,font =("Arial",18),
              activebackground= "azure4")
btn3 = Button(root, text='Word translator', bg ="azure3",command=lambda: word_translator(),cursor = "hand2", width =20,height=1 ,font =("Arial",18),
              activebackground= "azure4")
btn4 = Button(root, text='Spell Word', bg ="azure3",command=lambda: spell_word(),cursor = "hand2", width =20,height=1 ,font =("Arial",18),
              activebackground= "azure4")
btn5 = Button(root, text='Dictionary', bg ="azure3",command=lambda: dictionary(),cursor = "hand2", width =20,height=1 ,font =("Arial",18),
              activebackground= "azure4")


btn1.pack( )
btn2.pack( )
btn3.pack( )
btn4.pack( )
btn5.pack( )


root.mainloop()
