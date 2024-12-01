from interfaces.segment_Interface import (
    SegmentInterface,
)
from models.event import Event

# The Datathon class inherits from both Event and SegmentInterface
# This follows the "Interface Segregation Principle" (ISP) by implementing only the methods relevant to a specific event type.

class Datathon(Event, SegmentInterface):
    def __init__(self, name, description):
        # Calls the constructor of the Event class (super()) to initialize common event properties
        super().__init__(name, description)

    def register_participant(self, participant):
        # Registers a participant for the Datathon event. This method is part of the SegmentInterface.
        # Follows the "Dependency Inversion Principle" (DIP), as the method operates on abstractions (SegmentInterface), not concrete classes.
        self.participants.append(participant)

    def start_event(self):
        # Starts the event and outputs a message. This is the specific behavior for the Datathon event.
        # Follows "Single Responsibility Principle" (SRP) by ensuring the Datathon class is only responsible for Datathon-specific behavior.
        print("Datathon event is now starting!")
