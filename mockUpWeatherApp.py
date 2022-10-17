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

        self.submitBtn = QPushButton(weatherAPP, clicked = lambda : self.getWeather())
        # self.submitBtn = QPushButton(weatherAPP)
        self.submitBtn.setObjectName(u"submitBtn")
        self.submitBtn.setGeometry(QRect(570, 620, 141, 51))

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

        self.fiveDayForecast = QPushButton(weatherAPP)
        self.fiveDayForecast.setObjectName(u"fiveDayForecast")
        self.fiveDayForecast.setGeometry(QRect(390, 620, 141, 51))

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
        self.iconDayTwo.setGeometry(QRect(580, 80, 211, 211))
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

        # # 3

        # self.icon = QLabel(weatherAPP)
        # self.icon.setGeometry(QRect(450, 100, 211, 211))
        # self.icon.setText("")
        # self.icon.setScaledContents(True)
        # self.icon.setObjectName("icon")
        
        # self.labelDay = QLabel(weatherAPP)
        # self.labelDay.setObjectName(u"labelDay")
        # self.labelDay.setGeometry(QRect(550, 330, 171, 41))
        # self.labelDay.setFont(font3)
        # self.labelDay.setAlignment(Qt.AlignCenter)
        # self.labelDay.setStyleSheet(u"")

        # self.weatherDay = QLabel(weatherAPP)
        # self.weatherDay.setObjectName(u"weatherDay")
        # self.weatherDay.setGeometry(QRect(550, 370, 171, 41))
        # self.weatherDay.setFont(font2)
        # self.weatherDay.setAlignment(Qt.AlignCenter)
        # self.weatherDay.setStyleSheet(u"")

        # self.tempDay = QLabel(weatherAPP)
        # self.tempDay.setObjectName(u"tempDay")
        # self.tempDay.setGeometry(QRect(550, 410, 171, 41))
        # self.tempDay.setFont(font2)
        # self.tempDay.setAlignment(Qt.AlignCenter)

        # self.windDay = QLabel(weatherAPP)
        # self.windDay.setObjectName(u"windDay")
        # self.windDay.setGeometry(QRect(550, 450, 171, 41))
        # self.windDay.setFont(font2)
        # self.windDay.setAlignment(Qt.AlignCenter)

        # self.pressureDay = QLabel(weatherAPP)
        # self.pressureDay.setObjectName(u"pressureDay")
        # self.pressureDay.setGeometry(QRect(550, 490, 171, 41))
        # self.pressureDay.setFont(font2)
        # self.pressureDay.setAlignment(Qt.AlignCenter)

        # self.humidityDay = QLabel(weatherAPP)
        # self.humidityDay.setObjectName(u"humidityDay")
        # self.humidityDay.setGeometry(QRect(550, 540, 171, 41))
        # self.humidityDay.setFont(font2)
        # self.humidityDay.setAlignment(Qt.AlignCenter)

        


        self.retranslateUi(weatherAPP)

        QMetaObject.connectSlotsByName(weatherAPP)
    # setupUi

    def retranslateUi(self, weatherAPP):
        weatherAPP.setWindowTitle(QCoreApplication.translate("weatherAPP", u"weatherAPP", None))
        self.weatherAPPLabel.setText(QCoreApplication.translate("weatherAPP", u"Weather", None))
        self.enterCityLabel.setText(QCoreApplication.translate("weatherAPP", u"Search City or Zip Code:", None))
        self.submitBtn.setText(QCoreApplication.translate("weatherAPP", u"Current Forecast", None))
        # self.weatherDataUpddateLabel.setText("")
        # self.tempLabel.setText("")
        # self.windLabel.setText("")
        # self.pressureLabel.setText("")
        # self.humidityLabel.setText("")
        self.fiveDayForecast.setText(QCoreApplication.translate("weatherAPP", u"5-Day Forecast", None))
        self.getWeather()
    # retranslateUi

    def updateWeather(self, weather_data):
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
        self.iconLabel.setPixmap(QPixmap.fromImage(qIm))

    def getWeather(self):
        api_key = 'b6139f6046526366147abd5e0a2919ed'

        # user_input = self.enterCityLineEdit.text()
        user_input = "62703"

        # geocoding = requests.get(
            # f"http://api.openweathermap.org/geo/1.0/direct?q={user_input}&limit=5&appid={api_key}")

        # five_day_weather_data = requests.get(
        #     f"https://api.openweathermap.org/data/2.5/forecast?q={user_input}&appid={api_key}")
            # &units=metric&cnt=5

        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

        

        

        if weather_data.json()['cod'] == '404':
            self.weatherDataUpddateLabel.setText(f"No city found")
            print("No City Found")
        else:

            lat = weather_data.json()['coord']['lat']
            lon = weather_data.json()['coord']['lon']
            five_day_weather_data = requests.get(
                f"https://api.openweathermap.org/data/2.5/forecast?&lat={lat}&lon={lon}&appid={api_key}")
            

            # for item in five_day_weather_data.json()['list'][0]:
            #     print(item)
            #     print(five_day_weather_data.json()['list'][0][item])


            # self.updateWeather(weather_data)

            
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

            print(iconId)


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
            print(iconId)


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


            # # 3
            
            # weather = five_day_weather_data.json()['list'][1]['weather'][0]['description']
            # temp = round(five_day_weather_data.json()['list'][1]['main']['temp'])
            # windSpeed = round(five_day_weather_data.json()['list'][1]['wind']['speed'])
            # pressure = round(five_day_weather_data.json()['list'][1]['main']['pressure'])
            # humidity = five_day_weather_data.json()['list'][1]['main']['humidity']
            # iconId = five_day_weather_data.json()['list'][1]['weather'][1]['icon']
            # url = requests.get(f"http://openweathermap.org/img/wn/{iconId}@2x.png")
            # in_memory_file = io.BytesIO(url.content)
            # im = PIL.Image.open(in_memory_file)
            # qIm = ImageQt(im)
            
            # self.labelDay.setText(f"One")
            # self.pressureDay.setText(f"{pressure} pascals")
            # self.weatherDay.setText(f"{weather}")
            # self.humidityDay.setText(f"{humidity}%")
            # self.windDay.setText(f"{windSpeed} mph")
            # self.tempDay.setText(f"{temp}ºF")
            # # self.iconDay.setPixmap(QPixmap.fromImage(qIm))


            # # 4
            
            # weather = five_day_weather_data.json()['list'][1]['weather'][0]['description']
            # temp = round(five_day_weather_data.json()['list'][1]['main']['temp'])
            # windSpeed = round(five_day_weather_data.json()['list'][1]['wind']['speed'])
            # pressure = round(five_day_weather_data.json()['list'][1]['main']['pressure'])
            # humidity = five_day_weather_data.json()['list'][1]['main']['humidity']
            # iconId = five_day_weather_data.json()['list'][1]['weather'][1]['icon']
            # url = requests.get(f"http://openweathermap.org/img/wn/{iconId}@2x.png")
            # in_memory_file = io.BytesIO(url.content)
            # im = PIL.Image.open(in_memory_file)
            # qIm = ImageQt(im)
            
            # self.labelDay.setText(f"One")
            # self.pressureDay.setText(f"{pressure} pascals")
            # self.weatherDay.setText(f"{weather}")
            # self.humidityDay.setText(f"{humidity}%")
            # self.windDay.setText(f"{windSpeed} mph")
            # self.tempDay.setText(f"{temp}ºF")
            # # self.iconDay.setPixmap(QPixmap.fromImage(qIm))


            # # 5
            
            # weather = five_day_weather_data.json()['list'][1]['weather'][0]['description']
            # temp = round(five_day_weather_data.json()['list'][1]['main']['temp'])
            # windSpeed = round(five_day_weather_data.json()['list'][1]['wind']['speed'])
            # pressure = round(five_day_weather_data.json()['list'][1]['main']['pressure'])
            # humidity = five_day_weather_data.json()['list'][1]['main']['humidity']
            # iconId = five_day_weather_data.json()['list'][1]['weather'][1]['icon']
            # url = requests.get(f"http://openweathermap.org/img/wn/{iconId}@2x.png")
            # in_memory_file = io.BytesIO(url.content)
            # im = PIL.Image.open(in_memory_file)
            # qIm = ImageQt(im)
            
            # self.labelDay.setText(f"One")
            # self.pressureDay.setText(f"{pressure} pascals")
            # self.weatherDay.setText(f"{weather}")
            # self.humidityDay.setText(f"{humidity}%")
            # self.windDay.setText(f"{windSpeed} mph")
            # self.tempDay.setText(f"{temp}ºF")
            # # self.iconDay.setPixmap(QPixmap.fromImage(qIm))


            

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    weatherAPP = QWidget()
    ui = Ui_weatherAPP()
    ui.setupUi(weatherAPP)
    weatherAPP.show()
    # weatherAPP().get_weather()
    sys.exit(app.exec_())