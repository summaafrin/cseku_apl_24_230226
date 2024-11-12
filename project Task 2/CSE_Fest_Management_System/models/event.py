class Event:
    """
    The Event class represents a general event in the CSE Fest.
    Each event has a name, description, and a list of participants who have registered.
    """

    def __init__(self, name, description):
        """
        Initializes an Event object with a name, description, and an empty list of participants.
        
        Parameters:
        - name: The name of the event (e.g., "Symposium Talk", "Datathon").
        - description: A brief description of the event.
        """
        self.name = name  # Name of the event
        self.description = description  # Description of the event
        self.participants = []  # List to hold participants registered for this event

    def add_participant(self, participant):
        """
        Adds a participant to the event.
        
        Parameters:
        - participant: The participant object to register for the event.
        
        This method appends the participant to the participants list, tracking
        all individuals registered for this specific event.
        """
        self.participants.append(participant)
