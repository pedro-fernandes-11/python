import PySimpleGUI as sg


class ScreenTest:
    def __init__(self):
        sg.change_look_and_feel('Black')
        layout = [
                [sg.Text("Name", size=(5, 0)), sg.Input(size=(20, 0), key='name'),
                 sg.Text("Age", size=(5, 0)), sg.Input(size=(20, 0), key='age')],
                [sg.Text("Select the programming languages you're into to code with:")],
                [sg.Checkbox("Python", key='python'), sg.Checkbox("Java", key='java'),
                 sg.Checkbox("JavaScript", key='js'), sg.Checkbox("Ruby", key='ruby')],
                [sg.Text("Did you master 'em?")],
                [sg.Radio("Yes", "answer", key="mastered"), sg.Radio("No", "cartoes")],
                [sg.Text("How much do you want to earn working for us")],
                [sg.Slider((0, 10000), default_value=0, orientation='horizontal', size=(45, 20), key='wage')],
                [sg.Button("Send")],
                [sg.Output(size=(55, 10))]
                 ]

        self.window = sg.Window("Hiring Form", layout)

    def initialize(self):

        while True:
            button, values = self.window.Read()
            name = values['name']
            age = values['age']
            w_python = values['python']
            w_java = values['java']
            w_js = values['js']
            w_ruby = values['ruby']
            master = values['mastered']
            wage = values['wage']

            print(f"Your name is {name}, you're {age} old.\n you're able to code with \npython: {w_python},", end=' ')
            print(f"java: {w_java}, javascrpit: {w_js} and ruby: {w_ruby}.")
            print(f"You're willing to earn {wage} working for us.")

            if master:
                print(f"You're hired because you master them")
            else:
                print(f"You're not hired, keep focus and master them")


tela = ScreenTest()
tela.initialize()
