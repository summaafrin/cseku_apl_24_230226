# MVC Event Management System

This project implements an **Event Management System** using the **Model-View-Controller (MVC)** architecture.

## Explanation of MVC Architecture

### **1. Model**
The **Model** layer is responsible for managing the application's data, logic, and rules. It is independent of the View and Controller.

- **Components:**
  - `Event`: Represents event-specific data and operations.
  - `Participant`: Contains participant information.
  - `Registration`: Manages participant registrations for events.
  - `Scheduler`: Handles event scheduling with dates and times.
  - `Results`: Stores and displays event results.

- **Adherence to MVC:**
  - Models only handle data and business logic, ensuring they are reusable and independent.

---

### **2. View**
The **View** layer is responsible for presenting data. It formats data provided by the Controller for the user.

- **Components:**
  - `event_view`: Formats messages related to events.
  - `participant_view`: Displays participant registration details.
  - `notification_view`: Formats notifications for participants.
  - `result_view`: Displays event results.

- **Adherence to MVC:**
  - Views are stateless and only deal with UI formatting. They don’t contain or manipulate business logic.

---

### **3. Controller**
The **Controller** serves as an intermediary between the Model and the View. It processes user input, calls the Model for data manipulation, and prepares data for the View.

- **Components:**
  - `event_controller`: Manages event interactions between Model and View.
  - `registration_controller`: Handles participant registrations.
  - `result_controller`: Manages event result logic.

- **Adherence to MVC:**
  - Controllers coordinate between the Model and the View. They neither contain data nor present it directly.

---

### **4. Main Program**
The `main.py` file acts as the entry point, initializing the Models, Views, and Controllers and tying them together. It delegates all responsibilities to the appropriate MVC layers.

## File Structure
```plaintext
project/
├── model/
│ ├── event.py # Handles event data and logic 
│ ├── participant.py # Encapsulates participant information 
│ ├── registration.py # Manages participant registrations 
│ ├── scheduler.py # Manages event scheduling 
│ └── results.py # Stores and retrieves event results 
├── view/ 
│ ├── event_view.py # Formats and displays event messages 
│ ├── participant_view.py # Displays participant registration details 
│ ├── notification_view.py # Formats notifications for participants 
│ └── result_view.py # Prepares results for display 
├── controller/ 
│ ├── event_controller.py # Handles event interactions 
│ ├── registration_controller.py # Manages participant registrations 
│ └── result_controller.py # Manages event results 
└── main.py # Entry point tying the MVC components together
