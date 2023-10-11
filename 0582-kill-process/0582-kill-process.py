class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        child_dict = collections.defaultdict(list)
        ans = []
        for ind in range(len(pid)):
            child_dict[ppid[ind]].append(pid[ind])
        p_to_kill = [kill]
        while p_to_kill:
            tmp = []
            for id in p_to_kill:
                ans.append(id)
                tmp.extend(child_dict[id])
            p_to_kill = tmp
        return ans
