import PIL.Image
from PIL.ImageQt import ImageQt
import io
from tkinter import image_types
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QPushButton
import requests
import datetime
from PyQt5.QtWidgets import QMessageBox


    # Creating the Weather Application Object

class Ui_weatherAPP(object):

    # This is the API key we are using for
    # the openweathermap API 
    api_key = 'b6139f6046526366147abd5e0a2919ed'

    # Setting up UI with all the component placements
    # Version 1.0.0 - Current Weather Setup
    # These objects are located on the left side of the Window
    def setupUi(self, weatherAPP):

        # Setting up the Window bounds and background color
        if not weatherAPP.objectName():
            weatherAPP.setObjectName(u"weatherAPP")
        weatherAPP.resize(1080, 720)
        weatherAPP.setStyleSheet(u"")
        weatherAPP.setStyleSheet("background-color: rgb(104, 166, 242)")

        # App title UI object placement
        self.weatherAPPLabel = QLabel(weatherAPP)
        self.weatherAPPLabel.setObjectName(u"weatherAPPLabel")
        self.weatherAPPLabel.setGeometry(QRect(480, 20, 101, 51))
        font = QFont()
        font.setPointSize(14)
        self.weatherAPPLabel.setFont(font)

        # 5 Day Forecast Label - A part of Version 2.0.0
        self.fiveDayLabel = QLabel(weatherAPP)
        self.fiveDayLabel.setObjectName(u"fiveDayLabel")
        self.fiveDayLabel.setGeometry(QRect(675, 75, 150, 51))
        font = QFont()
        font.setPointSize(14)
        self.fiveDayLabel.setFont(font)

        # Current Forecast Label
        self.currentForecastLabel = QLabel(weatherAPP)
        self.currentForecastLabel.setObjectName(u"currentForecastLabel")
        self.currentForecastLabel.setGeometry(QRect(100, 75, 150, 51))
        font = QFont()
        font.setPointSize(14)
        self.currentForecastLabel.setFont(font)

        # current weather city search box UI object placement
        self.enterCityLineEdit = QLineEdit(weatherAPP)
        self.enterCityLineEdit.setObjectName(u"enterCityLineEdit")
        self.enterCityLineEdit.setGeometry(QRect(545, 20, 171, 41))
        self.enterCityLineEdit.setMaxLength(85)
        self.enterCityLabel = QLabel(weatherAPP)
        self.enterCityLabel.setObjectName(u"enterCityLabel")
        self.enterCityLabel.setGeometry(QRect(350, 20, 181, 41))
        font1 = QFont()
        font1.setPointSize(12)
        self.enterCityLabel.setFont(font1)
        self.enterCityLineEdit.setFont(font1)


        # current weather icon UI object placement
        self.iconLabel = QLabel(weatherAPP)
        self.iconLabel.setGeometry(QRect(65, 450, 211, 211))
        self.iconLabel.setText("")
        self.iconLabel.setScaledContents(True)
        self.iconLabel.setObjectName("iconLabel")

        # "Get Weather" button UI object placement
        self.submitBtn = QPushButton(weatherAPP, clicked = lambda : self.locationCheck(self.enterCityLineEdit.text()))
        self.submitBtn.setObjectName(u"submitBtn")
        self.submitBtn.setGeometry(QRect(460, 620, 141, 51))

        # current location UI object placement
        self.cityLabel = QLabel(weatherAPP)
        self.cityLabel.setObjectName(u"cityLabel")
        self.cityLabel.setGeometry(QRect(115, 150, 321, 51))
        self.cityLabel.setFont(font1)

        # current weather status UI object placement
        self.weatherDataUpddateLabel = QLabel(weatherAPP)
        self.weatherDataUpddateLabel.setObjectName(u"weatherDataUpddateLabel")
        self.weatherDataUpddateLabel.setGeometry(QRect(115, 200, 401, 51))
        self.weatherDataUpddateLabel.setFont(font1)
        self.weatherDataUpddateLabel.setStyleSheet(u"")

        # current temperature UI object placement
        self.tempLabel = QLabel(weatherAPP)
        self.tempLabel.setObjectName(u"tempLabel")
        self.tempLabel.setGeometry(QRect(115, 250, 321, 51))
        self.tempLabel.setFont(font1)

        # current wind speed UI object placement
        self.windLabel = QLabel(weatherAPP)
        self.windLabel.setObjectName(u"windLabel")
        self.windLabel.setGeometry(QRect(115, 300, 311, 51))
        self.windLabel.setFont(font1)

        # current pressure UI object placement
        self.pressureLabel = QLabel(weatherAPP)
        self.pressureLabel.setObjectName(u"pressureLabel")
        self.pressureLabel.setGeometry(QRect(115, 350, 311, 51))
        self.pressureLabel.setFont(font1)

        # current humidity UI object placement
        self.humidityLabel = QLabel(weatherAPP)
        self.humidityLabel.setObjectName(u"humidityLabel")
        self.humidityLabel.setGeometry(QRect(115, 400, 311, 51))
        self.humidityLabel.setFont(font1)

        # vertical line separator UI object placement
        self.line = QFrame(weatherAPP)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(420, 100, 20, 511))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        # horizontal line separator UI object placement
        self.line_2 = QFrame(weatherAPP)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(500, 240, 531, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        

        # function for five day forecast UI setup
        self.setupFiveDayUI()

        #Update the interface with components
        self.retranslateUi(weatherAPP)

        QMetaObject.connectSlotsByName(weatherAPP)
    # setupUi


    # Setting up the 5 Day Forecast Component Locations
    # The layout of this code is based off the current
    # weather components (Placement is the only difference)

    #These objects are located on the right side of the Window

    # This is for Version 2.0.0 - 5 Day Forecast Implementation
    def setupFiveDayUI(self):
        
        font2 = QFont()
        font2.setPointSize(8)

        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        
        # Start of Day 1 Components

        self.iconDayOne = QLabel(weatherAPP)
        self.iconDayOne.setGeometry(QRect(480, 150, 75, 75))
        self.iconDayOne.setText("")
        self.iconDayOne.setScaledContents(True)
        self.iconDayOne.setObjectName("iconDayOne")
        
        # Day 1 Label
        self.labelDayOne = QLabel(weatherAPP)
        self.labelDayOne.setObjectName(u"labelDayOne")
        self.labelDayOne.setGeometry(QRect(430, 330, 171, 41))
        self.labelDayOne.setFont(font3)
        self.labelDayOne.setAlignment(Qt.AlignCenter)
        self.labelDayOne.setStyleSheet(u"")

        # Day 1 Weather Description 
        self.weatherDayOne = QLabel(weatherAPP)
        self.weatherDayOne.setObjectName(u"weatherDayOne")
        self.weatherDayOne.setGeometry(QRect(430, 370, 171, 41))
        self.weatherDayOne.setFont(font2)
        self.weatherDayOne.setAlignment(Qt.AlignCenter)
        self.weatherDayOne.setStyleSheet(u"")

        # Day 1 Temperature
        self.tempDayOne = QLabel(weatherAPP)
        self.tempDayOne.setObjectName(u"tempDayOne")
        self.tempDayOne.setGeometry(QRect(430, 410, 171, 41))
        self.tempDayOne.setFont(font2)
        self.tempDayOne.setAlignment(Qt.AlignCenter)

        # Day 1 Wind Speed
        self.windDayOne = QLabel(weatherAPP)
        self.windDayOne.setObjectName(u"windDayOne")
        self.windDayOne.setGeometry(QRect(430, 450, 171, 41))
        self.windDayOne.setFont(font2)
        self.windDayOne.setAlignment(Qt.AlignCenter)

        # Day 1 Pressure 
        self.pressureDayOne = QLabel(weatherAPP)
        self.pressureDayOne.setObjectName(u"pressureDayOne")
        self.pressureDayOne.setGeometry(QRect(430, 490, 171, 41))
        self.pressureDayOne.setFont(font2)
        self.pressureDayOne.setAlignment(Qt.AlignCenter)

        # Day 1 Humidity
        self.humidityDayOne = QLabel(weatherAPP)
        self.humidityDayOne.setObjectName(u"humidityDayOne")
        self.humidityDayOne.setGeometry(QRect(430, 540, 171, 41))
        self.humidityDayOne.setFont(font2)
        self.humidityDayOne.setAlignment(Qt.AlignCenter)

        # Start of Day 2 Components

        self.iconDayTwo = QLabel(weatherAPP)
        self.iconDayTwo.setGeometry(QRect(600, 150, 75, 75))
        self.iconDayTwo.setText("")
        self.iconDayTwo.setScaledContents(True)
        self.iconDayTwo.setObjectName("iconDayTwo")
        
        # Day 2 Label
        self.labelDayTwo = QLabel(weatherAPP)
        self.labelDayTwo.setObjectName(u"labelDayTwo")
        self.labelDayTwo.setGeometry(QRect(560, 330, 171, 41))
        self.labelDayTwo.setFont(font3)
        self.labelDayTwo.setAlignment(Qt.AlignCenter)
        self.labelDayTwo.setStyleSheet(u"")

        # Day 2 Weather Description 
        self.weatherDayTwo = QLabel(weatherAPP)
        self.weatherDayTwo.setObjectName(u"weatherDayTwo")
        self.weatherDayTwo.setGeometry(QRect(560, 370, 171, 41))
        self.weatherDayTwo.setFont(font2)
        self.weatherDayTwo.setAlignment(Qt.AlignCenter)
        self.weatherDayTwo.setStyleSheet(u"")

        # Day 2 Temperature
        self.tempDayTwo = QLabel(weatherAPP)
        self.tempDayTwo.setObjectName(u"tempDayTwo")
        self.tempDayTwo.setGeometry(QRect(560, 410, 171, 41))
        self.tempDayTwo.setAlignment(Qt.AlignCenter)
        self.tempDayTwo.setFont(font2)

        # Day 2 Wind Speed
        self.windDayTwo = QLabel(weatherAPP)
        self.windDayTwo.setObjectName(u"windDayTwo")
        self.windDayTwo.setGeometry(QRect(560, 450, 171, 41))
        self.windDayTwo.setAlignment(Qt.AlignCenter)
        self.windDayTwo.setFont(font2)

        # Day 2 Pressure
        self.pressureDayTwo = QLabel(weatherAPP)
        self.pressureDayTwo.setObjectName(u"pressureDayTwo")
        self.pressureDayTwo.setGeometry(QRect(560, 490, 171, 41))
        self.pressureDayTwo.setAlignment(Qt.AlignCenter)
        self.pressureDayTwo.setFont(font2)

        # Day 2 Humidity
        self.humidityDayTwo = QLabel(weatherAPP)
        self.humidityDayTwo.setObjectName(u"humidityDayTwo")
        self.humidityDayTwo.setGeometry(QRect(560, 540, 171, 41))
        self.humidityDayTwo.setAlignment(Qt.AlignCenter)
        self.humidityDayTwo.setFont(font2)

        # Start of Day 3 Components

        self.iconDayThree = QLabel(weatherAPP)
        self.iconDayThree.setGeometry(QRect(725, 150, 75, 75))
        self.iconDayThree.setText("")
        self.iconDayThree.setScaledContents(True)
        self.iconDayThree.setObjectName("iconDayThree")
        
        # Day 3 Label
        self.labelDayThree = QLabel(weatherAPP)
        self.labelDayThree.setObjectName(u"labelDayThree")
        self.labelDayThree.setGeometry(QRect(685, 330, 171, 41))
        self.labelDayThree.setFont(font3)
        self.labelDayThree.setAlignment(Qt.AlignCenter)
        self.labelDayThree.setStyleSheet(u"")

        # Day 3 Weather Description 
        self.weatherDayThree = QLabel(weatherAPP)
        self.weatherDayThree.setObjectName(u"weatherDayThree")
        self.weatherDayThree.setGeometry(QRect(685, 370, 171, 41))
        self.weatherDayThree.setFont(font2)
        self.weatherDayThree.setAlignment(Qt.AlignCenter)
        self.weatherDayThree.setStyleSheet(u"")

        # Day 3 Temperature
        self.tempDayThree = QLabel(weatherAPP)
        self.tempDayThree.setObjectName(u"tempDayThree")
        self.tempDayThree.setGeometry(QRect(685, 410, 171, 41))
        self.tempDayThree.setFont(font2)
        self.tempDayThree.setAlignment(Qt.AlignCenter)

        # Day 3 Wind Speed
        self.windDayThree = QLabel(weatherAPP)
        self.windDayThree.setObjectName(u"windDayThree")
        self.windDayThree.setGeometry(QRect(685, 450, 171, 41))
        self.windDayThree.setFont(font2)
        self.windDayThree.setAlignment(Qt.AlignCenter)

        # Day 3 Pressure
        self.pressureDayThree = QLabel(weatherAPP)
        self.pressureDayThree.setObjectName(u"pressureDayThree")
        self.pressureDayThree.setGeometry(QRect(685, 490, 171, 41))
        self.pressureDayThree.setFont(font2)
        self.pressureDayThree.setAlignment(Qt.AlignCenter)

        # Day 3 Humidity
        self.humidityDayThree = QLabel(weatherAPP)
        self.humidityDayThree.setObjectName(u"humidityDayThree")
        self.humidityDayThree.setGeometry(QRect(685, 540, 171, 41))
        self.humidityDayThree.setFont(font2)
        self.humidityDayThree.setAlignment(Qt.AlignCenter)

        # Start of Day 4 Components

        self.iconDayFour = QLabel(weatherAPP)
        self.iconDayFour.setGeometry(QRect(845, 150, 75, 75))
        self.iconDayFour.setText("")
        self.iconDayFour.setScaledContents(True)
        self.iconDayFour.setObjectName("iconDayFour")
        
        # Day 4 Label
        self.labelDayFour = QLabel(weatherAPP)
        self.labelDayFour.setObjectName(u"labelDayFour")
        self.labelDayFour.setGeometry(QRect(810, 330, 171, 41))
        self.labelDayFour.setFont(font3)
        self.labelDayFour.setAlignment(Qt.AlignCenter)
        self.labelDayFour.setStyleSheet(u"")

        # Day 4 Weather Description 
        self.weatherDayFour = QLabel(weatherAPP)
        self.weatherDayFour.setObjectName(u"weatherDayFour")
        self.weatherDayFour.setGeometry(QRect(810, 370, 171, 41))
        self.weatherDayFour.setFont(font2)
        self.weatherDayFour.setAlignment(Qt.AlignCenter)
        self.weatherDayFour.setStyleSheet(u"")

        # Day 4 Temperature
        self.tempDayFour = QLabel(weatherAPP)
        self.tempDayFour.setObjectName(u"tempDayFour")
        self.tempDayFour.setGeometry(QRect(810, 410, 171, 41))
        self.tempDayFour.setFont(font2)
        self.tempDayFour.setAlignment(Qt.AlignCenter)

        # Day 4 Wind Speed
        self.windDayFour = QLabel(weatherAPP)
        self.windDayFour.setObjectName(u"windDayFour")
        self.windDayFour.setGeometry(QRect(810, 450, 171, 41))
        self.windDayFour.setFont(font2)
        self.windDayFour.setAlignment(Qt.AlignCenter)

        # Day 4 Pressure
        self.pressureDayFour = QLabel(weatherAPP)
        self.pressureDayFour.setObjectName(u"pressureDayFour")
        self.pressureDayFour.setGeometry(QRect(810, 490, 171, 41))
        self.pressureDayFour.setFont(font2)
        self.pressureDayFour.setAlignment(Qt.AlignCenter)

        # Day 4 Humidity
        self.humidityDayFour = QLabel(weatherAPP)
        self.humidityDayFour.setObjectName(u"humidityDayFour")
        self.humidityDayFour.setGeometry(QRect(810, 540, 171, 41))
        self.humidityDayFour.setFont(font2)
        self.humidityDayFour.setAlignment(Qt.AlignCenter)

        # Start of Day 5 Components

        self.iconDayFive = QLabel(weatherAPP)
        self.iconDayFive.setGeometry(QRect(950, 150, 75, 75))
        self.iconDayFive.setText("")
        self.iconDayFive.setScaledContents(True)
        self.iconDayFive.setObjectName("iconDayFive")
        
        # Day 5 Label
        self.labelDayFive = QLabel(weatherAPP)
        self.labelDayFive.setObjectName(u"labelDayFive")
        self.labelDayFive.setGeometry(QRect(920, 330, 171, 41))
        self.labelDayFive.setFont(font3)
        self.labelDayFive.setAlignment(Qt.AlignCenter)
        self.labelDayFive.setStyleSheet(u"")

        # Day 5 Weather Description 
        self.weatherDayFive = QLabel(weatherAPP)
        self.weatherDayFive.setObjectName(u"weatherDayFive")
        self.weatherDayFive.setGeometry(QRect(920, 370, 171, 41))
        self.weatherDayFive.setFont(font2)
        self.weatherDayFive.setAlignment(Qt.AlignCenter)
        self.weatherDayFive.setStyleSheet(u"")

        # Day 5 Temperature
        self.tempDayFive = QLabel(weatherAPP)
        self.tempDayFive.setObjectName(u"tempDayFive")
        self.tempDayFive.setGeometry(QRect(920, 410, 171, 41))
        self.tempDayFive.setFont(font2)
        self.tempDayFive.setAlignment(Qt.AlignCenter)

        # Day 5 Wind Speed
        self.windDayFive = QLabel(weatherAPP)
        self.windDayFive.setObjectName(u"windDayFive")
        self.windDayFive.setGeometry(QRect(920, 450, 171, 41))
        self.windDayFive.setFont(font2)
        self.windDayFive.setAlignment(Qt.AlignCenter)

        # Day 5 Pressure
        self.pressureDayFive = QLabel(weatherAPP)
        self.pressureDayFive.setObjectName(u"pressureDayFive")
        self.pressureDayFive.setGeometry(QRect(920, 490, 171, 41))
        self.pressureDayFive.setFont(font2)
        self.pressureDayFive.setAlignment(Qt.AlignCenter)

        # Day 5 Humidity
        self.humidityDayFive = QLabel(weatherAPP)
        self.humidityDayFive.setObjectName(u"humidityDayFive")
        self.humidityDayFive.setGeometry(QRect(920, 540, 171, 41))
        self.humidityDayFive.setFont(font2)
        self.humidityDayFive.setAlignment(Qt.AlignCenter)

    # Retain the information of the window object itself and the constants as we update the information
    # to the user specified location

    # Version 1.0.0 with fiveDayLabel added for Version 2.0.0
    def retranslateUi(self, weatherAPP):
        weatherAPP.setWindowTitle(QCoreApplication.translate("weatherAPP", u"Weather Application", None))
        self.currentForecastLabel.setText(QCoreApplication.translate("weatherAPP", u"Current Weather", None))
        self.fiveDayLabel.setText(QCoreApplication.translate("weatherAPP", u"5 Day Forecast", None))
        self.enterCityLabel.setText(QCoreApplication.translate("weatherAPP", u"Search City or Zip Code:", None))
        self.submitBtn.setText(QCoreApplication.translate("weatherAPP", u"Get Forecast", None))
        self.locationCheck(f"{self.getLocation()['city']}, {self.getLocation()['region']}")

        
    # retranslateUi

    # Get the users location based upon their IP as default data when the user
    # Opens the application

    def getLocation(self):
        # get current user external IP by making request to server that returns IP
        ip = requests.get('https://api64.ipify.org?format=json').json()['ip']

        # get IP location from server that queries IP location database
        location_response = requests.get(f'https://ipapi.co/{ip}/json').json()

        # store location data in dict for easy reference
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

    # A method to update interface with the current weather as the user enters in new locations - Version 1.0.0

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
        
        self.cityLabel.setText(f"{city}")
        self.pressureLabel.setText(f"{pressure} pascals")
        self.weatherDataUpddateLabel.setText(f"{weather}")
        self.humidityLabel.setText(f"{humidity}%")
        self.windLabel.setText(f"{windSpeed} mph")
        self.tempLabel.setText(f"{temp}ºF")
        self.iconLabel.setPixmap(QPixmap.fromImage(qIm))


    # A method to update interface with the 5 day forecast as the user enters in new locations - Version 2.0.0

    def updateFiveDayWeather(self, five_day_weather_data):
        # 5 day forecast - V 2.0.0

        format = "%Y-%m-%d %H:%M:%S"

        # Day 1 of the 5 Day Forecast
        timeData = datetime.datetime.strptime(five_day_weather_data.json()['list'][5]['dt_txt'], format).strftime('%m-%d')
        weather = five_day_weather_data.json()['list'][5]['weather'][0]['description']
        temp = round(five_day_weather_data.json()['list'][5]['main']['temp'])
        windSpeed = round(five_day_weather_data.json()['list'][5]['wind']['speed'])
        pressure = round(five_day_weather_data.json()['list'][5]['main']['pressure'])
        humidity = five_day_weather_data.json()['list'][5]['main']['humidity']
        iconId = five_day_weather_data.json()['list'][5]['weather'][0]['icon']
        url = requests.get(f"http://openweathermap.org/img/wn/{iconId}@2x.png")
        in_memory_file = io.BytesIO(url.content)
        im = PIL.Image.open(in_memory_file)
        qIm = ImageQt(im)

        
        # Setting the text with the proper data
        self.labelDayOne.setText(f"{timeData}")
        self.pressureDayOne.setText(f"{pressure} pascals")
        self.weatherDayOne.setText(f"{weather}")
        self.humidityDayOne.setText(f"{humidity}%")
        self.windDayOne.setText(f"{windSpeed} mph")
        self.tempDayOne.setText(f"{temp}ºF")
        self.iconDayOne.setPixmap(QPixmap.fromImage(qIm))

        # Day 2 of the 5 Day Forecast
        timeData = datetime.datetime.strptime(five_day_weather_data.json()['list'][13]['dt_txt'], format).strftime('%m-%d')
        weather = five_day_weather_data.json()['list'][13]['weather'][0]['description']
        temp = round(five_day_weather_data.json()['list'][13]['main']['temp'])
        windSpeed = round(five_day_weather_data.json()['list'][13]['wind']['speed'])
        pressure = round(five_day_weather_data.json()['list'][13]['main']['pressure'])
        humidity = five_day_weather_data.json()['list'][13]['main']['humidity']
        iconId = five_day_weather_data.json()['list'][13]['weather'][0]['icon']
        url = requests.get(f"http://openweathermap.org/img/wn/{iconId}@2x.png")
        in_memory_file = io.BytesIO(url.content)
        im = PIL.Image.open(in_memory_file)
        qIm = ImageQt(im)
        
        # Setting the text with the proper data
        self.labelDayTwo.setText(f"{timeData}")
        self.pressureDayTwo.setText(f"{pressure} pascals")
        self.weatherDayTwo.setText(f"{weather}")
        self.humidityDayTwo.setText(f"{humidity}%")
        self.windDayTwo.setText(f"{windSpeed} mph")
        self.tempDayTwo.setText(f"{temp}ºF")
        self.iconDayTwo.setPixmap(QPixmap.fromImage(qIm))

        # Day 3 of the 5 Day Forecast
        timeData = datetime.datetime.strptime(five_day_weather_data.json()['list'][21]['dt_txt'], format).strftime('%m-%d')
        weather = five_day_weather_data.json()['list'][21]['weather'][0]['description']
        temp = round(five_day_weather_data.json()['list'][21]['main']['temp'])
        windSpeed = round(five_day_weather_data.json()['list'][21]['wind']['speed'])
        pressure = round(five_day_weather_data.json()['list'][21]['main']['pressure'])
        humidity = five_day_weather_data.json()['list'][21]['main']['humidity']
        iconId = five_day_weather_data.json()['list'][21]['weather'][0]['icon']
        url = requests.get(f"http://openweathermap.org/img/wn/{iconId}@2x.png")
        in_memory_file = io.BytesIO(url.content)
        im = PIL.Image.open(in_memory_file)
        qIm = ImageQt(im)
        
        # Setting the text with the proper data
        self.labelDayThree.setText(f"{timeData}")
        self.pressureDayThree.setText(f"{pressure} pascals")
        self.weatherDayThree.setText(f"{weather}")
        self.humidityDayThree.setText(f"{humidity}%")
        self.windDayThree.setText(f"{windSpeed} mph")
        self.tempDayThree.setText(f"{temp}ºF")
        self.iconDayThree.setPixmap(QPixmap.fromImage(qIm))

        # Day 4 of the 5 Day Forecast
        timeData = datetime.datetime.strptime(five_day_weather_data.json()['list'][29]['dt_txt'], format).strftime('%m-%d')
        weather = five_day_weather_data.json()['list'][29]['weather'][0]['description']
        temp = round(five_day_weather_data.json()['list'][29]['main']['temp'])
        windSpeed = round(five_day_weather_data.json()['list'][29]['wind']['speed'])
        pressure = round(five_day_weather_data.json()['list'][29]['main']['pressure'])
        humidity = five_day_weather_data.json()['list'][29]['main']['humidity']
        iconId = five_day_weather_data.json()['list'][29]['weather'][0]['icon']
        url = requests.get(f"http://openweathermap.org/img/wn/{iconId}@2x.png")
        in_memory_file = io.BytesIO(url.content)
        im = PIL.Image.open(in_memory_file)
        qIm = ImageQt(im)
        
        # Setting the text with the proper data
        self.labelDayFour.setText(f"{timeData}")
        self.pressureDayFour.setText(f"{pressure} pascals")
        self.weatherDayFour.setText(f"{weather}")
        self.humidityDayFour.setText(f"{humidity}%")
        self.windDayFour.setText(f"{windSpeed} mph")
        self.tempDayFour.setText(f"{temp}ºF")
        self.iconDayFour.setPixmap(QPixmap.fromImage(qIm))

        # Day 5 of the 5 Day Forecast
        timeData = datetime.datetime.strptime(five_day_weather_data.json()['list'][37]['dt_txt'], format).strftime('%m-%d')
        weather = five_day_weather_data.json()['list'][37]['weather'][0]['description']
        temp = round(five_day_weather_data.json()['list'][37]['main']['temp'])
        windSpeed = round(five_day_weather_data.json()['list'][37]['wind']['speed'])
        pressure = round(five_day_weather_data.json()['list'][37]['main']['pressure'])
        humidity = five_day_weather_data.json()['list'][37]['main']['humidity']
        iconId = five_day_weather_data.json()['list'][37]['weather'][0]['icon']
        url = requests.get(f"http://openweathermap.org/img/wn/{iconId}@2x.png")
        in_memory_file = io.BytesIO(url.content)
        im = PIL.Image.open(in_memory_file)
        qIm = ImageQt(im)
        
        # Setting the text with the proper data
        self.labelDayFive.setText(f"{timeData}")
        self.pressureDayFive.setText(f"{pressure} pascals")
        self.weatherDayFive.setText(f"{weather}")
        self.humidityDayFive.setText(f"{humidity}%")
        self.windDayFive.setText(f"{windSpeed} mph")
        self.tempDayFive.setText(f"{temp}ºF")
        self.iconDayFive.setPixmap(QPixmap.fromImage(qIm))

        

    # Checking whether the location the user has entered is Valid or Not - Version 1.5.0
    # Added additional checks during Version 2.0.0 development
    
    def locationCheck(self, user_location):
        weather_data = {}

        

        #if the user location stores a number it will return an error
        #This is accounting for if the user location is a zip code - which would not return an error
        if user_location.isnumeric():
            weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_location}&units=imperial&APPID={self.api_key}")
        else:    
            for character in user_location:
                if character.isdigit():
                    msg = QMessageBox()
                    msg.setStyleSheet("QLabel{min-width: 300px;}")
                    msg.setText("No City Found")
                    msg.setInformativeText('Please Enter a Valid Location')
                    msg.setWindowTitle("Error")
                    x = msg.exec_()
                    return


        #if the user locations does not store any information it will return an error
        if user_location != "":
            weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={user_location}&units=imperial&APPID={self.api_key}")
        else:
            msg = QMessageBox()
            msg.setStyleSheet("QLabel{min-width: 300px;}")
            msg.setText("No City Found")
            msg.setInformativeText('Please Enter a Valid Location')
            msg.setWindowTitle("Error")
            x = msg.exec_()
            return


        if weather_data.json()['cod'] == '404':
            # return an error of "No city found" if input is not understood, real city or just a 404 error
            

            msg = QMessageBox()
            msg.setStyleSheet("QLabel{min-width: 300px;}")
            msg.setText("No City Found")
            msg.setInformativeText('Please Enter a Valid Location')
            msg.setWindowTitle("Error")
            x = msg.exec_()
        else:
            self.getWeather(weather_data)

    def getWeather(self, weather_data):
        # get lat and lon coordinates for five day forecast query
        lat = weather_data.json()['coord']['lat']
        lon = weather_data.json()['coord']['lon']

        # get five day forecast JSON and store in variable
        five_day_weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/forecast?&lat={lat}&lon={lon}&units=imperial&cnt=50&appid={self.api_key}")

        # call function used to update UI with current weather data
        self.updateCurrentWeather(weather_data)

        # call function used to update UI with five day weather forecast
        self.updateFiveDayWeather(five_day_weather_data)
            

# Driver code for initializing and running the application
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    weatherAPP = QWidget()
    ui = Ui_weatherAPP()
    ui.setupUi(weatherAPP)
    weatherAPP.show()
    sys.exit(app.exec_())
