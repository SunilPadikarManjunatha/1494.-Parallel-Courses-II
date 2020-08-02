import math
from itertools import combinations
import copy

class Solution:
    roots = []

    def minNumberOfSemesters(self, n: int, dependencies, k: int) -> int:

        levels = {n: [] for n in range(1, n+1)}
        
        subs = [i for i in range(1, n+1)]

        for dep in dependencies:
            if dep[0] in subs:
                subs.remove(dep[0])
            if  dep[1] in subs:
                subs.remove(dep[1])

        self.roots = self.get_root(dependencies,n) + subs
        visited = []
        queue = []
        self.aeiou = []
        self.check_dep(self.roots,[], dependencies, queue, k,n)
        print(self.aeiou)
        return (min(self.aeiou))


    def check_dep(self,poss, visited,dependencies, queue, k,n):
        if poss  == [] and len(visited) == n:
            return self.aeiou.append(len(queue))
        vis = copy.deepcopy(visited)
        q = copy.deepcopy(queue)
        if math.comb(n,k) <= len(self.aeiou): return 
        if len(poss) <= k:
            q.append(poss)
            for p in poss: 
                if p not in vis: vis.append(p)
            aoptions = self.get_options(dependencies, vis,n)
            self.check_dep(aoptions,vis,dependencies,q,k,n)
        else:
            options = combinations(poss,k)
            for option in options:
                q.append(option)
                for p in option: 
                    if p not in vis:
                        vis.append(p)
                aoptions = self.get_options(dependencies, vis,n)
                self.check_dep(aoptions,vis,dependencies,q,k,n)
                q.pop()
                
                for p in option: 
                    vis.remove(p)


    def get_options(self, dependencies, visited,n):
        options = []
        no_deps = []
        for i in range(1, n+1):
            if i not in no_deps and i not in visited: no_deps.append(i)

        for i in range(1, n+1):
            if i in visited: continue
            skip = False
            for dep in dependencies:
                if dep[0] in no_deps: no_deps.remove(dep[0])
                if dep[1] in no_deps: no_deps.remove(dep[1])

                if i == dep[1] and dep[0] not in visited:
                    skip = True
                    break

            if not skip and i not in options:
                options.append(i)
        for no_dep in no_deps:
            if no_dep not in options:
                options.append(no_dep)

        return options

    def get_root(self, dependencies,n):
        
        roots = []
        for i in range(1,n+1):
            node = [k for k in dependencies if k[0] == i]
            child = [k for k in dependencies if k[1] == i]
            if child == [] and node != []:
                roots.append(node[0][0])

        return roots

sol = Solution()

print(sol.minNumberOfSemesters(15,[[2,1]],4))
print(sol.minNumberOfSemesters(5,[[2,1],[3,1],[4,1],[1,5]],2))
print(sol.minNumberOfSemesters(4,[[2,1],[3,1],[1,4]],2))
print(sol.minNumberOfSemesters(5,[[2,1],[3,1],[4,1],[1,5]],2))
print(sol.minNumberOfSemesters(11,[],2))
print(sol.minNumberOfSemesters(4,[[2,1],[2,4]],2))
print(sol.minNumberOfSemesters(5,[[3,1]],4))
print(sol.minNumberOfSemesters(5, [[1,5],[1,3],[1,2],[4,2],[4,5],[2,5],[1,4],[4,3],[3,5],[3,2]],3))
print(sol.minNumberOfSemesters(12,[[1,2],[1,3],[7,5],[7,6],[4,8],[8,9],[9,10],[10,11],[11,12]],2))