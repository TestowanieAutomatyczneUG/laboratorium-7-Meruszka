class Planta:
    def wiek(self, wiek, nazwa):
        """
        Takes str and int and calculate the age of given platen out of seconds given
        >>> p = Planta()
        >>> p.wiek(1000000000, "Ziemia")
        31.688087814
        >>> p.wiek(2134835688, "Merkury")
        280.8793342399
        >>> p.wiek(9999999999, "Wenus")
        515.0882468309
        >>> p.wiek(9999999999, "Jowisz")
        26.7125653246
        >>> p.wiek(9999999999, "Neptun")
        1.9229221424
        >>> p.wiek(-200, "NAKLEJKA")
        Traceback (most recent call last):
          File "/snap/pycharm-community/252/plugins/python-ce/helpers/pycharm/docrunner.py", line 139, in __run
            compileflags, 1), test.globs)
          File "<doctest zad1.Planta.wiek[6]>", line 1, in <module>
            p.wiek(-200, "NAKLEJKA")
          File "/home/LABPK/smerski/PycharmProjects/laboratorium-7-Meruszka/Lab7/zad1.py", line 47, in wiek
            raise ValueError("Wiek musi byc wiekszy od zera")
        ValueError: Wiek musi byc wiekszy od zera
        >>> p.wiek(100, 100)
        Traceback (most recent call last):
          File "/snap/pycharm-community/252/plugins/python-ce/helpers/pycharm/docrunner.py", line 139, in __run
            compileflags, 1), test.globs)
          File "<doctest zad1.Planta.wiek[7]>", line 1, in <module>
            p.wiek(100, 100)
          File "/home/LABPK/smerski/PycharmProjects/laboratorium-7-Meruszka/Lab7/zad1.py", line 58, in wiek
            raise TypeError("Nazwa musi byc stringiem")
        TypeError: Nazwa musi byc stringiem
        >>> p.wiek(100000, "Mars")
        0.0016848055
        >>> p.wiek(100, "axx")
        Traceback (most recent call last):
          File "/usr/lib/python3.6/doctest.py", line 1330, in __run
            compileflags, 1), test.globs)
          File "<doctest __main__.Planta.wiek[3]>", line 1, in <module>
            p.wiek(100, "axx")
          File "/home/LABPK/smerski/PycharmProjects/pythonProject/main.py", line 28, in wiek
            raise TypeError("Nie ma takiej planety")
        TypeError: Nie ma takiej planety
        """
        if isinstance(wiek, int):
            if isinstance(nazwa, str):
                if wiek > 0:
                    self.dic = {
                        "Ziemia": 31557600,
                        "Merkury": 31557600 * 0.2408467,
                        "Wenus": 31557600 * 0.61519726,
                        "Mars": 31557600 * 1.8808158,
                        "Jowisz": 31557600 * 11.862615,
                        "Saturn": 31557600 * 29.447498,
                        "Uran": 31557600 * 84.016846,
                        "Neptun": 31557600 * 164.79132
                    }
                    pla = self.dic.get(nazwa)
                    if pla == None:
                        raise TypeError("Nie ma takiej planety")
                    else:
                        return float("{:.10f}".format(wiek / pla))
                else:
                    raise ValueError("Wiek musi byc wiekszy od zera")
            else:
                raise TypeError("Nazwa musi byc stringiem")
        else:
            raise TypeError("Zly wiek")


if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'p': Planta()})


