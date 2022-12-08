# Install the necessary libraries
#pip install beautifulsoup4 requests

# Import the necessary libraries
import requests
from bs4 import BeautifulSoup

# Send an HTTP request to the user's LinkedIn profile
response = requests.get('https://www.linkedin.com/in/USERNAME')

# Get the HTML content of the page
html = response.content

# Parse the HTML content
soup = BeautifulSoup(html, 'html.parser')

# Find the user's connections
connections = soup.find_all('a', class_='mn-connection-card__link')

# Initialize an empty queue and a set to store the 2nd degree connections
queue = []
second_degree_connections = set()

# Add the user's 1st degree connections to the queue
for connection in connections:
    queue.append(connection)

# Process the queue until all 2nd degree connections have been found
while queue:
    # Get the next connection from the queue
    current_connection = queue.pop(0)
    
    # Get the current connection's connections
    current_connections = soup.find_all('a', class_='mn-connection-card__link', href=current_connection['href'])
    
    # Add the current connection's connections to the queue
    for connection in current_connections:
        queue.append(connection)
        
    # Add the current connection to the set of 2nd degree connections
    second_degree_connections.add(current_connection)

# Print the user's 2nd degree connections
print(second_degree_connections)
