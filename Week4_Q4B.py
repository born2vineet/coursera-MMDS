__author__ = 'Vineets'

from math import sqrt

v = [2./7, 3./7, 6./7]
candidates = [[-.937, .312, .156],[-.548, .401, .273], [2.250, -.500, -.750], [.485, -.485, .728]]
for cand in candidates:
    norm = sqrt(sum([i * i for i in cand]))
    if abs(norm - 1) > 0.01:
    	print 'wrong answer:', cand
    	continue
    dot_product = sum([i * j for (i, j) in zip(v, cand)])
    if abs(dot_product) > 0.01:
    	print 'wrong answer:', cand
    else:
    	print 'correct answer:', cand