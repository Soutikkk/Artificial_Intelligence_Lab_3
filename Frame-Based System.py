
# Frame-Based System.py

class Frame:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.slots = {}

    def add_slot(self, slot, value):
        """Add a property and its value to the frame."""
        self.slots[slot] = value

    def get_slot(self, slot):
        """Get a value, inheriting it from the parent if needed."""
        if slot in self.slots:
            return self.slots[slot]

        if self.parent:
            return self.parent.get_slot(slot)

        return None

    def display(self):
        """Display frame information."""
        print(f"\nFrame: {self.name}")
        print(f"Parent: {self.parent.name if self.parent else 'None'}")

        if self.slots:
            print("Slots:")
            for slot, value in self.slots.items():
                print(f"  {slot}: {value}")
        else:
            print("Slots: None")


# Create a general frame
animal = Frame("Animal")
animal.add_slot("breathes", True)
animal.add_slot("movement", "Can move")
animal.add_slot("living_thing", True)

# Create a child frame
bird = Frame("Bird", parent=animal)
bird.add_slot("legs", 2)
bird.add_slot("covering", "Feathers")
bird.add_slot("can_fly", True)

# Create another child frame
penguin = Frame("Penguin", parent=bird)
penguin.add_slot("can_fly", False)
penguin.add_slot("habitat", "Cold regions")
penguin.add_slot("swims", True)


# Display all frames
animal.display()
bird.display()
penguin.display()

# Demonstrate inheritance
print("\n--- Knowledge Retrieval ---")
print("Does a penguin breathe?", penguin.get_slot("breathes"))
print("Does a penguin have feathers?", penguin.get_slot("covering"))
print("Can a penguin fly?", penguin.get_slot("can_fly"))
print("Where does a penguin live?", penguin.get_slot("habitat"))
print("Does a penguin swim?", penguin.get_slot("swims"))
