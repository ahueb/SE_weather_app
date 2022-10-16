#Weather Application created by Trey, Kyle, Alan and Caleb


import PIL.Image
from PIL.ImageQt import ImageQt
import io
from tkinter import image_types
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton
import requests

class Ui_weatherAPP(object):
    def setupUi(self, weatherAPP):
        weatherAPP.setObjectName("weatherAPP")
        weatherAPP.resize(1080, 720)
        weatherAPP.setStyleSheet("background-color: rgb(115, 182, 240)")

        self.weatherAPPLabel = QtWidgets.QLabel(weatherAPP)
        self.weatherAPPLabel.setGeometry(QtCore.QRect(490, 30, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.weatherAPPLabel.setFont(font)
        self.weatherAPPLabel.setObjectName("weatherAPPLabel")
        self.enterCityLineEdit = QtWidgets.QLineEdit(weatherAPP)
        self.enterCityLineEdit.setGeometry(QtCore.QRect(240, 110, 171, 41))
        self.enterCityLineEdit.setObjectName("enterCityLineEdit")
        self.enterCityLineEdit.setFont(font)
        self.enterCityLabel = QtWidgets.QLabel(weatherAPP)
        self.enterCityLabel.setGeometry(QtCore.QRect(30, 110, 210, 41))

        font = QtGui.QFont()
        font.setPointSize(14)
        self.enterCityLabel.setFont(font)
        self.enterCityLabel.setObjectName("enterCityLabel")

        self.submitBtn = QtWidgets.QPushButton(weatherAPP, clicked = lambda : self.getWeather())
        self.submitBtn.setGeometry(QtCore.QRect(570, 620, 141, 51))
        self.submitBtn.setObjectName("submitBtn")
        self.weatherDataUpddateLabel = QtWidgets.QLabel(weatherAPP)
        self.weatherDataUpddateLabel.setGeometry(QtCore.QRect(30, 190, 401, 51))

        font = QtGui.QFont()
        font.setPointSize(14)
        self.fiveDayForecast = QtWidgets.QPushButton(weatherAPP, clicked = lambda : self.getWeather())
        self.fiveDayForecast.setGeometry(QtCore.QRect(390, 620, 141, 51))
        self.fiveDayForecast.setObjectName("fiveDayForcast")
        self.weatherDataUpddateLabel = QtWidgets.QLabel(weatherAPP)
        self.weatherDataUpddateLabel.setGeometry(QtCore.QRect(30, 200, 401, 51))
        
        font = QtGui.QFont()
        font.setPointSize(14)
        self.weatherDataUpddateLabel.setFont(font)
        self.weatherDataUpddateLabel.setStyleSheet("")
        self.weatherDataUpddateLabel.setText("")
        self.weatherDataUpddateLabel.setObjectName("weatherDataUpddateLabel")
        self.tempLabel = QtWidgets.QLabel(weatherAPP)
        self.tempLabel.setGeometry(QtCore.QRect(30, 250, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tempLabel.setFont(font)
        self.tempLabel.setText("")
        self.tempLabel.setObjectName("tempLabel")
        self.windLabel = QtWidgets.QLabel(weatherAPP)
        self.windLabel.setGeometry(QtCore.QRect(30, 300, 311, 51))

        font = QtGui.QFont()
        font.setPointSize(14)
        self.windLabel.setFont(font)
        self.windLabel.setText("")
        self.windLabel.setObjectName("windLabel")
        self.pressureLabel = QtWidgets.QLabel(weatherAPP)
        self.pressureLabel.setGeometry(QtCore.QRect(30, 350, 311, 51))

        font = QtGui.QFont()
        font.setPointSize(14)
        self.pressureLabel.setFont(font)
        self.pressureLabel.setText("")
        self.pressureLabel.setObjectName("pressureLabel")
        self.humidityLabel = QtWidgets.QLabel(weatherAPP)
        self.humidityLabel.setGeometry(QtCore.QRect(30, 400, 311, 51))

        font = QtGui.QFont()
        font.setPointSize(14)
        self.humidityLabel.setFont(font)
        self.humidityLabel.setText("")
        self.humidityLabel.setObjectName("humidityLabel")

        self.iconLabel = QtWidgets.QLabel(weatherAPP)
        self.iconLabel.setGeometry(QtCore.QRect(800, 100, 211, 211))
        self.iconLabel.setText("")
        self.iconLabel.setScaledContents(True)
        self.iconLabel.setObjectName("iconLabel")

        self.retranslateUi(weatherAPP)
        QtCore.QMetaObject.connectSlotsByName(weatherAPP)

        
    def getWeather(self):
        api_key = '30d4741c779ba94c470ca1f63045390a'

        user_input = self.enterCityLineEdit.text()
        five_day_weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/forecast/daily?q={user_input}&units=metric&cnt=5&appid={api_key}")

        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

        

        if weather_data.json()['cod'] == '404':
            self.weatherDataUpddateLabel.setText(f"No city found")
            print("No City Found")
        else:
            weather = weather_data.json()['weather'][0]['description']
            temp = round(weather_data.json()['main']['temp'])
            windSpeed = round(weather_data.json()['wind']['speed'])
            pressure = round(weather_data.json()['main']['pressure'])
            humidity = weather_data.json()['main']['humidity']
            iconId = weather_data.json()['weather'][0]['icon']
            url = requests.get(f"http://openweathermap.org/img/wn/{iconId}@2x.png")
            in_memory_file = io.BytesIO(url.content)
            im = PIL.Image.open(in_memory_file)
            qIm = ImageQt(im)
            

            self.pressureLabel.setText(f"Current Pressure: {pressure} pascals")
            self.weatherDataUpddateLabel.setText(f"Current Weather: {weather}")
            self.humidityLabel.setText(f"Current Humidity: {humidity}%")
            self.windLabel.setText(f"Current Wind Speed: {windSpeed} mph")
            self.tempLabel.setText(f"Current Temperature: {temp}ºF")
            self.iconLabel.setPixmap(QtGui.QPixmap.fromImage(qIm))

    def retranslateUi(self, weatherAPP):
        _translate = QtCore.QCoreApplication.translate
        weatherAPP.setWindowTitle(_translate("weatherAPP", "weatherAPP"))
        self.weatherAPPLabel.setText(_translate("weatherAPP", "Weather App"))
        self.enterCityLabel.setText(_translate("weatherAPP", "Search City or Zip Code:"))
        self.submitBtn.setText(_translate("weatherAPP", "Current Weather"))
        self.fiveDayForecast.setText(_translate("weatherAPP", "5-Day Forecast"))

#Have to connect button to initiate this class
class fiveDayWeatherWindow(object):
    def setupUi(self, fiveDayWin):
        fiveDayWin.setObjectName("fiveDayWin")
        fiveDayWin.resize(1080, 720)
        fiveDayWin.setStyleSheet("background-color: rgb(115, 182, 240)")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    weatherAPP = QtWidgets.QWidget()
    ui = Ui_weatherAPP()
    ui.setupUi(weatherAPP)
    weatherAPP.show()
    sys.exit(app.exec_())
