# Model Class - Scheduler

class Scheduler:
    # The Scheduler class is part of the Model layer, handling data-related logic
    # It stores and manages event scheduling, without any concern for the user interface.
    
    def __init__(self):
        # Initialize an empty list of events
        self.events = []

    def add_event(self, event, date, time):
        # Adds an event along with its scheduled date and time to the events list
        # This is the business logic of scheduling, and it belongs in the Model
        # The method doesn't know anything about how or where the data will be displayed
        self.events.append((event, date, time))
