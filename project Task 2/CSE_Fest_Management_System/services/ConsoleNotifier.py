# ConsoleNotifier class implements the NotificationInterface.
# This demonstrates the **Dependency Inversion Principle (DIP)**, as the class relies on the abstraction (NotificationInterface) rather than a concrete class.

from interfaces.notification_Interface import NotificationInterface

class ConsoleNotifier(NotificationInterface):
    # The method `notify_participant` provides the actual implementation 
    # of the notification logic, sending a console message to the participant.
    def notify_participant(self, participant, message):
        print(f"Notification to {participant.name}: {message}")
