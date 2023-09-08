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