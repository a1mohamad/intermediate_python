import re
def is_valid_email(email):
    result = re.search(r'(^\w[\w\.]+)\@(w+)\.(w+)', email)
    if result == None:
        print ('WRONG')
    else:
        print('OK')
inserted_email = str(input('Please Insert Your Email: '))
is_valid_email(inserted_email)