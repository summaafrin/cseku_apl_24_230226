# Importing necessary interfaces
from interfaces.segment_Interface import SegmentInterface
from models.event import Event

# Applying the Interface Segregation Principle (ISP) by implementing the SegmentInterface.
# This class ensures that the event is consistent across different segments.
class SymposiumTalk(Event, SegmentInterface):
    def __init__(self, name, description):
        # Applying the Open/Closed Principle (OCP):
        # The class is open for extension (can add more specific event types like SymposiumTalk),
        # but closed for modification (we inherit common functionality from Event).
        super().__init__(name, description)

    def register_participant(self, participant):
        # The method adds a participant to the event's participants list.
        self.participants.append(participant)

    def start_event(self):
        # The event-specific action for starting the symposium is printed.
        print("Symposium Talk is now starting!")
