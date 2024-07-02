import requests
from django.http import JsonResponse
from django.views.decorators.http import require_GET
import public_ip as ip 
from django.views import View
import ipinfo 

IPINFO_API_KEY = '31c074dd9afc62'
OPENWEATHERMAP_API_KEY = 'f1b7c27195ed4a9c3aca54f8208dd55d'
handler = ipinfo.getHandler(IPINFO_API_KEY)

class Helloapi(View):
    def get(self,request):
        client_ip = ip.get() #while on local machine 
        # client_ip = request.META-get (HTTP_X_REAL_TP') #Use this to get the ip when hosting on pythonanywhere
        visitor_name = request.GET.get('visitor_name', 'Visitor').strip('()').strip('"')
        # # Get IP info
        client_location = handler.getDetails(client_ip)
        city = client_location.city 
        
        # # Get weather info
        weather_info = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={OPENWEATHERMAP_API_KEY}")
        weather_data = weather_info.json() 
        temp = weather_data["main"]["temp"]

        response_data = {
            "client_ip": client_ip,
            "location": city,
            "greeting": f"Hello, {visitor_name}!, the temperature is {temp} degrees Celsius in {city}"
        }
        
        return JsonResponse(response_data)