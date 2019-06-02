def read_data(filename, N):
    # define class *point*
    class point:
        def __init__(self, point_id, point_coordination):
            self.layer = 0
            self.id = point_id
            self.coordination = point_coordination
            self.times = 0

    # read file
    f = open(filename, 'r')
    lines = f.readlines()
    raw_list = []
    for i in range(0, N):
        line = lines[i]
        p = []
        for i in line.split():
            p.append(float(i))
        raw_list.append(p)

    # construct a list of point
    index = 0
    point_list = []
    for item in raw_list:
        new_point = point(index, list(item))
        point_list.append(new_point)
        index += 1
    return point_list, raw_list

def order_points(data, _if_all_dimension):
    Dimension = len(data[0])
    Number = len(data)
    order = []
    for i in range(0, Number):
        data[i].append(i)

    if _if_all_dimension == 1:
        for i in range(0, Dimension):
            sorted_list = sorted(data, key=lambda p: p[i])
            column = [x[Dimension] for x in sorted_list]
            order.append(column)
    else:
        sorted_list = sorted(data, key=lambda p: p[0])
        order = [x[Dimension] for x in sorted_list]
    return order


def print_result(model, t1, t2, t3, t4):
    print 'Model:                          ',
    print model
    print 'Time for ordering:              ',
    print t1
    print 'Time for to construct layers:   ',
    print t2
    print 'Total time consumption:         ',
    print t3
    print