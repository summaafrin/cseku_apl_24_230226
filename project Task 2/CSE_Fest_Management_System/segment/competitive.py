from interfaces.segment_Interface import SegmentInterface
from models.event import Event

# The CompetitiveProgramming class represents a specific event in the system.
# It adheres to the Single Responsibility Principle by focusing only on the logic of 
# a competitive programming event while delegating participant registration and 
# event starting functionality to the parent classes.

class CompetitiveProgramming(Event, SegmentInterface):
    def __init__(self, name, description):
        # The constructor initializes the event with a name and description.
        # It calls the parent class (Event) constructor using `super()`.
        super().__init__(name, description)

    def register_participant(self, participant):
        # This method adds a participant to the list of participants for the event.
        # This implementation follows the Interface Segregation Principle (ISP), 
        # where the class only implements methods that make sense for this event.
        self.participants.append(participant)

    def start_event(self):
        # This method starts the event and prints a message. 
        # It follows the Liskov Substitution Principle (LSP) by overriding 
        # the `start_event` method from the parent Event class.
        print("Competitive Programming Contest is now starting!")
