from abc import ABC, abstractmethod

# Defining an interface for event segments.
# This adheres to the **Interface Segregation Principle** by ensuring that only relevant methods 
# for managing event segments (like registration and starting an event) are included in this interface.
class SegmentInterface(ABC):
    @abstractmethod
    def register_participant(self, participant):
        """
        Abstract method for registering a participant in the segment.
        This ensures flexibility for each segment to define its own registration logic.
        """
        pass

    @abstractmethod
    def start_event(self):
        """
        Abstract method for starting the event.
        Enforces that every class implementing this interface must define its behavior when the event starts.
        """
        pass
