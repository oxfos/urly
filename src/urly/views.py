from django.shortcuts import render, redirect
from .forms import ShortcodeForm


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
            if entry.shortcode == '':
                entry.shortcode = 'plchol'
            entry.save()
    return redirect('urly:homepage')
