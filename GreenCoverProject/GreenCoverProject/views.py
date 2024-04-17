from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
    return render(request, "home.html")

def result(request):
    model = joblib.load('finalized_model.sav')
    list = []
    list.append(float(request.GET['feature1']))
    list.append(float(request.GET['feature2']))

    print("List:", list)#prints in the cmd prompt
    ans = model.predict([list])
    return render(request, "result.html", {'ans': ans})
