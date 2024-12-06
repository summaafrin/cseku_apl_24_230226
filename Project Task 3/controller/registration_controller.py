class RegistrationController:
    # The constructor takes the model (registration_model) and view (participant_view) as dependencies
    # This ensures the controller is responsible for coordinating between the model and the view
    def __init__(self, registration_model, participant_view):
        # Model (Registration) handles the business logic for participant registration
        self.registration_model = registration_model
        
        # View (ParticipantView) handles the presentation logic, displaying registration information
        self.participant_view = participant_view

    # This method serves as the bridge between the model and the view
    def register_participant(self, participant, event):
        # The controller calls the model's register_participant method to register the participant in the event
        self.registration_model.register_participant(participant, event)
        
        # After the participant is registered, the controller invokes the view to display the registration details
        return self.participant_view.display_registration(participant.name, event.name)

