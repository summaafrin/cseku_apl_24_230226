from task2.CSE_Fest_Management_System.interfaces.segment_Interface import (
    SegmentInterface,
)
from models.event import Event


class CompetitiveProgramming(Event, SegmentInterface):
    """
    The CompetitiveProgramming class represents a specific segment of the CSE Fest:
    the Competitive Programming Contest.
    It inherits from the Event class to manage general event properties and implements
    the SegmentInterface to ensure it has methods for participant registration and event starting.
    """

    def __init__(self, name, description):
        """
        Initializes a Competitive Programming event with a name and description.

        Parameters:
        - name: The name of the Competitive Programming event.
        - description: A brief description of the event.

        Uses the Event class's initializer to set these attributes.
        """
        super().__init__(name, description)

    def register_participant(self, participant):
        """
        Registers a participant for the Competitive Programming event.

        Parameters:
        - participant: The participant object to be added to the event's participant list.

        This method appends the participant to the `participants` list inherited from the Event class.
        """
        self.participants.append(
            participant
        )  # Add participant to the event's participant list

    def start_event(self):
        """
        Starts the Competitive Programming event.

        This method prints a message to indicate that the Competitive Programming Contest is starting.
        """
        print(
            "Competitive Programming Contest is now starting!"
        )  # Simulate starting the event
