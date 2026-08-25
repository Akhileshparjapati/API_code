import requests

def get_api_call():
    url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response=requests.get(url)
    data=response.json()
    if data["success"] and "data" in data:
        user_data=data["data"]
        user_id=user_data["login"]["uuid"]
        user_loc=user_data["location"]["state"]
        return user_id, user_loc
    else:
        raise Exception("Failed to fetch API")

# print(get_api_call())

def main():
    try:
        userid,country=get_api_call()
        print(f"{userid}: and \n{country}:")
    except Exception as e:
        print(str(e))
    pass

if __name__=="__main__":
    main()



#r=requests.get(https://api.freeapi.app/api/v1/public/randomusers/user/random)