def localize(colors,measurements,motions,sensor_right,p_move):
    pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
    p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]
    
    # execute once after move & sense
    for sequence in range(len(motions)):
        pcopy = [x[:] for x in p]
        move = motions[sequence]
        dy = move[0]
        dx = move[1]
        for y in range(len(pcopy)):
            for x in range(len(pcopy[0])):
                pcopy[y][x] = p[(y - dy) % len(p)][(x - dx) % len(p[y])] * p_move + p[y][x] * (1 - p_move)

        seqMeasure = measurements[sequence]
        for y in range(len(pcopy)):
            for x in range(len(pcopy[0])):
                hit = (seqMeasure == colors[y][x])
                pcopy[y][x] = pcopy[y][x] * (hit * sensor_right + (1 - hit) * (1 - sensor_right))

        p = [x[:] for x in pcopy]
        
    sum_l = map(lambda x: sum(x), p)
    sum_l = sum(sum_l)
    
    for y in range(len(p)):
        for x in range(len(p[0])):
            p[y][x] = p[y][x] / float(sum_l)
    
    return p

def show(p):
    rows = ['[' + ','.join(map(lambda x: '{0:.5f}'.format(x),r)) + ']' for r in p]
    print '[' + ',\n '.join(rows) + ']'
    
#############################################################
# For the following test case, your output should be 
# [[0.01105, 0.02464, 0.06799, 0.04472, 0.02465],
#  [0.00715, 0.01017, 0.08696, 0.07988, 0.00935],
#  [0.00739, 0.00894, 0.11272, 0.35350, 0.04065],
#  [0.00910, 0.00715, 0.01434, 0.04313, 0.03642]]
# (within a tolerance of +/- 0.001 for each entry)

colors = [['R','G','G','R','R'],
          ['R','R','G','R','R'],
          ['R','R','G','G','R'],
          ['R','R','R','R','R']]
measurements = ['G','G','G','G','G']
motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]
p = localize(colors,measurements,motions,sensor_right = 0.7, p_move = 0.8)
show(p)