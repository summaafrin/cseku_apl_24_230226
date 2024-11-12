from abc import ABC, abstractmethod

class SegmentInterface(ABC):
    """
    The SegmentInterface defines the necessary methods that any segment class
    (like SymposiumTalk, Datathon, etc.) must implement. This ensures that each
    segment can handle participant registration and event management in a standardized way.
    """
    
    @abstractmethod
    def register_participant(self, participant):
        """
        Abstract method to register a participant for the event.
        
        Parameters:
        - participant: The participant object that wants to register for the event.
        
        This method must be implemented by any class that inherits from SegmentInterface.
        """
        pass

    @abstractmethod
    def start_event(self):
        """
        Abstract method to start the event.
        
        This method should define the actions to be performed when the event begins
        (such as announcing the start or triggering event-related processes).
        It must be implemented by any class that inherits from SegmentInterface.
        """
        pass
