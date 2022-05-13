class Team:
    #Class attributes

    #Constructor
    def __init__(self, parname, parshortname, parfounded, parcolors, parvenue):
        self.name = parname
        self.shortname = parshortname
        self.founded = parfounded
        self.colors = parcolors
        self.venue = parvenue



    #Property's
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
    
    # ********** property shortname - (setter/getter) ***********
    @property
    def shortname(self):
        """ The shortname property. """
        return self.__shortname
    
    @shortname.setter
    def shortname(self, value):
        if value != "":
            self.__shortname = value
        else:
            raise ValueError("Invalid shortname")
    
    # ********** property founded - (setter/getter) ***********
    @property
    def founded(self):
        """ The founded property. """
        return self.__founded
    
    @founded.setter
    def founded(self, value):
        if value != "" and type(value) is int and value > 0:
            self.__founded = value
        else:
            raise ValueError("Invalid foundation date")

    # ********** property colors - (setter/getter) ***********
    @property
    def colors(self):
        """ The colors property. """
        return self.__colors
    
    @colors.setter
    def colors(self, value):
        if value != None:
            self.__colors = value
        else:
            raise ValueError("Invalid colors")

    # ********** property venue - (setter/getter) ***********
    @property
    def venue(self):
        """ The venue property. """
        return self.__venue
    
    @venue.setter
    def venue(self, value):
        if value != "":
            self.__venue = value
        else:
            raise ValueError("Invalid venue")
    
    
    
    
    

    #ToString method
    def __str__(self):
        return f"{self.name} ({self.shortname} - {self.founded}) --> colors: {self.colors} \tvenue: {self.venue}"

    #Repr method
    def __repr__(self):
        return f"{self.name} ({self.shortname})"

    #Static methods

    #Extra methods
    #Method overload: eq
    def __eq__(self, other):
        if self.shortname == other.shortname:
            return True
        else:
            return False
    
    #Method overload: lt
    def __lt__(self, other):
        if self.shortname < other.shortname:
            return True
        else:
            return False
    
    