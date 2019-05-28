from django.shortcuts import render
import os
import requests
import configparser # 설정값 관리하기, 내장모듈
from inspect import getcallargs
# Create your views here.

access_token = os.getenv('access_token')
secret_key = os.getenv('secret_key')

url = "https://api.coinone.co.kr/v2/account/balance"

def set_token(self, grant_type="refresh_token"):
    """
    set token
    grant_type: password, refresh_token
    
    saved self.access_token, self.refresh_token, self.token_type
    """
    token_api_path = "/oauth/refresh_token/"
    
    url_path = self.host + token_api_path
    if grant_type == "refresh_token":
        headers = {"content-type":"application/x-www-form-urlencoded"}
        data = {"access_token":self.access_token}
        config = configparser.ConfigParser()
        config.read('conf/config.ini')
        res = requests.post(url_path, headers=headers, data=data)
        result = res.json()
        self.access_token = result["accessToken"]
        config["COINONE"]["access_token"] = self.access_token
        with open('conf/config.ini', 'w') as configfile:
            config.write(configfile)
    else:
        config = configparser.ConfigParser()
        config.read('conf/config.ini')
        self.access_token = config["COINONE"]["access_token"]
        print("get config.ini")
        print(self.access_token)
    return self.access_token
    
def test_set_token(self):
    print(inspect.stack()[0][3])
    access_token = self.coinone_machine.set_token(grant_type="refresh_token")
    assert access_token
    



# exec '$SHELL'
# echo export 'token="<token>"' >> ~/.bashrc
# c9 ~/.bashrc