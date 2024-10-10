import PySimpleGUI as sg
window = sg.Window('Selamat Datang Di Kelas', 
    [[sg.Text("Selamat datang di kelas", font=("Arial",25,"italic","bold","underline",))],
        [sg.Text('NPM       : 2210010526'),],
        [sg.Text('Nama      : Muhammad Indy Ansyari')], 
        [sg.Text('kelas     : 5P Reguler Banjarmasin')],
        [sg.Text('matkul    : Pemrograman Visual')],
    ],size=(500,200))
event, values=window.read()
window.close()
