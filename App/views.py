from urllib import response
from django.shortcuts import render
# Create your views here.
from django.http import JsonResponse
from .models import PersonCount


def get_person_count(request):
    male_count= PersonCount.objects.filter(gender='male').count()
    Female_count= PersonCount.objects.filter(gender='female').count()
    print(male_count)


    response_data={
        'Male':male_count,
        'Female':Female_count
    }

    return JsonResponse(response_data)


