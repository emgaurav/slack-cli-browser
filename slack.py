import requests
import json

def list_all_channels(token):
    url = "https://slack.com/api/conversations.list"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        channels = response.json().get('channels', [])
        for channel in channels:
            print(f"ID: {channel['id']}, Name: {channel['name']}")
    else:
        print("Error: Failed to fetch channels")

def read_channel_messages(token, channel_id):
    url = f"https://slack.com/api/conversations.history?channel={channel_id}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        messages = response.json().get('messages', [])
        for message in reversed(messages):
            user = message.get('user', 'Unknown')
            text = message.get('text', '')
            print(f"User: {user}, Text: {text}")
    else:
        print("Error: Failed to fetch messages")

def main():
    token = input("Enter your Slack token: ")

    while True:
        try:
            print("\nOptions:\n1. List all channels\n2. Read latest messages in a channel\n3. Exit")
            choice = input("Enter your choice (1/2/3): ")

            if choice == '1':
                list_all_channels(token)
            elif choice == '2':
                channel_id = input("Enter Channel ID: ")
                read_channel_messages(token, channel_id)
            elif choice == '3':
                print("Exiting.")
                break
            else:
                print("Invalid choice, please try again.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user. Exiting.")
            break

if __name__ == "__main__":
    main()
