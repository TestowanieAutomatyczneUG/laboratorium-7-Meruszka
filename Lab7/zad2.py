class PassWord:
    """
    It check if password
    >>> val = PassWord()
    >>> val.ValidPassword("igermMM*!2mafi")
    True
    >>> val.ValidPassword("rrrrr")
    Traceback (most recent call last):
    ...
    ValueError: Za kórtkie słowo
    >>> val.ValidPassword("gsjrnKgui2@3a")
    True
    >>> val.ValidPassword("kowenoaf!fiwnoM")
    True
    >>> val.ValidPassword("opwjfw!damnfKloa")
    True
    >>> val.ValidPassword("Kkkk324$$a3rok")
    True
    >>> val.ValidPassword("gggg")
    Traceback (most recent call last):
    ...
    ValueError: Za kórtkie słowo
    >>> val.ValidPassword("tttttttttttttttttttttt")
    Traceback (most recent call last):
    ...
    ValueError: Nie ma znaku specjalego
    >>> val.ValidPassword("ANDAismefAMidsfni")
    Traceback (most recent call last):
    ...
    ValueError: Nie ma znaku specjalego
    >>> val.ValidPassword("ainfo")
    Traceback (most recent call last):
    ...
    ValueError: Za kórtkie słowo
    >>> val.ValidPassword("ami!3#")
    Traceback (most recent call last):
    ...
    ValueError: Za kórtkie słowo
    """

    def ValidPassword(self, word):
        upper = 'ABCDEFGHIJKLMNOPERSTUVQWXYZ'
        special = '~`!@#$%^&*()_+=-{}[]:;\"<>,.?/\|\''
        if len(word) >= 8:
            if any((c in special) for c in word):
                if any((c in upper) for c in word):
                    return True
                else:
                    raise ValueError("Nie ma dużej litery")
            else:
                raise ValueError("Nie ma znaku specjalego")
        else:
            raise ValueError("Za kórtkie słowo")


import unittest


class FizzBuzzTest(unittest.TestCase):
    def setUp(self):
        self.temp = PassWord()

    def test_password_1(self):
        self.assertEqual(True, self.temp.ValidPassword("faiaOAd1204!@fmaief"))

    def test_password_2(self):
        self.assertEqual(True, self.temp.ValidPassword("smfi#ij1iJoaf!daA"))

    def test_password_3(self):
        self.assertEqual(True, self.temp.ValidPassword("fnwie#in13IN!n"))

    def test_password_4(self):
        self.assertRaises(ValueError, self.temp.ValidPassword, "rrrrr")

    def test_password_5(self):
        self.assertRaises(ValueError, self.temp.ValidPassword, "fnwiee")

    def test_password_6(self):
        self.assertRaises(ValueError, self.temp.ValidPassword, "!@dfaE")

    def test_password_7(self):
        self.assertRaises(ValueError, self.temp.ValidPassword, "$&29fn")

    def test_password_8(self):
        self.assertRaises(ValueError, self.temp.ValidPassword, "ffienwiQW")

    def test_password_9(self):
        self.assertRaises(ValueError, self.temp.ValidPassword, "^1237bsjbffwiubefa")

    def test_password_10(self):
        self.assertRaises(ValueError, self.temp.ValidPassword, "fnseiAAAnvsoewfie")

    def TearDown(self):
        self.tmp = None


if __name__ == '__main__':
    unittest.main()
