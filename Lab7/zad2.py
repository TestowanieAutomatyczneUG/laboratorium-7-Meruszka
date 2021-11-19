class PassWord:
    """
    It check if password
    """
    def ValidPassword(self, word):
        upper = 'ABCDEFGHIJKLMNOPERSTUVQWXYZ'
        special = '~`!@#$%^&*()_+=-{}[]:;\"<>,.?/\|\''
        if len(word) >= 8:
            if any(special) in word:
                if any(upper) in word:
                    return True
                else:
                    raise ValueError("Nie ma dużej litery")
            else:
                raise ValueError("Nie ma znaku specjalego")
        else:
            raise ValueError("Za kórtkie słowo")

