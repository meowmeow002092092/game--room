class Room:
    def __init__(self, name, description, connected_rooms=None, items=None, action=None, special_action=None):
        self.name = name
        self.description = description
        self.connected_rooms = connected_rooms if connected_rooms else {}
        self.items = items if items else []
        self.action = action  # Optional action (e.g., NPC, hidden door, etc.)
        self.special_action = special_action  # Special interaction (e.g., push a shelf)

    def connect(self, room, direction):
        self.connected_rooms[direction] = room

    def describe(self):
        print(f"\nYou are in the {self.name}. {self.description}")
        if self.items:
            print(f"You see: {', '.join(self.items)}")

    def interact(self):
        if self.action:
            print(self.action)
            if self.special_action:
                self.special_action()


class Game:
    def __init__(self):
        self.current_room = None
        self.inventory = []

    def start_game(self):
        # Create rooms with different descriptions and interactive elements
        room1 = Room("Entrance Hall", 
                     "You are in a grand entrance hall. There are doors leading to the north and east.", 
                     items=["old painting", "rusty key"])
        
        room2 = Room("Library", 
                     "You are in a dusty library. Shelves full of ancient books surround you. A secret door might be hidden.", 
                     action="You notice a loose shelf. It could be hiding something!", 
                     special_action=self.push_shelf)
        
        room3 = Room("Kitchen", 
                     "You are in a warm kitchen with the smell of fresh bread. A kettle whistles in the corner.", 
                     items=["fresh bread", "rusty knife"])
        
        room4 = Room("Garden", 
                     "You are in a lush garden, with flowers blooming and a small pond in the middle. A bird is singing.", 
                     action="You see a small bird nest with something shiny inside.")
        
        room5 = Room("Cellar", 
                     "The air is damp and musty in this cellar. There are cobwebs everywhere, and the ground is wet.", 
                     action="You hear something scratching at the walls.")
        
        room6 = Room("Study", 
                     "You are in a quiet study. There are papers scattered on a desk, and a fire burns gently in the fireplace.", 
                     items=["book of magic", "quill pen"])

        # Connect rooms
        room1.connect(room2, 'north')
        room1.connect(room3, 'east')
        room2.connect(room4, 'west')
        room3.connect(room5, 'south')
        room4.connect(room6, 'north')

        self.current_room = room1

        # Start the adventure
        print("Welcome to the Adventure Game!")
        self.play()

    def play(self):
        while True:
            self.current_room.describe()

            action = input("What would you like to do? (go <direction>, inventory, interact, quit): ").lower()

            if action == "quit":
                print("Thank you for playing!")
                break
            elif action == "inventory":
                print("Your inventory:", self.inventory)
            elif action == "interact":
                self.current_room.interact()
            elif action.startswith("go "):
                direction = action.split(" ")[1]
                if direction in self.current_room.connected_rooms:
                    self.current_room = self.current_room.connected_rooms[direction]
                else:
                    print("You can't go that way.")
            else:
                print("Invalid action. Try again.")

    def push_shelf(self):
        print("You push the shelf, revealing a hidden door!")
        # You could add logic to open the door or move to another room here
        hidden_room = Room("Secret Room", "You have discovered a secret room with glowing artifacts!")
        self.current_room.connect(hidden_room, "north")  # Now the library has a new exit to the secret room
        print("A secret room has been unlocked to the north!")

# Start the game
game = Game()
game.start_game()
