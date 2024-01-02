from django.shortcuts import render
import requests

# Create your views here.
def all(request):
    records = {}
    url = "https://inshorts.deta.dev/news?category=all"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['alldata'] = inshorts_data
    return render(request,'index.html',records)

def sports(request):
    records = {}
    url1 = "https://inshorts.deta.dev/news?category=sports"
    response = requests.get(url=url1)
    sports_data = response.json()
    records['sportsdata'] = sports_data
    return render(request,'sports.html',records)

def fashion(request):
    records = {}
    url2 = "https://inshorts.deta.dev/news?category=fashion"
    response = requests.get(url=url2)
    fashion_data = response.json()
    records['fashiondata'] = fashion_data
    return render(request,'fashion.html',records)

def entertainment(request):
    records = {}
    url3 = "https://inshorts.deta.dev/news?category=entertainment"
    response = requests.get(url=url3)
    entertainment_data = response.json()
    records['entertainmentdata'] = entertainment_data
    return render(request,'entertainment.html',records)

def technology(request):
    records = {}
    url4 = "https://inshorts.deta.dev/news?category=technology"
    response = requests.get(url=url4)
    technology_data = response.json()
    records['technologydata'] = technology_data
    return render(request,'technology.html',records)