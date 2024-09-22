from django.shortcuts import render
from .models import Food, Restaurant
from rest_framework.response import Response
from .serializer import FoodSerializer, RestaurantSerializer
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

# add food


@api_view(['POST'])
def addFoodREST(request):
    foodSerializer = FoodSerializer(data=request.data)
    if foodSerializer.is_valid():
        foodSerializer.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

# featch all food


@api_view(['GET'])
def allFoodREST(request):
    foodSerializer = FoodSerializer(Food.objects.all(), many=True).data
    return Response(foodSerializer)

# search food by id


@api_view(['POST'])
def foodById(request):
    foodSerializer = FoodSerializer(Food.objects.filter(
        id=request.data.get('fid')), many=True).data
    return Response(foodSerializer)

# delete food


@api_view(['POST'])
def deleteFoodREST(request):
    fId = request.data.get('fid')  # Get 'fid' from the POST request body
    if fId:
        try:
            food = Food.objects.get(id=fId)
            food.delete()  # Delete the food object
            return Response({"message": "Food item deleted successfully"}, status=status.HTTP_200_OK)
        except Food.DoesNotExist:
            return Response({"error": "Food item not found"}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"error": "No food id provided"}, status=status.HTTP_400_BAD_REQUEST)

# upadte a food


@api_view(['POST'])
def updateFoodREST(request):
    fId = request.data.get('id')
    if fId:
        try:
            food = Food.objects.get(id=fId)
            if request.data.get('fName'):
                food.fName = request.data.get('fName')
            if request.data.get('fPrice'):
                food.fPrice = request.data.get('fPrice')
            food.save()
            return Response({"message": "Food item updated successfully"}, status=status.HTTP_200_OK)
        except Food.DoesNotExist:
            return Response({"error": "Food item not found"}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"error": "No food id provided"}, status=status.HTTP_400_BAD_REQUEST)

##################################################################


@api_view(['POST'])
def addRestaurantREST(request):
    rantSerializer = RestaurantSerializer(data=request.data)
    if rantSerializer.is_valid():
        rantSerializer.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def updateRestaurantREST(request):
    rId = request.data.get('id')
    if rId:
        try:
            restaurant = Restaurant.objects.get(id=rId)
            restaurant.rName = request.data.get('rName')
            restaurant.rLocation = request.data.get('rLocation')
            restaurant.save()
            return Response({"message": "restaurant updated successfully"}, status=status.HTTP_200_OK)

        except Restaurant.DoesNotExist:
            return Response({"error": "restaurant item not found"}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"error": "No restaurant id provided"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def allRestaurantREST(request):
    rantSerializer = RestaurantSerializer(
        Restaurant.objects.all(), many=True).data
    return Response(rantSerializer)


@api_view(['POST'])
def deleteRestaurantREST(request):
    rId = request.data.get('id')
    if rId:
        try:
            obj = Restaurant.objects.filter(id=rId)
            obj.delete()
            return Response({"message": "Restaurant deleted successfully"}, status=status.HTTP_200_OK)
        except Food.DoesNotExist:
            return Response({"error": "Restaurant not found"}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"error": "No Restaurant id provided"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def RestaurantByLoactionREST(request):
    location = request.data.get("location")
    if location:
        try:
            obj = RestaurantSerializer(Restaurant.objects.filter(
                rLocation=location), many=True).data
            return Response(obj)
        except Food.DoesNotExist:
            return Response({"error": "Restaurant not found"}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"error": "No Restaurant loaction provided"}, status=status.HTTP_400_BAD_REQUEST)
