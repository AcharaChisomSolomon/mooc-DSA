import math


def get_area(rec: tuple):
    (x1, y1, x2, y2) = rec

    width = abs(x1 - x2)
    height = abs(y1 - y2)

    return width * height


def get_overlap_area(rec1, rec2):
    area = 0
    (rec1_x1, rec1_y1, rec1_x2, rec1_y2) = rec1
    (rec2_x1, rec2_y1, rec2_x2, rec2_y2) = rec2


    if rec1_x2 <= rec2_x1 or rec1_x1 >= rec2_x2 or rec1_y2 >= rec2_y1 or rec1_y1 <= rec2_y2:
            print(area, None)
            return area, None

    new_rec_x1 = rec2_x1
    new_rec_y1 = rec1_y1

    new_rec_x2 = 0
    new_rec_y2 = 0

    if rec1_x1 < rec2_x1:
        new_rec_x1 = rec2_x1
    else:
        new_rec_x1 = rec1_x1

    if rec1_y1 > rec2_y1:
        new_rec_y1 = rec2_y1

    if rec1_x2 > rec2_x2:
        new_rec_x2 = rec2_x2
    else:
        new_rec_x2 = rec1_x2

    if rec1_y2 < rec2_y2:
        new_rec_y2 = rec2_y2
    else:
        new_rec_y2 = rec1_y2

    area = get_area((new_rec_x1, new_rec_y1, new_rec_x2, new_rec_y2))

    print(area, (new_rec_x1, new_rec_y1, new_rec_x2, new_rec_y2))
    return area, (new_rec_x1, new_rec_y1, new_rec_x2, new_rec_y2)


def area(rec1, rec2, rec3):
    has_overlap = False
    recs = [rec1, rec2, rec3]
    total_area = get_area(rec1) + get_area(rec2) + get_area(rec3)
    print('initial total:', total_area)

    for i in range(len(recs)):
        for j in range(i + 1, len(recs)):
            area = get_overlap_area(recs[i], recs[j])
            if area[1] != None:
                has_overlap = True
            total_area -= area[0]

    if has_overlap:
        print('triple:::')
        triple_overlap = (0, rec1)
        for i in range(1, len(recs)):
            triple_overlap = get_overlap_area(triple_overlap[1], recs[i])
            if triple_overlap[1] == None:
                break

        if triple_overlap[1] == None:
            pass
        else:
            total_area += triple_overlap[0]

    return int(total_area)


if __name__ == "__main__":
    rec1 = (37904748,847088754,800763268,371024299)
    rec2 = (-516071731,-515113038,597607792,-681585739)
    rec3 = (22452616,638287530,729050355,350766166)
    print(area(rec1,rec2,rec3)) #567011201506428002