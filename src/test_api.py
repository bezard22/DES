import unittest
from api import call
from des import DES
from bitstring import BitArray

class Test_des(unittest.TestCase):
    def test_1(self) -> None:
        """_summary_
        """
        payload = {
            "action": "encrypt",
            "encoding": "hex",
            "inText": "0000000000000000",
            "key": "0000000000000000",
        }
        res = call(*payload)
        des = DES()
        x = BitArray(hex="0000000000000000", length=64)
        k = BitArray(hex="0000000000000000", length=64)
        des.encrypt(x, k)
        self.assertEqual(res, des.data)


if __name__ == "__main__":
    unittest.main()