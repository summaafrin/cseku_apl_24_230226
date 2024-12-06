# Model: This class is part of the Model layer, as it manages the business logic related to storing and managing event results.

class Results:
    def __init__(self):
        # This initializes the results dictionary to store results for each event.
        self.results = {}

    def add_result(self, event, participant, score):
        # This method adds the result (score) for a participant in an event.
        # It ensures that the results are categorized by event and stores the participant and their score.
        
        if event not in self.results:
            self.results[event] = []  # If the event doesn't exist in results, create a new entry.
        
        # Append the participant and their score to the corresponding event's results.
        self.results[event].append((participant, score))

