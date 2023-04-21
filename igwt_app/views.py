from django.shortcuts import render

# Create your views here.
def igwt_view(request):
    return render(request, 'igwt.html')