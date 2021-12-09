import webbrowser
from datetime import date
from datetime import datetime

monday = ["iqa-ercy-phw", "undefined"]
tuesday = ["syx-yprw-ito", "ajd-gjre-fqm"]
wednesday = ["sks-zqbv-ynt", "uri-nfwx-xvf"]
thursday = ["vjh-dsyq-tna", "nho-dqpp-uti"]
friday = ["undefined", "vjh-dsyq-tna"]

today = date.today().weekday()
time = int(datetime.now().strftime("%H"))-12

if time <= 2:
    def f(day):
        return {
            0: monday[0],
            1: tuesday[0],
            2: wednesday[0],
            3: thursday[0],
            4: friday[0],
        }.get(day, "weekend")
elif time <= 5:
    def f(day):
        return {
            0: monday[1],
            1: tuesday[1],
            2: wednesday[1],
            3: thursday[1],
            4: friday[1],
        }.get(day, "weekend")

webbrowser.get('windows-default').open(f"http://meet.google.com/{f(today)}?authuser=2")
