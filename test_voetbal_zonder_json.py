from model.Competition import Competition
from model.Team import Team


wedstrijd = Competition(
    1007, "Howest competition", "HWST", "West-Vlaanderen")
team_a = Team("Multimedia en Informatietechnologie",
              "MIT", 2020, "Blauw Wit", "Kortrijke Weide")
team_b = Team("Multimedia en communicatie technologie",
              "MCT", 1998, "Oranje", "Kortrijke Weide")


wedstrijd.voeg_team_toe(team_a)
wedstrijd.voeg_team_toe(team_b)

print(f"{wedstrijd}")
print(f"\tTeams in list: {wedstrijd.teams}")


try:
    team_c = Team("Internet of Things", "IOT", -14, "Blauw", "")    #geen geldige locatie
except Exception as ex:
    print(ex)
