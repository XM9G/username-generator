# Password Generator

import PySimpleGUI as sg
import random
import pyperclip

sg.theme("Black")
layout = [[sg.Checkbox("Include Lowercase", default=True, key="-LOW-")],
          [sg.Checkbox("Include Capitals", default=False, key="-CAP-")],
          [sg.Checkbox("Include Numbers", default=False, key="-NUM-")],
          [sg.Checkbox("Include Symbols", default=False, key="-SYM-")],         
          [sg.Checkbox("Include Unsusual Symbols", default=False, key="-UNU-")],
          [sg.Slider(range=(8, 20), orientation="horizontal", key="-LEN-")],
          [sg.Text('Length')],
          [sg.Button("Generate", size=(10,1))],
          [sg.Text('Password: '), sg.Text("", key="output")],
          [sg.Button('Copy', size=(10,1))],
          [sg.Text("", key="copied")]]
    

window = sg.Window('Password Generator', layout, size=(300,350))

lowerCase =["a","b",'c',"d","e",'f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upperCase =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number =['1','2','3','4','5','6','7','8','9','0']
symbol =["~",'`','!','@','#','$','%',"^","&",'*',"(",")","_","-",'+','=','[',']','{','}',':',';','"',"'",',','.','/','<','>','?']
unsusualSymbols = ["ඞ","⁋","†","₿","₨","Ⅶ","√","Ꙛ","Ꝟ","‱","※","۞","֍","Ԫ","Ж","Ɋ","ʬ","ǁ","¦","¡","¾","ǂ","ჯ","฿","ᴁ","⁑","⃣",]

password =""
#length = int(input("Password Length: "))
#useUppercase = input('Uppercase (y/n): ')
#useNumbers = input('Numbers (y/n): ')
#useSymbols = input('Symbols (y/n): ')


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
# Calculation & output
    if event == "Generate":
        

        password = ""
        counter = int(0)
        length = values["-LEN-"]
        print(length)
        #generate
        # password = (password + random.choice(lowerCase))

        while counter < length:
            if counter == length:
                break
            if values["-LOW-"] == True:
                if counter == length:
                    break
                password = password + random.choice(lowerCase)
                counter = counter+1
            if values["-CAP-"] == True:
                if counter == length:
                    break
                password = password + random.choice(upperCase)
                counter = counter+1
            if values["-NUM-"] == True:
                if counter == length:
                    break
                password = password + random.choice(number)
                counter = counter+1
            if values["-NUM-"] == True:
                if counter == length:
                    break
                password = password + random.choice(number)
                counter = counter+1    
            if values["-SYM-"] == True:
                if counter == length:
                    break
                password = password + random.choice(symbol)
                counter = counter+1
            if values["-UNU-"] == True:
                if counter == length:
                    break
                password = password + random.choice(unsusualSymbols)
                counter = counter+1
            if counter == 0:
                break

        print(password)
        window['output'].update(password)
        
    if event == "Copy":
        pyperclip.copy(password)
        window['copied'].update('Copied')
        
window.close()