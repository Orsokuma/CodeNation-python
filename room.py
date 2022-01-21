class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
#############################################
# adv.py
#############################################
rooms = {
    'outside': Room(
        "Outside Cave Entrance",
        """
        You are standing to the South of the mouth of what
        appears to be a large cavern. It's dark inside of the
        cavern, but you think you make out the shadow of what
        appears to be a foyer with connected rooms...
        There also appears to be something skittering on the floor.
        """
    ),
    'foyer': Room(
        "Foyer",
        """
        Dim light filters in from the south. Dusty
        passages run north and east.
        """
    ),
    'overlook': Room(
        "Grand Overlook",
        """
        A steep cliff appears before you, falling
        into the darkness. Ahead to the north, a light flickers in
        the distance, but there is no way across the chasm.
        """
    ),
    'narrow':   Room(
        "Narrow Passage",
        """
        The narrow passage bends here from west
        to north. The smell of gold permeates the air.
        """
    ),
    'treasure': Room(
        "Treasure Chamber",
        """
        You've found the long-lost treasure
        chamber! Sadly, it has already been completely emptied by
        earlier adventurers. A dragon stubbornly guards the far end
        of the room. The only exit is to the south.
        """
    ),
}
# Link rooms together