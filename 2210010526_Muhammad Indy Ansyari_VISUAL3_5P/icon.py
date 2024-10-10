import PySimpleGUI as sg
susunan=[[sg.Text("UNISKA MAB",font=("helvetica",24))],
        [sg.Text("BANJARMASIN", font=("courier", 18))],]
Window =sg.Window(title="Icon",
                  layout=susunan,
                  element_justification = "ceter",
                  size=(430,200))
Window.read()
Window.close()