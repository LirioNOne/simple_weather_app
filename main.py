import sys

from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication
import requests
import json
from main_window import Ui_MainWindow
from date_choose import Ui_Dialog

from datetime import date

KEY = "ca9b69f89f27cc894e665e13a06b26c5"
URL = "https://api.openweathermap.org/data/2.5/weather/"


class Weather_app(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # city_name = self.lineEdit.text()
        city_name = input()
        self.weather_button.clicked.connect(self.get_city_weather(city_name))

    # class Get_Weather():
    def is_response_good(self, response):
        if 200 <= response.status_code < 300:
            return True

    def get_city_weather(self, city_name):
        lang = "ru"
        units = "metric"
        query = {
            "q": city_name,
            "appid": KEY,
            "lang": lang,
            "units": units
        }
        response = requests.get(URL, params=query)

        if self.is_response_good(response):
            result = response.json()

            description = result['weather'][0]['description']
            temperature = result['main']['temp']
            feel_like = result['main']['feels_like']
            pressure = result['main']['pressure']
            humidity = result['main']['humidity']

            out = ""
            out += str(description) + '\n'
            out += str(temperature) + '\n'
            out += str(feel_like) + '\n'
            out += str(pressure) + '\n'
            out += str(humidity) + '\n'
            # out = description + '\n' + temperature + '\n' + feel_like + '\n' + pressure + '\n' + humidity
            self.textBrowser.setText(out)
        else:
            self.textBrowser.setText('Something went wrong')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Weather_app()
    wnd.show()
    sys.exit(app.exec_())
