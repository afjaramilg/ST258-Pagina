from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from requests.auth import HTTPBasicAuth
import requests


from .models import Competitions, Teams, Players
HEADER = {'X-Auth-Token':'3e3e086673834f068c800b65e45aff94'}

def index_controller(request):
    context = {'info':'Veamos si esto fuciona index_controller'}
    return render(request, 'football/index.html', context)

def get_competitions_controller(request):
    url='http://api.football-data.org/v2/competitions'
    response = requests.get(url=url, headers=HEADER)
    json_info = response.json()
    for competition in json_info['competitions']:
        Competitions.save_competition(name=competition['name'],
                          code=competition['code'],
                          area_name=competition['area']['name'])
    context = {'info':json_info}
    return render(request, 'football/competitions.html', context)

def get_teams_controller(request):
    url='http://api.football-data.org/v2/teams'
    response = requests.get(url=url, headers=HEADER)
    json_info = response.json()
    for team in json_info['teams']:
        # .objects.create
        #darle directamente a rest
        #django extensions
        Teams.objects.create(name=team['name'], 
                   tla=team['tla'],
                   shortName=team['shortName'], 
                   areaName=team['area']['name'], 
                   email=team['email'])
    context = {'info': json_info['teams']}
    return render(request, 'football/teams.html', context)

    
def get_player_controller(request):
    url='http://api.football-data.org/v2/players/100'
    response = requests.get(url=url, headers=HEADER)
    json_info = response.json()
    context = {'info': json_info}
    return render(request, 'football/teams.html', context)


def get_league_controller(request, id):
    """This is the first method in obtaining the data
       first it searches if the information is already
       in the database, if it isn't it obtains it from 
       the api"""
    json_info = obtain_league(id)
    context = {'info': json_info}
    return render(request, 'football/league.html', context)

def obtain_league(id):
    """Method for obtaining the league"""

    url= f"http://api.football-data.org/v2/teams/{id}"
    response = requests.get(url=url, headers=HEADER)
    json_info = response.json()
    competition = json_info['activeCompetitions'][0] 
    try:
        Competitions.objects.create(
            name=competition['name'],
            code=competition['code'],
            area_name=competition['area']['name']
        )
    except: 
        pass
    obtain_team(json_info, league=competition['name'])

def obtain_team(info = None, league=None):
    """method for obtaining the team"""
    #mi idea con la variable league era que si llega la liga significa
    #que se quiere guardar la informacion
    #en caso contrario es que se quiere consultar la informacion guardada
    #esa fue mi idea en el momento, por ahora voy a dejar eso asi
    try: 
        Teams.objects.create(
        name=info['name'],
        tla=info['tla'],
        shortName=info['shortName'],
        areaName=info['area']['name'],
        email=info['email'],
        competition=Competitions.objects.filter(name__contains=league)[0]
        )
    except:
        pass
    obtain_squad(info=info['squad'],team=info['name'])

def obtain_squad(info = None, team=None):
    """Method for obtaining the squad"""
    for player in info:
        try:
            Players.objects.create(
            name=player['name'],
            position=player['position'],
            dateOfBirth=player['dateOfBirth'],
            countryOfBirth=player['countryOfBirth'],
            nationality=player['nationality'],
            team=Teams.objects.filter(name__contains=team)[0]
        )
        except:
            pass

def count_players_controller(request, code):
    #se que en laravel existe una ayuda ya del framework que puede hacer
    #consultas a tablas foraneas de golpe(eloquent), sin necesidad de haccer
    #tantas consultas como estoy haciendo
    #¿en django hay alguna forma?
    league = Competitions.objects.filter(code__contains=code)[0]
    teams = Teams.objects.filter(competition=league)
    player_count = 0
    for squad in teams:
        player_count += Players.objects.filter(team=squad).count()
    context = {'info': player_count}
    return render(request, 'football/count_players.html', context)
