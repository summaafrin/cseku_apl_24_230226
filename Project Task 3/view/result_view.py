# View: This function is part of the View layer, which is responsible for rendering and displaying the data.

def display_results(event_name, results):
    # The view formats the results output as a string.
    output = f"Results for {event_name}:\n"
    
    # The view loops through the results and formats the information to display it for each participant.
    for participant, score in results:
        output += f"{participant.name}: {score}\n"
    
    # The view returns the formatted output, which can be printed or displayed on the user interface.
    return output
