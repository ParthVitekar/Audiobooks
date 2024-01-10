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
print("---------------------------WELCOME TO THE AUDIO BOOK DICTIONARY-------------------------------")
iter = "y"
while(iter=="y"or iter=="Y"):
    word = input("enter the word whose meaning you want to find: ")

    output = translate(word)

    if type(output) == list:

        for item in output:
            print(item)



    else:

        print(output)

    iter = input("To continue browsing for more words,enter 'Y' or press the 'enter' key to exit:")
print("---------------------THANKYOU FOR USING AUDIO BOOK DICTIONARY---------------------------------")