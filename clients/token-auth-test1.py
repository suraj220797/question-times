import requests

def client():
    token_h = "Token 3a543f7db3c4323e68e384e0e30427b07181acab"
    # credentials = {'username':'admin', 'password':'django1234'}
    #
    # response = requests.post('http://127.0.0.1:7000/api/rest-auth/login/',
    #                         data= credentials)

    headers = {"Autherization": token_h}
    response = requests.get("http://127.0.0.1:7000/api/profiles", headers=headers)

    print('Stauts Code: ', response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == '__main__':
    client()
