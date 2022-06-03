"""Module for generating games with more than 5 players report"""
from django.shortcuts import render
from django.db import connection
from django.views import View
from gamerraterreports.views.helpers import dict_fetch_all

class GreaterThan5PlayersGameList(View):
    def get(self, request):
        with connection.cursor() as db_cursor:

            # TODO: Write a query to get all games along with the gamer first name, last name, and id
            db_cursor.execute("""
                SELECT *
                FROM gamerraterapi_game g
                WHERE g.number_of_players > 5
            """)
            # Pass the db_cursor to the dict_fetch_all function to turn the fetch_all() response into a dictionary
            dataset = dict_fetch_all(db_cursor)

            more_than_5_players = []

            for row in dataset:
                # TODO: Create a dictionary called game that includes 
                # the name, description, number_of_players, maker,
                # game_type_id, and skill_level from the row dictionary
                game = {
                    "id": row['id'],
                    "title": row['title'],
                    "description": row['description'],
                    "designer": row['designer'],
                    "year_released": row['year_released'],
                    "time_to_play": row['time_to_play'],
                    "number_of_players": row['number_of_players'],
                    "age_recommendation": row['age_recommendation'],
                    "gamer_id": row['gamer_id']
                }
                more_than_5_players.append(game)
        
        # The template string must match the file name of the html template
        template = 'more_than_5_players.html'
        
        # The context will be a dictionary that the template can access to show data
        context = {
            "more_than_5_players_list": more_than_5_players
        }

        return render(request, template, context)