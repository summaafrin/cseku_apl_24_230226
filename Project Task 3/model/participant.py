# Model - Participant class represents a participant in the event.
# It holds the data related to a participant but does not manage how it is presented (which is the responsibility of the View)
class Participant:
    def __init__(self, name, university):
        self.name = name  # Data attribute: Participant's name
        self.university = university  # Data attribute: University the participant belongs to
