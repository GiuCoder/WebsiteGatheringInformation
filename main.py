import os
import validators
import requests
import sys
import time
import json
from termcolor import colored
from emoji import emojize
import string


def save_data_to_file(data, file_name):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    file_name = ''.join(c for c in file_name if c in valid_chars)
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"{emojize(':white_check_mark:')} {colored('Data saved successfully.', 'green')}\n\n")


def get_response_data(url):
    response = requests.get(url)
    return response.content.decode('utf-8')


def main(web_url):
    print(f"{colored('GiuCoder Website Information Gathering', 'blue', attrs=['bold', 'underline'])}\n\n")

    # Retrieving IP address
    print(f"{colored('Retrieving IP address...', 'yellow')}")
    ip_url = f"https://api.ipify.org/?format=json"
    ip_data = json.loads(get_response_data(ip_url))
    save_data_to_file(ip_data, f"{web_url}_ip.txt")

    # Retrieving Headers
    print(f"{colored('Retrieving Headers...', 'yellow')}")
    header_url = f"https://api.hackertarget.com/httpheaders/?q={web_url}"
    header_data = get_response_data(header_url)
    save_data_to_file(header_data, f"{web_url}_headers.txt")

    # Retrieving DNS
    print(f"{colored('Retrieving DNS Records...', 'yellow')}")
    dns_url = f"https://api.hackertarget.com/dnslookup/?q={web_url}"
    dns_data = get_response_data(dns_url)
    save_data_to_file(dns_data, f"{web_url}_dns.txt")

    # Retrieving Whois
    print(f"{colored('Retrieving Whois Information...', 'yellow')}")
    whois_url = f"https://api.hackertarget.com/whois/?q={web_url}"
    whois_data = get_response_data(whois_url)
    save_data_to_file(whois_data, f"{web_url}_whois.txt")

    print(f"{emojize(':sparkles:')} {colored('All data retrieved and saved successfully!', 'green')}\n\n")

def valid_url(web_url):
    if not validators.url(web_url):
        os.system("clear")
        print(f"{emojize(':x:')} {colored(f'Invalid URL: {web_url}', 'red')}")
    else:
        os.system("clear")
        print(f"{emojize(':hourglass_flowing_sand:')} {colored(f'Validating URL {web_url} ', 'yellow')}")
        spinner = Spinner()
        while True:
            spinner.update()
            time.sleep(0.1)
            if spinner.counter > 10:
                break
        main(web_url)

class Spinner:
    def __init__(self):
        self.counter = 0

    def update(self):
        symbols = ["|", "/", "-", "\\"]
        sys.stdout.write(f"\r{symbols[self.counter % len(symbols)]} Validating...")
        sys.stdout.flush()
        self.counter += 1

while True:
    os.system("clear")
    print(f"{emojize(':globe_with_meridians:')} {colored('Creator GiuCoder Website Information Gathering', 'magenta', attrs=['bold', 'underline'])}\n\n")
    web_url = input("Enter website url : ")
    valid_url(web_url)
