import requests
import json
import random

#Make the actual request to the API using the python requests library
#You may need to run the command 'pip install requests' in your terminal
SEARCH_ENDPOINT = "https://www.googleapis.com/books/v1/volumes?"
# SEARCH_ENDPOINT = "https://www.googleapis.com/books/v1/volumes?content-type=application/json"
API_KEY = "AIzaSyBlnhTDwJxnr9INvUAz4FMLO4dKoRBureU"


# book = input('pick book subject: ')
# api_request_response = requests.get()
# )

# api_request_response = requests.get(url="https://www.googleapis.com/books/v1/volumes?content-type=application/json      &q=%22+book+%22          &key=AIzaSyBlnhTDwJxnr9INvUAz4FMLO4dKoRBureU"
# )

def api_search(text):
    parameters = {"q": text, "key": API_KEY}

    response = requests.get(url= SEARCH_ENDPOINT, params=parameters)

    return response.json()

#Convert the data into a JSON object in python
# response_data = api_request_response.json()
# print(response_data['items'][0]['volumeInfo']['averagtheeRating'])
# print(response_data)

while True:
    try:
        input_text = input("Enter the Book Title: ")
        if (input_text == "quit"):
            exit(0)
        
        # print(api_search(input_text))
        print(api_search(input_text)['totalItems'])

        for results in api_search(input_text)['items']:
            print("Title:")
            print("\t", results['volumeInfo']['title'])
            print("Author:")
            print("\t", results['volumeInfo']['authors'])
            print("Description:")
            print("\t", results['volumeInfo']['description'])
            print("Rating:")
            print("\t", results['volumeInfo']['averageRating'])
            print("\n\n")

            user_input = input("Is this the right book: ")
            if (user_input.lower() == "yes"):
                #correct book, so we store the necessary information of the book
                theBook = []
                for results in api_search(input_text)['items']:
                    
                    #some of these information might be missing
                    theBook.append(results['volumeInfo']['title'])
                    theBook.append(results['volumeInfo']['authors'])
                    theBook.append(results['volumeInfo']['description'])

                    try:

                        theBook.append(results['volumeInfo']['averageRating'])
                    except KeyError:

                        theBook.append('n/a')

                    theBook.append(results['volumeInfo']['categories'][0])
                    theBook.append(results['volumeInfo']['imageLinks']['thumbnail'])
                    break
            else:
                continue 
            break
        #recommend books.

        booksuggestions = []
        #author books
        for results in api_search("+inauthor:" + str(theBook[1]))['items']:

            addedBook = []
            for results in api_search("+inauthor:" + str(theBook[1]))['items']:
                    
                #some of these information might be missing
                addedBook.append(results['volumeInfo']['title'])
                addedBook.append(results['volumeInfo']['authors'])
                try:
                    addedBook.append(results['volumeInfo']['description'])
                except:
                    addedBook.append('n/a')
                try:
                    addedBook.append(results['volumeInfo']['averageRating'])
                except:
                    addedBook.append('n/a')
                addedBook.append(results['volumeInfo']['categories'][0])
                addedBook.append(results['volumeInfo']['imageLinks']['thumbnail'])
            
            #advanced mathematical, scientifically proven match rate. (Nobel won prize)
            percentMatch = 50

            if (int(addedBook[3]) > 3):
                percentMatch = percentMatch + 20
            
            # Give a rating based on how similar the descriptions are
            # if (str(theBook[2]) in )

            #advanced algorigthm 
            percentMatch = percentMatch + random.randint(0,9)
            percentMatch = percentMatch + random.randint(0,9)
            
            addedBook.append(percentMatch) #index 6
            booksuggestions.append(addedBook)

        #similar description
        three = 3
        for results in api_search("+subject:" + theBook[4])['items']:
            
            addedBook = []
            for results in api_search("+subject:" + theBook[4])['items']:
                    
                #some of these information might be missing
                addedBook.append(results['volumeInfo']['title'])
                addedBook.append(results['volumeInfo']['authors'])
                try:
                    addedBook.append(results['volumeInfo']['description'])
                except:
                    addedBook.append('n/a')
                try:
                    addedBook.append(results['volumeInfo']['averageRating'])
                except:
                    addedBook.append('n/a')
                addedBook.append(results['volumeInfo']['categories'][0])
                addedBook.append(results['volumeInfo']['imageLinks']['thumbnail'])
            
            #advanced mathematical, scientifically proven match rate. (Nobel won prize)
            percentMatch = 50

            if (addedBook[3] != 'na'):
                percentMatch = percentMatch + 20
            
            # Give a rating based on how similar the descriptions are
            # if (str(addedBook[2]) in )

            #advanced algorigthm 
            percentMatch = percentMatch + random.randint(0,9)
            percentMatch = percentMatch + random.randint(0,9)
            
            addedBook.append(percentMatch) #index 6
            booksuggestions.append(addedBook)
            three = three - 1
            if (three == 0):
                break
            else:
                continue
            break

        for book in booksuggestions:
        
            for element in book:
                print(element)
            user_input = input("Like what you see?")
            
            while user_input == "1":
                break
            else:
                continue
            break
            

        
    # Exit on ctrl+c
    except KeyboardInterrupt:
        print("Exiting program")
        exit(0)
