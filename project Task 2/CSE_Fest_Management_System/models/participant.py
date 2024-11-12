class Participant:
    """
    The Participant class represents an individual participant in the CSE Fest.
    Each participant has a name, affiliated university, and the segment they are interested in.
    """

    def __init__(self, name, university, segment):
        """
        Initializes a Participant object with a name, university, and segment.
        
        Parameters:
        - name: The name of the participant.
        - university: The name of the participant's university.
        - segment: The specific segment the participant is interested in (e.g., Symposium Talk, Datathon).
        """
        self.name = name  # Name of the participant
        self.university = university  # University the participant is associated with
        self.segment = segment  # Segment of the event the participant is joining
