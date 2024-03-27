class Account:
    def __init__(self):
        self.key = 426

    def validate_pass(self, input_password):
        """Check if the password meets the criteria."""
        if len(input_password) < 6:
            return False

        has_upper = any(char.isupper() for char in input_password)
        has_lower = any(char.islower() for char in input_password)
        has_digit = any(char.isdigit() for char in input_password)
        has_special = any(not char.isalnum() for char in input_password)

        return has_upper and has_lower and has_digit and has_special

    def encrypt(self, password):
        encrypted = ''.join(chr((ord(char) - self.key) % 256) for char in password)
        return encrypted

    def decrypt(self, encrypted_password):
        decrypted = ''.join(chr((ord(char) + self.key) % 256) for char in encrypted_password)
        return decrypted

