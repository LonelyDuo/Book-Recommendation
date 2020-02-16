import requests
import json

#important book information
#get title
def get_title(response_data, number):
    return (response_data['items'][number]['volumeInfo']['title'])

#get category
def get_category(response_data, number):
    return (response_data['items'][number]['volumeInfo']['categories'][0])

#get score
def get_rating(response_data, number):
    return (response_data['items'][number]['volumeInfo']['averageRating'])

#Make the actual request to the API using the python requests library
#You may need to run the command 'pip install requests' in your terminal
title = input('pick book subject: ')

api_request_response = requests.get(url="https://www.googleapis.com/books/v1/volumes?key=AIzaSyBlnhTDwJxnr9INvUAz4FMLO4dKoRBureU&content-type=application/json&q=" + title)

#Convert the data into a JSON object in python
response_data = api_request_response.json()
print(response_data)
theBook = [get_title(response_data, 0), get_category(response_data, 0), get_rating(response_data, 0)]
#Reccomendation system. Will be score based?

api_request_response = requests.get(url="https://www.googleapis.com/books/v1/volumes?key=AIzaSyBlnhTDwJxnr9INvUAz4FMLO4dKoRBureU&content-type=application/json&q=" + str(theBook[1]) + "+subject")
response_data = api_request_response.json()

books = []

for i in range(10):
    print([get_title(response_data, i), get_category(response_data, i), get_rating(response_data, i)])