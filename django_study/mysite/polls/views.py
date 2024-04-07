from django.shortcuts import render
from django.http import HttpResponse
from . import db_config
from .db_config import my_client,accounts
import sys
# sys.path.append('/path/to/scarping')
# from .scarping import main
# from main import startScraping 


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def sayHello(request):
    name='Thang shelby'
    return render(request,'hello.html',{'name':name})
def sayBye(request):
    return HttpResponse("Good bye See you again")

def form(request):
    key = request.GET['senderId ']
    print(db_config.accounts)
    return HttpResponse(db_config.accounts)
# def scraping(request):
#     userName = request.GET['userName']
#     print(accounts)
#     main.startScraping(userName)
#     return HttpResponse('Success!')


# def scraping(request):
#     # link= request.POST['link']
#     link='https://www.instagram.com/cristiano/'
#     print(link)
#     startScraping()
#     return render(request,'hello.html',{'name':link})


