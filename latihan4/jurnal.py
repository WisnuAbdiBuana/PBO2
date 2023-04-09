class Jurnal:
    def __init__(self,title,date):
        self.title = title
        self.date = date

class peneliti:
    def __init__(self,nama,jurnal):
        self.nama = nama
        self.jurnal = jurnal

    def daftar_jurnal(self):
        print(f'\nPeneliti\t:  {self.nama}\n')
        for jurnal in self.jurnal:
            print(f'Judul\t\t: ',jurnal.title)
            print(f'Published\t:  {jurnal.date}')
           
jurnal1 = Jurnal('Cara menggunakan mobil', 2000)
jurnal2 = Jurnal('Cara menggunakan motor', 2000)
peneliti1 = peneliti('Wisnu abdi buana', [jurnal1, jurnal2])
jurnal3 = Jurnal('cara menjadi programmer', 2016)
jurnal4 = Jurnal('cara menggunakan bahasa pemograman', 2020)
peneliti2 = peneliti('buana wisnu', [jurnal3, jurnal4])
peneliti1.daftar_jurnal()
peneliti2.daftar_jurnal()
 