
# Slack CLI Browser

A simple Python script to interact with the Slack API to list channels and read messages.

## Prerequisites

- Python 3
- `requests` library

## Installation

Clone the repository or download the script `slacker.py`.

Ensure you have Python 3 installed on your system. You can check this by running:

```bash
python --version
```

If you do not have Python installed, please install it from [python.org](https://www.python.org/).

You also need to install the `requests` library, which can be done using pip:

```bash
pip install requests
```

## Usage

To run the script, navigate to the directory containing `slacker.py` and execute:

```bash
python slacker.py
```

Upon running, you will be prompted to enter your Slack token:

```
Enter your Slack token:
```

After entering your Slack token, the script presents you with three options:

1. **List all channels:** Lists all channels available in the Slack workspace.
2. **Read latest messages in a channel:** After entering a channel ID, it lists recent messages from that channel.
3. **Exit:** Exits the script.

## Features

- List all channels in a Slack workspace.
- Read latest messages from a specific channel.
- Clean exit on user request or interrupt.

## Disclaimer

This tool is for educational purposes only. Ensure you have the right authorization to access the Slack workspace.

## Contributions

Contributions are welcome. Please fork the repository and submit a pull request with your enhancements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

