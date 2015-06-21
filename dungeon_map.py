#This is to be the Dungeon Map Creator/Interaction file.
import dungeon_room as room
#import dungeon_display as disp

class Dungeon_Map():
    """Creates and maintains the map of the dungeon, and provides methods
    for character interaction."""

    def __init__(self, extents = 10):
        """Generates a new dungeon map of 'extent' maximum size (i.e.
        distance from the center in any of the 4 cardinal directions)."""
        self.extents = extents
        self.rooms = {}
        self.rooms[0,0] = room.Start_Room()
        #Should start game with rooms going in all 4 directions, to get as good a
        # start as possible, with as large a map as possible.
        for coords in [(1,0), (0,-1), (-1,0), (0,1)]:
            self.rooms[coords] = room.Dungeon_Room()
        #As long as not all rooms are "branched out" (meaning they've gone through
        # the process of being checked on each side to see if, by the probabilities,
        # another room should branch off in that side's direction if there's not
        # already one in that direction), continue branching off the unbranched rooms.
        while not all [room.branched_out for room in self.rooms]:
            for coords, room in self.rooms.items():
                if room.branched_out == False:
                    self.branch(coords, room)
                
        return self

    def __getitem__(self, i):
        """Handles calls of the nature dungeon_map_obj[x_coord, y_coord], returns the
        appropriate room."""
        x, y = i
        return self.rooms[x, y]

    def branch(self, coords, room_obj):
        """Defines how to branch out from an unbranched room to up to three additional
        rooms in the remaining directions (the excluded direction being the one from
        which this room ostensibly branched from, even if that's not where a door ends
        up being."""
        x, y = coords
        branch_coords = ((x+1, y), (x, y-1), (x-1, y), (x, y+1))
        for coord_pair in branch_coords:
            if coord_pair not in self.rooms.keys():
                #TODO: figure out this probability function.
                prob_room = ((x**2+y**2)**0.5)/
        pass
