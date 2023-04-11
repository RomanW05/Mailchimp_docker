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
  - Type in your username <code>admin@admin.com</code> and password <code>123</code>
  - Once you are logged in create a new server
  - Under the general tab option:
    - "Name", type <code>postgres</code>
  - Under the connection tab option:
    - "Host name/address", type <code>0.0.0.0</code>
    - "Port", type <code>5050</code>
    - "Maintenance database", type <code>mailchimp</code>
    - "Username", type <code></code>


  # Issues:
  - <pre><code>ERROR: Couldn't connect to Docker daemon at http+docker://localhost - is it running?
    
      If it's at a non-standard location, specify the URL with the DOCKER_HOST environment variable.</pre></code>
    - Run: <code>$ sudo chown $USER /var/run/docker.sock</code> to include the user in the allowed clients
    - Run: <code>export DOCKER_HOST=unix:///var/run/docker.sock</code> to declare the variable DOCKER_HOST into the reachable hosts
  
  - <code>ERROR: Encountered errors while bringing up the project.</code> OR <pre><code>ERROR: for RabbitMQ  Cannot create container for service RabbitMQ: Conflict. The container name "/RabbitMQ" is already in use by container "CONTAINER_ID". You have to remove (or rename) that container to be able to reuse that name.</code></pre>
    - Stop and remove all previous running containers by:
      - Run: <code>docker stop CONTAINER_ID</code>
      - Run: <code>docker rm CONTAINER_ID</code>
    - Finally build and run the containers. Run: <code>docker-compose up --build</code>
