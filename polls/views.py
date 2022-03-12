from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import pickle
# Create your views here.

from .forms import my_form


def index(request):

    return render(request, 'polls/index.html')


def result(request):
    lis = []

    file = pickle.load(open('model_pickel.pkl', 'rb'))

    lis.append(request.GET.get('name'))
    lis.append(request.GET.get('email'))
    lis.append(request.GET.get('phone'))

    results = list(map(int, lis))
    print(results)

    ans = file.predict([lis])

    return render(request, 'polls/result.html', {'ans': ans})
