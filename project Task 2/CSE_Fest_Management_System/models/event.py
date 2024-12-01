from interfaces.segment_Interface import SegmentInterface

# Single Responsibility Principle (SRP): 
# The Event class has a single responsibility of managing participants and starting the event.
# It does not handle unrelated tasks like notifications or results.

class Event(SegmentInterface):
    def __init__(self, name, description):
        # The Event class is initialized with a name, description, and an empty list of participants.
        self.name = name
        self.description = description
        self.participants = []

    # Open/Closed Principle (OCP): 
    # The Event class is open for extension (you can create subclasses for different types of events)
    # but closed for modification. It doesn't require modification to add new event types, just inheritance.
    def register_participant(self, participant):
        self.participants.append(participant)
        # This method adds a participant to the event's list of participants.
        print(f"{participant.name} has been registered for {self.name}.")

    def start_event(self):
        # This method starts the event.
        print(f"{self.name} is now starting!")
