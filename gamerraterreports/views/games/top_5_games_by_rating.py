"""Module for generating top 5 games report"""
from django.shortcuts import render
from django.db import connection
from django.views import View
from gamerraterreports.views.helpers import dict_fetch_all


class Top5GameList(View):
    def get(self, request):
        with connection.cursor() as db_cursor:

            # TODO: Write a query to get all games along with the gamer first name, last name, and id
            db_cursor.execute("""
                SELECT
                    g.*,
                    CASE WHEN AVG(r.rating) ISNULL THEN 0 ELSE AVG(r.rating) END AS Rating
                FROM gamerraterapi_game g
                LEFT JOIN gamerraterapi_rating r
                    ON r.game_id = g.id
                GROUP BY g.id
                ORDER BY rating DESC
                LIMIT 5
                
            """)
            # Pass the db_cursor to the dict_fetch_all function to turn the fetch_all() response into a dictionary
            dataset = dict_fetch_all(db_cursor)

            top_5_games = []

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
                    "gamer_id": row['gamer_id'],
                    "rating": row['Rating'],
                }
                top_5_games.append(game)

        # The template string must match the file name of the html template
        template = 'top_5_games.html'

        # The context will be a dictionary that the template can access to show data
        context = {
            "top_5_games_list": top_5_games
        }

        return render(request, template, context)
