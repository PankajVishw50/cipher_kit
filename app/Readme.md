## [cipher_kit] Module which helps in encryption and decryption

This module helps in Encryption and decryption.

### Encryption Algorithm:

1. Create list of unicode value of each letter of key (key_list).
2. Iterate key_list (i).
3. Multiple text[i] with key_list[i] and store somewhere (data).
4. divide data by 2 and store remainder (remainder).
5. Now append data and remainder in our encrypted data.
6. Repeat this process until all data encrypted.

### Decryption Algorithm

1. Create a list of unicode value of each letter of key (key_list), index=0.
2. Create a list of pair of text (text_list = [[data, remainder], ...]).
3. Iterate text_list (i).
4. 
5. Multiply first element of text_list[i] with 2 
5. Add second element of text_list[i] 
6. Now divide by key_list[index]. 
7. Append decrypted text with unicode character of this value.
8. Increment index by 1 and set to 0 if index >= length of key_list.
9. Repeat this process until all data decrypted.

###  Usage

**How to import**
```python
from cipher_kit import Cipher
```


**To Encrypt**
```python
data = "Data to be encrypted"
key = "Secret key"

encrypted_data = Cipher.encrypt(data, key)
```

**To decrypt**
```python
encrypted_data: str
decryted_data = Cipher.decrypt(encrypted_data, key)
```






