from django.shortcuts import render

# Create your views here.
def v_help(request):
    return render(request,'help.html')