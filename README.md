# IMPORTANT
This code is old. Refactor in progress to comply with SOLID principles and a clean architecture. Clean up in progress
The file .ini should be hidden as it contains credentials


# MailChimp
Send newsletters to all your subscribers


# NOTES:
  1. You have been working on a project and already have a populated subscribers list
  
  
# INSTALLATION:
  
  # Local install:
  - Docker and docker-compose are needed. You can download it from their official website https://www.docker.com/
  - Open up a terminal windows
  - Clone this repository via <pre><code>git clone https://github.com/RomanW05/Mailchimp_docker.git</pre></code> or download it as a zip and uncompress it
  - Move to the folder <pre><code>cd Mailchimp_docker</pre></code>
  - And once inside the folder run: <pre><code>docker-compose up --build</pre></code>
  
  - Once the containers are up and running open a browser window and type: <pre><code>0.0.0.0:5050</pre></code>
  - Here the pgAdmin starts and it is time to create the subscribers database
