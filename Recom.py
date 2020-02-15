import requests
import json

#Make the actual request to the API using the python requests library
#You may need to run the command 'pip install requests' in your terminal
SEARCH_ENDPOINT = "https://www.googleapis.com/books/v1/volumes?content-type=application/json"
API_KEY = "AIzaSyBlnhTDwJxnr9INvUAz4FMLO4dKoRBureU"


# book = input('pick book subject: ')
# api_request_response = requests.get()
# )

# api_request_response = requests.get(url="https://www.googleapis.com/books/v1/volumes?content-type=application/json      &q=%22+book+%22          &key=AIzaSyBlnhTDwJxnr9INvUAz4FMLO4dKoRBureU"
# )
def api_search(text):
    parameters = {"q": text, 
                "key": API_KEY}

    response = requests.get(url= SEARCH_ENDPOINT, params=parameters)

    return response.json()





#Convert the data into a JSON object in python
# response_data = api_request_response.json()
# print(response_data['items'][0]['volumeInfo']['averageRating'])
# print(response_data)

while True:
    try:
        input_text = input("Enter your query text: ")
        if (input_text == "quit"):
            exit(0)
        
        print("Title: ")
        print(api_search(input_text)['items'][0]['volumeInfo']['title'])
        print("\n")
        print("Author:")
        print(api_search(input_text)['items'][0]['volumeInfo']['authors'])
        print("\n")
        print("Description:")
        print(api_search(input_text)['items'][0]['volumeInfo']['description'])
        # for result in api_search(input_text):
        #     print("Result")
        #     print(result)

            
    # Exit on ctrl+c
    except KeyboardInterrupt:
        print("Exiting program")
        exit(0)