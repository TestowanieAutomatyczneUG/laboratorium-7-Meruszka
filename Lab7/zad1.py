class Planta:
    def wiek(self, wiek, nazwa):
        """
        Takes str and int and calculate the age of given platen out of seconds given
        >>> p = Planta()
        >>> p.wiek(1000000000, "Ziemia")
        31.688087814
        >>> p.wiek(2134835688, "Merkury")
        280.8793342399
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


