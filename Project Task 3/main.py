from model.event import Event
from model.participant import Participant
from model.registration import Registration
from model.results import Results
from view.event_view import display_event_start
from view.participant_view import display_registration
from view.result_view import display_results
from controller.event_controller import EventController
from controller.registration_controller import RegistrationController
from controller.result_controller import ResultController

def main():
    
    # Models
    symposium = Event("Symposium Talk", "Hear from top industry professionals.")
    datathon = Event("Datathon", "Showcase your machine learning skills.")
    registration = Registration()
    results = Results()

    # Controllers
    symposium_controller = EventController(symposium, display_event_start)
    datathon_controller = EventController(datathon, display_event_start)
    registration_controller = RegistrationController(registration, display_registration)
    result_controller = ResultController(results, display_results)

    # Participants
    participant1 = Participant("Saiful Islam Reyad", "KU")
    participant2 = Participant("Sumaiya Afrin Summa", "KU")

    # Register Participants
    print(registration_controller.register_participant(participant1, symposium))
    print(registration_controller.register_participant(participant2, datathon))

    # Start Events
    print(symposium_controller.start_event())
    print(datathon_controller.start_event())

    # Add and Display Results
    result_controller.add_result(symposium, participant1, "1st Place")
    result_controller.add_result(datathon, participant2, "2nd Place")
    print(result_controller.display_results(symposium))
    print(result_controller.display_results(datathon))

if __name__ == "__main__":
    main()
