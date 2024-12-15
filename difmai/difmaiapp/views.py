from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    
    data=request.POST.get('inputData')
    #return HttpResponse("Hello World !")
    print(data)
    return render(request,'index.html',{"generatedData": data })