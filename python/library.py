'''
security functionality
'''

# modules needed
from bcrypt import hashpw, gensalt
hashed = hashpw(plaintext_password, gensalt(log_rounds=12)) # 12 is default
print hashed    # save this value to the database for this user
# example hashed:
'$2a$12$8vxYfAWCXe0Hm4gNX8nzwuqWNukOkcMJ1a9G2tD71ipotEZ9f80Vu'

# retrieve user's password and match:
if hashpw(password_attempt, users_hashed_pwd) == users_hashed_pwd: #hashpw extract salt from users_hashed_pwd
    print "It matches"
else:
    print "It does not match"


