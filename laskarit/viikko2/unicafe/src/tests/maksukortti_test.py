import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_lataa_rahaa(self):
        self.maksukortti.lataa_rahaa(1000)

        self.assertEqual(self.maksukortti.saldo_euroina(), 20.0)

    def test_rahan_otto_onnistuu(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 5.0)

    def test_rahan_otto_ei_onnistuu(self):
        self.maksukortti.ota_rahaa(5000)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)
    