from django.shortcuts import render

# Create your views here.


def about(request):
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    return render(request, 'rules.html')
