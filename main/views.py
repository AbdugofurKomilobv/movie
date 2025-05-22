from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,template_name='index.html')


def toqmi_juftmi(son):
    if son % 2 == 0:
        return "Juft"
    else:
        return "Toq"

def sozlar_soni(matn):
    return len(matn.split())

