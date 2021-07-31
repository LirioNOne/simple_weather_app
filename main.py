import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
import requests

from main_window import Ui_MainWindow

KEY = "ca9b69f89f27cc894e665e13a06b26c5"
URL = "https://api.openweathermap.org/data/2.5/weather/"


class Weather_app(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.weather_button.clicked.connect(self.get_city_weather)

    def is_response_good(self, response):
        if 200 <= response.status_code < 300:
            return True

    def get_city_weather(self):
        city_name = self.lineEdit.text()
        city_text = 'in ' + city_name + ':' + '\n'

        lang = "en"
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
            wind_speed = result['wind']['speed']
            visibility = result['visibility']

            out = ""
            out += city_text
            out += str(description) + '\n'
            out += 'Temperature: ' + str(temperature) + '°C' + '\n'
            out += 'Feels like: ' + str(feel_like) + '°C' + '\n'
            out += 'Pressure: ' + str(pressure) + ' hPa' + '\n'
            out += 'Humidity: ' + str(humidity) + '%' + '\n'
            out += 'Wind speed: ' + str(wind_speed) + ' m/s' + '\n'
            out += 'Visibility: ' + str(visibility) + ' m' + '\n'

            self.textBrowser.setText(out)
        else:
            self.textBrowser.setText('Something went wrong')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Weather_app()
    wnd.show()
    sys.exit(app.exec_())
