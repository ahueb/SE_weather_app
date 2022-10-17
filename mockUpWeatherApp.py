import PIL.Image
from PIL.ImageQt import ImageQt
import io
from tkinter import image_types
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QPushButton
import requests


class Ui_weatherAPP(object):
    def setupUi(self, weatherAPP):
        if not weatherAPP.objectName():
            weatherAPP.setObjectName(u"weatherAPP")
        weatherAPP.resize(1080, 720)
        weatherAPP.setStyleSheet(u"")

        self.weatherAPPLabel = QLabel(weatherAPP)
        self.weatherAPPLabel.setObjectName(u"weatherAPPLabel")
        self.weatherAPPLabel.setGeometry(QRect(480, 20, 101, 51))
        font = QFont()
        font.setPointSize(14)
        self.weatherAPPLabel.setFont(font)

        self.enterCityLineEdit = QLineEdit(weatherAPP)
        self.enterCityLineEdit.setObjectName(u"enterCityLineEdit")
        self.enterCityLineEdit.setGeometry(QRect(220, 110, 171, 41))
        self.enterCityLabel = QLabel(weatherAPP)
        self.enterCityLabel.setObjectName(u"enterCityLabel")
        self.enterCityLabel.setGeometry(QRect(10, 110, 181, 41))
        font1 = QFont()
        font1.setPointSize(12)
        self.enterCityLabel.setFont(font1)

        self.iconLabel = QLabel(weatherAPP)
        self.iconLabel.setGeometry(QRect(30, 450, 211, 211))
        self.iconLabel.setText("")
        self.iconLabel.setScaledContents(True)
        self.iconLabel.setObjectName("iconLabel")

        self.submitBtn = QPushButton(weatherAPP, clicked = lambda : self.getWeather(self.enterCityLineEdit.text()))
        self.submitBtn.setObjectName(u"submitBtn")
        self.submitBtn.setGeometry(QRect(460, 620, 141, 51))

        self.cityLabel = QLabel(weatherAPP)
        self.cityLabel.setObjectName(u"cityLabel")
        self.cityLabel.setGeometry(QRect(30, 150, 321, 51))
        self.cityLabel.setFont(font1)

        self.weatherDataUpddateLabel = QLabel(weatherAPP)
        self.weatherDataUpddateLabel.setObjectName(u"weatherDataUpddateLabel")
        self.weatherDataUpddateLabel.setGeometry(QRect(30, 200, 401, 51))
        self.weatherDataUpddateLabel.setFont(font1)
        self.weatherDataUpddateLabel.setStyleSheet(u"")

        self.tempLabel = QLabel(weatherAPP)
        self.tempLabel.setObjectName(u"tempLabel")
        self.tempLabel.setGeometry(QRect(30, 250, 321, 51))
        self.tempLabel.setFont(font1)

        self.windLabel = QLabel(weatherAPP)
        self.windLabel.setObjectName(u"windLabel")
        self.windLabel.setGeometry(QRect(30, 300, 311, 51))
        self.windLabel.setFont(font1)

        self.pressureLabel = QLabel(weatherAPP)
        self.pressureLabel.setObjectName(u"pressureLabel")
        self.pressureLabel.setGeometry(QRect(30, 350, 311, 51))
        self.pressureLabel.setFont(font1)

        self.humidityLabel = QLabel(weatherAPP)
        self.humidityLabel.setObjectName(u"humidityLabel")
        self.humidityLabel.setGeometry(QRect(30, 400, 311, 51))
        self.humidityLabel.setFont(font1)

        self.line = QFrame(weatherAPP)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(420, 100, 20, 511))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.line_2 = QFrame(weatherAPP)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(500, 240, 531, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.setupFiveDayUI()

        self.retranslateUi(weatherAPP)

        QMetaObject.connectSlotsByName(weatherAPP)
    # setupUi

    def setupFiveDayUI(self):
        # 5 day forecast:
        font2 = QFont()
        font2.setPointSize(8)

        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)

        # 1

        self.iconDayOne = QLabel(weatherAPP)
        self.iconDayOne.setGeometry(QRect(380, 80, 211, 211))
        self.iconDayOne.setText("")
        self.iconDayOne.setScaledContents(True)
        self.iconDayOne.setObjectName("iconDayOne")

        self.labelDayOne = QLabel(weatherAPP)
        self.labelDayOne.setObjectName(u"labelDayOne")
        self.labelDayOne.setGeometry(QRect(450, 330, 171, 41))
        self.labelDayOne.setFont(font3)
        self.labelDayOne.setAlignment(Qt.AlignCenter)
        self.labelDayOne.setStyleSheet(u"")

        self.weatherDayOne = QLabel(weatherAPP)
        self.weatherDayOne.setObjectName(u"weatherDayOne")
        self.weatherDayOne.setGeometry(QRect(450, 370, 171, 41))
        self.weatherDayOne.setFont(font2)
        self.weatherDayOne.setAlignment(Qt.AlignCenter)
        self.weatherDayOne.setStyleSheet(u"")

        self.tempDayOne = QLabel(weatherAPP)
        self.tempDayOne.setObjectName(u"tempDayOne")
        self.tempDayOne.setGeometry(QRect(450, 410, 171, 41))
        self.tempDayOne.setFont(font2)
        self.tempDayOne.setAlignment(Qt.AlignCenter)

        self.windDayOne = QLabel(weatherAPP)
        self.windDayOne.setObjectName(u"windDayOne")
        self.windDayOne.setGeometry(QRect(450, 450, 171, 41))
        self.windDayOne.setFont(font2)
        self.windDayOne.setAlignment(Qt.AlignCenter)

        self.pressureDayOne = QLabel(weatherAPP)
        self.pressureDayOne.setObjectName(u"pressureDayOne")
        self.pressureDayOne.setGeometry(QRect(450, 490, 171, 41))
        self.pressureDayOne.setFont(font2)
        self.pressureDayOne.setAlignment(Qt.AlignCenter)

        self.humidityDayOne = QLabel(weatherAPP)
        self.humidityDayOne.setObjectName(u"humidityDayOne")
        self.humidityDayOne.setGeometry(QRect(450, 540, 171, 41))
        self.humidityDayOne.setFont(font2)
        self.humidityDayOne.setAlignment(Qt.AlignCenter)

        # 2

        self.iconDayTwo = QLabel(weatherAPP)
        self.iconDayTwo.setGeometry(QRect(600, 80, 211, 211))
        self.iconDayTwo.setText("")
        self.iconDayTwo.setScaledContents(True)
        self.iconDayTwo.setObjectName("iconDayTwo")
        
        self.labelDayTwo = QLabel(weatherAPP)
        self.labelDayTwo.setObjectName(u"labelDayTwo")
        self.labelDayTwo.setGeometry(QRect(550, 330, 171, 41))
        self.labelDayTwo.setFont(font3)
        self.labelDayTwo.setAlignment(Qt.AlignCenter)
        self.labelDayTwo.setStyleSheet(u"")

        self.weatherDayTwo = QLabel(weatherAPP)
        self.weatherDayTwo.setObjectName(u"weatherDayTwo")
        self.weatherDayTwo.setGeometry(QRect(550, 370, 171, 41))
        self.weatherDayTwo.setFont(font2)
        self.weatherDayTwo.setAlignment(Qt.AlignCenter)
        self.weatherDayTwo.setStyleSheet(u"")

        self.tempDayTwo = QLabel(weatherAPP)
        self.tempDayTwo.setObjectName(u"tempDayTwo")
        self.tempDayTwo.setGeometry(QRect(550, 410, 171, 41))
        self.tempDayTwo.setAlignment(Qt.AlignCenter)
        self.tempDayTwo.setFont(font2)

        self.windDayTwo = QLabel(weatherAPP)
        self.windDayTwo.setObjectName(u"windDayTwo")
        self.windDayTwo.setGeometry(QRect(550, 450, 171, 41))
        self.windDayTwo.setAlignment(Qt.AlignCenter)
        self.windDayTwo.setFont(font2)

        self.pressureDayTwo = QLabel(weatherAPP)
        self.pressureDayTwo.setObjectName(u"pressureDayTwo")
        self.pressureDayTwo.setGeometry(QRect(550, 490, 171, 41))
        self.pressureDayTwo.setAlignment(Qt.AlignCenter)
        self.pressureDayTwo.setFont(font2)

        self.humidityDayTwo = QLabel(weatherAPP)
        self.humidityDayTwo.setObjectName(u"humidityDayTwo")
        self.humidityDayTwo.setGeometry(QRect(550, 540, 171, 41))
        self.humidityDayTwo.setAlignment(Qt.AlignCenter)
        self.humidityDayTwo.setFont(font2)

        # 3

        self.iconDayThree = QLabel(weatherAPP)
        self.iconDayThree.setGeometry(QRect(450, 100, 211, 211))
        self.iconDayThree.setText("")
        self.iconDayThree.setScaledContents(True)
        self.iconDayThree.setObjectName("iconDayThree")
        
        self.labelDayThree = QLabel(weatherAPP)
        self.labelDayThree.setObjectName(u"labelDayThree")
        self.labelDayThree.setGeometry(QRect(650, 330, 171, 41))
        self.labelDayThree.setFont(font3)
        self.labelDayThree.setAlignment(Qt.AlignCenter)
        self.labelDayThree.setStyleSheet(u"")

        self.weatherDayThree = QLabel(weatherAPP)
        self.weatherDayThree.setObjectName(u"weatherDayThree")
        self.weatherDayThree.setGeometry(QRect(650, 370, 171, 41))
        self.weatherDayThree.setFont(font2)
        self.weatherDayThree.setAlignment(Qt.AlignCenter)
        self.weatherDayThree.setStyleSheet(u"")

        self.tempDayThree = QLabel(weatherAPP)
        self.tempDayThree.setObjectName(u"tempDayThree")
        self.tempDayThree.setGeometry(QRect(650, 410, 171, 41))
        self.tempDayThree.setFont(font2)
        self.tempDayThree.setAlignment(Qt.AlignCenter)

        self.windDayThree = QLabel(weatherAPP)
        self.windDayThree.setObjectName(u"windDayThree")
        self.windDayThree.setGeometry(QRect(650, 450, 171, 41))
        self.windDayThree.setFont(font2)
        self.windDayThree.setAlignment(Qt.AlignCenter)

        self.pressureDayThree = QLabel(weatherAPP)
        self.pressureDayThree.setObjectName(u"pressureDayThree")
        self.pressureDayThree.setGeometry(QRect(650, 490, 171, 41))
        self.pressureDayThree.setFont(font2)
        self.pressureDayThree.setAlignment(Qt.AlignCenter)

        self.humidityDayThree = QLabel(weatherAPP)
        self.humidityDayThree.setObjectName(u"humidityDayThree")
        self.humidityDayThree.setGeometry(QRect(650, 540, 171, 41))
        self.humidityDayThree.setFont(font2)
        self.humidityDayThree.setAlignment(Qt.AlignCenter)

        # 4

        self.icon = QLabel(weatherAPP)
        self.icon.setGeometry(QRect(450, 100, 211, 211))
        self.icon.setText("")
        self.icon.setScaledContents(True)
        self.icon.setObjectName("icon")
        
        self.labelDayFour = QLabel(weatherAPP)
        self.labelDayFour.setObjectName(u"labelDayFour")
        self.labelDayFour.setGeometry(QRect(750, 330, 171, 41))
        self.labelDayFour.setFont(font3)
        self.labelDayFour.setAlignment(Qt.AlignCenter)
        self.labelDayFour.setStyleSheet(u"")

        self.weatherDayFour = QLabel(weatherAPP)
        self.weatherDayFour.setObjectName(u"weatherDayFour")
        self.weatherDayFour.setGeometry(QRect(750, 370, 171, 41))
        self.weatherDayFour.setFont(font2)
        self.weatherDayFour.setAlignment(Qt.AlignCenter)
        self.weatherDayFour.setStyleSheet(u"")

        self.tempDayFour = QLabel(weatherAPP)
        self.tempDayFour.setObjectName(u"tempDayFour")
        self.tempDayFour.setGeometry(QRect(750, 410, 171, 41))
        self.tempDayFour.setFont(font2)
        self.tempDayFour.setAlignment(Qt.AlignCenter)

        self.windDayFour = QLabel(weatherAPP)
        self.windDayFour.setObjectName(u"windDayFour")
        self.windDayFour.setGeometry(QRect(750, 450, 171, 41))
        self.windDayFour.setFont(font2)
        self.windDayFour.setAlignment(Qt.AlignCenter)

        self.pressureDayFour = QLabel(weatherAPP)
        self.pressureDayFour.setObjectName(u"pressureDayFour")
        self.pressureDayFour.setGeometry(QRect(750, 490, 171, 41))
        self.pressureDayFour.setFont(font2)
        self.pressureDayFour.setAlignment(Qt.AlignCenter)

        self.humidityDayFour = QLabel(weatherAPP)
        self.humidityDayFour.setObjectName(u"humidityDayFour")
        self.humidityDayFour.setGeometry(QRect(750, 540, 171, 41))
        self.humidityDayFour.setFont(font2)
        self.humidityDayFour.setAlignment(Qt.AlignCenter)

        # 5

        self.icon = QLabel(weatherAPP)
        self.icon.setGeometry(QRect(450, 100, 211, 211))
        self.icon.setText("")
        self.icon.setScaledContents(True)
        self.icon.setObjectName("icon")
        
        self.labelDayFive = QLabel(weatherAPP)
        self.labelDayFive.setObjectName(u"labelDayFive")
        self.labelDayFive.setGeometry(QRect(850, 330, 171, 41))
        self.labelDayFive.setFont(font3)
        self.labelDayFive.setAlignment(Qt.AlignCenter)
        self.labelDayFive.setStyleSheet(u"")

        self.weatherDayFive = QLabel(weatherAPP)
        self.weatherDayFive.setObjectName(u"weatherDayFive")
        self.weatherDayFive.setGeometry(QRect(850, 370, 171, 41))
        self.weatherDayFive.setFont(font2)
        self.weatherDayFive.setAlignment(Qt.AlignCenter)
        self.weatherDayFive.setStyleSheet(u"")

        self.tempDayFive = QLabel(weatherAPP)
        self.tempDayFive.setObjectName(u"tempDayFive")
        self.tempDayFive.setGeometry(QRect(850, 410, 171, 41))
        self.tempDayFive.setFont(font2)
        self.tempDayFive.setAlignment(Qt.AlignCenter)

        self.windDayFive = QLabel(weatherAPP)
        self.windDayFive.setObjectName(u"windDayFive")
        self.windDayFive.setGeometry(QRect(850, 450, 171, 41))
        self.windDayFive.setFont(font2)
        self.windDayFive.setAlignment(Qt.AlignCenter)

        self.pressureDayFive = QLabel(weatherAPP)
        self.pressureDayFive.setObjectName(u"pressureDayFive")
        self.pressureDayFive.setGeometry(QRect(850, 490, 171, 41))
        self.pressureDayFive.setFont(font2)
        self.pressureDayFive.setAlignment(Qt.AlignCenter)

        self.humidityDayFive = QLabel(weatherAPP)
        self.humidityDayFive.setObjectName(u"humidityDayFive")
        self.humidityDayFive.setGeometry(QRect(850, 540, 171, 41))
        self.humidityDayFive.setFont(font2)
        self.humidityDayFive.setAlignment(Qt.AlignCenter)

    def retranslateUi(self, weatherAPP):
        weatherAPP.setWindowTitle(QCoreApplication.translate("weatherAPP", u"weatherAPP", None))
        self.weatherAPPLabel.setText(QCoreApplication.translate("weatherAPP", u"Weather", None))
        self.enterCityLabel.setText(QCoreApplication.translate("weatherAPP", u"Search City or Zip Code:", None))
        self.submitBtn.setText(QCoreApplication.translate("weatherAPP", u"Get Forecast", None))
        location_string = f"{self.getLocation()['city']}, {self.getLocation()['region']}"
        self.getWeather(location_string)        
    # retranslateUi

    def getLocation(self):
        ip = requests.get('https://api64.ipify.org?format=json').json()['ip']
        location_response = requests.get(f'https://ipapi.co/{ip}/json').json()

        location_data = {
            "ip": ip,
            "city": location_response['city'],
            "region": location_response['region'],
            "country": location_response["country_name"],
            "lat": location_response['latitude'],
            "lon": location_response['longitude'],
            "postal": location_response['postal']
        }

        return location_data

    def updateCurrentWeather(self, weather_data):
        city = weather_data.json()['name']
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
        
        self.cityLabel.setText(f"Current City: {city}")
        self.pressureLabel.setText(f"Current Pressure: {pressure} pascals")
        self.weatherDataUpddateLabel.setText(f"Current Weather: {weather}")
        self.humidityLabel.setText(f"Current Humidity: {humidity}%")
        self.windLabel.setText(f"Current Wind Speed: {windSpeed} mph")
        self.tempLabel.setText(f"Current Temperature: {temp}ºF")
        self.iconLabel.setPixmap(QPixmap.fromImage(qIm))

    def updateFiveDayWeather(self, five_day_weather_data):
        # 5 day forecast

        # 1

        weather = five_day_weather_data.json()['list'][0]['weather'][0]['description']
        temp = round(five_day_weather_data.json()['list'][0]['main']['temp'])
        windSpeed = round(five_day_weather_data.json()['list'][0]['wind']['speed'])
        pressure = round(five_day_weather_data.json()['list'][0]['main']['pressure'])
        humidity = five_day_weather_data.json()['list'][0]['main']['humidity']
        iconId = five_day_weather_data.json()['list'][0]['weather'][0]['icon']
        url = requests.get(f"http://openweathermap.org/img/wn/{iconId}@2x.png")
        in_memory_file = io.BytesIO(url.content)
        im = PIL.Image.open(in_memory_file)
        qIm = ImageQt(im)
        
        self.labelDayOne.setText(f"One")
        self.pressureDayOne.setText(f"{pressure} pascals")
        self.weatherDayOne.setText(f"{weather}")
        self.humidityDayOne.setText(f"{humidity}%")
        self.windDayOne.setText(f"{windSpeed} mph")
        self.tempDayOne.setText(f"{temp}ºF")
        self.iconDayOne.setPixmap(QPixmap.fromImage(qIm))
        # print(iconId)


        # 2
        
        weather = five_day_weather_data.json()['list'][1]['weather'][0]['description']
        temp = round(five_day_weather_data.json()['list'][1]['main']['temp'])
        windSpeed = round(five_day_weather_data.json()['list'][1]['wind']['speed'])
        pressure = round(five_day_weather_data.json()['list'][1]['main']['pressure'])
        humidity = five_day_weather_data.json()['list'][1]['main']['humidity']
        iconId = five_day_weather_data.json()['list'][1]['weather'][0]['icon']
        url = requests.get(f"http://openweathermap.org/img/wn/{iconId}@2x.png")
        in_memory_file = io.BytesIO(url.content)
        im = PIL.Image.open(in_memory_file)
        qIm = ImageQt(im)
        
        self.labelDayTwo.setText(f"Two")
        self.pressureDayTwo.setText(f"{pressure} pascals")
        self.weatherDayTwo.setText(f"{weather}")
        self.humidityDayTwo.setText(f"{humidity}%")
        self.windDayTwo.setText(f"{windSpeed} mph")
        self.tempDayTwo.setText(f"{temp}ºF")
        self.iconDayTwo.setPixmap(QPixmap.fromImage(qIm))


        # 3
        
        weather = five_day_weather_data.json()['list'][2]['weather'][0]['description']
        temp = round(five_day_weather_data.json()['list'][2]['main']['temp'])
        windSpeed = round(five_day_weather_data.json()['list'][2]['wind']['speed'])
        pressure = round(five_day_weather_data.json()['list'][2]['main']['pressure'])
        humidity = five_day_weather_data.json()['list'][2]['main']['humidity']
        iconId = five_day_weather_data.json()['list'][2]['weather'][0]['icon']
        url = requests.get(f"http://openweathermap.org/img/wn/{iconId}@2x.png")
        in_memory_file = io.BytesIO(url.content)
        im = PIL.Image.open(in_memory_file)
        qIm = ImageQt(im)
        
        self.labelDayThree.setText(f"Three")
        self.pressureDayThree.setText(f"{pressure} pascals")
        self.weatherDayThree.setText(f"{weather}")
        self.humidityDayThree.setText(f"{humidity}%")
        self.windDayThree.setText(f"{windSpeed} mph")
        self.tempDayThree.setText(f"{temp}ºF")
        # self.iconDayThree.setPixmap(QPixmap.fromImage(qIm))


        # 4
        
        weather = five_day_weather_data.json()['list'][3]['weather'][0]['description']
        temp = round(five_day_weather_data.json()['list'][3]['main']['temp'])
        windSpeed = round(five_day_weather_data.json()['list'][3]['wind']['speed'])
        pressure = round(five_day_weather_data.json()['list'][3]['main']['pressure'])
        humidity = five_day_weather_data.json()['list'][3]['main']['humidity']
        iconId = five_day_weather_data.json()['list'][3]['weather'][0]['icon']
        url = requests.get(f"http://openweathermap.org/img/wn/{iconId}@2x.png")
        in_memory_file = io.BytesIO(url.content)
        im = PIL.Image.open(in_memory_file)
        qIm = ImageQt(im)
        
        self.labelDayFour.setText(f"Four")
        self.pressureDayFour.setText(f"{pressure} pascals")
        self.weatherDayFour.setText(f"{weather}")
        self.humidityDayFour.setText(f"{humidity}%")
        self.windDayFour.setText(f"{windSpeed} mph")
        self.tempDayFour.setText(f"{temp}ºF")
        # self.iconDayFour.setPixmap(QPixmap.fromImage(qIm))


        # 5
        
        weather = five_day_weather_data.json()['list'][4]['weather'][0]['description']
        temp = round(five_day_weather_data.json()['list'][4]['main']['temp'])
        windSpeed = round(five_day_weather_data.json()['list'][4]['wind']['speed'])
        pressure = round(five_day_weather_data.json()['list'][4]['main']['pressure'])
        humidity = five_day_weather_data.json()['list'][4]['main']['humidity']
        iconId = five_day_weather_data.json()['list'][4]['weather'][0]['icon']
        url = requests.get(f"http://openweathermap.org/img/wn/{iconId}@2x.png")
        in_memory_file = io.BytesIO(url.content)
        im = PIL.Image.open(in_memory_file)
        qIm = ImageQt(im)
        
        self.labelDayFive.setText(f"Five")
        self.pressureDayFive.setText(f"{pressure} pascals")
        self.weatherDayFive.setText(f"{weather}")
        self.humidityDayFive.setText(f"{humidity}%")
        self.windDayFive.setText(f"{windSpeed} mph")
        self.tempDayFive.setText(f"{temp}ºF")
        # self.iconDayFive.setPixmap(QPixmap.fromImage(qIm))

    def getWeather(self, user_location):
        api_key = 'b6139f6046526366147abd5e0a2919ed'

        # user_location = "62703"

        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={user_location}&units=imperial&APPID={api_key}")


        if weather_data.json()['cod'] == '404':
            self.weatherDataUpddateLabel.setText(f"No city found")
            print("No City Found")
        else:
            lat = weather_data.json()['coord']['lat']
            lon = weather_data.json()['coord']['lon']
            five_day_weather_data = requests.get(
                f"https://api.openweathermap.org/data/2.5/forecast?&lat={lat}&lon={lon}&units=imperial&appid={api_key}")


            self.updateCurrentWeather(weather_data)
            self.updateFiveDayWeather(five_day_weather_data)
            

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    weatherAPP = QWidget()
    ui = Ui_weatherAPP()
    ui.setupUi(weatherAPP)
    weatherAPP.show()
    # weatherAPP().get_weather()
    sys.exit(app.exec_())