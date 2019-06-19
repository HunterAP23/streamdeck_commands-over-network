# StreamDeck Commands-Over-Network
Send StreamDeck commands to other computers over an internet connection.

# Outline
Inspired from the [Streaming Remote](https://github.com/fredemmott/streaming-remote)
plugin for the Elgato StreamDeck, I wanted to look into sending StreamDeck
commands from one computer to another.
My first idea was to imitate the method the Streaming Remote project used,
which is to use custom webhooks to access OBS and xSplit remotely, but making
a system for users to create their own webhooks would be really tedious.

That's when I came across another StreamDeck plugin, the [Python Elgato Stream Deck Library](https://github.com/abcminiuser/python-elgato-streamdeck) (will be
referred to as PESDL from now on for brevity ), which nearly solves the issue of
allowing users to create their own commands to be mapped to a StreamDeck button.

This project aims to extend the abilities of the PESDL to work on a user's registered devices over an internet connection.

# Objectives
  1. Make secure socket connection between two or more devices.
    * Requires handshaking when connection is made.
  2. Send PESDL-defined command name over the network to another device.
    - Needs security validations before sending command name.
    - Packets need to be encrypted by the sending device.
  3. Receiving device will run that command based on the name.
    - Packets need to be decrypted by the receiving device.
    - Commands need to be validated prior to being run (similar to SQL DB
      validation).

# Requirements
  - Python 3 (prefer newest stable version).
  - pycrypto==2.6.1 for encryption.
  - [Python Elgato Stream Deck Library](https://github.com/abcminiuser/python-elgato-streamdeck) & it's requirements:
    - hidapi==0.7.99.post21
    - Pillow>=5.0.0
The Python package for PESDL is already included in the requirements.txt file.
To install the requirements, run `pip install -r requirements.txt`
