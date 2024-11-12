class Scheduler:
    def __init__(self):
        """
        Initializes a Scheduler object with an empty list of events.
        The events list will store each scheduled event.
        """
        self.events = []  # List to store scheduled events

    def add_event(self, event):
        """
        Adds an event to the events list and prints a confirmation message.
        
        Parameters:
        - event: The event object to be scheduled. It is expected to have a 'name' attribute for identification.
        """
        self.events.append(event)  # Add event to the list of scheduled events
        print(f"{event.name} has been scheduled.")  # Confirmation message for the scheduled event
