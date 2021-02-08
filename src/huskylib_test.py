import pytest

class BusMock:
    def __init__(self, send):
        self.send = send
        self.recv = []

    def write(self, address , data):
        cmd = ''.join('{:02x}'.format(x) for x in bytearray(data))
        self.recv.append(cmd)

    def read(self, address , datalen):

        if len(self.send) == 0:
            raise Exception("Cannot read data")
        
        cmd = self.send.pop(0)

        return bytes.fromhex(cmd) 

def test_init():
    from huskylib import HuskyLensLibrary
    huskyLens = HuskyLensLibrary(None,address=0x32)

def test_algorithm():
    from huskylib import HuskyLensLibrary
    busmock = BusMock(["55aa11002E","3E"])
    huskyLens = HuskyLensLibrary(busmock,address=0x32)
    huskyLens.algorthim("ALGORITHM_FACE_RECOGNITION")

    assert 1 == len(busmock.recv)
    assert "55aa11022d00003f" == busmock.recv[0]


def test_blocks():
    from huskylib import HuskyLensLibrary
    from huskylib import Block
    busmock = BusMock(["55aa110A29","01000000000000000000FF",
                       "55AA110A2A","2C01C8000A001400010058"])

    huskyLens = HuskyLensLibrary(busmock,address=0x32)
    data = huskyLens.blocks()
    assert 1 == len(data)
    assert 1 == data[0].ID
    assert 1 == len(busmock.recv)
    assert "55aa11002131" == busmock.recv[0]

