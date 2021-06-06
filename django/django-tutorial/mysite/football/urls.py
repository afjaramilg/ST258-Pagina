from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_controller, name='index'),
    path('/get/teams', views.get_teams_controller, name='get_teams'),
    path('/get/players',views.get_player_controller,name='get_player'),
    path('/get/league/<int:id>', views.get_league_controller, name='get_league'),
    path('/count/players/<code>', views.count_players_controller, name='count_players')
]