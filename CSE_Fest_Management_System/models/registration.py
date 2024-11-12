class Registration:
    """
    The Registration class manages participant registrations for various events in the CSE Fest.
    It holds a list of all registered participants and the events they have registered for.
    """

    def __init__(self):
        """
        Initializes the Registration class with an empty list to store registrations.
        Each registration is a tuple containing a participant and an event.
        """
        self.registrations = []

    def register(self, participant, event):
        """
        Registers a participant for a specific event.
        
        Parameters:
        - participant: The participant object who wants to register.
        - event: The event object for which the participant is registering.
        
        This method calls the event's `add_participant` method to add the participant to the event
        and then stores the registration details as a tuple in the `registrations` list.
        """
        event.add_participant(participant)  # Add participant to the event's participant list
        self.registrations.append((participant, event))  # Store the registration
