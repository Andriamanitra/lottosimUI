# Lottosimulaattori!
#
# Tässä pelissä voit lotota.
# Valitse ensin numerot numeronappuloita klikkaamalla ja haluamasi
# animaatiotyyppi pudotusvalikosta. Kun olet valmis voit painaa
# "Aloita arvonta" aloittaaksesi arvonnan. Valikon kautta voit muuttaa
# pelin asetuksia kuten numeroiden määrää ja ikkunan värejä.
#
# Tarkemmat ohjeet löytyvät pelin sisältä valitsemalla
# Ohje -> Näytä ohjeet

from tkinter import *
from tkinter.messagebox import showerror, askokcancel
from math import factorial as fact
import random
import time


MAX_NUM_LKM = 400  # Maksimi numeromäärä joka voidaan asettaa asetusten kautta
NUM_LKM = 39  # Montako numeroa (ja numeronappia)
VAL_LKM = 7  # Montako valitaan?
ARV_LKM = 7  # Montako arvotaan?
OPTIOT = ["Animoi arvonta", "Näytä vain tulokset", "Ei animaatiota"]
TERWETULIAISTEXT = "Tervetuloa Lottosimulaattorin pariin!\n"
OTSIKKO = "LottoSimulaattori v1.0"
PALETTI = "#EDEDED"
BUTTON_HL_COLOR = "red"
SPD = 4
# Pari ohjelman toiminnan kannalta elintärkeää
# kuvatiedostoa base64-encoodattuna:
KUVA1 = """R0lGODlhAAGrAPcAAAgHBBIQCR0jJhk4OyYeHjw3HSclKCY8Ii01ODQvKDs3OTBINy1pPjdsMDpwLTZ2OxRCRRdPUBtaXBheYBRmXht0Xgx3ehZoaRdtcBh5ZRV2dydLTSlPUSZYWjVLTDdOUTZWWCdeYTdeYCpuRCt5SSFzVSllZyNucCpvciVydDdlZzJzdkE7K0U8PEE+QEdaGklHOU1aLExWMFNMKVFdL1VaOE15G1NqG1p3GEl8JFVnKFhkN2RcO2B9Gm1kO2N5J2Z7MHNpP39zP0pGR0pOUEVSU0dXWUVZXEtUVUlXWEtaW1VISVBOUVVXR1dWWEdeYF5eYFpkQ11hVUFhY0RmaEJqbEtiZElnaU5oa0VtcEtzdFdlZ1dxc2BNTWBPUmRVVnJbW2BfYWFpR2NnWGhySW50XHJqRWRjZGRmaGNpa2hkZmhnaGttZWtqa2ttcG9zZmt2d3ZmZ3BvcHJ0a3d3eA1/gRZ/gSN/gnp+gA6GfxaEdRuXflyFEGWKDWSHFGqSC26TEnSfCnGXEWeEIHinCXyDbQyHiQuOkAqRjwuSlAqXmQybkwmamxOChBKGiBGLgBKKjBiFhhyJiRCTiBCTlQmeoAqhnQioqAausAWztAa6ugiyswm2uAi7vCWAggS+wAXDwwTLywjDxATP0ATT0wTX2APb2wLf4ALi4wLn6AHr6wHv8ALw7wD09AL49wD+/n2ChIB1P4V5QoNoaId4eJZ3d4F/gICvCYa5BouASZOGTJ2RUIOEf6iaVa+hWbusXYvBBZHKBZvYA6DeBaboAa3yAbX+AMCwX8i4Y9C/Z9LBaIeHh4+OkI6QkpCOkJiYmJ+foJ+goaeEhKCfn7KNjbyVlaCfoKCgn6SkpKemqKinpqinqKiopquqqq+vsLCurrCvsLCwrrOzsre3uLi2tri3uLi4t7u7ur+/wMWcnMmgn82iosC+vtKmpui6usC/wMDAvsPDw8fHyMjHxsjHyMjIx8vLy8/P0NDPz9DP0NDQz9TU1NfX2NjY2PzJyQAAACH5BAEAAP8ALAAAAAAAAasAAAj/AF8JHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePIEOKHEmypMmTKFOqXMmypcuXMGPKnEmzps2bOHPq3Mmzp8+fQFuqYhSpUaigSJPSLHWkXL99bTYpnUo1JSor+/o97YeGVNWvYD+eiKd1X1Z7U1aFXct2YqtG2PZ1a7NkCbZ+3Ri13ctXIaS4c+Kka7duiD1+bkz1XbxY1LJ9dMC0m9xOGp1+8Uww3tz2xL5ncShTXqIVVinOqKuigmOvhWjKs55hdpS6dlIN9uhIez05nROtWFqVRKXKtnGLrtbsW8Kb8pd5/ZYpFqlqAhQnGoQf3/6w07Nvs5pP/7bcT5zUkJdAOHFyZpkh7vAZOspNTfzkJfvIcQKJKoSLJbW08wUt78Vn4EEr7OOEfZPNIg47kHwEygctDDZZLXQUeOCGr7SyhT1dMNhOOl/0c4R2GrWSiBMwqCMaGHRcwiGH3j0ToIhfiNMNBhuZcsEXLrhI2TottIHKjBs2gs8X64jYTjVOdCMHJhmZ8sEyzL1WyxknImkgK1vwk6WTXzyDDQgYXfLBM0NUw1sL7nlpICjPiPOFk5NR0wI2MVZEygVpsOnma9KcsUVxcsKnAVQW4gkjNgioIKmkImiQCaIIkaKBE8+wuRtvSyxzQaLwedgankPuicYy2LTqKh1HWP9wZEGhSHCGmVg2+toQdIhCKneq0KEbqpTFEcczTriqLDbPFKGBJqFckkgHZ7j6zBJNNldLHB248ut2pNAxJrFEImvmsq5OI+wy57Y6zRC6vtZCn98al4oJzoRHbi1fDLHMMtWiK7CyS9Qn3pZo1mtbKx3Es8ygTqozyxJ0tLvGwBjToW9z6bTghowK13aJbA/jWcsQsGSD8crKOpFtc18sw2PItanATz82iljNF22w7LOrd4qXjgJnHEUzaqtsodU7TDB4crs/r6zNguJRPMXRqakCh1Y4b/zaF2pELfYatbzcG8XYiIA10ltz/YXBon1Bh9h0y7HEp+08jc00o66wvZnWXGM2bjpL0KIy3XSf4cQXPLu6DMh+L+Zh4Pjkug41S0CNeNTaoJsNHZ1EvpkKWfVTT6vLrKeG5pu33uoZs4reVyP29GOPsp27rvuyT8jO2CXz7PPN7gN/ww023ZyDuAS+L3YJOfEQ76o2x3eDzTzxdGPW8VEvo1fzfIHSjTi5E8/NPvHIZVZW+3D/Mwgogs9WKLIpT/czdKyBhhqrYqNN6fpg31POkb7orawNkJP/H1tSAYt+2C9qdEhAL5BBQWQEoVr6CJwGn8KOlT1DAwrkiyoaeLuoPUMBu1CGMpLxixXWgA6122DgOoixD2AqhGsZYT/4UT6fnQEZKpQFAFToAwWQRYaBm8fAvNeQVajiiVBURfxwSBPA9aOHLPuhCmcwRGXooj1I5Jpc8FcxZdFBA5dABSpawUZVnCITl9DABULgBCjY8Y5QMAIILgAJSKTxhlRsSZgwY72faVEZPiiACn+huDBq5Rsw4EEvesGDubXqGW1YRhugYAUldDKT7NqGzzoFMCV0oAONSGMgV3IFMQ7PZ8swgwqTAURlICMMTiidDPfRhF/0QoXK4MEz/zr3DChID3eXXAYSOqDKVZpEBLp8IMucoAtgqrAXdDjDEWUoDlnIIgDJsCULhnDJMBwTY89IXQcYcQpnjiRBWonHNXzWuWs4IRe1REYN/iUbJNLhF7EAQDiR4YTUdcqc50SXNg6HjdRpoJ3u/Ag88YI4OgzBDGbwlzbYhURe0lIIi+wZu4qZ0J89gwiJiKhHJroPe5CjddXjqAy7IctZIgMG9rCfsEoKQQl4RaUaScHNAicOxHUDHucQhzjAgcRzwGCSuhDDEo7YwTA8o5A8ZdkzkCAroGJkolwrIT3rcQ5d6lKG9OiUOeixw7J0g5xZFdtWDRE7r0oErFrhRzh+dv/EszryKUPV4DkCFlexLaMIhpiiXRuCV60UFWPf6AY7/kpZDaazsJtbxgYysViICHWD+8CHPawnDnNwQxwt9WtlKcsuzLbOCQnsrEKeEFiuDdUsgVUtEvPRDVrYgl3p061WCOtaxCFhOrJNyCaeUVvQrjZw3fiCNNzhD3e0YxZxuIwM7ZGs4m7uGR1IbkJUcQThPleGePCHeter3jUg8V/ebR0dUipeg1BCHI7cB2rPq5VlUJe96lXDdofA0PjSDQR1rS8qBulIg5pXhuwY0H/9IY1kyVAOrDOwSftWX4FoYJv5Td2DN9gNAxBAve4wTHNt110Nbw6BHX5FKNq2WnH/tIG/8XBBO9zxBXTssj0udh0IANnZEODjvPygwzJiuNp98ArEgcNfkF3nDA7LNhF34a9cLFxZe3C3rRqEDHGnjLg2cFa2qtjCiMO4DzQ8w6/7OEen5jwEAzB3g+dwgiXJLGQiqzQR+OWvbfehSSbjhQ7iOIeiF32GNph1GUzIMJ/lCsLOKkHQGrxZnh+TaX54eqjdOGKe9zxp3RXBz840BR4wvUF+7AMbBTV0R58R6VJLL052ZYRTWI1EWGcZifEoaJzFUWBbbw5+djWErHktxn7QwQnn2KA43HAGeYD5scbe3Ea/B9Q7MPuv8WhDGZlBbTrEw9NhzbburhFer6JgxM3Mzt74hIuPcmBV3WLTBr1UWoVvn/fBcsE34q6hGaBmwd8If4rAN7cF5LpTaQn/tquxvfBRttudpFhGxP0d54qLbb4RpdPGvy1Wj/8Mxs68RLRHzmyKm5xlRABFylfOclZL8+Us88BPqfiJftYc0y7HOTo9gGrfoYIOK/55ZW8udHR2QLHgg6bStRz0pi+x0jhkRDamfl4aWv1nGaKiKp4Ab67bDotfx5gTjBbCQ3TD7DVOe9Q+kODmTQ7ulL233NE5Aaj/y84Qv8b7dvceNVoogoogKLvS3Ud4liFh5/IDhcYFL0NzNN6kHPC76EhHeQ3GA+2X95yocHiJwFO+5JidRhyKrWE4xNZ3ae481wzoWm6Iu9RDYDv4MLBsuDM9Y5LWKlwnDd6ir20Tb+98wCFoC/myqtTaKL78VqP8vcp1zFEbgjWyPXr5cV7wtP9ZN5C1OTr0zHXaCODv5ash3ymC5nBHvc+gcQa9+6zFm9tvVsTxfOIlwfg0Qz+dZ31REw34FzUHCFnxYA/rI0BaYQ8KcEzS5zut8H1453U/Aw3GhDgJiC6hVlkDcH7E8wzM0zy4QXnhN0odyDKZtDLaU1nxYAgX/xB8dEMHFtA8pqBdgrd+AoNJjGdSwycwvcdNl1AKSHBOZ0BfsmOBeDdaYNd/NSiCy1JWq0UOMnIJ2Oc6Seg7kDCEU6df96c7Q8A6+1VjIKMBULg7baCEfiN5svcU06As45M+OXUOQYg4yHJawWMW/FUOINMKF5CGupMGbLg2VDBy6UNZccYO5wAPfLgVtpOFYjMEfYVp4wA5gCiIrgNykXOCEQdDWrZB9iCFmeVzmIYO7ZeJ0vM/z3ABmvcrlQB//vYMsohp5+AGu4NJ36YCBdEKE6CJdINf/CAOICBzWJNxG1cn/gZfy3I+XENWP9gy3wYLkNchGCCJUUNz9gAL7f+nMKqQBht3DjrIagqSDePjZY8YZgNDa4onQ/OAdQSRHsDoM7KYNpVwNJ/1V+noSLnxbYOViLfVawOjZO24QXQwCgfRCnVwK9oma6/WAZnwihxCCVC2XWewZqP4bctQi2FEgOiyBniQdKtlD7yIEKAAAjSIMVBmFthgBYYQChK5EFHEF+FSWf8yYgrCbAqyj/m1MmvAaayGDY0wXhdAamIDZa6GPsuwBWgEgL14CSEAB1IJBybglEihAqu1DLYwYo7Ga/EwAClgAm+miEqEMZlUkGIEC2eGEBpAitmoW66GD9GQBibACLqHEJqAkul4DlYWFolQkbsEDXRgXpCBllz/8wxnlgiTl3crcwa2wGv7kAZ3WRCZsIIsow1euENxtgwgkAKXcAmZEAqkIJqgkAgqAJSBww9wUHdVkQmmF0ZJZoobtAyAuVppgCJwsXTTFGiYZg/IlhCa0AEpOTDi4IU3czPoEw/iMGedIg/mdQ7cFhZH91yQMZi9JpvntQIEwTCZ+Ugrww3IYphacQ7weBCmEAHzyDLdCViamZSUZQ8R0hatRJ3dUFDywCduoAIrsAU2Ro4pUBCmoGaOlIIDk0vMBguT2YsXYDibEw7i+VfwuRcmIGj7AA4IcAmYggodMASsFoMGcQl4YF5Vhy5jyGz2UHAK0QoagI0sg1oN2IBe/xmfbDEfgqYPM0MQqCAAtflX2bCWBMEIqKlBr8QyJgACIrlaXOAQl+ABw0k3Fbk+jpRkDhcWpSdo2OCjA2EI2FlZz6AJCHEJaKBbGIgxdRkNzJakDqGhRkk8R1YW9vBYXogNhRgWrTCOWTmlAmEKy3CkYUQHRacJR7Bsy7cymmECvCloz5CgCVEJStCkP7Nf9jCkraJb+5AwfAFx57UFCOEKmHpeVbAQGupjYWZ/rrINzzCUqhACO/pX2GCMD+EjW+CoPkOqFckPy+Cqe8GElYWmB9Gpq3UO3XgQqtAworgyjyMQqgAC6ylD2OClEmEKFlAE6bk7tSiUjPGXSFaSvf8qaNDgrKDqq5ixMkWAIqigrIImDq/3EK1wCEcwra5zDjEkF325F5fAVM/FD56AENTHX1sQkwIRCYb2ahiDawNhCuZ6XucwpxHRCowAAmXEUwvYBnnAGXrKX/l6EIxwqF02rwlxCSBGqq4yZAZRru0YDworEa0ACoYwAXoWh7ozfgCjAhqAkJwRLBaLEHVQkFf6EB6bbhjzMQixXAh7shWhCptgAerBDC9mAmiEp5vBBTd7EErAp6D1mwxBCmTHNSDLLDd6ECawrPFEtBihCtOiZ+vCnGjbKbAFH1h5XhdbEKSwaufloQ1xCR8yVPKnLAimEKFgp46UsCShCqEwuJdroAiKsAiJsAiLwAiIu7hYahwr8G/lKRCisKUNVo3CegHNcFYE6ioopxAmUHYmG2MFoasDGqyvwAhsRZ0h0BAXUIvr14oNoQmL+VfoILZXJqqVNQ+HcBAX0I7icI8MwWBENTAe4LQH0baUBbj/pDsQIrda8dC7BtFv50UHrFkQjLClVbdvDJECq5WozTsQqOAGz7WzBYEKN0ad2poQmQCOMlQO6EKCnpWV/rpYoUu1WvEMuCoQo3Bn0BsJCxGgIsl0aYC5CuG9uxq+BIEJGhtGcKBYDHxe0rEQHxZGZaksF+cQE1pZKKrAeoq//cCrBFEJ8ECd/aoQtHukKXisEKEFq9XBOeFGpnAKppAJmZAIiJDDOkynVoCkByEJimcPkysQwmG3D3ZzVrsQbQSuMhQP2eEWbBTFUjzFrWAKpEAKmYAJn6nFn5kHeqAHGUACDmADOUDGZpwDfEAIakwIwBAMwkAMxQDHxEAMRNwK/08ULYqbxxmwx3zMx4+wCJYwuII8yKQQRU9ExYg8xRARuhz8w4r3DF+cASPwAAwAAZYsABvQQH9FcW1AAXn8yYswCXtcAg9QyjjgBzjgt9z0AnxQyhWQAZOQx5cwyNECxhXwADjAB7q8y7zMy37wB7iAC8AgDMRczG9sDMZQDMi8zMzczM7MzCUwAmXcB31ACG88x3OszM88x8IQzN7szcBACH8wzn8ACHyQA+iczuq8zuncACVQAnowCbGcCaSgRvasRp6YXxagCsRBEED8XHNwzMZACFLwDPFw0MtKgM8QA9jc0Nj8zMYQDJarQeKAC83c0MIADBqt0QIN0R790f8gHdIiPdIkXdIfLcfEIAxrvNKEcAPruQ8HgAOE4AcNoAd7oAcLUHb7EAXLjAtBCr2eGwwmbQy4kHybbNFDndRKvdRM3dROjcyE0MAbpA998Mx+oHhAgMzC0ASGWULO8AJJjQPLCg5I/dRmfdZondYiDQwTrbWB8MyDUHb20APGQAxNkEG9iQ1jgAPaXNLEMAYgXNFqPdiEXdhOPQy1i0TOMAzOTAxOAMIO9NYxcBisVg9OUNYlLQw1sKpRJtSG/dmgHdrPXNSU5QzC4Mx/wJFI1A3C3Nb6OAbAMNTCkMoMuFrOQAyindu6TdjEIAM4+QyM3cxc/Vx0QAzBkNjPZQ//UoDZIn0LNIAHYMs1y4Dbu13d1r3UwiAD58Za1L3MwqDKYTQGyKwDcfFv3bADp03SxRADYwnZXPMG1x3f8h3SxOAHdJAP35vey4wDnB048YADy0wINWDU+kgHfjDUfiDVlaUPOjDfDv7gde0HbGAO7m3azCwIyO1IbNDdyewHrv0Uyz3UxJC+mAYOhADhKG7dwNAE41CQi73MHn5e+ADgzowDY7lL4gADsT3U/M1rxZ3iQC7agPDTq8UM6X3c/NUNJ/7MhBAFc9AN3bAMY7ADOlDlfdDXJj0GvHYONB7kXk7YgPDhYTTdyNwD/a1B+rADJx3MwoDlS10MbGBzMsDh/19e52b9G7xWCMus5YJGBrsdBe1oD5+jA25u54a+1MTAC8ym58YgDBlOWX6u24Tw6GE1fnNA5bhA54e+6UlNDJReWYwuDGK+QZGu2ziwkQcdPcJyBmLwAzLN3Jwe60rt6V6p5hE96hpk67sdDOQMzHAs68B+1p7ejko5BzpA3VEtaPbQ5cHe7M6+zH/dZA5TA33Q0XU9BsWJjvooDk6g38/+7cHeB0rmDHXiZfdgFvGwDVOuA33g2c+s0j3gBz8wBi8oRi11DtvQBH+g6eDe75uOzcIQCH6AylWOA5ku4oRAA2Ww8GVA5a9e6P4e8RKf1MoM8RN/8Rif8Rq/8Rzf8Qwe//EgH/IiP/IiHRAAOw=="""
KUVA2 = """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"""


