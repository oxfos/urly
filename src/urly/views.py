from django.shortcuts import render


def homepage(request):
    """View for / url, i.e. homepage.""" 

    return render(request, 'urly/index.html')