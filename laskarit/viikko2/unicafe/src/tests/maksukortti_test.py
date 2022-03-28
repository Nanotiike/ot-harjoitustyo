import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.kortti, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.kortti), "saldo: 10.0")

    def test_kortille_voi_ladata_rahaa(self):
        self.kortti.lataa_rahaa(2500)
        self.assertEqual(str(self.kortti), "saldo: 35.0")

    def test_kortilta_voi_ottaa_rahaa(self):
        palaute=self.kortti.ota_rahaa(500)
        self.assertEqual(str(self.kortti), "saldo: 5.0")
        self.assertEqual(palaute,True)
        palaute=self.kortti.ota_rahaa(1000)
        self.assertEqual(str(self.kortti), "saldo: 5.0")
        self.assertEqual(palaute,False)