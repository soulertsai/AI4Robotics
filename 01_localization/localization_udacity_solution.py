def sense(p, colors, measurement):
	aux = [[0.0 for row in range(len(p[0]))] for col in range(len(p))]

	s = 0.0

	for i in range(len(p)):
		for j in range(len(p[i])):
			hit = (colors[i][j] == measurement)
			aux[i][j] = p[i][j] * (sensor_right * hit + (1 - sensor_right) * (1 - hit))
			s += aux[i][j]

	for i in range(len(aux)):
		for j in range(len(aux[i])):
			aux[i][j] /= s

	return aux


def move(p, motion):
	aux = [[0.0 for row in range(len(p[0]))] for col in range(len(p))]

	for i in range(len(p)):
		for j in range(len(p[i])):
			aux[i][j] = p_move * p[(i - motion[0]) % len(p)][(j - motion[1]) % len(p[i])] + (1 - p_move) * p[i][j]

	return aux

def show(p):
    rows = ['[' + ','.join(map(lambda x: '{0:.5f}'.format(x),r)) + ']' for r in p]
    print '[' + ',\n '.join(rows) + ']'



colors = [['R','G','G','R','R'],
          ['R','R','G','R','R'],
          ['R','R','G','G','R'],
          ['R','R','R','R','R']]
measurements = ['G','G','G','G','G']
motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

p_move = 0.8
sensor_right = 0.7

pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]

for k in range(1):
	print k
	p = move(p, motions[k])
	p = sense(p, colors, measurements[k])

show(p)