import PySimpleGUI as sg
susunan=[[sg.Text("UNISKA MAB",font=("helvetica",24))],
        [sg.Text("BANJARMASIN", font=("courier", 18))],]
Window =sg.Window(title="Resize",
                  layout=susunan,
                  element_justification = "ceter",
                  icon="favicon.ico",
                  resizable=True,
                  size=(430,200))
Window.read()
Window.close()