from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView
from django.http import HttpResponse, JsonResponse
from base_app.models import School, Student
from django.core.serializers import serialize
from django.urls import reverse

# Create your views here.
class IndexView(View):

    def get(self, request):
        return HttpResponse("This is a Class Based View")


class IndexTemplateView(TemplateView):

    template_name = 'base_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "Class Based View"
        return context


class SchoolListView(ListView):

    model = School
    template_name = 'base_app/schools.html'
    context_object_name = 'schools'


class SchoolDetailsView(DetailView):

    model = School
    template_name = 'base_app/school_detail.html'
    context_object_name = 'school'


class SchoolCreateView(CreateView):

    model = School
    fields = "__all__"
    template_name ='base_app/new_school.html'

    # def get_success_url(self) -> str:
    #     url = reverse('base_app:school', kwargs={'pk': self.object.pk})
    #     return url

def school(request):
    data = Student.objects.all()
    data = serialize('json', data)
    return JsonResponse(data, safe=False)