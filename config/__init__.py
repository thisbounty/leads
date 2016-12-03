import os
print
def values():
    return {
        'username': os.environ['freelance_username'],
        'password': os.environ['freelance_password'],
    }
