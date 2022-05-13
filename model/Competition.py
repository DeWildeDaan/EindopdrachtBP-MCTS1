from .Team import Team

class Competition:
    #Class attributes

    #Constructor
    def __init__(self, parid, parname, parcode, pararea):
        self.__id = parid
        self.name = parname
        self.code = parcode
        self.__area = pararea
        self.__teams = []



    #Property's
    # ********** property id - (enkel getter) ***********
    @property
    def id(self):
        """ The id property. """
        return self.__id
    
    # ********** property name - (setter/getter) ***********
    @property
    def name(self):
        """ The name property. """
        return self.__name
    
    @name.setter
    def name(self, value):
        if value != "":
            self.__name = value
        else:
            raise ValueError("Invalid name")

    # ********** property code - (setter/getter) ***********
    @property
    def code(self):
        """ The code property. """
        return self.__code
    
    @code.setter
    def code(self, value):
        if value != "":
            self.__code = value
        else:
            raise ValueError("Invalid code")
    
    # ********** property area - (enkel getter) ***********
    @property
    def area(self):
        """ The area property. """
        return self.__area
    
    # ********** property teams - (enkel getter) ***********
    @property
    def teams(self):
        """ The teams property. """
        return self.__teams
    
    
    
    

    #ToString method
    def __str__(self):
        return f"Competition: {self.id} {self.name} {self.code} {self.area} aantal teams:{len(self.__teams)}"

    #Repr method
    def __repr__(self):
        return f""

    #Static methods
    #Static method: search_team_by_founded
    @staticmethod
    def search_team_by_founded(object_competition, gezocht_jaartal):
        resultaat = []
        for team in object_competition.teams:
            if gezocht_jaartal == team.founded:
                resultaat.append(team)
        return resultaat

    #Static method: search_team_by_clubcolor
    @staticmethod
    def search_team_by_clubcolor(uefa, kleur):
        resultaat = []
        for team in uefa.teams:
            if kleur in team.colors.lower():
                resultaat.append(team)
        return resultaat
    

    #Extra methods
    def voeg_team_toe (self, object_team):
        if type(object_team) is Team and object_team not in self.__teams:
            self.__teams.append(object_team)

    