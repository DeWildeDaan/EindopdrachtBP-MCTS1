from model.CompetitionRepository import CompetitionRepository
from model.Competition import Competition
from model.Team import Team


def print_ploegen_uit_competition(parcompetitie):
    # hier komt een object van het type Competition binnen
    for t in parcompetitie.teams:
        print(f"{t.shortname:30}\t{t.colors} ")


def print_ploegen_uit_list_teams(parlist_teams):
    # hier komt een list met objecten van het type teams binnen
    for t in parlist_teams:
        print(f"{t.shortname:30}\t{t.colors} ")


def verwerk_gegevens():
    print(f"start laden...")
    uefa = CompetitionRepository.load_competition()
    print(f"...laden is gedaan")
    print(f"\nprint info competition")
    print(uefa)

    print(f"\nprint de ploegen uit de competition")
    print_ploegen_uit_competition(uefa)

    print(f"\nzoek ploegen, founded in 1904")
    selectie = Competition.search_team_by_founded(uefa, 1904)
    print_ploegen_uit_list_teams(selectie)

    print(f"\nzoek ploegen, met geel in de clubkleuren")
    selectie2 = Competition.search_team_by_clubcolor(uefa, 'yellow')
    print_ploegen_uit_list_teams(selectie2)
    
    print(f"\nsorteer de ploegen alfabetisch met geel in de clubkleuren")
    selectie2.sort()
    print_ploegen_uit_list_teams(selectie2)


verwerk_gegevens()


