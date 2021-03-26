import PySimpleGUI as sg


class WelcomeGuest:
    def __init__(self):
        layout = [
            [sg.Text('Test'), sg.Button('Send')]
        ]

        self.window = sg.Window("Testing", layout, size=(400, 200))

    def display(self):

        while True:
            button, values = self.window.Read()
            if button == sg.WINDOW_CLOSED or button == 'Send':
                break


test = WelcomeGuest()
test.display()
