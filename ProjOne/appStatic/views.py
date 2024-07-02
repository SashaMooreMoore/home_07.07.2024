from django.shortcuts import render
from django.views import View


class PageStatic(View):
    def get(self, request):
        return render(request, 'appStatic/home/index.html')
    
class PageHelp(View):
    def get(self, request):
        return render(request, 'appStatic/help/index.html')
    
class PageContacts(View):
    def get(self, request):
        return render(request, 'appStatic/contacts/index.html')
    
class PageCat(View):
    def get(self, request):
        return render(request, 'appStatic/cats/index.html') 