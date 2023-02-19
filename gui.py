import random
import PySimpleGUI as sg

sg.theme('Black')

layout = [[sg.Button('Generate Names')],
          [sg.Multiline(size=(25, 5), key='-OUTPUT-')]]

window = sg.Window('Username Generator', layout, icon="icon.ico")

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Generate Names':
        repeat = 5
        name_list = []
        for i in range(repeat):
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

window.close()
