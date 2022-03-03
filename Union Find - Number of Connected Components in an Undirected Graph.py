class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #union find algorithm
        
        parent = [i for i in range(n)] #index = number, value = parent node it is connected to
        rank = [1] * n #index = number, value = how many nodes are connected to this node
        #child nodes will have a rank of 1, parent nodes > 1 unless its a standalone node
        
        def find(node1): #finds the parent of a node
            result = node1
            while result != parent[result]:
                parent[result] = parent[parent[result]] #optimization to set the parent to the grandparent
                #useful to optimize long chains of parents, will do nothing if there is no grandparent
                result = parent[result]
            return result
        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            if parent1 == parent2: #they already have the same parent
                return 0 #no union is needed, because they are probably already connected
            
            #actually do the union
            if rank[parent2]>rank[parent1]: #parent2 will be the parent of parent1
                parent[parent1]= parent2
                rank[parent2] += 1
            else:
                parent[parent2]= parent1 #parent1 is parent of parent2
                rank[parent1] += 1
            return 1 #union successful
        
        result = n
        for n1, n2 in edges:
            result -= union(n1, n2) #every time a successful union is made decrement num components by 1
        return result
