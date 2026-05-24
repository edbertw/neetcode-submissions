class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        """
        TO-DO

        must find a way to first create an ordered graph like DAGs

        after that just use Kahn's algorithm to output the sequence

        1. Compare two adjacent entries in the input list. 
        2. Traverse the two entries until we find a different letter. 
          Say we traversed till i-th index, then entry1[i] < entry2[i] and add this to the DAG
        3. Do Khan's algo, then return the list


        """
        adj = {c: set() for w in words for c in w}
        in_degree = {c:0 for c in adj}
        for i in range(1, len(words)):
            prev_word = words[i-1]
            cur_word = words[i]
            minlen = min(len(prev_word), len(cur_word))
            if len(prev_word) > len(cur_word) and prev_word[:minlen] == cur_word[:minlen]:
                return "" 
            
            for j in range(minlen):
                if prev_word[j] != cur_word[j]:
                    if cur_word[j] not in adj[prev_word[j]]:
                        adj[prev_word[j]].add(cur_word[j])
                        in_degree[cur_word[j]] += 1
                    break

        q = deque([i for i in in_degree if in_degree[i] == 0])
        res = []

        while q:
            cur = q.popleft()
            res.append(cur)
            for neigh in adj[cur]:
                in_degree[neigh] -= 1
                if in_degree[neigh] == 0:
                    q.append(neigh)
        
        if len(res) != len(in_degree):
            return ""
        
        return "".join(res)





        
        









        
