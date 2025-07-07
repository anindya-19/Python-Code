import requests

def get_random_book():
    url = "https://api.freeapi.app/api/v1/public/books/book/random"
    data = requests.get(url)
    obj = data.json()
    
    if obj["success"] and "data" in obj:
        message = obj["message"]
        country = obj["data"]["saleInfo"]["country"]
        bookDesc = obj["data"]["volumeInfo"]["description"]
        bookTitle = obj["data"]["volumeInfo"]["title"]
        #print(bookDesc)
        return message,country,bookDesc,bookTitle
    else:
        raise Exception("Not found")

def main():
    try:
        message,country,bookDesc,bookTitle = get_random_book()
        print(f"The message is :{message} ")
        print()
        print(f"The country is {country}")
        print()
        print(f"The BOOK Title is :\n {bookTitle}")
        print()
        print(f"The BOOK DESCRIPTION is :\n {bookDesc}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()