# -*- coding: utf-8 -*-
"""
Created on Fri May  8 13:04:14 2020

@author: Chana Sandberg
"""
#add try statements and wrong data message
import requests
from requests.exceptions import HTTPError


class Weather(object):
        
    def getWeatherZip(self):
        
        try:
            zipCode = int(input("Please enter zipcode:\n")) #receives zipcode input
            request = requests.get('http://api.openweathermap.org/data/2.5/weather?zip={zipcode}&appid=4025c7eaa97ecf4da1a7924a6720b966'.format(zipcode = zipCode)) #connects to weather website
            request.raise_for_status()# If the response was successful, no Exception will be raised
            response = request.json() #gets readable format
            data = response["main"] 
            current_temperature = (data["temp"] - 273.15)* 9/5 + 32 #calculates specifically the temperature
            print("The current weather in {zipcode} is {temp}\n".format(zipcode = zipCode, temp = current_temperature)) #prints weather
        
        except HTTPError: #if input invalid, notifies user
            print('Invalid zipcode. Try again.') 
        
        except Exception as err: #if no connection to server or other error, notifies user
            print('Other error occurred: {err}'.format(err = err))  
        
        
    def getWeatherCity(self):
        
        try:
            city = input("Please enter city:\n") #receives city input
            request = requests.get('http://api.openweathermap.org/data/2.5/weather?q={cityname}&appid=4025c7eaa97ecf4da1a7924a6720b966'.format(cityname = city)) #connects to weather website
            request.raise_for_status()# If the response was successful, no Exception will be raised
            response = request.json() #gets readable format
            data = response["main"]
            current_temperature = (data["temp"] - 273.15)* 9/5 + 32 #calculates specifically the temperature
            print("The current weather in {city} is {temp}\n".format(city = city, temp = current_temperature)) #prints weather
        
        except HTTPError: #if input invalid, notifies user
            print('Invalid city. Try again.') 
        
        except Exception as err: #if no connection to server or other error, notifies user
            print('Other error occurred: {err}'.format(err = err))  
    
if __name__ == '__main__': #calls weather function
    while(True):
        myWeather = Weather()
        typeLocation = input("Do you want to enter a city or zipcode?\n") #user decides if they are entering a city or zipcode
        if typeLocation == "city":
            myWeather.getWeatherCity() #calls city function because input was city
        if typeLocation == "zipcode":
            myWeather.getWeatherZip() #calls zipcode function because input was zipcode
        counter = input("stop or continue:\n") # allows user to continue program or stop
        if counter == "stop":
            break
        if counter == "continue":
            False
        
