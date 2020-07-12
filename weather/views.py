from django.shortcuts import render 
import requests 
import json 
  

def get_weather(location):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=efa4cf0fbf485183c28e614762c1c1e2'.format(location)
    r = requests.get(url)
    return r.json()


def index(request): 
    if request.method == 'POST': 
        city = request.POST['city']
        
        list_of_data = get_weather(city)
        
        if list_of_data["cod"]==200:
            data = { 
                "city": str(city)+",    "+str(list_of_data['sys']['country']), 
                "temperature": "{:.2f}".format((list_of_data['main']['temp'])-273.15) , 
                'description' : str(list_of_data['weather'][0]['description']), 
                'icon' : list_of_data['weather'][0]['icon'],
            }
        else:
            data={"flag":"notFound"}
        return render(request, "weather.html",data)        
    else:
        return render(request, "weather.html")