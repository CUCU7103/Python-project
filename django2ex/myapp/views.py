from django.shortcuts import render

def showFunc(request):
    return render(request,"main.html")

def selectFunc(request):
    name = request.GET.get("name")
    return render(request,"select.html",{'결과':name})



# Create your views here.
