import requests #Allows us to make a request. Kinda like having a bowser without the browser
import hashlib #Allows us to use SHA1 hashing
import sys

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char #call website and enter password as argument
    res = requests.get(url)
    if res.status_code != 200: #If API doesn't return 200, raise error below
        raise RuntimeError(f"Error fetching: {res.status_code} check the API and try again.")
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines()) #Split the string into a two lists at the ':'.
    for h, count in hashes:
        if h == hash_to_check: #checking tail of hash and if it matches, return count
            return count
    return 0

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper() #Returns string argument as hexadecimal digits. We need it returned in uppercase using UTF-8.
    first5_char, tail = sha1password[:5], sha1password[5:] #Store first 5 characters in first variable, the remaining characters are the tail.
    response = request_api_data(first5_char) #Argument for request_api_data func 
    
    return get_password_leaks_count(response, tail) #Arguemnts for get_password_leaks_count

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times... you should probably change your password.')
        else:
            print(f"{password} was NOT found. Carry on!")
    return 'done!'
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:])) #exit process after file has been run

