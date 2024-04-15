from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,View,CreateView
from django.contrib import messages
from my_work.models import GarbageBin,CollectionRequest,Area
from my_work.models import *
from driver.forms import RquestForm
# Create your views here.


class HomePage(TemplateView):
    template_name="driver/home.html"


# class CollectionRequestView (View):
#     def get(self,request,*args,**kwargs):
#         form=RquestForm()
#         return render(request,"driver/col_request.html",{"form":form})
    
#     def post(self,request,*args,**kwargs):
#         form=RquestForm(request.POST)
#         if form.is_valid():
#             CollectionRequest.objects.create(**form.cleaned_data)


class CollectionRequestView(CreateView):
    template_name='driver/col_request.html'
    form_class= RquestForm
    model=CollectionRequest
    success_url=reverse_lazy('home_3')
    areas = Area.objects.all()
    bin = GarbageBin.objects

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)






