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

print("THIS PROGRAM SUGGESTS A BOOK BASED ON BOOKS YOU'VE READ! JUST TYPE IN A BOOK YOU'VE READ AND RECIEVE RECOMENDATIONS AND A % MATCH!")
while True:
    try:

        input_text = input("Enter A Book Title: ")
        if (input_text == "quit"):
            exit(0)
        
        # print(api_search(input_text))
        #print(api_search(input_text)['totalItems'])

        for results in api_search(input_text)['items']:
            print("Title:")
            print("\t", results['volumeInfo']['title'])
            print("Author:")
            print("\t", results['volumeInfo']['authors'])

            print("Description:")
            try:
                print("\t", results['volumeInfo']['description'])
            except KeyError:
                print("N/A")
            
            
            print("Rating:")

            try:
                print("\t", results['volumeInfo']['averageRating'])
            except KeyError:
                print("N/A")


            print("\n\n")

            user_input = input("Is this the right book?")
            if (user_input.lower() == "yes"):
                #correct book, so we store the necessary information of the book
                theBook = []
                for results in api_search(input_text)['items']:
                    
                    #some of these information might be missing
                    theBook.append(results['volumeInfo']['title'])
                    theBook.append(results['volumeInfo']['authors'])
                    
                    try:
                        theBook.append(results['volumeInfo']['description'])
                    except KeyError:
                        theBook.append('n/a')

                    try:

                        theBook.append(results['volumeInfo']['averageRating'])
                    except KeyError:

                        theBook.append('n/a')

                    try:
                        theBook.append(results['volumeInfo']['categories'][0])
                    except KeyError:
                        theBook.append("fiction")

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
                    
            #some of these information might be missing
            addedBook.append(results['volumeInfo']['title'])
            try:

                addedBook.append(results['volumeInfo']['authors'])
            except:
                addedBook.append("n/a")
            try:
                addedBook.append(results['volumeInfo']['description'])
            except:
                addedBook.append('n/a')
            try:
                addedBook.append(results['volumeInfo']['averageRating'])
            except:
                addedBook.append('n/a')
            try:
                addedBook.append(results['volumeInfo']['categories'][0])
            except:
                addedBook.append("n/a")
            try:
                addedBook.append(results['volumeInfo']['imageLinks']['thumbnail'])
            except:
                addedBook.append("no available cover")
            
            #advanced mathematical, scientifically proven match rate. (Nobel won prize)
            percentMatch = 50

            #if the rating is good, I CAN'T SEEM TO IMPLEMENT IT
            if (addedBook[3] != 'na'):
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

            
            
        for results in api_search("+subject:" + str(theBook[4]))['items']:
            addedBook = []  
            
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
            dummy_list = ["Title:", "Author:", "Description:", "Rating:", "Category:", "Book Cover:", "% Match:"]
            k = 0
            print ("\n")
            for element in book:
                print(dummy_list[k])
                print('\t' + str(element))
                k = k+1

            user_input = input("Would you like another suggestion?")

            while user_input == "yes":
                break
            else:
                continue
            break
            
        

        
    # Exit on ctrl+c
    except KeyboardInterrupt:
        print("Exiting program")
        exit(0)
