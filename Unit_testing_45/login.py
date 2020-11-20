import requests


class Login:
    def __init__(self, url='http://172.16.102.49'):
        self.url = url
        self.msg = None

    def login(self, name, passw):
        if not name:
            self.msg = 'ERR:username_empty'
        elif any(c in ['@','?','!'] for c in name):
            self.msg = 'ERR:unsupported_chars'
        else:
            payload = {'user': name, 'pass': passw}
            authentication = tuple(payload.values())
            print(f'authentication:{authentication}')
            r = requests.get(self.url, auth=authentication)
            if r.status_code == 200:
                self.msg = 'success'
            elif r.status_code == 401:
                self.msg = f'ERR:authentication_failed'
            else:
                self.msg = f'ERR status code: {r.status_code}'


if __name__ == "__main__":
    username = 'guest'
    password = 'guest'
    urlLogin = Login()
    urlLogin.login(name=username, passw=password)
    print(urlLogin.msg)