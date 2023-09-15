class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        em_to_name = {}
        graph = collections.defaultdict(set)
        
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                # use acc[1] to build a bridge
                graph[email].add(acc[1])
                graph[acc[1]].add(email)
                em_to_name[email] = name
        print(graph)
        seen = set()
        ans = []
        for email in graph:
            if email not in seen:
                seen.add(email)
                component = []
                stack = [email]
                while stack:
                    node = stack.pop()
                    component.append(node)
                    for nei in graph[node]:
                        if nei not in seen:
                            stack.append(nei)
                            seen.add(nei)
            
                ans.append([em_to_name[email]] + sorted(component))
        
        return ans  
              