class Scheduler:
    def __init__(self):
        self.events = []  # Stores all scheduled events

    # Adding an event to the scheduler
    def add_event(self, event, date, time):
        self.events.append((event, date, time))  # Append event details
        print(f"{event.name} has been scheduled for {date} at {time}.")  # Confirmation message
