# Functions for running an encryption or decryption.

# The values of the two jokers.
JOKER1 = 27
JOKER2 = 28


# Write your functions here:
def clean_message(message):
    '''(str) -> str
    Given a message as a string (message), this function returns the message
    stripped of all spaces, whith each character changed to uppercase.
    REQ: len(message) > 0
    >>> clean_message('I am a boy')
    'IAMABOY'
    '''
    new_message = ''
    for index in range(len(message)):
        if (message[index].isalpha()):
            new_message += message[index]
    new_message = new_message.upper()
    return new_message


def encrypt_letter(char, value):
    '''(str, int) -> int
    Given a letter, char and a keystream value, value, this function returns
    the encrypted value of the letter using the keystream value.
    REQ: len(char) = 1
    REQ: value >= 0
    REQ: value <= 26
    >>> encrypt_letter('B', 8)
    'J'
    >>> encrypt_letter('Z', 16)
    'P'
    '''
    char = char.upper()
    max_key_value = 26
    encrypted = (ord(char) - 65) + value
    encrypted = encrypted % max_key_value
    return (chr(encrypted + 65))


def decrypt_letter(char, value):
    '''(str, int) -> int
    Given a letter, char and a keystream value, value, this function returns
    the decrypted value of the letter using the keystream value.
    REQ: char must be uppercase
    REQ: len(char) = 1
    REQ: value >= 0
    REQ: value <= 26
    >>> decrypt_letter('C', 10)
    'S'
    >>> decrypt_letter('X', 9)
    'O'
    '''
    char = char.upper()
    max_key_value = 26
    decrypted = (ord(char) - 65) - value
    # if the decrypted value is negative then add 26
    if (decrypted < 0):
        decrypted += max_key_value
    return (chr(decrypted + 65))


def swap_cards(deck, index):
    '''(list of int) -> NoneType
    Given a deck of cards as a list of integres (deck), and index, this
    function swaps the card at index with the following card. and when
    the index card is at the very bottom it's swapped with the card at the top
    REQ: index < len(deck)
    >>> my_list = [1, 2, 3, 4, 5, 6, 7]
    >>> swap_cards(my_list, 3)
    >>> my_list == [1, 2, 3, 5, 4, 6, 7]
    True
    >>> my_list = [1, 2, 3, 4, 5, 6, 7]
    >>> swap_cards(my_list, 6)
    >>> my_list == [7, 2, 3, 4, 5, 6, 1]
    True
    '''
    # if the index value is the last index then switch it with the top index
    # value
    if (index == (len(deck) - 1)):
            temp = deck[0]
            deck[0] = deck[index]
            deck[index] = temp
    # if not, Swap the values in index and the following index
    else:
        temp = deck[index+1]
        deck[index+1] = deck[index]
        deck[index] = temp


def move_joker_1(deck):
    '''(list of int) -> NoneType
    Given a deck of cards as a list of integers(deck), this function swaps the
    JOKER1 with the card that follows it.
    REQ: deck must be a valid card deck with not more than 2 different jokers
    REQ: JOKER1 in deck
    REQ: len(deck) > 0
    >>> my_list = [1, 3, 4, 28, 14, 27, 19, 24]
    >>> move_joker_1(my_list)
    >>> my_list == [1, 3, 4, 28, 14, 19, 27, 24]
    True
    >>> my_list = [1, 3, 4, 28, 14, 24, 19, 27]
    >>> move_joker_1(my_list)
    >>> my_list == [27, 3, 4, 28, 14, 24, 19, 1]
    True
    '''
    # Get the index of the JOKER1 and swap the cards for its index
    index = deck.index(JOKER1)
    swap_cards(deck, index)


def move_joker_2(deck):
    '''(list of int) -> NoneType
    Given a deck of cards as a list of integers, this function swaps the JOKER2
    with the card following it twice, I.E moves it two cards down in the deck.
    REQ: deck must be a valid card deck with not more than 2 differentjokers
    REQ: JOKER2 in deck
    REQ: len(deck) > 0
    >>> my_list = [1, 2, 4, 5, 28, 9, 10, 18, 17]
    >>> move_joker_2(my_list)
    >>> my_list == [1, 2, 4, 5, 9, 10, 28, 18, 17]
    True
    >>> my_list = [1, 2, 4, 5, 17, 9, 10, 18, 28]
    >>> move_joker_2(my_list)
    >>> my_list == [2, 28, 4, 5, 17, 9, 10, 18, 1]
    True
    '''
    # Get the indec of JOKER2 and swap it with it's following card twice
    index = deck.index(JOKER2)
    swap_cards(deck, index)
    index = deck.index(JOKER2)
    swap_cards(deck, index)


