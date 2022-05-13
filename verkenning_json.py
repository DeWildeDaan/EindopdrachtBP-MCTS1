import json

#Neem deze code NIET over. Dit is enkel om de structuur van de json-file te verkennen en te testen.

def __read_local_json_file(bestandsnaam):
    fo = open(bestandsnaam, encoding="utf8")
    response_json = fo.read()
    fo.close()
    return json.loads(response_json)

def test():
    dict_json = __read_local_json_file("doc/uefa.json")      #je krijgt een dict terug
    # dict_json = __read_local_json_file("doc/fifa.json")      #je krijgt een dict terug

    aantal = dict_json["count"]
    print(f"Aantal deelnemende landen: {aantal}")

    #competition ophalen -> is opnieuw dict -> bijhouden in dict_comp
    dict_comp = dict_json["competition"]

    #uit dict_comp 'name' halen
    print(f"Naam competitie: {dict_comp['name']}")

    #uit dict_comp 'area' halen ->  is opnieuw een dict...  -> testen door 'name' op te vragen
    print(f"Regio waar competitie plaats vindt: {dict_comp['area']['name']}")

    #teams geeft een list van dictionaries terug...
    list_teams = dict_json["teams"]
    print(f"De {len(list_teams)} teams zijn: ")

    for team in list_teams:
        print(team["name"])

test()