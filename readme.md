# Carpark Availability Project
This project is a web application that helps users to find the nearest HDB carpark to their current location and check its availability. The application uses the government's open-source API to fetch carpark data and display it to the user.

# Technology Stack
The application is developed using Flask, a Python web framework, and Gunicorn, a Python WSGI HTTP Server for UNIX. Flask provides the back-end functionality for handling user requests and fetching data from the API. Gunicorn is used to deploy the Flask application on a server.

# How to Use
To use the application, simply enter your current location on the home page, and the application will display the nearest HDB carpark and its availability status. The user can also filter the results by carpark type.

# Installation
To install the application, follow these steps:

# Clone the repository
Install the dependencies using pip:
Copy code
`pip install -r requirements.txt`
Start the application using Gunicorn:
Copy code
`gunicorn app:app`
Open a web browser and navigate to http://localhost:8000 to access the application.

# Contributions
Contributions to this project are welcome. If you find any issues or want to suggest improvements, please submit an issue or a pull request.