class LottosimUI:
    def __init__(self, val_lkm=VAL_LKM, arv_lkm=ARV_LKM, num_lkm=NUM_LKM,
                 nopeus=SPD, paletti=PALETTI, button_hl_color=BUTTON_HL_COLOR):

        self.__ikkuna = Tk()
        self.__ikkuna.title(OTSIKKO)
        self.__ikkuna.minsize(450, 400)
        self.__ikkuna.tk_setPalette(paletti)

        # Olion attribuutit
        self.__val_lkm = val_lkm
        self.__arv_lkm = arv_lkm
        self.__num_lkm = num_lkm
        self.__suosikkinumerot = [i+1 for i in range(self.__val_lkm)]
        self.__valitut_numerot = []
        self.__nopeus = nopeus
        self.__fancy_colors = False
        self.__paletti = paletti
        self.__button_hl_color = button_hl_color

        # Valikot
        self.__menubar = Menu(self.__ikkuna)

        valikko = Menu(self.__menubar, tearoff=0)
        valikko.add_command(label="Uusi", command=self.reset)
        valikko.add_command(label="Lataa suosikkinumerot", command=self.lataa)
        valikko.add_command(label="Tallenna suosikkinumerot", command=self.tallenna)
        valikko.add_command(label="Asetukset", command=self.asetukset)
        valikko.add_separator()
        valikko.add_command(label="Poistu", command=self.__ikkuna.destroy)
        self.__menubar.add_cascade(label="Valikko", menu=valikko)

        view = Menu(self.__menubar, tearoff=0)
        view.add_command(label="Päävoiton todennäköisyys",
                         command=self.näytä_todnäk)
        view.add_command(label="Todennäköisyystaulukko",
                         command=self.todennäköisyystaulukko)
        view.add_command(label="Kissa", command=kisu)
        view.add_command(label="Koala", command=koala)
        self.__menubar.add_cascade(label="Näytä", menu=view)

        ohje = Menu(self.__menubar, tearoff=0)
        ohje.add_command(label="Näytä ohjeet", command=ohjeet)  # TODO
        ohje.add_command(label="Tietoja", command=tietoja)
        self.__menubar.add_cascade(label="Ohje", menu=ohje)

        self.__menubar.add_command(label="Fancy colors!",
                                   command=self.fancy_colors_on)
        self.__menubar.add_command(label="Palauta värit", state=DISABLED,
                                   command=self.fancy_colors_off)

        self.__ikkuna.config(menu=self.__menubar)

        # Graafiset elementit:
        self.alusta_widgetit()

        self.__ikkuna.mainloop()

    # Nimensä mukaisesti alustaa graafiset
    # widgetit - ei koske muihin muuttujiin
    def alusta_widgetit(self):
        textframe = Frame(self.__ikkuna)
        textframe.grid(column=0, row=0, columnspan=3, sticky=N+S+W+E,
                       padx=10, pady=10)

        self.alusta_numeronapit()

        self.__scrollbar = Scrollbar(textframe)
        self.__tekstikenttä = Text(textframe, yscrollcommand=self.__scrollbar.set)
        self.__tekstikenttä.insert(END, TERWETULIAISTEXT)
        self.__tekstikenttä.config(height=8, width=50, state=DISABLED)
        self.__tekstikenttä.pack(expand=1, fill=BOTH, side=LEFT)
        self.__scrollbar.pack(side=LEFT, fill=Y)
        self.__scrollbar.config(command=self.__tekstikenttä.yview)

        # Tämä varmistaa että  asiat venyvät kivasti:
        self.__ikkuna.grid_rowconfigure(0, weight=4, minsize=120)
        self.__ikkuna.grid_columnconfigure(0, weight=2)
        self.__ikkuna.grid_rowconfigure(7, weight=2)
        self.__ikkuna.grid_columnconfigure(1, minsize=180)

        self.__valitse_numerot = Label(self.__ikkuna)
        self.__valitse_numerot.config(text="Valitse {0} numeroa"
                                     .format(self.__val_lkm))
        self.__valitse_numerot.grid(row=1, column=0)

        self.__arvonta_label = Label(self.__ikkuna)
        self.__arvonta_label.config(text="Kuinka monta arvontaa?\n"
                                        "(0 = pelaa päävoittoon saakka)")
        self.__arvonta_label.grid(row=1, column=1, sticky=S)

        self.__arvontojen_lkm_valinta = Entry(self.__ikkuna)
        self.__arvontojen_lkm_valinta.config(justify=RIGHT)
        self.__arvontojen_lkm_valinta.insert(END, "1")
        self.__arvontojen_lkm_valinta.grid(row=2, column=1, sticky=W+E, padx=10)

        self.__anim_var = StringVar(self.__ikkuna)
        self.__anim_var.set(OPTIOT[0])  # default
        self.__animaatioval = OptionMenu(self.__ikkuna, self.__anim_var,
                                          OPTIOT[0], OPTIOT[1], OPTIOT[2])
        self.__animaatioval.grid(row=3, column=1, padx=8, sticky=W+E)

        self.__pelaa_nappi = Button(self.__ikkuna, text="Aloita arvonta",
                                    command=self.arvonta, state=DISABLED)
        self.__pelaa_nappi.grid(row=4, column=1, sticky=S+E+W+N, padx=10)

        reset_nappi = Button(self.__ikkuna, text="Resetoi peli",
                             command=self.reset)
        reset_nappi.grid(row=5, column=1, sticky=S+E+W+N, padx=10)

        lopeta_nappi = Button(self.__ikkuna, text="Lopeta",
                              command=self.__ikkuna.destroy)
        lopeta_nappi.grid(row=6, column=1, sticky=S+E+W+N, padx=10)

    # Tää tekee numeronappei!
    def alusta_numeronapit(self):
        self.__numframe = Frame(self.__ikkuna)
        self.__numframe.grid(column=0, row=2, rowspan=6,
                             sticky=N+S+W+E, padx=6, pady=6)
        numlev = int(self.__num_lkm**0.5)
        numkork = int((self.__num_lkm / numlev)+1)
        self.__num_napit = []
        i = 1
        for y in range(numkork):
            Grid.grid_rowconfigure(self.__numframe, y, weight=1, minsize=30)
            for x in range(numlev):
                Grid.grid_columnconfigure(self.__numframe, x, weight=1, minsize=30)
                uusi_button = Button(self.__numframe)
                uusi_button.grid(row=y, column=x, padx=2, pady=2, sticky=N+S+W+E)
                uusi_button.config(text=str(i), bd=4,
                                   command=lambda a=i: self.valitse_numero(a))
                self.__num_napit.append(uusi_button)
                i += 1
                if i > self.__num_lkm:
                    break
            if i > self.__num_lkm:
                break

    # Valitsee parametrina (int) annetun numeron (mikäli numeroita ei ole
    # vielä valittu tarpeeksi) tai poistaa sen valinnan.
    def valitse_numero(self, x):
        # Poistetaan ensin mahdolliset korostukset edellisen arvonnan jäljiltä
        # kaikista numeronapeista
        self.reset_buttons()
        self.__ikkuna.update_idletasks()

        if x in self.__valitut_numerot:
            self.__valitut_numerot.remove(x)
            self.__num_napit[x-1].config(background=self.bg_color())
            self.päivitä_valitse_numerot()

        elif len(self.__valitut_numerot) == self.__val_lkm:
            pass

        else:
            self.__valitut_numerot.append(x)
            if self.__fancy_colors:
                väri = fancy_color()
            else:
                väri = self.__button_hl_color
            self.__num_napit[x-1].config(background=väri)
            self.päivitä_valitse_numerot()

    # Päivittää labelia joka kehottaa valitsemaan numeroita
    def päivitä_valitse_numerot(self):
        val_lkm = self.__val_lkm-len(self.__valitut_numerot)
        if val_lkm == self.__val_lkm:
            self.__valitse_numerot.config(text="Valitse {0} numeroa"
                                          .format(val_lkm))
        elif val_lkm > 1:
            self.__valitse_numerot.config(text="Valitse vielä {0} numeroa"
                                          .format(val_lkm))
            self.__pelaa_nappi.config(state=DISABLED)
        elif val_lkm == 1:
            self.__valitse_numerot.config(text="Valitse vielä yksi numero")
            self.__pelaa_nappi.config(state=DISABLED)
        else:
            self.__valitse_numerot.config(text="Arvonta voidaan aloittaa!")
            self.__pelaa_nappi.config(state=NORMAL)

    # Tulostaa tekstikenttään
    def puts(self, teksti):
        self.__tekstikenttä.config(state=NORMAL)
        self.__tekstikenttä.insert(END, teksti+"\n")
        self.__tekstikenttä.see(END)
        self.__tekstikenttä.config(state=DISABLED)

    def arvonta(self):
        self.reset_buttons()
        toistot = self.__arvontojen_lkm_valinta.get()
        tyyp = self.__anim_var.get()

        # Virhetilanteiden tarkistukset ja vahvistukset
        try:
            toistot = int(toistot)
            if toistot < 0:
                raise ValueError
        except ValueError:
            showerror("Virhe!",
                      "Virheellinen syöte \"{0}\"\nToistokertojen täytyy olla "
                      "positiivinen kokonaisluku tai 0.".format(toistot))
            return

        # p_taulu[i] sisältää tiedon kuinka monta kertaa keskimäärin
        # saadaan i oikein valituilla toistokerroilla: tätä hyödynnetään
        # kun päätetään halutaanko tulostaa arvonnan tulos näytölle
        p_taulu = [todnäk(self.__val_lkm, i, self.__arv_lkm, self.__num_lkm)
                   for i in range(self.__val_lkm+1)]
        if toistot != 0:
            p_taulu[:] = [p*toistot for p in p_taulu]
        # Toistoja päävoittoon asti..
        if toistot == 0:
            p = p_taulu[self.__val_lkm]
            # 1) ..ja päävoiton todennäköisyys 0:
            if p == 0:
                showerror("Idiootti!",
                          "Näillä asetuksilla et voi ikinä voittaa päävoittoa.\n"
                          "Valitse positiivinen arvontamäärä tai muuta asetuksia.")
                return
            # 2) ..ja todennäköisyys mitättömän pieni:
            elif p < 1/500000 and not\
                askokcancel("Oletko varma?",
                            "Haluatko varmasti pelata päävoittoon asti?\n"
                            "Peli saattaa kestää useita minuutteja."):
                return
        # Toistoja yli 9 ja animaatiot päällä:
        if (toistot == 0 or toistot > 9) and (tyyp == OPTIOT[0] or tyyp == OPTIOT[1])\
                and not askokcancel("Vahvista aikeesi!",
                                    "Haluatko varmasti pelata näin\n"
                                    "monta kierrosta ({0}) animaatiot päällä?"
                                    .format(toistot)):
            return

        # Tarkistukset suoritettu: arvonta alkaa
        self.__pelaa_nappi.config(state=DISABLED)
        numerot = [i+1 for i in range(self.__num_lkm)]
        omat = self.__valitut_numerot
        päävoitot = 0
        i = 0
        # Tallennetaan arvonnan alkuaika
        t0 = time.time()
        self.puts("Arvonta aloitettu..")
        self.__ikkuna.update_idletasks()

        # Ei animaatiota
        if tyyp == OPTIOT[2]:
            while i != toistot or toistot == 0:
                i += 1
                arvotut = random.sample(numerot, self.__arv_lkm)
                oikein = len(set(omat).intersection(set(arvotut)))
                if oikein >= len(omat):
                    päävoitot += 1
                    self.puts("Voitit päävoiton kierroksella {0}!".format(i))
                    self.__ikkuna.update_idletasks()
                    if toistot == 0:
                        break
                else:
                    self.tarkista(oikein, i, p_taulu[oikein], toistot)

        # Vain tulokset animoidaan
        elif tyyp == OPTIOT[1]:
            while i != toistot or toistot == 0:
                self.reset_buttons()
                self.__ikkuna.update_idletasks()
                time.sleep(0.2)
                i += 1
                arvotut = random.sample(numerot, self.__arv_lkm)
                for numero in arvotut:
                    self.korosta_button(numero)
                    self.__ikkuna.update_idletasks()
                time.sleep(1-0.2*self.__nopeus)
                oikein = len(set(omat).intersection(set(arvotut)))
                if oikein >= len(omat):
                    päävoitot += 1
                    self.puts("Voitit päävoiton kierroksella {0}!".format(i))
                    self.__ikkuna.update_idletasks()
                    if toistot == 0:
                        break
                else:
                    self.tarkista(oikein, i, p_taulu[oikein], toistot)

        # Animaatiot päällä
        else:
            while i != toistot or toistot == 0:
                self.reset_buttons()
                self.__ikkuna.update_idletasks()
                time.sleep(0.2)
                i += 1
                arvotut = random.sample(numerot, self.__arv_lkm)
                for numero in arvotut:
                    for j in range(random.randint(2, 5)):
                        rand = random.randint(1, self.__num_lkm)
                        self.temp_korosta_button(rand)
                    self.temp_korosta_button(numero)
                    self.korosta_button(numero)
                    self.__ikkuna.update_idletasks()
                time.sleep(1-0.2*self.__nopeus)
                oikein = len(set(omat).intersection(set(arvotut)))
                if oikein >= len(omat):
                    päävoitot += 1
                    self.puts("Voitit päävoiton kierroksella {0}!".format(i))
                    self.__ikkuna.update_idletasks()
                    if toistot == 0:
                        break
                else:
                    self.tarkista(oikein, i, p_taulu[oikein], toistot)

        # Arvonnan loppuaika
        t1 = time.time()
        if toistot != 1:
            self.puts("{0} arvontaa suoritettu ajassa {1:.3f}s!"
                      .format(toistot, t1-t0))
            self.__ikkuna.update_idletasks()
            if toistot != 0 and päävoitot > 1:
                self.puts("Voitit päävoiton {0} kertaa.".format(päävoitot))
            elif päävoitot == 0:
                self.puts("Et voittanut päävoittoa. :(")
        self.__pelaa_nappi.config(state=NORMAL)
        self.__ikkuna.update_idletasks()

    # Tulostetaan tulos vain jos todennäköisyys*toistot on pienempi kuin 1
    # tai mikäli pelataan päävoittoon asti niin mikäli todennäköisyys on
    # pienempi kuin 1/50,000.
    def tarkista(self, oikein, i, p, toistot):
        if toistot == 0:
            if p < 1/50000:
                self.puts("Sait {0} oikein kierroksella {1}! (p = {2})"
                      .format(oikein, i, formatoi_todennäköisyys(p)))
        elif p < 1:
            self.puts("Sait {0} oikein kierroksella {1}! (p = {2})"
                      .format(oikein, i, formatoi_todennäköisyys(p/toistot)))

    # Kaikista nappuloista reunat takaisin normaaliksi
    def reset_buttons(self):
        for i in range(1, self.__num_lkm+1):
            self.dekorosta_button(i)

    # Kaikki värit takaisin normaaleiksi,
    # numerovalinnat ja tekstikenttä tyhjäksi.
    def reset(self):
        self.fancy_colors_off()
        self.reset_buttons()
        for i in self.__valitut_numerot:
            self.button_deselected(i)
        self.__tekstikenttä.config(state=NORMAL)
        self.__tekstikenttä.delete(1.0, END)
        self.__tekstikenttä.insert(END, TERWETULIAISTEXT)
        self.__tekstikenttä.config(state=DISABLED)
        self.__pelaa_nappi.config(state=DISABLED)
        self.__valitut_numerot = []
        self.päivitä_valitse_numerot()

    # Tarkistaa nykyisen taustavärin
    def bg_color(self):
        return self.__ikkuna.cget("bg")

    # Asettaa satunnaisen paletin ja napin valintavärit,
    # "Palauta oletusvärit"-nappi aktiiviseksi
    def fancy_colors_on(self):
        self.__ikkuna.tk_setPalette(fancy_color())
        self.__fancy_colors = True
        self.__menubar.entryconfig(5, state=NORMAL)
        for i in self.__valitut_numerot:
            self.button_selected(i)

    # Värit pois, "Palauta oletusvärit"-nappi deaktiiviseksi
    def fancy_colors_off(self):
        self.__ikkuna.tk_setPalette(self.__paletti)
        self.__fancy_colors = False
        for i in self.__valitut_numerot:
            self.button_selected(i)
        self.__menubar.entryconfig(5, state=DISABLED)

    # Numeronapin taustavärin asetus
    def button_selected(self, i):
        if self.__fancy_colors:
            väri = fancy_color()
        else:
            väri = self.__button_hl_color
        self.__num_napit[i-1].config(background=väri)

    # Numeronapin taustaväri takaisin normaaliksi
    def button_deselected(self, i):
        self.__num_napit[i-1].config(background=self.bg_color())

    # Numeronapin reuna korostetuksi
    def korosta_button(self, i):
        self.__num_napit[i-1].config(relief=RIDGE)

    # Numeronapin reuna takaisin normaaliksi
    def dekorosta_button(self, i):
        self.__num_napit[i-1].config(relief=RAISED)

    # Väläyttää numeronappia mikäli se ei ole jo korostettu
    def temp_korosta_button(self, i):
        if self.__num_napit[i-1].cget("relief") == RAISED:
            self.__num_napit[i-1].config(state=ACTIVE)
            self.__ikkuna.update_idletasks()
            time.sleep(0.5-0.1*self.__nopeus)
            self.__num_napit[i-1].config(state=NORMAL)

    # Tallentaa suosikkinumerot mikäli kaikki numerot on jo valittu
    def tallenna(self):
        if len(self.__valitut_numerot) == self.__val_lkm:
            self.__suosikkinumerot = []
            for numero in self.__valitut_numerot:
                self.__suosikkinumerot.append(numero)
            self.puts("Suosikkinumerot tallennettu!")
        else:
            self.puts("Toiminto epäonnistui:\nSinun on valittava kaikki "
                      "numerot ennen\nsuosikkinumerojen tallentamista")

    # Lataa suosikkinumerot - onnistuu aina, koska suosikkinumeroja on
    # (pitäisi olla) aina oikea määrä muualla asetettujen ehtojen ansiosta.
    def lataa(self):
        for numero in self.__valitut_numerot:
            self.button_deselected(numero)
        self.__valitut_numerot = []
        for numero in self.__suosikkinumerot:
            self.__valitut_numerot.append(numero)
        for numero in self.__valitut_numerot:
            self.button_selected(numero)
        self.päivitä_valitse_numerot()
        self.puts("Suosikkinumerot ladattu!")

    # Aukaisee asetusikkunan, kutsuu self.aseta()-metodia mikäli painetaan OK.
    def asetukset(self):
        self.__asetusikkuna = Toplevel()
        self.__asetusikkuna.resizable(width=FALSE, height=FALSE)
        self.__asetusikkuna.title("Asetukset")

        # Muuttujien asetus
        self.__numvar = IntVar()
        self.__numvar.set(self.__num_lkm)
        valvar = IntVar()
        valvar.set(self.__val_lkm)
        arvvar = IntVar()
        arvvar.set(self.__arv_lkm)

        # Rekisteröidään validoimismetodi numerokentille widgettien
        # universaalilla register-metodilla
        validoi = self.__asetusikkuna.register(self.validoi)

        # Graafiset elementit
        num_label = Label(self.__asetusikkuna, text="Numeroiden lkm (2-{0})"
                          .format(MAX_NUM_LKM))
        num_label.grid(row=0, column=0)
        self.__num_spinbox = Spinbox(self.__asetusikkuna,
                                     from_=2, to=MAX_NUM_LKM,
                                     textvariable=self.__numvar)
        self.__num_spinbox.grid(row=0, column=1, sticky=E+W)

        self.__val_label = Label(self.__asetusikkuna)
        self.__val_label.grid(row=1, column=0)
        self.__val_spinbox = Spinbox(self.__asetusikkuna,
                                     from_=1, to=MAX_NUM_LKM,
                                     textvariable=valvar)
        self.__val_spinbox.grid(row=1, column=1, sticky=E+W)

        self.__arv_label = Label(self.__asetusikkuna)
        self.__arv_label.grid(row=2, column=0)
        self.__arv_spinbox = Spinbox(self.__asetusikkuna, from_=1,
                                     to=MAX_NUM_LKM, textvariable=arvvar)
        self.__arv_spinbox.grid(row=2, column=1, sticky=E+W)

        nopeus_label = Label(self.__asetusikkuna, text="Animaationopeus")
        nopeus_label.grid(row=3, column=0)
        self.__speed_slider = Scale(self.__asetusikkuna, from_=1, to=5,
                                    orient=HORIZONTAL, showvalue=0)
        self.__speed_slider.set(self.__nopeus+1)
        self.__speed_slider.grid(row=3, column=1, sticky=E+W)
        värilabel1 = Label(self.__asetusikkuna, text="Teeman väri")
        värilabel1.grid(row=4, column=0)
        self.__värientry1 = Entry(self.__asetusikkuna)
        self.__värientry1.insert(END, self.__paletti)
        self.__värientry1.grid(row=4, column=1)
        värilabel2 = Label(self.__asetusikkuna, text="Valintojen väri")
        värilabel2.grid(row=5, column=0)
        self.__värientry2 = Entry(self.__asetusikkuna)
        self.__värientry2.insert(END, self.__button_hl_color)
        self.__värientry2.grid(row=5, column=1)

        # Asetetaan tarkistukset
        self.__num_spinbox.config(validate=ALL, vcmd=(validoi, "%P", 2),
                                  command=lambda: self.päivitä_spinbox_labelit(
                                      self.__numvar.get()))
        self.__val_spinbox.config(validate=ALL, vcmd=(validoi, "%P", 1))
        self.__arv_spinbox.config(validate=ALL, vcmd=(validoi, "%P", 1))
        self.__numvar.set(self.__num_lkm)
        self.päivitä_spinbox_labelit(self.__numvar.get())

        # Napit
        peruuta_button = Button(self.__asetusikkuna, text="Peruuta",
                           command=self.__asetusikkuna.destroy)
        peruuta_button.grid(row=6, column=0, sticky=E+W, padx=5, pady=5)
        ok_button = Button(self.__asetusikkuna, text="Tallenna",
                           command=self.aseta)
        ok_button.grid(row=6, column=1, sticky=E+W, padx=5, pady=5)
        self.__asetusikkuna.mainloop()

    # Tarkistaa että väriasetukset ovat oikein, resetoi ikkunan käyttäen
    # self.reset()-metodia
    def aseta(self):
        try:
            self.__paletti = self.__värientry1.get()
            self.__button_hl_color = self.__värientry2.get()
            # Tämä funktio tuottaa TclErrorin mikäli värit ovat epäkelpoja
            self.fancy_colors_off()
        except TclError:
            showerror("Tuntematon väri!",
                      "Syöttämäsi värikoodi oli virheellinen.\n"
                      "Oletusvärit palautettu.")
            self.__paletti = PALETTI
            self.__button_hl_color = BUTTON_HL_COLOR
            self.fancy_colors_off()
        else:
            # Tyhjennetään valitut_numerot ja tekstikenttä
            self.reset()
            self.__num_lkm = int(self.__num_spinbox.get())

            # Nollataan suosikkinumerot, jos val_lkm muuttui
            # tai jokin suosikkinumeroista on liian suuri
            uusi_val_lkm = int(self.__val_spinbox.get())
            if self.__val_lkm != uusi_val_lkm or max(self.__suosikkinumerot) > self.__num_lkm:
                self.__suosikkinumerot = [i+1 for i in range(uusi_val_lkm)]

            self.__val_lkm = uusi_val_lkm
            self.__arv_lkm = int(self.__arv_spinbox.get())
            self.__nopeus = self.__speed_slider.get()-1
            self.__asetusikkuna.destroy()

            # Tämän rivin ansiosta ikkuna osaa muuttaa kokoaan oikein, vaikka
            # joku pellehermanni olisi mennyt sitä manuaalisesti muuttelemaan
            self.__ikkuna.wm_geometry("")

            self.__numframe.destroy()
            self.alusta_numeronapit()
            self.päivitä_valitse_numerot()

    # Tulostaa yksinkertaisen ikkunan jossa on todennäköisyystaulukko
    # nykyisillä asetuksilla
    def todennäköisyystaulukko(self):
        todnäktaulukko = Toplevel()
        todnäktaulukko.title("Todennäköisyystaulukko")
        todnäktaulukko.minsize(150, 100)
        otsikkolabelit = []
        todnäklabelit = []
        Grid.grid_columnconfigure(todnäktaulukko, 0, weight=1)
        Grid.grid_columnconfigure(todnäktaulukko, 1, weight=1)
        for i in range(self.__val_lkm+1):
            Grid.grid_rowconfigure(todnäktaulukko, i, weight=1)
            p = todnäk(self.__val_lkm, i, self.__arv_lkm, self.__num_lkm)
            otsikkolabelit.append(Label(todnäktaulukko, text="{0} oikein:"
                                  .format(i,)))
            todnäklabelit.append(Label(todnäktaulukko,
                                       text=formatoi_todennäköisyys(p)))
            otsikkolabelit[i].grid(row=i, padx=10)
            todnäklabelit[i].grid(row=i, column=1, padx=10)
        sulje = Button(todnäktaulukko, text="Sulje", command=todnäktaulukko.destroy)
        sulje.grid(row=self.__val_lkm+1, sticky=W+E, padx=20, pady=5, columnspan=2)

    # Tulostaa päävoiton todennäköisyyden tekstikenttään
    def näytä_todnäk(self):
        self.puts("Päävoiton todennäköisyys nykyisillä asetuksilla:")
        p = todnäk(self.__val_lkm, self.__val_lkm, self.__arv_lkm, self.__num_lkm)
        self.puts(formatoi_todennäköisyys(p))

    # Vahvistus asetusikkunan numeroiden muutoksille
    def validoi(self, new, minimi):
        minimi = int(minimi)
        try:
            new = int(new)
        except ValueError:
            return False
        if minimi <= new <= MAX_NUM_LKM:
            # Jos validoidaan num_lkm niin päivitetään
            # val ja arv rajoitteet
            if minimi == 2:
                self.päivitä_spinbox_labelit(new)
            elif new > self.__numvar.get():
                return False
            return True
        else:
            return False

    # Päivittää omien numeroiden ja arvottavien numeroiden lukumäärän maksimin
    # parametrina annettavaksi numeroiden kokonaismääräksi
    def päivitä_spinbox_labelit(self, numvar):
        self.__val_label.config(text="Omien lkm (1-{0})".format(numvar))
        self.__val_spinbox.config(to=int(numvar))
        self.__arv_label.config(text="Arvottavien lkm (1-{0})".format(numvar))
        self.__arv_spinbox.config(to=int(numvar))


