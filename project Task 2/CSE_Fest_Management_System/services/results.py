class Results:
    def __init__(self):
        """
        Initializes a Results object with an empty dictionary to store results.
        The results dictionary will use events as keys, with each event having a list of (participant, score) tuples.
        """
        self.results = {}  # Dictionary to store results for each event

    def add_result(self, event, participant, score):
        """
        Adds a result for a specific event and participant.
        
        Parameters:
        - event: The event for which the result is being recorded. It is used as a key in the results dictionary.
        - participant: The participant whose score is being recorded.
        - score: The score achieved by the participant in the event.
        
        If the event does not already exist in the dictionary, a new list is created for it.
        The (participant, score) tuple is then appended to the list for the specified event.
        """
        if event not in self.results:
            self.results[event] = []  # Initialize an empty list for the event if it doesn't exist
        self.results[event].append((participant, score))  # Add participant's score to the event's results list

    def display_results(self, event):
        """
        Displays all results for a specified event, printing each participant's name and their score.
        
        Parameters:
        - event: The event whose results are to be displayed. It is expected to have a 'name' attribute for identification.
        
        If the event exists in the results dictionary, each participant and their score will be printed.
        """
        print(f"Results for {event.name}:")  # Print header with event name
        for participant, score in self.results.get(event, []):  # Retrieve list of results for the event
            print(f"{participant.name}: {score}")  # Print each participant's name and score
