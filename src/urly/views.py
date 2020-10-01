from django.shortcuts import render, redirect
from .forms import ShortcodeForm
from .utils import get_unique_shortcode
from .models import Shortcode


def homepage(request):
    """View for / url, i.e. homepage.""" 
    form = ShortcodeForm()
    return render(request, 'urly/index.html', {'form':form})


def shorten(request):
    """View to shorten url."""
    if request.method == 'POST':
        form = ShortcodeForm(data=request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            if form.cleaned_data['shortcode'] == '':
                entry.shortcode = get_unique_shortcode(6)
            entry.save()
    return redirect('urly:homepage')
