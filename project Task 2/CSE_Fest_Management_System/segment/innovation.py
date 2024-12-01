# Importing required interfaces and classes
from interfaces.segment_Interface import (
    SegmentInterface,  # Interface for segment-related functionalities
)
from models.event import Event  # Event base class for common event functionalities


# The InnovationShowcase class represents a specific event and follows the principles of SegmentInterface
class InnovationShowcase(Event, SegmentInterface):
    def __init__(self, name, description):
        # Using super() to call the parent class (Event) initializer
        # This adheres to the Open/Closed principle by allowing extension without modifying the base class
        super().__init__(name, description)

    def register_participant(self, participant):
        # Adding the participant to the event's list (delegating participant management to the event)
        self.participants.append(participant)

    def start_event(self):
        # Start the specific event (Innovation Showcase) and print the corresponding message
        # This adheres to the Interface Segregation Principle by providing a clear, simple method for this specific event type
        print("Innovation Showcase is now starting!")
