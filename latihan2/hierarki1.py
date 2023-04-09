print('\nHierarchical Inheritance_KPOP\n\n')

class Grup:
    def __init__(self, grup, anggota):
        self.grup = grup
        self.anggota = anggota

    def ket(self):
        print(f'{self.grup} beranggotakan {self.anggota} orang\n\n')
    
    def getGrup(self):
        return self.grup
    
    def getAnggota(self):
        return self.anggota

class Gen(Grup):
    def __init__(self, grup, anggota, gen):
        super().__init__(grup, anggota)
        self.gen = gen
    
    def detail(self):
        print(f'Grup {self.grup} merupakan Generasi Ke-{self.gen} Grupband\n')

    def getGen(self):
        return self.gen

class Agensi(Gen):
    def __init__(self, grup, anggota, gen, fandom, agensi):
        super().__init__(grup, anggota, gen)
        self.fandom = fandom
        self.agensi = agensi

    def keterangan(self):
        print(f'Grup: {self.grup}\nAnggota: {self.anggota} Orang\nFandom: {self.fandom}\nGen: {self.gen}\nAgensi: {self.agensi}\n')

if __name__ == '__main__':
    grup1 = Agensi('JKT',9,3,'JKT 48','fortune coockies')
    grup1.keterangan()
    grup1.detail()
    grup1.ket()

    grup2 = Agensi('smash',5,4,'smashing','i heart you')
    grup2.keterangan()

    grup3 = Agensi('cherrybelle',23,4,'cherrysquad','i love you')
    grup3.keterangan()