def triple_cut(deck):
    '''(list of int) -> NoneType
    Given a deck of cards as a list of integers, this function swaps the cards
    above JOKER1 with the cards below JOKER2.
    REQ: deck must be a valid card deck with no more than 2 different jokers
    REQ: JOKER2, JOKER1 in deck
    REQ: len(deck) > 0
    >>> my_list = [1, 2, 3, 4, 5, 27, 6 ,7, 8, 28, 9, 10]
    >>> triple_cut(my_list)
    >>> my_list == [9, 10, 27, 6, 7, 8, 28, 1, 2, 3, 4, 5]
    True
    >>> my_list = [28, 1, 2, 3, 4, 5, 27, 6, 7, 8, 9]
    >>> triple_cut(my_list)
    >>> my_list == [6, 7, 8, 9, 28, 1, 2, 3, 4, 5, 27]
    True
    >>> my_list = [27, 1, 2, 3, 4, 5, 6, 7, 8, 9, 28]
    >>> triple_cut(my_list)
    >>> my_list == [27, 1, 2, 3, 4, 5, 6, 7, 8, 9, 28]
    True
    >>> my_list = [1, 2, 3, 4, 5, 27, 6, 7, 8, 9, 28]
    >>> triple_cut(my_list)
    >>> my_list == [27, 6, 7, 8, 9, 28, 1, 2, 3, 4, 5]
    True
    '''
    # find the indexes of the jokers, then find which comes first
    index_J1 = deck.index(JOKER1)
    index_J2 = deck.index(JOKER2)
    first_joker = 0
    second_joker = 0
    if (index_J1 < index_J2):
        first_joker = index_J1
        second_joker = index_J2
    else:
        first_joker = index_J2
        second_joker = index_J1

    # Swap the cards above the first joker with the cards below the second
    # joker
    first = []
    second = []
    third = []
    # if the second joker is not the last card in the deck...
    if (second_joker != (len(deck) - 1)):
        first = deck[second_joker+1:]

    second = deck[first_joker: second_joker+1]
    third = deck[0: first_joker]
    First_Second = len(first) + len(second)
    deck[0: len(first)] = first
    deck[len(first): len(second)] = second
    deck[First_Second: len(deck)] = third


def insert_top_to_bottom(deck):
    '''(list of int) -> NoneType
    Given a deck of cards (deck), this function finds the number on the bottom
    card and removes that number of cards from the top of the deck and inserts
    the cards right before the botton card. However, if the bottom card is
    JOKER2 then the number for JOKER1 is used.
    REQ: deck must be a valid card deck with no more than 2 different jokers
    REQ: len(deck) > 0
    >>> my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,\
    18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    >>> insert_top_to_bottom(my_list)
    >>> my_list == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,\
    18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    True
    >>> my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 28, 11, 12, 13, 14, 15, 16, 17,\
    18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 10]
    >>> insert_top_to_bottom(my_list)
    >>> my_list == [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,\
    25, 26, 27, 1, 2, 3, 4, 5, 6, 7, 8, 9, 28, 10]
    True
    '''
    # find the value of the last card, if it's JOKER2, use JOKER1
    last_card = deck[-1]
    if (last_card == JOKER2):
        last_card = JOKER1
    # Create the top segment by splitting the list up to the last_card value
    # and the middle segment by splitting the list from the last_card to the
    # card before the last
    top_seg = deck[0: last_card]
    middle_seg = deck[last_card: len(deck)-1]
    # Then rearrange the segments
    deck[0: len(middle_seg)] = middle_seg
    deck[len(middle_seg): len(deck)-1] = top_seg


def get_card_at_top_index(deck):
    '''(list of int) -> int
    Given a deck of cards as a list of integers (deck), this function returns
    the card at an index where index = number of the card on top, but uses
    JOKER1 as the index if the card on top is JOKER2
    REQ: deck must be a valid card deck with no more than 2 different jokers
    REQ: len > 0
    >>> get_card_at_top_index([9, 2, 3, 4, 5, 6, 7, 8, 13, 28, 11, 12, 1, 14,\
    15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 10])
    28
    >>> get_card_at_top_index([28, 2, 3, 4, 5, 6, 7, 8, 13, 9, 11, 12, 1, 14,\
    15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 10])
    10
    '''
    # Get the number of the first card and make that the index
    index = deck[0]
    if (index == JOKER2):
        index = JOKER1
    return deck[index]


def get_next_value(deck):
    '''(list of int) -> int
    Given a deck of cards as a list of integers (deck), this function returns
    the new potential keystream value.
    REQ: deck must be a valid card deck with no more than 2 different jokers
    REQ: len(deck) > 0
    REQ: JOKER1 and JOKER2 in deck
    >>> get_next_value([1, 2, 3, 4, 5, 6, 28, 8, 9, 10, 11, 12, 13, 27, 15,\
    16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 14, 7])
    23
    '''
    # Move JOKER1 and JOKER2 then do a Triple cut on the deck
    move_joker_1(deck)
    move_joker_2(deck)
    triple_cut(deck)
    # Do a top to bottom switch on the deck then get the card at the index of
    # the number of teh card on top
    insert_top_to_bottom(deck)
    potential_Keystream = get_card_at_top_index(deck)
    return potential_Keystream


