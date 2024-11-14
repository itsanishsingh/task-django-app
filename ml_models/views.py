from django.shortcuts import render
from django.http import HttpResponse
import joblib
import numpy as np

classification_model = joblib.load("ml_models/classification_model.joblib")
regression_model = joblib.load("ml_models/regression_model.joblib")


# Create your views here.
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
    if request.method == "POST":
        hours = float(request.POST.get("hours"))
        prev_score = float(request.POST.get("prev_score"))

        input_data = np.array([[hours, prev_score]])

        output = regression_model.predict(input_data)
        result = str(output[0])

        result = {"output": f"The score would be {result}"}

        return render(request, "score.html", result)

    return render(request, "score.html")
