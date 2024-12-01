# Class representing a Participant in the event.
# The class adheres to the **Single Responsibility Principle (SRP)**:
# - Each class should have only one reason to change. The Participant class is focused on storing participant-related data, 
#   such as their name, university, and the segment they are part of.

class Participant:
    def __init__(self, name, university, segment):
        self.name = name          # Name of the participant
        self.university = university  # University where the participant is from
        self.segment = segment      # Segment (event category) the participant is part of
