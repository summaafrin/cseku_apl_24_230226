from models.participant import Participant
from segment.symposium import SymposiumTalk
from segment.datathon import Datathon
# from segment.innovation import InnovationShowcase
# from segment.competitive import CompetitiveProgramming
from services.scheduler import Scheduler
from services.ConsoleNotifier import ConsoleNotifier
from services.EmailNotifier import EmailNotifier
from services.SMSNotifier import SMSNotifier
from services.results import Results
from models.registration import Registration

def main():
    # Creating Events
    # These are specific segment events which follow the SegmentInterface for polymorphism.
    symposium = SymposiumTalk("Symposium Talk", "Hear from top industry professionals.")
    datathon = Datathon("Datathon", "Showcase your machine learning skills.")

    # Creating Services
    # Services like Scheduler, Notifiers, and Results are instantiated, demonstrating separation of concerns.
    scheduler = Scheduler()
    registration = Registration()
    console_notifier = ConsoleNotifier()
    email_notifier = EmailNotifier()
    sms_notifier = SMSNotifier()
    results = Results()

    # Creating Participants
    # Instances of Participant are created, linking them to specific events (segments).
    participant1 = Participant("Saiful Islam Reyad", "University A", "Symposium")
    participant2 = Participant("Sumaiya Afrin Summa", "University B", "Datathon")

    # Registering Participants
    # Participants are registered for the relevant events, ensuring encapsulation in the Registration class.
    registration.register_participant(participant1, symposium)
    registration.register_participant(participant2, datathon)

    # Scheduling Events
    # The events are scheduled with the help of the Scheduler service.
    scheduler.add_event(symposium, "2024-12-01", "10:00 AM")
    scheduler.add_event(datathon, "2024-12-02", "11:00 AM")

    # Starting Events
    # Events are triggered to start by invoking their respective start_event() methods.
    symposium.start_event()
    datathon.start_event()

    # Notifying Participants
    # Notifications are sent to the participants based on the notification method chosen (Console, Email, SMS).
    console_notifier.notify_participant(participant1, "Your event Symposium Talk starts at 10:00 AM.")
    email_notifier.notify_participant(participant2, "Your event Datathon starts at 11:00 AM.")
    sms_notifier.notify_participant(participant1, "Reminder: Symposium Talk at 10:00 AM.")

    # Adding Results
    # Results are added to the Results service, maintaining separation of concerns between event handling and result management.
    results.add_result(symposium, participant1, "1st Place")
    results.add_result(datathon, participant2, "2nd Place")

    # Displaying Results
    # Results are displayed for each event in a consistent format.
    results.display_results(symposium)
    results.display_results(datathon)

# Entry point for the program, triggering the main function.
if __name__ == "__main__":
    main()
