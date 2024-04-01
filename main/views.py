from django.shortcuts import redirect, render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .forms import MainPageForm
from .models import MAinPageModel


@method_decorator([csrf_exempt], name='dispatch')
class Main_page(View):
    def get(self, request):
        form = MainPageForm()
        text = MAinPageModel.objects.last()
        return render(request, 'main/main_page.html', context={'form':form, 'text':text})


    def post(self, request):
        form = MainPageForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            db = MAinPageModel.objects.create(text=text)
            db.save()
            return redirect('main-page')

        form.add_error('text', 'مشکلی پیش امد')