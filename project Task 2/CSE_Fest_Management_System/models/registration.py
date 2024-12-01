class Registration:
    def __init__(self):
        self.registrations = []  # Holds all registrations

    def register_participant(self, participant, event):
        # The method delegates the responsibility of registering the participant to the event
        event.register_participant(participant)
        
        # Adds the registration to the list of registrations
        self.registrations.append((participant, event))
