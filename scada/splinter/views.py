import datetime
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse, HttpResponse, StreamingHttpResponse
from django.conf import settings
from splinter import utils, models


def control_mode(request):
        
    return render(
                    request,
                    "splinter/control_mode.html",
                    {
                    }
    )


def data_table(request):
        
    return render(
                    request,
                    "splinter/data_table.html",
                    {
                    }
    )

def graph(request):
        
    return render(
                    request,
                    "splinter/graph.html",
                    {
                    }
    )