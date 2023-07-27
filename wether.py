import requests 
apikey = "70a06932143958adce988c465faf6cbb"
userinput = input("city:-")
# print(userinput)
wetherdata = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={userinput}&appid={apikey}")

# print(wetherdata.status_code)

# print(wetherdata.json())
if wetherdata.json()['cod'] == '404':
    print("city is not available")
else:
    weather = wetherdata.json()['weather'][0]['main']
    temp = round(wetherdata.json()['main']['temp'])

    print(f"the weather in {userinput} is: {weather}")
    print(f"the temprature in {userinput} is: {(temp-32)/9}°C")
