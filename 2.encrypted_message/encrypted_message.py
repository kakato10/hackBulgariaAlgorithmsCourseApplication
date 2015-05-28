def decrypt(string):
    message_info = analyze_message(string)
    alphabet = message_info['alphabet']
    encrypted_message = message_info['encrypted_message']
    times_to_repeat_key = message_info['times_to_repeat_key']
    left_symbols_count = message_info['left_symbols_count']
    key = message_info['key']
    full_key = message_info['full_key']
    key_indeces = []
    for symbol in key:
        key_indeces.append(alphabet.index(symbol))
    key_indeces = key_indeces * times_to_repeat_key + key_indeces[:left_symbols_count]
    real_message = ''
    for i, symbol in enumerate(encrypted_message):
        if (alphabet.index(symbol) < key_indeces[i]):
            real_message = real_message + alphabet[len(alphabet) + alphabet.index(symbol) - key_indeces[i]]
        else:
            real_message = real_message + alphabet[alphabet.index(symbol) - key_indeces[i]]
    print(real_message)


def analyze_message(message):
    proper_string = message[int(len(message) / 2):] + message[:int(len(message) / 2)]
    string_compounds = proper_string.split('~')
    alphabet_length = int(string_compounds[0])
    key_length = int(string_compounds[len(string_compounds) - 1])
    del string_compounds[0]
    del string_compounds[len(string_compounds) - 1]
    string = ''.join(string_compounds)
    alphabet = string[0:alphabet_length]
    encrypted_message = string[alphabet_length:len(string) - key_length]
    key = string[len(string) - key_length:]
    times_to_repeat_key = int(len(encrypted_message) / len(key))
    left_symbols_count = len(encrypted_message) - len(key) * times_to_repeat_key
    full_key = key * times_to_repeat_key + key[:left_symbols_count]
    return {
        'alphabet': alphabet,
        'encrypted_message': encrypted_message,
        'key': key,
        'full_key': full_key,
        'times_to_repeat_key': times_to_repeat_key,
        'left_symbols_count': left_symbols_count
    }

decrypt('o?uin uw?stutnfwat?~413~orwa? thfuisnnrsiu')
