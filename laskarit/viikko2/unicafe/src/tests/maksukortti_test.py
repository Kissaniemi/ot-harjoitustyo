import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_alussa_saldo_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lisaaminen(self):
        self.maksukortti.lataa_rahaa(2500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 35.00 euroa")

    def test_rahan_ottaminen(self):
        maksukortti = Maksukortti(2500)
        assert(maksukortti.ota_rahaa(1500)) == True
        assert(maksukortti.ota_rahaa(1000)) == True
        assert(maksukortti.ota_rahaa(200)) == False



