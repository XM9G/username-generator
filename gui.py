import random
import PySimpleGUI as sg
import pyperclip

sg.theme('Black')
layout = [
    [sg.TabGroup([
        [sg.Tab('Username', [
            [sg.Text("Username Generator", font=(20))],
            [sg.HSeparator()],
            [sg.Button('Generate Names')],
            [sg.Slider(range=(1, 50), key='-UTIMES-', orientation='horizontal')],
            [sg.Multiline(size=(25, 10), key='-OUTPUT-')],
        ])],
        [sg.Tab('Password', [
            [sg.Text('Password Generator', font=(20))],
            [sg.HSeparator()],
            [sg.Checkbox("Include Lowercase", default=True, key="-LOW-")],
            [sg.Checkbox("Include Capitals", default=False, key="-CAP-")],
            [sg.Checkbox("Include Numbers", default=False, key="-NUM-")],
            [sg.Checkbox("Include Symbols", default=False, key="-SYM-")],
            [sg.Checkbox("Include Unsusual Symbols", default=False, key="-UNU-")],
            [sg.Slider(range=(8, 20), orientation="horizontal", key="-LEN-")],
            [sg.Text('Length')],
            [sg.Button("Generate", size=(10,1))],
            [sg.Text('Password: '), sg.Text("", key="output")],
            [sg.Button('Copy', size=(10,1))],
            [sg.Text("", key="copied")]
        ])]
    ])]
]  
          

window = sg.Window('Username/Password Generator', layout, icon="icon.ico", )

lowerCase =["a","b",'c',"d","e",'f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upperCase =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number =['1','2','3','4','5','6','7','8','9','0']
symbol =["~",'`','!','@','#','$','%',"^","&",'*',"(",")","_","-",'+','=','[',']','{','}',':',';','"',"'",',','.','/','<','>','?']
unsusualSymbols = ["ඞ","⁋","†","₿","₨","Ⅶ","√","Ꙛ","Ꝟ","‱","※","۞","֍","Ԫ","Ж","Ɋ","ʬ","ǁ","¦","¡","¾","ǂ","ჯ","฿","ᴁ","⁑","⃣",]

password =""

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Generate Names':
        repeat = values['-UTIMES-']
        name_list = []
        for i in range(int(repeat)):
            with open("word1.txt", "r") as file:
                word1 = file.read().split()    
                cword1 = random.choice(word1)

            with open("word2.txt", "r") as file:
                word2 = file.read().split()    
                cword2 = random.choice(word2)

            number = str(random.randint(21, 99))

            name = cword1 + " " + cword2 + " " + number
            name_list.append(name)
            print(cword1 + " " + cword2 + " " + number)

        window['-OUTPUT-'].update('\n'.join(name_list))

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