class Solution {
public:
    string foreignDictionary(vector<string>& words) {
        unordered_map<char, unordered_set<char>> adj;
        unordered_map<char, int> indegree;
        
        for (string w: words) {
            for (char c: w) {
                adj[c] = unordered_set<char>();
                indegree[c] = 0;
            }
        }

        for (int i = 0; i < words.size() - 1; i++) {
            string w1 = words[i];
            string w2 = words[i+1];
            int minlen = min(w1.size(), w2.size());
            if (w1.size() > w2.size() && w1.substr(0, minlen) == w2.substr(0, minlen)) {
                return "";
            }

            for (int j = 0; j < minlen; j++) {
                if (w1[j] != w2[j]) {
                    if (!adj[w1[j]].count(w2[j])) {
                        adj[w1[j]].insert(w2[j]);
                        indegree[w2[j]]++;
                    }
                    break;
                }
            }
        }
        queue<char> q;
        for (auto &[c, deg]: indegree) {
            if (deg == 0) {
                q.push(c);
            }
        }

        string res;
        while (!q.empty()) {
            char chr = q.front();
            q.pop();
            res += chr;
            for (char neighbor : adj[chr]) {
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }

        if (res.size() != indegree.size()){
            return "";
        } else {
            return res;
        }

            
            
        
    }
};
