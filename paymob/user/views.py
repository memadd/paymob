import json

from fuzzywuzzy import fuzz

from django.shortcuts import render

# Opening JSON file
f = open('user/data.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Closing file
f.close()

def home(requset):
    context = {'listings':data}
    return render(requset, 'user/list.html', context )

def result(request):
    results = []
    key = request.GET['keys']
    for d in data:
        ratio = fuzz.ratio(key.lower(),d["Key"].lower())
        if ratio > 50:
            d['percentage'] = ratio
            results.append(d)   
    context = {'results': results}
    return render(request, 'user/result.html', context)