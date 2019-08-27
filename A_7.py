def tempMeasurements():
    total_temperature = 0
    count_temperature = 0
    temp_error = True
    wind_error = True 
    humidity_error = True 

    tempStr = input("Enter temperature: ")
    while tempStr !="":
        temp_error = False
        temp = int(tempStr) 
        total_temperature = total_temperature + temp
        count_temperature = count_temperature + 1
        average_temperature = int(total_temperature/count_temperature)
        tempStr = input("Enter temperature: ")
            
    wind_speed = int(input("Enter wind speed: "))
    total_windSpeed = 0
    while wind_speed != -1:
        wind_error = False
        total_windSpeed = [wind_speed]
        windSpeed_max = total_windSpeed[0]
                
        for i in total_windSpeed:
            if i > windSpeed_max:
                windSpeed_max = i        
        wind_speed = int(input("Enter wind speed: "))        
    
    humidity = int(input("Enter humidity: "))
    while humidity >=0 and humidity <= 100:
        humidity_error = False
        current_humidity = humidity
        humidity = int(input("Enter humidity: "))        
   
    if temp_error == True and wind_error == False and humidity_error == False:
        print("Average temperature: No info on temperature")
        print("Maximum wind speed: ", windSpeed_max)
        print("Current humidity: ", current_humidity)
        
    elif temp_error == True and wind_error == True and humidity_error == False:
        print("Average temperature: No info on Temperature")
        print("Maximum wind speed: No info on wind speed")
        print("Current humidity: ",current_humidity)
    
    elif temp_error == False and wind_error == False and humidity_error == True:
        print("Average temperature: ",average_temperature )
        print("Maximum wind speed: ",windSpeed_max)
        print("Current humidity: No info on current humidity")
    
    elif temp_error == False and wind_error == True and humidity_error == True:
        print("Average temperature: ",average_temperature)
        print("Maximum wind speed: No info on wind speed")
        print("Current humidity: No info on current humidity")
    
    elif temp_error == True and wind_error == False and humidity_error == True:
        print("Average temperature: No info on Temperature")
        print("Maximum wind speed: ",windSpeed_max)
        print("Current humidity: No info on current humidity")
    
    elif temp_error == True and wind_error == True and humidity_error == False:
        print("Average temperature: No info on Temperature")
        print("Maximum wind speed: No info on wind speed")
        print("Current humidity: ",current_humidity)
        
    elif temp_error == False and wind_error == True and humidity_error == False:
        print("Average temperature: ", average_temperature)
        print("Maximum wind speed: No info on weed speed")
        print("Current humidity: ", current_humidity)      
   
    elif temp_error == True and wind_error == True and humidity_error == True:
        print("Average temperature: No info on Temperature")
        print("Maximum wind speed: No info on wind speed")
        print("Current humidity: No info on current humidity") 

    else:
        print("Average temperature: ",average_temperature)
        print("Maximum wind speed: ",windSpeed_max)
        print("Current humidity: ",current_humidity)
tempMeasurements()
    
