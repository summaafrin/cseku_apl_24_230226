# Model: Event class - This class represents the Model layer. It contains the business logic and data related to events.

class Event:
    def __init__(self, name, description):
        self.name = name  # Event name (data)
        self.description = description  # Event description (data)
        self.participants = []  # List of participants for the event (data)

    def register_participant(self, participant):
        # This method handles the business logic of registering a participant for the event.
        # It modifies the internal data of the event (participants list).
        self.participants.append(participant)

    def start_event(self):
        # This method returns a string indicating that the event has started.
        # It is the business logic for starting the event, and it returns a message (presentation logic in the Model).
        return f"{self.name} is now starting!"
