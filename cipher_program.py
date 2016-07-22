"""
Encrypt or decrypt the contents of a message file using a deck of cards.
"""

import cipher_functions

DECK_FILENAME = 'deck1.txt'
MSG_FILENAME = 'message1.txt'
MODE = 'e'  # 'e' for encryption, 'd' for decryption.


def main():
    """ () -> NoneType

    Perform the encryption using the deck from a file called DECK_FILENAME and
    the messages from a file called MSG_FILENAME. If MODE is 'e', encrypt;
    otherwise, decrypt.
    """
    deck_file = open(DECK_FILENAME, 'r')
    msg_file = open(MSG_FILENAME, 'r')
    # Read the deck of cards from the deck_file, and the list of messages from
    # the msg_file
    deck = cipher_functions.read_deck(deck_file)
    message_list = cipher_functions.read_messages(msg_file)
    # Encrypt or decrypt the messages, depending on the mode, using the deck
    new_messages_list = cipher_functions.process_messages(deck, message_list,
                                                          MODE)
    for message in new_messages_list:
        print(message)


main()
