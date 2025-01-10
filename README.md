Contact Management System


Introduction:
Efficient management of contacts is essential in daily life, especially when dealing with a growing number of entries.
The Contact Management System is a Python-based application developed using Flask, offering an easy-to-use interface for managing contact data.
The system allows users to perform CRUD (Create, Read, Update, Delete) operations and ensures data persistence using JSON files, providing a reliable solution for contact organization.


Problem Domain:
Contact management becomes challenging when:
There is no centralized storage for contact information.
Searching, updating, or deleting data is cumbersome.
The system lacks user-friendly tools for interaction.
This project addresses these issues by implementing an efficient, scalable, and user-friendly solution for managing contacts.

Solution Domain:
The Contact Management System provides:
CRUD Operations:Add, update, delete, and search for contacts.
Persistent Storage:Use of JSON files ensures data retention across sessions.
API Integration:RESTful APIs facilitate seamless integration with front-end applications.
Ease of Use:A simple structure and intuitive interface for end-users.

Technique Required:
RESTful API Design:Implemented using Flask to handle HTTP methods like GET, POST, PUT, and DELETE.
File Handling:Reading from and writing to JSON files for data persistence.
Error Handling:Ensures robustness by managing exceptions such as file not found or invalid input.
Serialization:Converts data structures to and from JSON format for seamless processing.

Data Structure Use:

Hash Map (Dictionary):The contacts are stored in a dictionary, with names as keys and details as values.
This ensures O(1) average time complexity for adding, updating, and searching contacts.
List:Used to convert the dictionary into a structured JSON format for display purposes.

Methodology
Initialization:The application loads existing contacts from contacts.json into a dictionary during startup.
CRUD Operations:Performed through Flask routes using efficient data management techniques.
Persistent Storage:Ensures contact data is saved after every update.
User Interface:The system uses a placeholder HTML file for future front-end development, allowing interaction with the backend.

Conclusion:
The Contact Management System effectively addresses the challenges of contact organization with a lightweight, scalable design. 
It demonstrates efficient use of Python’s data structures and REST API principles, 
providing a solid foundation for future enhancements like database integration and advanced UI/UX features.


![image](https://github.com/user-attachments/assets/66e55c02-5dc1-4b89-ad85-e10e9ee92a99)





