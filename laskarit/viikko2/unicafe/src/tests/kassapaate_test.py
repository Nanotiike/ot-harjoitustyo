import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(400)

    def test_alustus(self):
        self.assertEqual(self.kassa.kassassa_rahaa,100000)
        self.assertEqual(self.kassa.edulliset,0)
        self.assertEqual(self.kassa.maukkaat,0)
        self.assertEqual(self.kortti.saldo,400)

    def test_syo_edullisesti_kateisella(self):
        maksu=240
        palaute=self.kassa.syo_edullisesti_kateisella(maksu)
        self.assertEqual(self.kassa.kassassa_rahaa,100240)
        self.assertEqual(self.kassa.edulliset,1)
        self.assertEqual(palaute,maksu-240)
        maksu=100
        palaute=self.kassa.syo_edullisesti_kateisella(maksu)
        self.assertEqual(self.kassa.kassassa_rahaa,100240)
        self.assertEqual(self.kassa.edulliset,1)
        self.assertEqual(palaute,maksu)

    def test_syo_maukkaasti_kateisella(self):
        maksu=400
        palaute=self.kassa.syo_maukkaasti_kateisella(maksu)
        self.assertEqual(self.kassa.kassassa_rahaa,100400)
        self.assertEqual(self.kassa.maukkaat,1)
        self.assertEqual(palaute,maksu-400)
        maksu=100
        palaute=self.kassa.syo_maukkaasti_kateisella(maksu)
        self.assertEqual(self.kassa.kassassa_rahaa,100400)
        self.assertEqual(self.kassa.maukkaat,1)
        self.assertEqual(palaute,maksu)

    def test_syo_edullisesti_kortilla(self):
        palaute = self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(palaute,True)
        self.assertEqual(self.kassa.edulliset,1)
        self.assertEqual(self.kortti.saldo,160)
        self.assertEqual(self.kassa.kassassa_rahaa,100000)
        palaute = self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(palaute,False)
        self.assertEqual(self.kassa.edulliset,1)
        self.assertEqual(self.kortti.saldo,160)
        self.assertEqual(self.kassa.kassassa_rahaa,100000)


    def test_syo_maukkaasti_kortilla(self):
        palaute = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(palaute,True)
        self.assertEqual(self.kassa.maukkaat,1)
        self.assertEqual(self.kortti.saldo,0)
        self.assertEqual(self.kassa.kassassa_rahaa,100000)
        palaute = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(palaute,False)
        self.assertEqual(self.kassa.maukkaat,1)
        self.assertEqual(self.kortti.saldo,0)
        self.assertEqual(self.kassa.kassassa_rahaa,100000)

    def test_lataa_rahaa_kortille(self):
        self.kassa.lataa_rahaa_kortille(self.kortti,200)
        self.assertEqual(self.kortti.saldo,600)
        self.assertEqual(self.kassa.kassassa_rahaa,100200)
        self.kassa.lataa_rahaa_kortille(self.kortti,-200)
        self.assertEqual(self.kortti.saldo,600)
        self.assertEqual(self.kassa.kassassa_rahaa,100200)