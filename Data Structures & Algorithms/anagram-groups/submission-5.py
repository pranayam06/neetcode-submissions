class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hash by the ordered characters since each char is 100 char max 
        hmap = defaultdict(list)
        for s in strs: 
            hmap[tuple(sorted(s))].append(s)
        return list(hmap.values())
