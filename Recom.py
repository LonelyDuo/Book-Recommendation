import requests
import json

#Make the actual request to the API using the python requests library
#You may need to run the command 'pip install requests' in your terminal
book = input('pick book subject: ')
api_request_response = requests.get(url="https://www.googleapis.com/books/v1/volumes?content-type=application/json&q="+book+"&key=AIzaSyBlnhTDwJxnr9INvUAz4FMLO4dKoRBureU"
)

#Convert the data into a JSON object in python
response_data = api_request_response.json()
print(response_data['items'][0]['volumeInfo']['averageRating'])
google.books.DefaultViewer(div, opt_options)
# print(response_data)