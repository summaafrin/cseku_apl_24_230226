class Results:
    def __init__(self):
        # Initializes an empty dictionary to store event results.
        self.results = {}

    def add_result(self, event, participant, score):
        # Adds a result for a given event and participant.
        # If the event doesn't exist in the results dictionary, it's created.
        if event not in self.results:
            self.results[event] = []
        self.results[event].append((participant, score))

    def display_results(self, event):
        # Displays the results for a specific event.
        print(f"Results for {event.name}:")
        # Iterates through the results for the given event and displays the participant's name and score.
        for participant, score in self.results.get(event, []):
            print(f"{participant.name}: {score}")
