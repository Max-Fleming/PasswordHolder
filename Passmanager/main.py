import PasswordGenerator

# write site, password, and username
def write_password(site, username, password):
  with open('PasswordList.txt', 'a') as f:
    f.write(f'{site}|{username}|{password}\n')


# read password and username based on site
def read_password(check_site):
  with open('PasswordList.txt', 'r') as f:

    # ToDo This will only get the last version of the site password as the only return is the last instance of this loop
    for x in f:
      if check_site in x:
        x = x.strip()
        site, username, password = x.split('|')
  
  login_info = f'\nSite: {site}\nUsername: {username}\nPassowrd: {password}\n'

  return login_info

# Ask caller what they want to do for adding passwords
def get_login_info():
  site = input('\nWhat is the name of the site this login info is for: ')
  username = input('\nWhat is the username you are using for the site: ')
  
  while True:
    gen_pass = input('\nWould you like us to generate a random password for you (Y/N): ')
    if gen_pass.lower() == 'n':
      password = input('\nWhat password are you using: ')
      break
    elif gen_pass.lower() == 'y':
      password = PasswordGenerator.generate_password()
      break
    else:
      break
  
  write_password(site, username, password)
    

# Ask user to add or get a password
def password_decision_engine():
  while True:
    print('Type EXIT at anytime to exit the application.\n')
    user_request = input('Would you like to add or get a password? ')

    if user_request.lower() == 'add':
      get_login_info()
    elif user_request.lower() == 'get':
      site = input('\nWhat site would you like the login info for? ')
      logon_info = read_password(site)
      print(f'Your Login info is {logon_info}')
    elif user_request.lower() == 'exit':
      break
    else:
      #ToDo add extra situaions
      break


      
print('Hello welcome to the password manager application!\n')
password_decision_engine()