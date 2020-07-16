def libraryFine(d1, m1, y1, d2, m2, y2):
    if (d1,m1,y1) > (d2,m2,y2):

if __name__ == '__main__':
    d1M1Y1 = input().split()

    d1 = int(d1M1Y1[0])

    m1 = int(d1M1Y1[1])

    y1 = int(d1M1Y1[2])

    d2M2Y2 = input().split()

    d2 = int(d2M2Y2[0])

    m2 = int(d2M2Y2[1])

    y2 = int(d2M2Y2[2])
    libraryFine(d1, m1, y1, d2, m2, y2)