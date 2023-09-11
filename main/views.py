from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Nabil Nazir Ahmad',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)