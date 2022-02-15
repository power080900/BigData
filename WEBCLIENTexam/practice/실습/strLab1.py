def myemail_info (email):
    if "@" in email:
        return tuple(email.split('@'))
    else :
        return None

print(myemail_info("power080900@naver.com"))
print(myemail_info("power080900naver.com"))