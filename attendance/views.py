from django.shortcuts import render
from django.views import View

class IndexView(View):
    template_name = "attendance/index.html"
    def get(self, request):
        return render(request, "attendance/index.html")

