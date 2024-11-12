from models.participant import Participant
from segment.symposium import SymposiumTalk
from segment.datathon import Datathon
from segment.innovation import InnovationShowcase
from segment.competitive import CompetitiveProgramming
from services.scheduler import Scheduler
from services.notifier import Notifier
from services.results import Results

def main():
    # Create event segments
    symposium = SymposiumTalk("Symposium Talk", "Hear from top industry professionals.")
    datathon = Datathon("Datathon", "Showcase your machine learning skills.")
    innovation = InnovationShowcase("Innovation Showcasing", "Present innovative ideas.")
    competitive = CompetitiveProgramming("Competitive Programming", "Test your coding skills.")

    # Initialize services
    scheduler = Scheduler()
    notifier = Notifier()
    results = Results()

    # Register participants
    participant1 = Participant("Alice", "University A", "Symposium")
    participant2 = Participant("Bob", "University B", "Datathon")

    symposium.register_participant(participant1)
    datathon.register_participant(participant2)

    # Schedule events
    scheduler.add_event(symposium, "2024-12-01", "10:00 AM")
    scheduler.add_event(datathon, "2024-12-02", "11:00 AM")

    # Start events
    symposium.start_event()
    datathon.start_event()

    # Notify participants
    notifier.notify_participant(participant1, "Your event Symposium Talk starts at 10:00 AM.")
    notifier.notify_participant(participant2, "Your event Datathon starts at 11:00 AM.")

    # Record and display results
    results.add_result("Symposium", participant1, "1st Place")
    results.add_result("Datathon", participant2, "2nd Place")
    results.display_results("Symposium")
    results.display_results("Datathon")

if __name__ == "__main__":
    main()
