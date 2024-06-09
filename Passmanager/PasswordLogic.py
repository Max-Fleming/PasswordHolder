import PasswordGenerator

# write site, password, and username
def write_password(site, username, password):
  site = str(site)
  username = str(username)
  password = str(password)

  with open('PasswordList.txt', 'a') as f:
    f.write(f'{site}|{username}|{password}\n')


# read password and username based on site
def read_password(check_site):

  check_site = str(check_site)

  with open('PasswordList.txt', 'r') as f:

    # ToDo This will only get the last version of the site password as the only return is the last instance of this loop
    for line in f:
      line = line.strip()
      site, username, password = line.split('|')
      if check_site.lower() == site.lower():
        login_info = {"site": site, "username": username, "password": password}
        #ToDo: This now only returns the first entry that matches
        return login_info
      else:
        pass


def delete_password(check_site):
  with open('PasswordList.txt', "r") as fr:
    lines = fr.readlines()
  with open('PasswordList.txt', "w") as fw:
    for line in lines:
      line = line.strip()
      site, username, password = line.split('|')
      if check_site != site:
        fw.write(line + '\n')