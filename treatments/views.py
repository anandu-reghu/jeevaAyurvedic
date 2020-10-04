from django.shortcuts import render

# Create your views here.
def treatments(request):
    return render(request, 'treatments/treatments.html')