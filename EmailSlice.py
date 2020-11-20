# This is a sample Python script - Email Slicer

email=input("What is the email address:").strip()
user = email[:email.index("@")]
domain = email[email.index("@")+1:]
output = "The username is {} and domain is {}".format(user,domain)
print(output)