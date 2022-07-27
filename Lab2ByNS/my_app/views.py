from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from datetime import date
import random
# Create your views here.

today = [
    {"date" : "Today is 2022-06-06 !" }
]

@api_view(['GET'])
def today (request : Request):

    response_data = {
        "date" : f"today is {date.today()}"
    }
    return Response(response_data)


@api_view (['POST'])
def random_number (request : Request):

    min_number = request.data["min"]
    max_number = request.data["max"]

    if min_number < 0:
        res_data = {"msg" : "not allowed, please provide a min that is bigger than 0"}
        return Response(res_data)

    my_random_number = random.randint(min_number, max_number)
    res_data = {"random" : my_random_number}
    return Response(res_data)
