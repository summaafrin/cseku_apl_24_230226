class ResultController:
    def __init__(self, result_model, result_view):
        # The Controller is initialized with the Model (Result) and View (Result View)
        # It will coordinate the interaction between the Model and View.
        self.result_model = result_model  # Model: Contains the logic and data (Results)
        self.result_view = result_view    # View: Responsible for displaying the data

    def add_result(self, event, participant, score):
        # The Controller calls the Model to add a result.
        # It processes the interaction between the event, participant, and score.
        self.result_model.add_result(event, participant, score)
        # The Model handles the data and business logic (storing the result).

    def display_results(self, event):
        # The Controller retrieves the results from the Model for a given event.
        # It then passes the data to the View to be formatted and displayed.
        results = self.result_model.results.get(event, [])  # Retrieve results from the Model
        return self.result_view.display_results(event.name, results)
        # The View is responsible for presenting the data in a user-readable format.
