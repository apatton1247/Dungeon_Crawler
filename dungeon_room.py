#This is to be the Dungeon Room Creator/Interaction file.

class Dungeon_Room():
    """A generic Room class that defines appropriate methods for all Rooms,
    such as __contains__ (for determining if a person or thing is 'in' the
    room)"""
    #TODO: Determine what other sorts of things the Room class needs to handle.

    def __init__(self):
        return self

class Start_Room(Dungeon_Room):
    """Defines the Starting Room, where each person/group begins the game."""

    def __init__(self):
        pass

class Dark_Room(Dungeon_Room):
    """Defines a Dark Room, which players have either never entered before or
    haven't visited in at least 10 turn cycles.  A Dark Room, upon entering,
    is revealed to be (object is actually replaced by) a lit room of one of
    the remaining Room types."""

    def __init__(self):
        pass

class Battle_Room(Dungeon_Room):
    """Defines a Battle Room, where a monster lurks and engages the entering
    player/group in battle."""
    #Should also hold the code for generic battles, including whatever happens
    # when another person/group enters in the middle of an undecided battle or
    # after a battle has ended but the original player/group remains inside.

    def __init__(self):
        pass

class Bazaar_Room(Dungeon_Room):
    """Defines a Bazaar Room, where players may buy new items, sell old items,
    barter with others for items, and even redefine groups."""

    def __init__(self):
        pass

class Trap_Room(Dungeon_Room):
    """Defines a Trap Room, where the only thing inside is... well... a Trap."""

    def __init__(self):
        pass
