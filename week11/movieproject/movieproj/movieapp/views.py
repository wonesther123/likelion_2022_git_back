from django.shortcuts import render
import requests
import json
from .forms import SearchForm

# Create your views here.

my_id = 'd2c162b4bed7b12771ce4db117b07775'

def home(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        searchword = request.POST.get('search')
        if form.is_valid():
            url = 'https://api.themoviedb.org/3/search/movie?api_key='+my_id+'&query='+searchword
            response = requests.get(url)
            resdata = response.text
            obj = json.loads(resdata)
            obj = obj['results']
            return render(request, 'search.html', {'obj':obj})
        # https://api.themoviedb.org/3/search/movie?api_key=d2c162b4bed7b12771ce4db117b07775&query=hello&page=1
        # 위 형태의 url로 get 요청 보내기
    else:
        form = SearchForm()
        url = 'https://api.themoviedb.org/3/trending/movie/week?api_key='+my_id
        response = requests.get(url)
        resdata = response.text
        obj = json.loads(resdata)
        obj = obj['results']

    return render(request, 'index.html', {'obj':obj, 'form':form})

def detail(request, movie_id):
    
    # https://api.themoviedb.org/3/movie/300?api_key=d2c162b4bed7b12771ce4db117b07775&language=en-US
    # 이 url에 get 요청 보내기

    url = 'https://api.themoviedb.org/3/movie/'+movie_id+'?api_key='+my_id
    response = requests.get(url)
    resdata = response.text

    return render(request, 'detail.html', {'resdata':resdata})