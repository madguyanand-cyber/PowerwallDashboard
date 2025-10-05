Powerwall Dashboard
This project is a real-time, web-based monitoring dashboard for a Tesla Powerwall. It is designed to be run on an always-on tablet, providing an at-a-glance view of a home's energy status.

Architecture
The project uses a secure and robust two-part architecture: a dedicated back-end API server and a lightweight front-end client.

1. Back-End (Python API Server)
The back-end is a simple Python application designed to run 24/7 on a remote server (e.g., a cloud VM). Its sole responsibility is to act as a secure and stable gateway to the complex Tesla API.

Core Technology: TeslaPy

This is the cornerstone of the entire project. TeslaPy is a powerful Python library that handles the incredibly complex authentication and communication with the official Tesla API.

It manages the difficult OAuth2 login flow, the secure storage of authentication tokens (cache.json), and the automatic refreshing of those tokens.

By using TeslaPy, our back-end completely abstracts away all the API difficulties, providing a simple and reliable data source for our dashboard.

Server Framework:

Flask is used as a lightweight web framework to create the simple API endpoints (e.g., /api/live_status).

Waitress serves as the production-ready web server to run the Flask application.

2. Front-End (Web Dashboard)
The front-end is a single, self-contained index.html file that runs in any modern web browser.

Core Technology: It is built with plain HTML, CSS, and JavaScript.

Styling: Tailwind CSS is used for a modern and responsive user interface.

Functionality: Its only job is to periodically call the back-end API server, receive the live data, and update the display. It contains no complex authentication logic itself.

External Services
Tesla API: The primary source of live and historical data for the Powerwall. All communication is managed via the TeslaPy back-end.

Solcast API (Planned): This will be our chosen service for providing highly accurate, real-time solar production forecasts. The plan is for the front-end to make a separate, once-daily call to the Solcast API to fetch the forecast, which will then be displayed and stored locally.

Current Status
Back-End Complete & Verified: The app.py server is complete. We have successfully deployed it to the VM, completed the one-time authentication, and confirmed via curl that it can fetch and return live data from the Powerwall.

Front-End UI Complete: The index.html file contains the complete user interface layout.

Next Step: The final step of Stage 1 is to connect the front-end to the back-end and confirm that the live data populates the dashboard UI.

Setup Instructions
Back-End (on a Linux VM):

Install prerequisites: sudo apt install python3 python3-pip python3-venv npm -y

Create a project directory (e.g., teslapy-server) and cd into it.

Create a Python virtual environment: python3 -m venv venv and activate it: source venv/bin/activate.

Place app.py and requirements.txt in the folder.

Install dependencies: pip install -r requirements.txt.

Perform the one-time TeslaPy authentication by running python3 app.py and following the on-screen prompts.

Install and configure pm2 to run the server continuously.

Open port 5000 in your cloud provider's firewall.

Front-End (Local or Hosted):

Open the index.html file in a web browser.

Click the settings icon.

Enter the public URL of your back-end server (e.g., http://<your-vm-ip>:5000).

Click "Save". The dashboard will connect and display live data.
