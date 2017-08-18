from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from web_app.models import web_app_data
from django.forms import ModelForm

# Create your views here.
#modelでは編集するデータベースを指定，fieldsでは投稿画面で編集する内容を記載します．
class webform(ModelForm):
    class Meta:
        model = web_app_data
        fields = ('title', 'text', 'date', )

def edit(request):
    web_apps = web_app_data()
    form = None
    if request.method == 'POST':
        form = webform(request.POST, instance=web_apps)
        if form.is_valid():
            web_app = form.save(commit=False)
            web_app.save()
            return redirect('web_app:show')
        pass
    else:
        form = webform(instance=web_apps)
    return render(request, 'web_app/edit.html', {'form': form})
 

def show(request):
    web_apps = web_app_data.objects.all()
    return render(request, 'web_app/show.html', {'web_apps': web_apps})

