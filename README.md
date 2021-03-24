# Insurer

The project has the ability to edit and save the result after calling to the customer.
Also, the app called "customer_service" allows use Django Rest Framework and Twilio.com for send SMS 
messages to customers to notify them that insurance policy is ending.

## Requirements
1. You must have [Docker](https://docs.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) on your machine.
2. You must have your Account SID and your Auth Token from twilio.com/console. To do this, get ACCOUNT_SID and AUTH_TOKEN 
from twilio.com and create .twilio.env file:  
   `touch .twilio.env`  
    Then add ACCOUNT_SID=your_sid and AUTH_TOKEN=your_token to him.

## Clone and Run the development server
1. Clone this repo with command:  
     `git clone git@github.com:mosiahr/insurer.git && cd insurer`

2. Create and start containers:  
    `docker-compose up -d`
    
3. Displays log output from services:  
    `docker-compose logs -f`
    
4. Display log output only from web service:  
    `docker-compose logs -f web`
    
5.  Stop and remove containers, networks, images, and volumes:  
    `docker-compose down -v`
