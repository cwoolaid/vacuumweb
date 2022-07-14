from django.shortcuts import render
from .models import Type, Brand, Model, InventoryNumber, Country
from django.views.generic import ListView, DetailView



# Create your views here.

def index(request):
    types = Type.objects.all()

    context = {
       'types': types
    }

    return render(request, 'index.html', context)


class AllModelList(ListView):
    model = Model


class CordlessModelList(ListView):
    # model = Model
    context_object_name = 'cordless_model_list'
    # context_object_name = 'cordless_list'
    queryset = Model.objects.filter(type__name='Cordless')
    template_name = 'vacuums/model_list_cordless.html'


class RobotModelList(ListView):
    # model = Model
    context_object_name = 'robot_model_list'
    # context_object_name = 'robot_list'
    queryset = Model.objects.filter(type__name='Robot')
    template_name = 'vacuums/model_list_robot.html'


class CordlessDetailView(DetailView):
    # model = Model
    queryset = Model.objects.filter(type__name='Cordless')

    # model_detail.html is used since not declared with a 'template_name'

class RobotDetailView(DetailView):
    # model = Model
    queryset = Model.objects.filter(type__name='Robot')

    # model_detail.html is used since not declared with a 'template_name'

