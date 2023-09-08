from django.http import JsonResponse
from http import HTTPStatus
from drinks.models import Drink
from drinks.serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET','POST'])
def drink_list(request):
    if request.method=='GET':
        drinks=Drink.objects.all()
        serializer=DrinkSerializer(drinks, many=True)
        return JsonResponse({'drinks':serializer.data})
    
    if request.method=='POST':
        serializer =  DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status= HTTPStatus.CREATED)

@api_view(['GET','PUT','DELETE'])
def drink_detail(request,id):
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=HTTPStatus.NOT_FOUND)

    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data, status=HTTPStatus.OK)

    elif request.method == 'PUT':
        serializer=DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTPStatus.CREATED)
        return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)
    if request.method == 'DELETE':
        pass