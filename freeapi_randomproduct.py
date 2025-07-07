import requests as re

def fetch_randomproduct_api():
    url = "https://api.freeapi.app/api/v1/public/randomproducts/product/random"
    response = re.get(url)
    data = response.json()
    #print(data)
    if data["success"] and "data" in data:
        user_data = data["data"]
        price = user_data["price"]
        message = data["message"]
        return price,message
    else:
        raise Exception("Failed to Fetch user data")
def main():
    try:
        price,message = fetch_randomproduct_api()
        print(f"The price is :{price}")
        print(f"The message is :{message}")
    except Exception as e:
        print(str(e))
if __name__ == "__main__":
    main()