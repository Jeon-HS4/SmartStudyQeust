from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect


urlpatterns = [
    path('admin/', admin.site.urls),
    #re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
    path('', include('quiz_app.urls')),
    re_path(r'^(?!admin|static|api).*$', lambda request: HttpResponseRedirect('http://localhost:3000/')),

]
