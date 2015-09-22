__author__ = 'Vineets'

def pagerank(graph, beta, total=3., iteration=5):
        n = len(graph)
        # initialize importance
        prev = [total/n] * n
        curr = [0] * n
        degree = [0] * n

        for i in range(n):
            for j in range(n):
                if graph[i][j] > 0:
                    degree[j] += 1

        print 'initial value of pagerank:', prev
        for it in range(iteration):
            for col in range(n):
                cols = sum([graph[row][col] * 1. for row in range(n)])
            # normalization
            for row in range(n):
                if cols == 0:
                    print 'error: ', [graph[row][col] for row in range(n)]
                    graph[row][col] = (1. / n) * total
                else:
                    graph[row][col] = (graph[row][col] * 1. / cols) * total

            for i in range(n):
                for j in range(n):
                    if graph[i][j] > 0:
                        curr[i] += beta * prev[j] / degree[j]
            curr[i] += (1 - beta) * (total / n)
            # prev = curr will lead to shallow copy problem
            t = sum(curr)
            # normalization
            prev = [(score / t) * total for score in curr]

            print 'score after', it + 1, 'iterations:', prev
            curr = [0] * n

        return

if __name__ == '__main__':
    # given data
    beta = 0.7
    total = 3
    V = 3

    # create the graph
    graph = [[0]*V for _ in range(V)]
    a, b, c = 0, 1, 2
    graph[a][b] = 1
    graph[a][c] = 1
    graph[c][a] = 1
    graph[b][c] = 1
    pagerank(graph, beta= 1., iteration = 10)