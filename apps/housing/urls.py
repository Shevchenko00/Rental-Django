from django.urls import path
from .views.housing_views import HousingCreateAPI, HouseChangeActiveAPI, HousingGetAPI
from .views.search_views import HousingSearchByKeywordAPI, HousingSearchByCityAPI, HousingSearchByPriceAPI, \
    HousingSearchByTypeAPI, HousingSearchByStreetAPI, HousingSearchByCountRoomAPI

urlpatterns = [
    path('', HousingGetAPI.as_view(), name='active_hotels'),#Предаставление всех отелей (GET)
    path('get_hotel/<int:pk>/',  HousingGetAPI.as_view(), name='get_hotel'),# Получение отеля по id(GET)
    path('create_housing/', HousingCreateAPI.as_view(), name='create_hotel'),# Создание отеля черезе метод POST
    path('update_housing/<int:pk>/', HousingGetAPI.as_view(), name='update_hotel'),# Эндпойнт для обновления какой-либо записи по ПК(PUT)
    path('delete_housing/<int:pk>/', HousingGetAPI.as_view(), name='views_delete_hotel'), # Эндпоинт для удаления какой-либо записи по ПК(DELETE)
    path('change_active/<int:pk>/', HouseChangeActiveAPI.as_view(), name='change-active-housing'),# Эндпоитн для изменения статуса is_active {"is_active":"False" or "True"}
    path('search_by_keyword/', HousingSearchByKeywordAPI.as_view(), name='search-hotels'), #{localhost}/housing/search_by_keyword/q='Значение'
    path('search_by_city/',HousingSearchByCityAPI.as_view(), name='search-hotels' ), #{localhost}/housing/search_by_city/?q='Город'
    path('search_by_price/', HousingSearchByPriceAPI.as_view(), name='search-hotels'),#{localhost}/housing/search_by_price/?min_price={min цена}&max_price={max цена}
    path('search_by_type/', HousingSearchByTypeAPI.as_view(), name='search-hotels'),#{localhost}/housing/search_by_type/?q=ПЕРВЫЙ АРГУМЕНТ, ВТОРОЙ
    path('search_by_street/', HousingSearchByStreetAPI.as_view(), name='search-hotels'),#{localhost}/housing/search_by_street/?q=НАЗВАНИЕ УЛИЦЫ
    path('search_by_room/', HousingSearchByCountRoomAPI.as_view(), name='search-hotels'),#{localhost}/housing/search_by_room/?min_room=ЧИСЛО&max_room=ЧИСЛО
]

