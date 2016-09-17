class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        start = []
        state = start
        i = 0
        statelist = [start]
        while i < len(p):
            if i == len(p) - 1 or p[i + 1] != '*':
                new_state = []
                state += [p[i], len(statelist)]
                statelist.append(new_state)
                state = new_state
                i += 1
            else:
                repeat_state, new_state = [p[i], len(statelist) - 1], []
                state += [len(statelist), len(statelist) + 1]
                statelist += [repeat_state, new_state]
                state = new_state
                i += 2
        final_state = len(statelist) - 1
        def follow_forks(state):
            if not statelist[state] or type(statelist[state][0]) is not int:
                return {state}
            else:
                return {s for t in statelist[state] for s in follow_forks(t)}
        states = follow_forks(0)
        for c in s:
            new_states = set()
            for state in states:
                if not statelist[state] or (statelist[state][0] != '.' and statelist[state][0] != c):
                    continue
                new_states |= follow_forks(statelist[state][1])
            if not new_states:
                return False
            states = new_states
        return final_state in states
