from django.http import HttpResponse
from django.shortcuts import render
import joblib

def index(request):
    #return HttpResponse("This is Home")
    return render(request,"index.html")


def result(request):
    #return render(request, "result.html")
    cls = joblib.load('final_model.sav')

    lis = []
    lis.append(request.GET['RI'])
    lis.append(request.GET['Na'])
    lis.append(request.GET['Mg'])
    lis.append(request.GET['Al'])
    lis.append(request.GET['Si'])
    lis.append(request.GET['K'])
    lis.append(request.GET['Ca'])
    lis.append(request.GET['Ba'])
    lis.append(request.GET['Fe'])

    #print(lis)

    ans = cls.predict([lis])

    return render(request,"result.html",{'ans':ans,'lis':lis})
