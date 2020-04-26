while 1:
    def solved(rooms):
        n = len(rooms)

        visited = [0 for _ in range(n)]
        def sarch(rooms, now, visited):

            for i in rooms[now]:
                if visited[i] == 0:
                    visited[i] = 1
                    sarch(rooms, i, visited)

        visited[0] = 1
        sarch(rooms, 0, visited)
        if sum(visited) == n:
            return True
        else:
            return False
    rooms = [[1,3],[3,0,1],[2],[0]]
    solved(rooms)
    break
