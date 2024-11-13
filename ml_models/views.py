from django.shortcuts import render
from django.http import HttpResponse
import joblib
import numpy as np

classification_model = joblib.load("ml_models/classification_model.joblib")


# Create your views here.
def say_hello(request):
    return render(request, "hello.html", {"name": "Anish"})


def classification_function(request):
    if request.method == "POST":
        seplen = float(request.POST.get("seplen"))
        sepwid = float(request.POST.get("sepwid"))
        petlen = float(request.POST.get("petlen"))
        petwid = float(request.POST.get("petwid"))

        input_data = np.array([[seplen, sepwid, petlen, petwid]])

        output = classification_model.predict(input_data)
        output = str(output[0])

        result_dict = {"1": "setosa", "2": "versicolor", "3": "virginica"}
        result = result_dict[output]

        result = {"output": f"The result is {result}"}

        return render(request, "iris.html", result)
    return render(request, "iris.html")


def regression_function(request):
    if request.method == "Post":
        return HttpResponse("Will implement later")
    return HttpResponse("Hello")
