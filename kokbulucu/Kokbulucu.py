from kok_bulma_arayuz_py import Ui_KokBulucu
import sys
from PyQt5 import QtWidgets



class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()
        self.ui = Ui_KokBulucu()
        self.ui.setupUi(self)

        self.ui.btn_calc_2kok.clicked.connect(self.kok_Bulma_ikinci_dereceden) #for calculate left side  

        self.ui.btn_clr_2kok.clicked.connect(self.temizle_kok2) #for clear left side result

        self.ui.btn_calc_3kok.clicked.connect(self.kok_bulma_ucuncu_dereceden) #for calculate right side  
    
        self.ui.btn_clr_3kok.clicked.connect(self.temizle_kok3) #for clear right side result

        self.ui.btn_eng.clicked.connect(self.translate_eng) #for translate english

        self.ui.btn_trk.clicked.connect(self.translate_tr) #for translate turkish

    def translate_tr(self):
        self.ui.btn_calc_2kok.setText("Hesapla")
        self.ui.btn_clr_2kok.setText("Temizle")
        self.ui.btn_calc_3kok.setText("Hesapla")
        self.ui.btn_clr_3kok.setText("Temizle")

        self.ui.label_2baslik.setText("2. dereceden Kökler")
        self.ui.label_3baslik.setText("3. dereceden Kökler")

        self.ui.label_2_x2.setText("X^2 nin Katsayısı :")
        self.ui.label_2_x1.setText("X^1 in Katsayısı :")
        self.ui.label_2_x0.setText("Sabit :")
        
        self.ui.label_3_x3.setText("X^3 ün Katsayısı :")
        self.ui.label_3_x2.setText("X^2 nin Katsayısı :")
        self.ui.label_3_x1.setText("X^1 in Katsayısı :")
        self.ui.label_3_x0.setText("Sabit :")
        self.ui.label_3_xi_info.setText("İrrasyonel kökleri göstermek için 1 yazmanız yeterli")
        self.ui.label_3_xi_tf.setText("İmaginel aktivasyon (0 : False, 1: True) : ")

    def translate_eng(self):
        self.ui.btn_calc_2kok.setText("Calculate")
        self.ui.btn_clr_2kok.setText("Clear")
        self.ui.btn_calc_3kok.setText("Calculate")
        self.ui.btn_clr_3kok.setText("Clear")

        self.ui.label_2baslik.setText("Second Order Roots")
        self.ui.label_3baslik.setText("3rd Order Roots")

        self.ui.label_2_x2.setText("Coefficient of X^2:")
        self.ui.label_2_x1.setText("Coefficient of X^1:")
        self.ui.label_2_x0.setText("Coefficient of X^0:")
        
        self.ui.label_3_x3.setText("Coefficient of X^3:")
        self.ui.label_3_x2.setText("Coefficient of X^2:")
        self.ui.label_3_x1.setText("Coefficient of X^1:")
        self.ui.label_3_x0.setText("Coefficient of X^0:")
        self.ui.label_3_xi_info.setText("To show irrational roots, just write 1")
        self.ui.label_3_xi_tf.setText("Imaginal activation (0: False, 1: True):")

    def kok_Bulma_ikinci_dereceden(self):
        x_karenin_katsayisi = int(self.ui.txt2_kat2.text())
        x_in_katsayisi = int(self.ui.txt2_kat1.text())
        sabit = int(self.ui.txt2_kat0.text())
        delta = x_in_katsayisi**2 - 4*x_karenin_katsayisi*sabit
        if delta < 0:
            kokyok = ('kök yok (no root)')
            self.ui.albl_2result.setText(f"Result : {kokyok}")
        elif delta > 0:
            kok1 = ((-1 * x_in_katsayisi) + delta**0.5)/2*x_karenin_katsayisi
            kok2 = ((-1 * x_in_katsayisi) - delta**0.5)/2*x_karenin_katsayisi
            self.ui.albl_2result.setText(f"Result: {kok1} ve {kok2}")
        else:
            kok = ((-1 * x_in_katsayisi) - delta ** 0.5) / 2 * x_karenin_katsayisi or ((-1 * x_in_katsayisi) + delta**0.5)/2*x_karenin_katsayisi
            self.ui.albl_2result.setText(f"Result : {kok} (çift kök (double root))")
    
    def temizle_kok2(self):
        self.ui.albl_2result.setText("Result :")

    def temizle_kok3(self):
        self.ui.albl_3result.setText("Result :")
        
    def kok_bulma_ucuncu_dereceden(self):
        x_kupun_katsayisi = int(self.ui.txt3_kat3.text())
        x_karenin_katsayisi = int(self.ui.txt3_kat2.text())
        x_in_katsayisi = int(self.ui.txt3_kat1.text())
        sabit = int(self.ui.txt3_kat0.text())
        imaginal_aktivasyon = int(self.ui.txt3_kat_i.text())
        kokler = []
        if sabit != 0:
            alfa = sabit /(2*x_kupun_katsayisi) + (x_karenin_katsayisi**3)/(27 * x_kupun_katsayisi**3) - (x_karenin_katsayisi*x_in_katsayisi)/(6 * x_kupun_katsayisi**2)
            beta = x_in_katsayisi/(3*x_kupun_katsayisi) - (x_karenin_katsayisi**2)/(9 * x_kupun_katsayisi**2)

            deltas = (alfa**2 + beta**3)**(1/2) - alfa

            kok1 = deltas**(1/3) - x_karenin_katsayisi/(3*x_kupun_katsayisi) - beta/(deltas**(1/3))

            kok2 =beta / (2 * deltas**(1/3)) - x_karenin_katsayisi/(3*x_kupun_katsayisi) - (1/2) * deltas**(1/3) -(3**(1/2) / 2)*(beta/deltas**(1/3) + deltas**(1/3))*(-1)**(1/2)

            kok3 =beta / (2 * deltas**(1/3)) - x_karenin_katsayisi/(3*x_kupun_katsayisi) - (1/2) * deltas**(1/3) +(3**(1/2) / 2)*(beta/deltas**(1/3) + deltas**(1/3))*(-1)**(1/2)
            #if type(kok1) or type(kok2) or type(kok3) == complex:
                #m = str(input('Köklerde (program kaynaklı veya gerçekten mevcut) gerçel olmayan kısımlar mevcut bunları da istiyor musun?\nGenellikle tavsiye etmiyorum -Numa (e/h)'))

            if imaginal_aktivasyon:
                kokler = [str(kok1.real)+' ('+str(kok1.imag)+')i',str(kok2.real)+' ('+str(kok2.imag)+')i',str(kok3.real)+' ('+str(kok3.imag)+')i']
                self.ui.albl_3result.setText(f"Result : {kokler[0]} , {kokler[1]} ve {kokler[2]}")
                
            else:
                kokler = [kok1.real,kok2.real,kok3.real]        
                self.ui.albl_3result.setText(f"Result : {kokler[0]} , {kokler[1]} ve {kokler[2]}")
        else:
            delta = x_karenin_katsayisi**2 - 4*x_kupun_katsayisi*x_in_katsayisi
            if delta < 0:
                kokler.append(0)
                self.ui.albl_3result.setText(f"Result : {kokler[0]}")
            elif delta > 0:
                k1 = ((-1 * x_karenin_katsayisi) + delta**0.5)/2*x_kupun_katsayisi
                k2 = ((-1 * x_karenin_katsayisi) - delta**0.5)/2*x_kupun_katsayisi
                kokler.append(k1)
                kokler.append(k2)
                if 0 not in kokler:
                    kokler.append(0)
                self.ui.albl_3result.setText(f"Result : {kokler[0]} , {kokler[1]} ve {kokler[2]}")
            else:
                kok = ((-1 * x_karenin_katsayisi) - delta ** 0.5) / 2 * x_kupun_katsayisi or ((-1 * x_karenin_katsayisi) + delta**0.5)/2*x_kupun_katsayisi
                kokler.append(kok)
                if 0 not in kokler:
                    kokler.append(0)
                self.ui.albl_3result.setText(f"Result : {kokler[0]} ve {kokler[1]}")
            
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())
app()