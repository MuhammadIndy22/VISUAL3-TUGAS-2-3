import PySimpleGUI as sg
susunan=[[sg.VPush()],
            [sg.Text("UNISKA MAB",font=("helvetica",24))],
            [sg.Text("BANJARMASIN", font=("courier", 18))],
            [sg.VPush()]]
Window =sg.Window(title="VPush2",
                  layout=susunan,
                  element_justification = "ceter",
                  size=(430,200))
Window.read()
Window.close()