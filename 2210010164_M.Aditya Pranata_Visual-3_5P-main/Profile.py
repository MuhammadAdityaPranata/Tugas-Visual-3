import PySimpleGUI as sg
window = sg.Window('Profile', 
    [[sg.Text('NPM :2210010164'),],
        [sg.Text('Nama :M. Aditya Pranata')], 
        [sg.Text('kelas :5P reguler Banjarmasin')],
        [sg.Text('matkul : pempgraman Visual')],
    ],size=(500,200))
event, values=window.read()
window.close()