# Yksinkertainen funktio kombinaatioiden laskemiseen
def nCr(n, r):
    return fact(n)/(fact(r)*fact(n-r))


# Funktio ottaa parametreina 4 kokonaislukua (int)
#   1) v (valitut): Kuinka monta numeroa on valittu?
#   2) o (oikeat): Kuinka moni valituista meni oikein?
#   3) a (arvottavat): Kuinka monta numeroa arvotaan?
#   4) n (numerot): Kuinka monta numeroa arvonnassa on mukana?
# ja palauttaa todennäköisyyden saada o oikein (float)
def todnäk(v, o, a, n):
    if o > v or o > a or n-a < v-o:
        return 0.0
    else:
        return (nCr(a, o)*nCr(n-a, v-o))/nCr(n, v)


# Funktio formatoi todennäköisyyden (float) helpommin luettavaksi
# merkkijonoksi
def formatoi_todennäköisyys(p):
    if p == 0:
        return "0"
    elif p < 0.01:
        return "1/{0:,.0f}".format(1/p)
    else:
        return "{0:.2f}%".format(p*100)


# Funktio palauttaa satunnaisen värin heksakoodin
def fancy_color():
    return "#" + "".join([random.choice("0123456789ABCDEF")
                          for x in range(6)])


# kutsuu kisun :3
def kisu():
    kuvaikkuna("Kisu :3", KUVA1)


