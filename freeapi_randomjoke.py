import requests

def get_jokes_api():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/100"
    data = requests.get(url)
    user_data = data.json()
    #print(user_data)
    
    if user_data["success"] and "data" in user_data:
        content = user_data["data"]["content"]
        message = user_data["message"]
        return content,message
    else:
        raise Exception("No data found!")

def main():
    try:
        content,message = get_jokes_api()
        print(f"The joke is: {content}")
        print(f"The message is :{message}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()