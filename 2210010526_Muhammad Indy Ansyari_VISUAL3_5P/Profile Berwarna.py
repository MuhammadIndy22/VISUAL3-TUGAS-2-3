import PySimpleGUI as sg
sg.theme("Black")
sg.theme_text_color("#F5F5DC")
window = sg.Window('Profile Berwarna', 
    [[sg.Text('NPM :2210010526'),],
        [sg.Text('Nama :Muhammad Indy Ansyari')], 
        [sg.Text('kelas :5P reguler Banjarmasin')],
        [sg.Text('matkul : pempgraman Visual')],
    ],size=(500,200)).read(close=True)
event, values=window.read()
window.close()