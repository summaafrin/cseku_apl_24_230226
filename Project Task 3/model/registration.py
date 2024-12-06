# Model - Registration Class
# The Registration class is part of the Model layer, responsible for handling business logic 
# related to participant registrations. It manages data (registrations) and performs operations 
# like registering a participant for an event.

class Registration:
    def __init__(self):
        self.registrations = []  # List that holds participant-event registrations

    def register_participant(self, participant, event):
        # Registers a participant for an event by calling the event's register_participant method
        event.register_participant(participant)
        
        # Adds the registration data (participant, event) to the registrations list
        self.registrations.append((participant, event))
