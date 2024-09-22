from django.urls import path
from fr_app import views


urlpatterns = [
    path('add_food_REST', views.addFoodREST, name='addFoodREST'),
    path('all_food_REST', views.allFoodREST, name='allFoodREST'),
    path('food_by_id_REST', views.foodById, name='foodById'),
    path('delete_food', views.deleteFoodREST, name='deleteFoodREST'),
    path('update_food', views.updateFoodREST, name='updateFoodREST'),

    path('add_restaurant_REST', views.addRestaurantREST, name='addRestaurantREST'),
    path('update_restaurant_REST', views.updateRestaurantREST,
         name='updateRestaurantREST'),
    path('all_restaurant_REST', views.allRestaurantREST, name='allRestaurantREST'),
    path('delete_restaurant_REST', views.deleteRestaurantREST,
         name='deleteRestaurantREST'),
    path('restaurant_by_location_REST', views.RestaurantByLoactionREST,
         name='RestaurantByLoactionREST'),
]
