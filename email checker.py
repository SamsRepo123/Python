#TODO MAKE GUI VERSION of EMAIL CHECKER

## MODULES REQUIRED ##
# verify-email


from verify_email import verify_email
email = input("Enter a email you want to check: ")
var = verify_email(str(email))
if(str(var) == 'True'):
    print("Email exists")
elif(str(var) == 'False'):
    print("Email not exists")
else:
    print("Error, Something went wrong")