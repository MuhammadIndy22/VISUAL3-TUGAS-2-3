import PySimpleGUI as sg
sg.theme("Black")
sg.theme_text_color("#00ffff")
window = sg.Window('Selamat Datang Di Kelas', 
    [[sg.Text('FTI UNISKA'),],
        [sg.Text('FAKULTAS TEKNOLOGI INFORMASI')], 
        [sg.Text('UNISKA MAB BANJARMASIN')],
    ],size=(700,300),font=("Arial",25,"italic","bold","underline",))
event, values=window.read()
window.close()
