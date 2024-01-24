import requests
import random
import json
import time
auth = ''
channel = input("Channel ID: ")
def Send(contentt):
    url = f"https://discord.com/api/v9/channels/{channel}/messages"

    headers = {
        "accept": "*/*",
        "accept-language": "pl,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
        "authorization": auth,
        "content-type": "application/json"
    }

    body = {
        "mobile_network_type": "unknown",
        "content": contentt,
        "nonce": random.randint(100000000000000000, 999999999999999999),
        "tts": False,
        "flags": 0
    }

    response = requests.post(url, headers=headers, data=json.dumps(body))
    time.sleep(0.1)
    print(response.status_code)
    print(response.text)
def lol():
    for a in range(int(inpitb)):
        Send(inpit)
def send_message():
    global inpit
    global inpitb
    inpit = input("Message: ")
    inpitb = input("How many messages: ")
    lol()
def send_message_from_file():
    filename = input("Enter the name of the text file: ")
    with open(filename, 'r') as file:
        content = file.read()

    for i in range(0, len(content), 2000):
        message_chunk = content[i:i+2000]
        Send(message_chunk)

    print("All messages sent.")

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Send Message")
        print("2. Send Message from File")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            send_message()
        elif choice == '2':
            send_message_from_file()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")

# Call the main menu function
main_menu()
