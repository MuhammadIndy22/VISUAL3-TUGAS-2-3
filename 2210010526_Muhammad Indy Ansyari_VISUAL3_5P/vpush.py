import PySimpleGUI as sg
susunan=[[sg.VPush(),
          sg.Text("UNISKA MAB",font=("helvetica",24)),
          sg.Push()],
          [sg.Push(),
           sg.Text("BANJARMASIN", font=("courier", 18)),
           sg.Push()],
           [sg.VPush()]
           ]
Window =sg.Window(title="VPush",
                  layout=susunan,
                  size=(430,200))
Window.read()
Window.close()