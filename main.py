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
            "content-type": "application/json",
            "Cookie": "__dcfduid=e29ff9f0a82711eebc62cf1c162412e6; __sdcfduid=e29ff9f1a82711eebc62cf1c162412e638629af57e0db6b1439f6cc5f456518cc9d4fad82b8420bce0f245ff23a59c36; __cfruid=352928fe753130f3a5950edf35fe590840ebe5a4-1706113696; _cfuvid=MDIJGTmxV82Hi8hpz.FXXUmwGMOsmZaY59uLDxcQdBk-1706113696006-0-604800000; cf_clearance=n16bVwk5PxN5nADFQ08S30o2SC.09axEfHApNjhN_CI-1706113696-1-AfBhitSqG4xJRrP4XIPnei110abrf6TvDi/lG3DHv8xnLX/cgVc1vMRsr4vd0pieEFvscWPoDSci0Vr7/VCqaQc=; locale=pl; OptanonConsent=isIABGlobal=false&datestamp=Wed+Jan+24+2024+17%3A28%3A22+GMT%2B0100+(Central+European+Standard+Time)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0",
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
