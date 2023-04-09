class mobil:
    def __init__(self,nama,jenis,tahun_keluar,harga):
        self.nama = nama
        self.jenis = jenis
        self.tahun_keluar = tahun_keluar
        self.harga = harga

    def bonus(self):
        return self.harga*0.15

    def display(self):
        print('\n\t\tInfo MOBIL\t\t\n'+'='*40)
        print('Nama\t\t: ',self.nama)
        print('MERK\t\t: ',self.jenis)
        print(f'Tahun_Keluar\t:  {self.tahun_keluar} jam')
        print('Harga\t\t: ',self.harga)

class motor(mobil):
    def __init__(self,nama,jenis,tahun_keluar,harga):
        super().__init__(nama,nama,jenis,tahun_keluar,harga)

    def bonus(self):
        return self.harga*0.05

def info_bonus(object):
    x = object.bonus()
    y = object.harga + object.bonus()
    print(f'Bonus\t\t:  {x}')
    print(f'Total harga\t:  {y}\n')


worker1 = mobil('BMW','A1',2000,7500000)
worker1.display()
info_bonus(worker1)

worker2 = motor('SUPRA','RX 8',1998,4500000)
worker2.display()
info_bonus(worker2)