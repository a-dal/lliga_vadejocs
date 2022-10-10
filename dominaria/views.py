from django.shortcuts import render
from django.db.models import Q
from operator import attrgetter
from .models import Matchup
from .models import Player
# Create your views here.
def games(request):
    context = {
        'matchups': Matchup.objects.all().order_by('date'),
        'title':'Lliga Dominaria'
    }
    return render(request, 'dominaria/games.html', context)

def classif(request):
    players = Player.objects.all() 
    classification = []
    class classificate:
        def __init__(self, player, points, per_games_won, rounds_played):
            self.player = player
            self.points = points
            self.per_games_won = per_games_won
            self.rounds_played = rounds_played
        def __repr__(self):
            return repr((self.player, self.points, self.per_games_won, self.rounds_played))
    for player in players:
        rounds_played = Matchup.objects.filter(
            Q(player1=Player.objects.filter(name=player.name)[0].id) | Q(player2=Player.objects.filter(name=player.name)[0].id))
        rounds_won = rounds_played.filter(winner=Player.objects.filter(name=player.name)[0].id)
        games_won = 0
        gl = 0
        per_games_won = 0
        for _round in rounds_played:
            if _round.player1 == player:
                games_won += _round.games_won_by_p1
                gl += _round.games_won_by_p2
            elif _round.player2 == player:
                games_won+=_round.games_won_by_p2
                gl += _round.games_won_by_p1
        if games_won > 0:
            per_games_won = round(games_won/(games_won+gl)*100)
        draws = rounds_played.filter(winner=None).count()
        points = rounds_won.count() * 3 + draws
        classification.append(classificate(player.name, points, per_games_won, rounds_played.count()))
    sorted_classification = sorted(classification, key=attrgetter('points', 'per_games_won'), reverse=True)
    context= {
        'classification':sorted_classification,
        'title':'Lliga Dominaria'
    }
    return render(request, 'dominaria/classif.html', context)