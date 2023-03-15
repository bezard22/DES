import unittest
from des import DES
from bitstring import BitArray

dataInit = {
    "x": None,
    "k": None,
    "y": None,
    "IP": None,
    "L": [],
    "R": [],
    "PC1": None,
    "ki": [],
    "E": [],
    "EXor": [],
    "S": [[] for _ in range(8)],
    "F": [],
    "Srow": [[] for _ in range(8)],
    "Scol": [[] for _ in range(8)],
    "C": [],
    "D": [],
    "perm": {
        "PC1": [
            57, 49, 41, 33, 25, 17, 9, 1,
            58, 50, 42, 34, 26, 18, 10, 2,
            59, 51, 43, 35, 27, 19, 11, 3,
            60, 52, 44, 36, 63, 55, 47, 39,
            31, 23, 15, 7, 62, 54, 46, 38,
            30, 22, 14, 6, 61, 53, 45, 37,
            29, 21, 13, 5, 28, 20, 12, 4,
        ],
        "PC2": [
            14, 17, 11, 24, 1, 5, 3, 28,
            15, 6, 21, 10, 23, 19, 12, 4,
            26, 8, 16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55, 30, 40,
            51, 45, 33, 48, 44, 49, 39, 56,
            34, 53, 46, 42, 50, 36, 29, 32,
        ],
        "IP": [
            58, 50, 42, 34, 26, 18, 10, 2,
            60, 52, 44, 36, 28, 20, 12, 4,
            62, 54, 46, 38, 30, 22, 14, 6,
            64, 56, 48, 40, 32, 24, 16, 8,
            57, 49, 41, 33, 25, 17, 9, 1,
            59, 51, 43, 35, 27, 19, 11, 3,
            61, 53, 45, 37, 29, 21, 13, 5,
            63, 55, 47, 39, 31, 23, 15, 7,
        ],
        "E": [
            32, 1, 2, 3, 4, 5,
            4, 5, 6, 7, 8, 9,
            8, 9, 10, 11, 12, 13,
            12, 13, 14, 15, 16, 17,
            16, 17, 18, 19, 20, 21,
            20, 21, 22, 23, 24, 25,
            24, 25, 26, 27, 28, 29,
            28, 29, 30, 31, 32, 1,
        ],
        "S": [
            [
                [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,],
                [00, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,],
                [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,],
                [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13,],
            ],
            [
                [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
                [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
                [00, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
                [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
            ],
            [
                [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
                [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
                [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
                [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
            ],
            [
                [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
                [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
                [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
                [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
            ],
            [
                [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
                [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
                [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
                [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
            ],
            [
                [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
                [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
                [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
                [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
            ],
            [
                [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
                [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
                [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
                [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
            ],
            [
                [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
                [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
                [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
                [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
            ],
        ],
        "P": [
            16, 7, 20, 21, 29, 12, 28, 17,
            1, 15, 23, 26, 5, 18, 31, 10,
            2, 8, 24, 14, 32, 27, 3, 9,
            19, 13, 30, 6, 22, 11, 4, 25,
        ],
        "FP": [
            40, 8, 48, 16, 56, 24, 64, 32,
            39, 7, 47, 15, 55, 23, 63, 31,
            38, 6, 46, 14, 54, 22, 62, 30,
            37, 5, 45, 13, 53, 21, 61, 29,
            36, 4, 44, 12, 52, 20, 60, 28,
            35, 3, 43, 11, 51, 19, 59, 27,
            34, 2, 42, 10, 50, 18, 58, 26,
            33, 1, 41, 9, 49, 17, 57, 25,
        ],
    }
}

class Test_des(unittest.TestCase):
    def test_init(self) -> None:
        des = DES()
        self.assertEqual(des.data, dataInit, "Data init incorrect")
    
    def test_reset(self) -> None:
        des = DES()
        x = BitArray(hex="0000000000000000", length=64)
        k = BitArray(hex="0000000000000000", length=64)
        des.encrypt(x, k)
        des.dataReset()
        self.assertEqual(des.data, dataInit, "Data reset incorrect")
    
    def test_PC1_1(self) -> None:
        des = DES()
        k = BitArray(hex="0000000000000000", length=64)
        res = des.PC1(k)
        self.assertEqual(res.hex, "00000000000000", "function should return 00000000000000")
        self.assertEqual(des.data["PC1"], "00000000000000", "data should have 00000000000000")
    
    def test_PC1_2(self) -> None:
        des = DES()
        k = BitArray(hex="0123456789abcdef", length=64)
        res = des.PC1(k)
        self.assertEqual(res.hex, "f0ccaa0aaccf00", "function should return f0ccaa0aaccf00")
        self.assertEqual(des.data["PC1"], "f0ccaa0aaccf00", "data should have f0ccaa0aaccf00")
    
    def test_PC2_1(self) -> None:
        des = DES()
        k = BitArray(hex="00000000000000", length=64)
        res = des.PC2(k)
        self.assertEqual(res.hex, "000000000000", "function should return 000000000000")
        self.assertEqual(des.data["ki"][0], "000000000000", "data should have 000000000000")
    
    def test_PC2_2(self) -> None:
        des = DES()
        k = BitArray(hex="e1995415599e01", length=64)
        res = des.PC2(k)
        self.assertEqual(res.hex, "0b02679b49a5", "function should return 0b02679b49a5")
        self.assertEqual(des.data["ki"][0], "0b02679b49a5", "data should have 0b02679b49a5")

    def test_transform_1(self) -> None:
        des = DES()
        kPC = BitArray(hex="00000000000000", length=64)
        c = kPC[:28]
        d = kPC[28:]
        for i in [0, 1, 8, 15]:
            ci, di, ki = des.transform(c, d, i)
            self.assertEqual(ci.hex, "0000000", f"function should return 0000000 with i={i}")
            self.assertEqual(des.data["C"][0], "0000000", f"data should have 0000000 with i={i}")
            self.assertEqual(di.hex, "0000000", f"function should return 0000000 with i={i}")
            self.assertEqual(des.data["D"][0], "0000000", f"data should have 0000000 with i={i}")
    
    def test_transform_2(self) -> None:
        des = DES()
        kPC = BitArray(hex="00000000000000", length=64)
        c = kPC[:28]
        d = kPC[28:]
        for i in (set([i for i in range(16)]) - set([0, 1, 8, 15])):
            ci, di, ki = des.transform(c, d, i)
            self.assertEqual(ci.hex, "0000000", f"function should return 0000000 with i={i}")
            self.assertEqual(des.data["C"][0], "0000000", f"data should have 0000000 with i={i}")
            self.assertEqual(di.hex, "0000000", f"function should return 0000000 with i={i}")
            self.assertEqual(des.data["D"][0], "0000000", f"data should have 0000000 with i={i}")
    
    def test_transform_3(self) -> None:
        des = DES()
        kPC = BitArray(hex="f0ccaa0aaccf00", length=64)
        c = kPC[:28]
        d = kPC[28:]
        for i in [0, 1, 8, 15]:
            ci, di, ki = des.transform(c, d, i)
            self.assertEqual(ci.hex, "e199541", f"function should return e199541 with i={i}")
            self.assertEqual(des.data["C"][0], "e199541", f"data should have e199541 with i={i}")
            self.assertEqual(di.hex, "5599e01", f"function should return 5599e01 with i={i}")
            self.assertEqual(des.data["D"][0], "5599e01", f"data should have 5599e01 with i={i}")
    
    def test_transform_4(self) -> None:
        des = DES()
        kPC = BitArray(hex="c332a83ab33c02", length=64)
        c = kPC[:28]
        d = kPC[28:]
        for i in (set([i for i in range(16)]) - set([0, 1, 8, 15])):
            ci, di, ki = des.transform(c, d, i)
            self.assertEqual(ci.hex, "0ccaa0f", f"function should return 0ccaa0f with i={i}")
            self.assertEqual(des.data["C"][0], "0ccaa0f", f"data should have 0ccaa0f with i={i}")
            self.assertEqual(di.hex, "accf00a", f"function should return accf00a with i={i}")
            self.assertEqual(des.data["D"][0], "accf00a", f"data should haveaccf00a with i={i}")

    def test_keySchedule_1(self) -> None:
        des = DES()
        k = BitArray(hex="0000000000000000", length=64)
        sched = des.keySchedule(k)
        expected = ["000000000000" for _ in range(16)]
        for i in range(16):
            self.assertEqual(sched[i].hex, expected[i], f"function should return {expected[i]}")
            self.assertEqual(des.data["ki"][i], expected[i], f"data should have {expected[i]}")
    
    def test_keySchedule_2(self) -> None:
        des = DES()
        k = BitArray(hex="0123456789abcdef", length=64)
        sched = des.keySchedule(k)
        expected = [
            "0b02679b49a5",
            "69a659256a26",
            "45d48ab428d2",
            "7289d2a58257",
            "3ce80317a6c2",
            "23251e3c8545",
            "6c04950ae4c6",
            "5788386ce581",
            "c0c9e926b839",
            "91e307631d72",
            "211f830d893a",
            "7130e5455c54",
            "91c4d04980fc",
            "5443b681dc8d",
            "b691050a16b5",
            "ca3d03b87032",
        ]
        for i in range(16):
            self.assertEqual(sched[i].hex, expected[i], f"function should return {expected[i]}")
            self.assertEqual(des.data["ki"][i], expected[i], f"data should have {expected[i]}")
    
    def test_IP_0(self) -> None:
        des = DES()
        x = BitArray(hex="0000000000000000", length=64)
        res = des.IP(x)
        self.assertEqual(res.hex, "0000000000000000", "function should return 0000000000000000")
        self.assertEqual(des.data["IP"], "0000000000000000", "data should have 0000000000000000")
    
    def test_IP_1(self) -> None:
        des = DES()
        res = des.IP(BitArray(hex="0123456789abcdef", length=64))
        self.assertEqual(res.hex, "cc00ccfff0aaf0aa", "function should return cc00ccfff0aaf0aa")
        self.assertEqual(des.data["IP"], "cc00ccfff0aaf0aa", "data should have cc00ccfff0aaf0aa")
    
    def test_E_1(self) -> None:
        des = DES()
        r = BitArray(hex="00000000", length=32)
        res = des.E(r)
        self.assertEqual(res.hex, "000000000000", "function should return 000000000000")
        self.assertEqual(des.data["E"][0], "000000000000", "data should have 000000000000")
    
    def test_E_2(self) -> None:
        des = DES()
        r = BitArray(hex="f0aaf0aa", length=32)
        res = des.E(r)
        self.assertEqual(res.hex, "7a15557a1555", "function should return 7a15557a1555")
        self.assertEqual(des.data["E"][0], "7a15557a1555", "data should have 7a15557a1555")
    
    def test_s_1(self) -> None:
        des = DES()
        r = BitArray(hex="000000000000", length=32)
        res = [des.S(r[i*6:(i+1)*6], i) for i in range(8)]
        expected = [14 ,15 ,10 ,7 ,2 ,12 ,4 ,13]
        for i in range(8):
            self.assertEqual(res[i].uint, expected[i], f"function should return {expected[i]}")
            self.assertEqual(des.data["S"][i][0], expected[i], f"data should have {expected[i]}")
    
    def test_s_2(self) -> None:
        des = DES()
        r = BitArray(hex="7a15557a1555", length=32)
        res = [des.S(r[i*6:(i+1)*6], i) for i in range(8)]
        expected = [7, 13, 5, 2, 9, 4, 5, 6]
        for i in range(8):
            self.assertEqual(res[i].uint, expected[i], f"function should return {expected[i]}")
            self.assertEqual(des.data["S"][i][0], expected[i], f"data should have {expected[i]}")

    def test_P_2(self) -> None:
        des = DES()
        r = BitArray(hex="00000000", length=32)
        res = des.P(r)
        self.assertEqual(res.hex, "00000000", "function should return 00000000")
        self.assertEqual(des.data["F"][0], "00000000", "data should have 00000000")

    def test_P_2(self) -> None:
        des = DES()
        r = BitArray(hex="efa72c4d", length=32)
        res = des.P(r)
        self.assertEqual(res.hex, "d8d8dbbc", "function should return d8d8dbbc")
        self.assertEqual(des.data["F"][0], "d8d8dbbc", "data should have d8d8dbbc")
    
    def test_F(self) -> None:
        des = DES()
        r = BitArray(hex="000000000000", length=32)
        ki = BitArray(hex="000000000000", length=32)
        res = des.F(r, ki)
        self.assertEqual(res.hex, "d8d8dbbc", "function should return d8d8dbbc")
        self.assertEqual(des.data["F"][0], "d8d8dbbc", "data should have d8d8dbbc")
    
    def test_F_1(self) -> None:
        des = DES()
        r = BitArray(hex="00000000", length=32)
        ki = BitArray(hex="000000000000", length=48)
        res = des.F(r, ki)
        self.assertEqual(res.hex, "d8d8dbbc", "function should return d8d8dbbc")
        self.assertEqual(des.data["F"][0], "d8d8dbbc", "data should have d8d8dbbc")
    
    def test_F_2(self) -> None:
        des = DES()
        r = BitArray(hex="00000000", length=32)
        ki = BitArray(hex="0b02679b49a5", length=48)
        res = des.F(r, ki)
        self.assertEqual(res.hex, "2f52d0bd", "function should return 2f52d0bd")
        self.assertEqual(des.data["F"][0], "2f52d0bd", "data should have 2f52d0bd")
    
    def test_F_3(self) -> None:
        des = DES()
        r = BitArray(hex="f0aaf0aa", length=32)
        ki = BitArray(hex="000000000000", length=48)
        res = des.F(r, ki)
        self.assertEqual(res.hex, "275bc23a", "function should return 275bc23a")
        self.assertEqual(des.data["F"][0], "275bc23a", "data should have 275bc23a")
    
    def test_F_4(self) -> None:
        des = DES()
        r = BitArray(hex="f0aaf0aa", length=32)
        ki = BitArray(hex="0b02679b49a5", length=48)
        res = des.F(r, ki)
        self.assertEqual(res.hex, "921c209c", "function should return 921c209c")
        self.assertEqual(des.data["F"][0], "921c209c", "data should have 921c209c")
    
    def test_desRound_1(self) -> None:
        des = DES()
        x = BitArray(hex="0000000000000000", length=64)
        k = BitArray(hex="000000000000", length=48)
        res = des.desRound(x, k)
        self.assertEqual(res.hex, "00000000d8d8dbbc", "function should return 00000000d8d8dbbc")
    
    def test_desRound_2(self) -> None:
        des = DES()
        x = BitArray(hex="cc00ccfff0aaf0aa", length=64)
        k = BitArray(hex="000000000000", length=48)
        res = des.desRound(x, k)
        self.assertEqual(res.hex, "f0aaf0aaeb5b0ec5", "function should return f0aaf0aaeb5b0ec5")
    
    def test_desRound_3(self) -> None:
        des = DES()
        x = BitArray(hex="0000000000000000", length=64)
        k = BitArray(hex="0b02679b49a5", length=48)
        res = des.desRound(x, k)
        self.assertEqual(res.hex, "000000002f52d0bd", "function should return 000000002f52d0bd")
    
    def test_desRound_4(self) -> None:
        des = DES()
        x = BitArray(hex="cc00ccfff0aaf0aa", length=64)
        k = BitArray(hex="0b02679b49a5", length=48)
        res = des.desRound(x, k)
        self.assertEqual(res.hex, "f0aaf0aa5e1cec63", "function should return f0aaf0aa5e1cec63")
    
    def test_FP_1(self) -> None:
        des = DES()
        z = BitArray(hex="0000000000000000", length=64)
        res = des.FP(z)
        self.assertEqual(res.hex, "0000000000000000", "function should return 0000000000000000")
        self.assertEqual(des.data["y"], "0000000000000000", "data should have 0000000000000000")
    
    def test_FP_2(self) -> None:
        des = DES()
        z = BitArray(hex="1c2087fcbbea0dc2", length=64)
        res = des.FP(z)
        self.assertEqual(res.hex, "8ca64de9c1b123a7", "function should return 8ca64de9c1b123a7")
        self.assertEqual(des.data["y"], "8ca64de9c1b123a7", "data should have 8ca64de9c1b123a7")
    
    def test_encrypt_1(self) -> None:
        des = DES()
        x = BitArray(hex="0000000000000000", length=64)
        k = BitArray(hex="0000000000000000", length=64)
        res = des.encrypt(x, k)
        self.assertEqual(res.hex, "8ca64de9c1b123a7", "function should return 8ca64de9c1b123a7")
    
    def test_encrypt_2(self) -> None:
        des = DES()
        x = BitArray(hex="0123456789abcdef", length=64)
        k = BitArray(hex="0000000000000000", length=64)
        res = des.encrypt(x, k)
        self.assertEqual(res.hex, "617b3a0ce8f07100", "function should return 617b3a0ce8f07100")
    
    def test_encrypt_3(self) -> None:
        des = DES()
        x = BitArray(hex="0000000000000000", length=64)
        k = BitArray(hex="0123456789abcdef", length=64)
        res = des.encrypt(x, k)
        self.assertEqual(res.hex, "d5d44ff720683d0d", "function should return d5d44ff720683d0d")
    
    def test_encrypt_4(self) -> None:
        des = DES()
        x = BitArray(hex="0123456789abcdef", length=64)
        k = BitArray(hex="0123456789abcdef", length=64)
        res = des.encrypt(x, k)
        self.assertEqual(res.hex, "56cc09e7cfdc4cef", "function should return 56cc09e7cfdc4cef")
    
    def test_decrypt_1(self) -> None:
        des = DES()
        x = BitArray(hex="0000000000000000", length=64)
        k = BitArray(hex="0000000000000000", length=64)
        res = des.decrypt(x, k)
        self.assertEqual(res.hex, "8ca64de9c1b123a7", "function should return 8ca64de9c1b123a7")
    
    def test_decrypt_2(self) -> None:
        des = DES()
        x = BitArray(hex="0123456789abcdef", length=64)
        k = BitArray(hex="0000000000000000", length=64)
        res = des.decrypt(x, k)
        self.assertEqual(res.hex, "617b3a0ce8f07100", "function should return 617b3a0ce8f07100")
    
    def test_decrypt_3(self) -> None:
        des = DES()
        x = BitArray(hex="0000000000000000", length=64)
        k = BitArray(hex="0123456789abcdef", length=64)
        res = des.decrypt(x, k)
        self.assertEqual(res.hex, "14aad7f4dbb4e094", "function should return 14aad7f4dbb4e094")
    
    def test_decrypt_4(self) -> None:
        des = DES()
        x = BitArray(hex="0123456789abcdef", length=64)
        k = BitArray(hex="0123456789abcdef", length=64)
        res = des.decrypt(x, k)
        self.assertEqual(res.hex, "ed31057490f985dd", "function should return ed31057490f985dd")

if __name__ == "__main__":
    unittest.main()