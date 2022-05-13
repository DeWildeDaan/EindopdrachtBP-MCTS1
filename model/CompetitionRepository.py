import json
from .Competition import Competition
from .Team import Team

class CompetitionRepository:
    __filename = "doc/uefa.json"

     
    @staticmethod
    def __read_local_json_file(bestandsnaam):
        fo = open(bestandsnaam, encoding="utf8")
        response_json = fo.read()
        fo.close()
        return json.loads(response_json)
    
    @staticmethod
    def load_competition():
        dict_json = CompetitionRepository.__read_local_json_file(CompetitionRepository.__filename)
        dict_comp = dict_json["competition"]
        temp_comp_naam = dict_comp["name"]
        temp_comp_code = dict_comp["code"]
        temp_comp_id = dict_comp["id"]

        # nieuwe dict die in area zit
        dict_comp_area = dict_comp["area"]
        temp_comp_area_name = dict_comp_area["name"]
        geladen_comp = Competition(temp_comp_id, temp_comp_naam, temp_comp_code, temp_comp_area_name)

        # alle teams opvragen
        dict_teams = dict_json["teams"]
        for team in dict_teams:
            try:
                temp_name = team["name"]
                temp_short_name = team["shortName"]
                temp_founded = team["founded"]
                temp_colors = team["clubColors"]
                temp_venue = team["venue"]
                temp_team = Team(temp_name, temp_short_name, temp_founded, temp_colors, temp_venue)
                geladen_comp.voeg_team_toe(temp_team)
            except ValueError as ex:
                print(f"Foutmelding: {ex}")


        return geladen_comp