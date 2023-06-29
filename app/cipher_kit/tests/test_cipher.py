import json

from .. import Cipher


class TestCipher:

    def test_basic(self):
        data = "My name is Subhash and i work on great projects"
        key = "9d3f90jfi39320820932jkj302932290i0jiofjijfw0932iifjeojf3"

        encrypted_data = Cipher.encrypt(data, key)

        assert encrypted_data != data

        decrypted_data = Cipher.decrypt(encrypted_data, key)

        assert decrypted_data == data

    def unfixed_key_value_0(self):
        """
        Will generate error due to key being 0
        Will fix in the future.
        """

        data = """
        Once upon a time, in a small village, a curious cat named Whiskers embarked on a quest to find 
        the legendary Golden Fish. Along the way, Whiskers encountered talking trees, mischievous squirrels, 
        and a wise old owl. With courage and determination, 
        Whiskers discovered that the real treasure was the journey itself.
        """

        key = "\x00"

        encrypted_data = Cipher.encrypt(data, key)

        assert encrypted_data != data

        decrypted_data = Cipher.decrypt(encrypted_data, key)

        assert decrypted_data == data

    def test_json_data(self):
        """ Testing if it can encrypt and decrypt json """
        data = {
            "name": "Neha",
            "age": 23,
            "bachelor": True,
            "height": 5.4
        }
        key = "Secret Key"

        json_data = json.dumps(data)

        assert type(json_data) == str

        encrypted_json = Cipher.encrypt(json_data, key)

        assert json_data != encrypted_json

        decrypted_json = Cipher.decrypt(encrypted_json, key)

        assert decrypted_json == json_data

        obj_data = json.loads(decrypted_json)

        assert data == obj_data

    def test_various_keys(self):
        data = "Who knows what can happen"
        key = "#StrongPassword_1000x"

        encrypted_data = Cipher.encrypt(data, key)

        assert encrypted_data != data

        decrypted_data_with_wrong_key = Cipher.decrypt(encrypted_data, "#StrongPassword_999x")

        assert decrypted_data_with_wrong_key != data

        decrypted_data_with_different_case_letter = Cipher.decrypt(encrypted_data, "#strongPassword_1000x")

        assert decrypted_data_with_different_case_letter != data

        decrypted_data = Cipher.decrypt(encrypted_data, key)

        assert decrypted_data == data

    def test_unencrypted_data(self):
        """
        In this test we are providing non encrypted data to see how
        our module handles it.
        """
        data = "Who knows what can happen"
        key = "Very strong key"

        encrypted_data = Cipher.encrypt(data, key)
        assert encrypted_data != data

        decrypted_data_with_non_encrypted_data = Cipher.decrypt(data, key)
        assert decrypted_data_with_non_encrypted_data != data

        decrypted_data = Cipher.decrypt(encrypted_data, key)
        assert decrypted_data == data
