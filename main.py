# Uses PyShark to capture MAC address packets
import pyshark

capture = pyshark.LiveCapture(interface='Local Area Connection* 2')
for packet in capture.sniff_continuously(packet_count=1):
    try:
        print(packet.eth.src)
    except:
        print("No Ethernet Layer in Packet")

#######################################################

import re
import os


def find_mac(file_name, mac):
    with open(file_name, 'r') as a:
        for line in a:
            if mac.rstrip('\n') == line.rstrip('\n'):
                return True
    return False


if find_mac('C:/Users/chanm/OneDrive/Desktop/AuthorizedDevices.txt', packet.eth.src):
    print("Device found in Authorized Text File!")
else:
    print("Device not recognized!")
    from twilio.rest import Client

    account_sid = 'AC5215f4a18bd0462ce9e85a229bbaf4ab'
    auth_token = '2dbf73161cfa7bfb86be73e0f484878d'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="New Unauthorized Device has connected to the Network!!!",
        from_='+12514414835',
        to='+13343181216'
    )

    print(message.sid)

#######################################################
