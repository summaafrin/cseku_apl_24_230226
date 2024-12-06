# This function is part of the View layer because it formats and prepares the notification message
# It takes the participant's name and a message, then returns the formatted string for display.
def send_notification(participant_name, message):
    # This is a View function because it directly deals with formatting the data for presentation.
    return f"Notification to {participant_name}: {message}"
