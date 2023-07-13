from django.shortcuts import render
from django.shortcuts import redirect
from .forms import MyModelForm
from .models import MyModel


def home(request):
    uylar = MyModel.objects.filter(tur='uy')
    domlar = MyModel.objects.filter(tur='dom')
    kvartiralar = MyModel.objects.filter(tur='kvartira')
    beznizlar = MyModel.objects.filter(tur='bezniz')
    context = {'uylar': uylar,'domlar': domlar,'kvartiralar': kvartiralar,'beznizlar': beznizlar}
    return render(request, 'index.html', context)


def add_home(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = MyModelForm()
    return render(request, 'add.html', {'form': form})

