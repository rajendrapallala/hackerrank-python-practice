def check_valid(email):
    try:
        username, url = email.split("@")
        website, extension = url.split(".")
    except ValueError:
        return False
    
    if username.replace("-", "").replace("_", "").isalnum() is False:
        return False
    elif website.isalnum() is False:
        return False
    elif len(extension) > 3:
        return False
    else:
        return True

n = int(input())
emails = [input() for email in range(n)]

valid = list(filter(check_valid, emails))
print(sorted(valid))

''' 
import re
def fun(s):
    # return True if s is a valid email, else return False
    regstr = '([a-zA-Z0-9_-]+)@([a-zA-Z0-9]+)\.([a-zA-z]{1,3}$)'
    return re.match(regstr, s)

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
'''
