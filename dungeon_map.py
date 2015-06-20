#This is to be the Dungeon Map Creator/Interaction file.
import dungeon_room as room
#import dungeon_display as disp

class Dungeon_Map():
    """Creates and maintains the map of the dungeon, and provides methods
    for character interaction."""

    def __init__(self, median = 10):
        """Generates a new dungeon map of 'median' maximum size (i.e.
        distance from the center in any of the 4 cardinal directions)."""
        self.median = median
        self.rooms = {}
        self.rooms[0,0] = room.Start_Room()
        return self

    def __getitem__(self, i):
        """Handles calls of the nature dungeon_map_obj[2, 9], returns the
        appropriate room."""
        x, y = i
        return self.rooms[x, y]
