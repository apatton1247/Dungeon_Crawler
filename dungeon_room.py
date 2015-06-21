#This is to be the Dungeon Room Creator/Interaction file.
import weighted_random as wrand

class Battle_Event():
    """Defines a Battle Event, where a monster lurks and engages the entering
    player/group in battle."""
    #Should also hold the code for generic battles, including whatever happens
    # when another person/group enters in the middle of an undecided battle or
    # after a battle has ended but the original player/group remains inside.

    def __init__(self):
        pass

class Bazaar_Event():
    """Defines a Bazaar Event, where players may buy new items, sell old items,
    barter with others for items, and even redefine groups."""

    def __init__(self):
        pass

class Trap_Event():
    """Defines a Trap Event, where the only thing inside is... well... a Trap."""

    def __init__(self):
        pass

class Dungeon_Room():
    """A generic Room class that defines appropriate methods for all Rooms,
    such as __contains__ (for determining if a person or thing is 'in' the
    room)"""
    #TODO: Determine what other sorts of things the Room class needs to handle.

    PROB_BATTLE = .60
    PROB_BAZAAR = .20
    PROB_TRAP = .20
    room_rand = wrand.weight_rand({Battle_Event:PROB_BATTLE,
                                  Bazaar_Event:PROB_BAZAAR,
                                  Trap_Event:PROB_TRAP})
    
    def __init__(self):
        """On construction, an dark dungeon room with as-yet no branches is
        created. By consulting the weighted probability, the room event is
        determined."""
        self.branched_out = False
        self.dark = True
        self.event = room_rand.random()
        
        return self

    def enter(self, *players):
        """Players cause the following to take place on entering a room: the
        room becomes lit up, showing its type on the map, and the room event
        commences."""
        if self.dark == True:
            self.dark = False

class Start_Room(Dungeon_Room):
    """Defines the Starting Room, where each person/group begins the game."""

    def __init__(self):
        #TODO: Figure out how to program in doors such that any border with the
        # Start_Room will have a door, but all other are based on chance such
        # that each border of a room that lies next to another room has an equal
        # chance of having a door in it, unless it's the last border to test and
        # the room doesn't have any doors yet; in that case the probability for
        # making a door should be 100%.
        self.dark = False
        pass

