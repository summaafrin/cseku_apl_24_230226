class EventController:
    def __init__(self, model, view):
        # The Controller initializes with references to both the Model (Event) and the View.
        # This ensures the controller can mediate between the data layer (Model) and the presentation layer (View).
        self.model = model
        self.view = view

    def start_event(self):
        # The Controller calls the View to display a message about starting the event.
        # The data for the event (name) comes from the Model (`self.model.name`).
        # This demonstrates the separation of concerns:
        # - Model: Holds event data (`self.model.name`).
        # - Controller: Facilitates the interaction between Model and View.
        # - View: Responsible for presenting the message.
        return self.view.display_event_start(self.model.name)
