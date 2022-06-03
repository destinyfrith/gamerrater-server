from django.urls import path
from .views import GamesUnderAge8List, MostReviewedGameList, GreaterThan5PlayersGameList, NoImageGamesList, CategoryGameCountList
from .views import Bottom5GameList, Top5GameList, MostGamesAddedByGamerList, Top3ReviewersList

urlpatterns = [
    path('reports/childrenunder8', GamesUnderAge8List.as_view()),
    path('reports/mostreviewedgame', MostReviewedGameList.as_view()),
    path('reports/morethan5players', GreaterThan5PlayersGameList.as_view()),
    path('reports/noimages', NoImageGamesList.as_view()),
    path('reports/gamesbycategory', CategoryGameCountList.as_view()),
    path('reports/bottom5games', Bottom5GameList.as_view()),
    path('reports/top5games', Top5GameList.as_view()),
    path('reports/mostgamesbyuser', MostGamesAddedByGamerList.as_view()),
    path('reports/top3reviewers', Top3ReviewersList.as_view()),
]
