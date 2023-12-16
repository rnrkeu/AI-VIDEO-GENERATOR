import pyperclip

# Get email from clipboard
copied_email = pyperclip.paste()
file_path = 'ALL_CODE/Email/stored_email.txt'
def savingemailtofile():

    # Save the email to a text file

    with open(file_path, 'w') as file:
        file.write(copied_email)
        print(f"Email '{copied_email}' saved to '{file_path}'")



def retrieveemailfromfile():
# Later, retrieve the email from the stored file
    with open(file_path, 'r') as file:
        stored_email = file.read()
        pyperclip.copy(stored_email)
        print(f"Retrieved email '{stored_email}' from '{file_path}'")