# kutsuu koalan :3
def koala():
    kuvaikkuna("Koala :3", KUVA2)


# Ottaa parametrina otsikon ja kuvan, näyttää kuvaikkunan
def kuvaikkuna(title, kuvadata):
    ikkuna = Toplevel()
    ikkuna.resizable(width=FALSE, height=FALSE)
    ikkuna.title(title)
    kuva = PhotoImage(data=kuvadata)
    kuvalabel = Label(ikkuna)
    kuvalabel.grid(row=0, sticky=N+W+E+S)
    kuvalabel.configure(image=kuva)
    sulje = Button(ikkuna, text="Sulje", command=ikkuna.destroy)
    sulje.grid(row=1, sticky=W+E, padx=20, pady=5)
    ikkuna.mainloop()


# Avaa uuden ikkunan jossa on ohjeita välilehdissä
def ohjeet():
    # Vaihtaa ohjeen sivulle x (int)
    def sivu(x):
        for t in tab:
            t.config(relief=SUNKEN)
        tab[x].config(relief=FLAT)
        ohjetext.config(state=NORMAL)
        ohjetext.delete(1.0, END)
        ohjetext.insert(1.0, ohje[x])
        ohjetext.config(state=DISABLED)
    # Ohjeen sivujen sisältö kätevässä listassa
    ohje = ['''1.\tValitse numerot joko klikkaamalla numeronappuloita tai\n\tvalitsemalla "Valikko - Lataa suosikkinumerot" \n\t(oletuksena tallennettu numerot 1, 2, 3...)\n\n2.\tValitse kierrosten määrä syöttämällä (positiivinen \n\tkokonais)luku tekstikenttään. Päävoittoon asti pelatessa\n\tkannattaa varmistaa että todennäköisyydet eivät ole \n\tmitättömät. Voit tarkistaa todennäköisyydet valitsemalla\n\t"Näytä - Todennäköisyystaulukko"\n\n3.\tValitse haluamasi animaatio pudotusvalikosta.\n\n4.\tValittuasi kaikki numerot "Aloita arvonta"-nappi aktivoituu \n\tja voit aloittaa arvonnan. Mikäli valitsemasi asetukset ovat\n\tliian hazardeja, sinulta pyydetään vielä vahvistus.\n\n5.\tArvonnan aikana tulostetaan tulokset jotka esiintyvät \n\tvalituilla toistokerroilla keskimäärin alle kerran. Jos siis\n\tvalitsit yhden toistokerran tulostuu mikä tahansa tulos, mutta\n\ttuhannella arvonnalla pelattaessa tulostuvat vain ne tulokset \n\tjoiden todennäköisyys on alle 1/1000.''',
            '''Numeroiden lkm:\n\tVaihtaa numeroiden lukumäärää.\nOmien lkm:\n\tVaihtaa valittavien numeroiden lukumäärää. Ei voida asettaa \n\tkorkeammaksi kuin numeroiden lkm.\nArvottavien lkm:\n\tVaihtaa arvottavien numeroiden lukumäärää. Voi olla pienempi\n\ttai suurempi kuin omien lkm, mutta korkeintaan yhtä suuri\n\tkuin numeroiden lkm.\nAnimaationopeus:\n\tVaihtaa animaation nopeutta. Ei vaikutusta mikäli on valittu\n\t"Ei animaatiota".\nTeeman ja valintojen väri:\n\tVoit vaihtaa ikkunan väriteemaa syöttämällä tähän joko \n\tvärin englanninkielisen nimen tai heksakoodin. Oletusvärit \n\tpalautetaan mikäli jompikumpi valituista väreistä on \n\tvirheellinen.''',
            '''Voit resetoida pelin (poistaa kaikki numerovalinnat, tyhjentää \ntekstikentän ja poistaa fantsut värit käytöstä) joko painamalla\n "Resetoi peli"-nappia tai valitsemalla "Valikko - Uusi".\n\nFancy colors -napin vimmattu paineleminen on hauskaa.\n\n"Näytä"-valikosta löydät upeita eläinpiirroksiani.\n\nVoit tallettaa suosikkinumerosi valitsemalla \n"Valikko - Tallenna suosikkinumerosi". Tämä onnistuu vain \nmikäli olet valinnut kaikki numerot. Jos muutat asetuksista \nomien numeroiden määrää niin suosikkinumerot nollaantuvat. \nSuosikkinumeroiden tallentaminen tiedostoon ei valitettavasti\nole mahdollista.''']
    ikkuna = Toplevel()
    ikkuna.minsize(550, 400)
    ikkuna.title("Ohjeet")
    ohjeframe = Frame(ikkuna)
    ohjeframe.pack(fill=X, expand=0, anchor=N)
    for i in range(3):
        Grid.grid_columnconfigure(ohjeframe, i, minsize=150)
    Grid.grid_columnconfigure(ohjeframe, 3, weight=1)
    tab = list()
    tab.append(Button(ohjeframe, text="Pelaaminen", command=lambda: sivu(0)))
    tab[0].grid(column=0, row=0, sticky=W+E)
    tab.append(Button(ohjeframe, text="Asetukset", command=lambda: sivu(1)))
    tab[1].grid(column=1, row=0, sticky=W+E)
    tab.append(Button(ohjeframe, text="Muut", command=lambda: sivu(2)))
    tab[2].grid(column=2, row=0, sticky=W+E)
    # Neljäs nappi just for looks
    Button(ohjeframe, relief=SUNKEN, state=DISABLED)\
        .grid(column=3, row=0, sticky=W+E)
    ohjetext = Text(ikkuna, width=70, tabs="0.8c", relief=FLAT)
    ohjetext.pack(fill=BOTH, expand=1, padx=10, pady=10)
    sivu(0)


def tietoja():
    bgc = "#001000"
    fgc = "#33FF66"
    ikkuna = Toplevel(bg=bgc)
    ikkuna.title("Tietoja")
    ikkuna.resizable(width=FALSE, height=FALSE)
    Label(ikkuna, font=("DejaVu Sans Mono", 14), text=OTSIKKO,
          bg=bgc, fg=fgc).pack(padx=45, pady=15)
    Label(ikkuna, bg=bgc, fg=fgc,
          text="Johdatus ohjelmointiin -kurssin\nharjoitustyö keväältä 2015\n"
               "\nTehnyt Mikko Esko (mikko.esko@student.tut.fi)").pack(pady=10)


def main():
    LottosimUI()

main()