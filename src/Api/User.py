import requests
def random_user():
    url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    res=requests.get(url)
    data=res.json()
    if(res.ok):
        first=data["data"]["name"]["first"]
        last=data["data"]["name"]["last"]
        gender=data["data"]["gender"]
        email=data["data"]["email"]
        age = data["data"]["dob"]["age"]
        country=data["data"]["location"]["country"]
        print(f"Name => {first} {last}\nGender => {gender}\nEmail => {email}\nAge => {age}\nCountry => {country} ")
    else:
       raise AttributeError(data)
def random_user_id(id):
    try:
        response=requests.get(f"https://api.freeapi.app/api/v1/public/randomusers/{id}")
        data=response.json()
        if(response.ok):
            first = data["data"]["name"]["first"]
            last = data["data"]["name"]["last"]
            gender = data["data"]["gender"]
            email = data["data"]["email"]
            age = data["data"]["dob"]["age"]
            country = data["data"]["location"]["country"]
            print(f"Name => {first} {last}\nGender => {gender}\nEmail => {email}\nAge => {age}\nCountry => {country} ")
        else:
            raise AttributeError(data["data"])
    except Exception as e:
        print(e)
def register_user():
    try:
        data={}
        uname=input("Enter ur uname:")
        data["username"]=uname
        email=input("Enter ur email:")
        data["email"]=email
        password=input("Enter secure password:")
        data["password"]=password
        role=input("Enter ur role:")
        data["role"]=role
        print(data)
        url="https://api.freeapi.app/api/v1/users/register"
        response=requests.post(url,data=data)
        data=response.json()
        if(response.ok):
            print("username => ",data["data"]["user"]["username"],
                  "\nEmail => ",data["data"]["user"]["email"],
                  "\nRole => ",data["data"]["user"]["role"])
        else:
            print("error: ",data["message"])
    except Exception as ex:
        raise AttributeError("Error: ",ex)
def login_user():
    try:
        data={}
        username=input("Enter ur username:")
        data["username"]=username
        password=input("Enter ur password:")
        data["password"]=password
        url="https://api.freeapi.app/api/v1/users/login"
        response=requests.post(url,data=data)
        data=response.json()
        if(response.ok):
            print("username => ", data["data"]["user"]["username"],
                  "\nEmail => ", data["data"]["user"]["email"],
                  "\nRole => ", data["data"]["user"]["role"])
        else:
            print("error: ", data["message"])
    except Exception as e:
        raise AttributeError("Error: ",e)
def main():
    try:
        random_user()
        print("Get specific  user base on id!!!")
        id=int(input("enter ur id:"))
        random_user_id(id)
        #register_user()
        #login_user()
    except Exception as e:
        print("Error: ",e)
if __name__=='__main__':
    main()