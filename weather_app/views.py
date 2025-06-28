# Create your views here.
from django.shortcuts import render, HttpResponse
from django.contrib import messages
import requests
import datetime
def home(request):

    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'indore'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=afa92eed932b19fec0e19fcacb7bea01'
    PARAMS = {'units': 'metric'}

    API_KEY = 'AIzaSyD0E5uqcPU91PDdnPOGSkSbQWxrgL6HLxw'
    SEARCH_ENGINE_ID = ('c6c44fe04e162431e')

    query = city + "1920x1080"
    page = 1
    start  = (page-1) * 10 + 1
    searchType = 'image'
    city_url = f'https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&searchType={searchType}&start={start}'
    data = requests.get(city_url).json()
    count =  1
    search_items = data.get("items")
    image_url = search_items[1]['link']

    try:

        data = requests.get(url, params=PARAMS).json()

        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']

        day =  datetime.date.today()


        return render(request, 'weather_app/index.html', {'description': description, 'icon': icon, 'temp': temp, 'day':day, 'city':city, 'exception_occured' : False, 'image_url': image_url})
    except:
        images_urls = 'https://www.google.com/search?q=funny+weather&oq=funny+weather&aqs=chrome..69i57j69i60l3j69i61.3234j1j4&sourceid=chrome&ie=UTF-8'
        exception_occured = True
        messages.errors(request, 'entered data is not availabale to API')
        day = datetime.date.today()
        return render(request, 'weather_app/index.html',
                {'description': 'clear sky', 'icon': 'Old', 'temp': temp, 'day': day, 'city': 'indore', 'exception_occured': True})