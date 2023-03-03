from bitstring import BitArray

class DES:
    def __init__(self) -> None:
        self.dataReset()

    def dataReset(self):
        self.data = {
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

    def PC1(self, k):
        val = BitArray([k[i - 1] for i in self.data["perm"]["PC1"]])
        self.data["PC1"] = val.hex
        return val

    def PC2(self, k):
        val = BitArray([k[i - 1] for i in self.data["perm"]["PC2"]])
        self.data["ki"].append(val.hex)
        return val

    def transform(self, ci, di, i):
        if i in [0, 1, 8, 15]:
            ciEnd = ci[:1]
            diEnd = di[:1]
            ci = ci[1:]
            di = di[1:]
            ci.append(ciEnd)
            di.append(diEnd)
        else:
            ciEnd = ci[:2]
            diEnd = di[:2]
            ci = ci[2:]
            di = di[2:]
            ci.append(ciEnd)
            di.append(diEnd)
        self.data["C"].append(ci.hex)
        self.data["D"].append(di.hex)
        return ci, di, self.PC2(ci + di)

    def keySchedule(self, k):
        kPC = self.PC1(k)
        ci = kPC[:28]
        di = kPC[28:]
        self.data["C"].append(ci.hex)
        self.data["D"].append(di.hex)
        sched = []
        for i in range(16):
            ci, di, ki = self.transform(ci, di, i)
            sched.append(ki)
        return sched

    def IP(self, x):
        val = BitArray([x[i - 1] for i in self.data["perm"]["IP"]])
        self.data["IP"] = val.hex
        return val

    def E(self, ri):
        val = BitArray([ri[i - 1] for i in self.data["perm"]["E"]])
        self.data["E"].append(val.hex)
        return val

    def S(self, rzi, i):
        row = BitArray([rzi[0], rzi[5]])
        col = BitArray(rzi[1:5])
        val = BitArray(uint=self.data["perm"]["S"][i][row.uint][col.uint], length=4)
        self.data["Srow"][i].append(row.bin)
        self.data["Scol"][i].append(col.bin)
        self.data["S"][i].append(val.uint)
        return val

    def P(self, rzi):
        val = BitArray([rzi[i - 1] for i in self.data["perm"]["P"]])
        self.data["F"].append(val.hex)
        return val

    def F(self, ri, ki):
        rzi = self.E(ri) ^ ki
        self.data["EXor"].append(rzi.hex)
        rzi = sum([self.S(rzi[i*6:(i+1)*6], i) for i in range(8)])
        return self.P(rzi)

    def desRound(self, zi, ki):
        li = zi[:32]
        ri = zi[32:]
        self.data["L"].append(li.hex)
        self.data["R"].append(ri.hex)
        return ri + (li ^ self.F(ri, ki))

    def FP(self, z, decrypt=False):
        val = BitArray([z[i - 1] for i in self.data["perm"]["FP"]])
        if decrypt:
            self.data["x"] = val.hex
        else:
            self.data["y"] = val.hex
        return val

    def encrypt(self, x, k):
        self.dataReset()
        self.data["x"] = x.hex
        self.data["k"] = k.hex
        zi = self.IP(x)
        kis = self.keySchedule(k)
        for i in range(16):
            zi = self.desRound(zi, kis[i])
        return self.FP(zi[32:] + zi[:32])

    def decrypt(self, y, k):
        self.dataReset()
        self.data["y"] = y.hex
        self.data["k"] = k.hex
        zi = self.IP(y)
        kis = self.keySchedule(k)
        kis = kis[::-1]
        for i in range(16):
            zi = self.desRound(zi, kis[i])
        return self.FP(zi[32:] + zi[:32], decrypt=True)


def call(action, encoding, inText, key):
    des = DES()
    if action == "encrypt":
        x = BitArray(hex=inText, length=64)
        k = BitArray(hex=key, length=64)
        des.encrypt(x, k)
    return des.data

if __name__ == "__main__":
    x = BitArray(hex="166B40B44ABA4BD6", length=64)
    k = BitArray(hex="0000000000000001", length=64)
    des = DES()
    try:
        # des.encrypt(x, k)
        des.decrypt(x, k)
    except Exception as e:
        for k, v in des.data.items():
            if k != "perm":
                print(k, v)    
        raise e
    for k, v in des.data.items():
        if k != "perm":
            print(k, v)