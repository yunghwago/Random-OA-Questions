class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        #solution: run BFS simultaneously from every gate 
        ROWS, COLS = len(rooms), len(rooms[0])
        visited = set()
        queue = deque()
        
        def addRoom(row, column):
            #check for out of bounds OR room in visited OR room is a wall
            if(row < 0 or row >= ROWS or column < 0 or column >= COLS
              or (row,column) in visited or rooms[row][column] == -1):
                return
            else:
                visited.add((row,column))
                queue.append([row,column])
                
        #initialize queue with gate positions
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    queue.append([r,c])
                    visited.add((r,c))
        
        #actually start doing our BFS
        distance = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                rooms[r][c] = distance #replace gate with gate, or INF with current distance
                #add all rooms adjacent to the one updated to the queue
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
                #some of these rooms might be out of bounds, or in visited, which is why a helper
                #function is nice here, to handle that logic
            distance += 1