def get_next_keystream_value(deck):
    '''(list of int) -> int
    Given a deck of cards as a list of integers (deck), this function returns
    the keystream value for that deck, repeating the 5 steps until a valid
    keystream value is generated.
    REQ: deck must be a valid card deck with no more than 2 different jokers
    REQ: len(deck) > 0
    REQ: JOKER1 and JOKER2 in deck
    >>> get_next_keystream_value([1, 2, 3, 4, 5, 6, 28, 8, 9, 10, 11, 12, 13,\
    27, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 14, 7])
    23
    '''
    # Generate a new keystream value while the Keystream value is JOKER1 or
    # JOKER2
    keystream_value = get_next_value(deck)
    while (keystream_value in {JOKER1, JOKER2}):
        keystream_value = get_next_value(deck)
    return keystream_value


def process_message(deck, message, mode):
    '''(list of int, str, str) -> str
    Given a deck of cards as a list of integers (deck), a message (message),
    and a mode of ecnryption or decryption (mode), this function decrypts or
    encrypts the message, depending the value specified in mode.
    REQ: deck must be a valid card deck with no more than 2 different jokers
    REQ: len(deck) > 0
    REQ: len(message) > 0
    REQ: mode in {'e', 'd'}
    >>> my_deck = [1, 2, 3, 17, 23, 28, 5, 7, 6, 9, 8, 11, 10, 12, 14, 13, 15,\
    16, 18, 20, 22, 21, 25, 24, 27, 19, 4, 26]
    >>> process_message(my_deck, 'This is quite long', 'e')
    'SQNVMFJIKQFOURW'
    >>> my_deck = [1, 2, 3, 17, 23, 28, 5, 7, 6, 9, 8, 11, 10, 12, 14, 13, 15,\
    16, 18, 20, 22, 21, 25, 24, 27, 19, 4, 26]
    >>> process_message(my_deck, 'SQNVMFJIKQFOURW', 'd')
    'THISISQUITELONG'
    '''
    # First clean the message to get rid of all non-letter charachters
    message = clean_message(message)
    keystream_list = []
    new_message = ''
    # Generate a list keystream values, one for each character in the message,
    # and encrypt of decrypt each character in the message using the
    # corresponding keystream value
    for index in range(len(message)):
        keystream_list.append(get_next_keystream_value(deck))
        if (mode == 'e'):
            new_message += encrypt_letter(message[index],
                                          keystream_list[index])
        elif (mode == 'd'):
            new_message += decrypt_letter(message[index],
                                          keystream_list[index])
    return new_message


def process_messages(deck, message_list, mode):
    '''(list of int, list of str, str) -> list of str
    Given a deck of cards as a list of integers (deck), and a list of messages,
    and a mode of encryption or decryption (mode), this function decrypts or
    encrypts the messages in the list message_list depening on the value of
    mode.
    REQ: deck must be a valid card deck with no more than 2 different jokers.
    REQ: len(message_list) > 0
    REQ: mode in {e, d}
    REQ: len(deck) > 0
    >>> my_deck = [1, 2, 3, 17, 23, 28, 5, 7, 6, 9, 8, 11, 10, 12, 14, 13, 15,\
    16, 18, 20, 22, 21, 25, 24, 27, 19, 4, 26]
    >>> my_list = ['This is quite long', 'Hello', 'colour blue', 'Assignment1']
    >>> process_messages(my_deck, my_list, 'e')
    ['SQNVMFJIKQFOURW', 'VSVDU', 'FPBSBYRWAG', 'WGECYWMRJV']
    >>> my_deck = [1, 2, 3, 4, 5, 6, 28, 8, 9, 10, 11, 12, 13, 27, 15, 16, 17,\
    18, 19, 20, 21, 22, 23, 24, 25, 26, 14, 7]
    >>> my_list = ["Goodbye", "I need lemons", "Honey's sweet", "black"]
    >>> process_messages(my_deck, my_list, 'e')
    ['DWRXQEM', 'TOYJYGMSBXV', 'QTKUWJYSRTI', 'TCQBY']
    '''
    new_message_list = []
    # loop through each message in message_list and encrypt or decrypt it
    # depending on the mode
    for message in message_list:
        new_message_list.append(process_message(deck, message, mode))
    return new_message_list


def read_messages(file):
    '''(file open for reading) -> list of str
    Given a file handle open for reading containing messages, this function
    reads the file and returns its contents as a list of messages without the
    newline character.
    REQ: file must not be empty
    '''
    message_list = []
    # loop through the file, reaidng each line into a list and stripping off
    # the '\n' charachter
    for line in file:
        if (line != '\n'):
            line = line.strip('\n')
            message_list.append(line)
    return message_list


def read_deck(file):
    '''(file open for reading) -> list of int
    Given a file handle open for reading, this function reads the file and
    returns its contents, as a list of integers.
    REQ: file must not be empty
    '''
    deck_list = []
    # loop through the file line by line
    for line in file:
        line = line.strip('\n')
        line_list = line.split()
        # loop through each integer in line_list add them to the deck_list
        for item in line_list:
            deck_list.append(int(item))
    return deck_list
