# IMPORTANT
This code is in progress and refactoring the old solution. Applying SOLID principles and a clean architecture


# MailChimp
Send newsletters to all your subscribers


# NOTES:
  1. You have been working on a project and already have a populated subscribers list
  
  
# INSTALLATION:
The first thing we need to add is a ".ini" file inside the app folder. The contents of such file correspond to the credentials for the database, encoder, nominatim agent and email in the following format:
<pre><code>
[postgresql]
host=localhost
database=mailchimp
user=postgres
password=123

[encoder]
encoder_key=Qb9AtyJ7ASMlQO0qGhjxNfH9tyUg8EcWgdxAqDQ66lI=

[nominatim]
agent_number=1234

[email]
server=server101.web-hosting.com
password=123
email_address=info@example.io
</pre></code>

  
  # Local install:
  - Docker and docker-compose are needed. You can download it from their official website https://www.docker.com/
  - Open up a terminal windows
  - Clone this repository via <pre><code>git clone https://github.com/RomanW05/Mailchimp_docker.git</pre></code> or download it as a zip and uncompress it
  - Move to the folder <pre><code>cd Mailchimp_docker</pre></code>
  - And once inside the folder run: <pre><code>docker-compose up --build</pre></code>
  
  - Once the containers are up and running open a browser window and type: <pre><code>127.0.0.1:5050</pre></code>
  - Here the pgAdmin starts and it is time to create the subscribers database
