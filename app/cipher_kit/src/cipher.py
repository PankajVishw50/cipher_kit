class Cipher:
    """
    This Class helps in Encryption and decryption.

    Encryption Algorithm:

    1. Creates a list of unicode value of each letter of key.
    2. Multiply each letter in text with list value in sequence and divide by 2 and stores remainder.
    3. Now append data and remainder in our encrypted data.
    4. Repeat this process until all data encrypted


    """

    @staticmethod
    def format_key(key: str):
        """
        For internal Use.
        returns list of unicode values of characters.
        :param key:
        :return list:
        """
        key_list = list()

        for letter in key:
            key_list.append(ord(letter))

        return key_list

    @staticmethod
    def encrypt(text: str, key: str):
        """
        Perform encryption on given text.

        :param text:
        :param key:
        :return Encrypted String:
        """

        key_list = Cipher.format_key(key)
        index = 0
        length = len(key_list)
        new_data = bytes()

        for letter in text:
            unicode_value = ord(letter)
            val = (unicode_value * key_list[index]) // 2
            remainder = 0 if unicode_value % 2 == 0 else 1

            new_data += chr(val).encode("utf-8")
            new_data += chr(remainder).encode("utf-8")

            # changes index to 0 if index >= length
            # otherwise increment index by 1
            index += 1 if index + 1 < length else -length

        return new_data.decode("utf-8")

    @staticmethod
    def decrypt(text: str, key: str):
        """
        Performs decryption on given text which was encrypted by Cipher.encrypt

        :param text:
        :param key:
        :return String:
        """
        key_list = Cipher.format_key(key)
        index = 0
        length = len(key_list)
        new_data = str()

        text_list = [text[x:x + 2] for x in range(0, len(text), 2)]

        for letter in text_list:
            if len(letter) != 2:
                # This block will only be true when have text which is not encrypted by Cipher.encrypt or
                # text is corrupted
                # In either case method should not raise any error
                continue

            value = ord(letter[0])
            remainder = ord(letter[1])

            value = (value * 2) + remainder
            value //= key_list[index]

            new_data += chr(value)

            index += 1 if index + 1 < length else -length

        return new_data

    def __str__(self):
        return "Performs Encryption and decryption"

    def __repr__(self):
        return "Performs Encryption and decryption"
