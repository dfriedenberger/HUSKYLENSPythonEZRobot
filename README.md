
## EZ Robot porting of HUSKYLENS Python Library

Ported Version from Raspberry Pi HUSKYLENS python Library (https://github.com/HuskyLens/HUSKYLENSPython) to EZ Robot ( https://www.ez-robot.com/ , https://synthiam.com/)

## get started

1. Copy content of huskylib.py to python tab of script element.
2. Create sample program

### detect faces
```
huskyLens = HuskyLensLibrary(Bus(),address=0x32)
huskyLens.algorthim("ALGORITHM_FACE_RECOGNITION")
while(true):
    data=huskyLens.blocks()
    x=0
    for i in data:
        x=x+1
        print("Face {} ID: {}".format(x,i.ID)
```
