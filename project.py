import gtts
from googletrans import Translator
import os
import playsound
def word_translator():
    Quicky ="\nHello... \nQuicky the Translator is here to help you..... \nTell Quicky What to translate............\n"
    print(Quicky)
    Quickysay = gtts.gTTS(Quicky)

    Quickysay.save("audio1.mp3")
    playsound.playsound("audio1.mp3")
    os.remove("audio1.mp3")

    translator= Translator()

    user_input = str(input( "PLEASE ENTER YOUR INPUT : "))

    while True:
        try :
            output = gtts.gTTS(user_input)



            dest_lang = str(input(" \nTell Quicky The Language you want to translate the input \n(Enter the code of the language) : "))

            print(translator.detect(user_input))
            translated = translator.translate(user_input , dest = dest_lang , slow = True )

            print("")
            print(translated.text)
            Output = gtts.gTTS(translated.text , lang = dest_lang )


            Output.save("audio.mp3")
            playsound.playsound("audio.mp3")
            os.remove("audio.mp3")
        except (AssertionError):
            print("\nInvalid Input Please try again .")
word_translator()