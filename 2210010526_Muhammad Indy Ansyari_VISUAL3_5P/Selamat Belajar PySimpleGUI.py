import PySimpleGUI as sg
window = sg.Window(title="Latihan Pertama", layout=[[sg.Text("Selamat Belajar PySimpleGUI")]], size=(500,300))
event, values=window.read()
window.close()