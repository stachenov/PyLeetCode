class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        state_chars = []
        state_transitions = []
        i = 0
        while i < len(p):
            if i == len(p) - 1 or p[i + 1] != '*':
                state_chars.append(p[i])
                state_transitions.append([len(state_chars)])
                i += 1
            else:
                state_chars.append(None) # fork
                state_transitions.append([len(state_chars), len(state_chars) + 1])
                state_transitions.append([len(state_chars) - 1])
                state_chars.append(p[i])
                i += 2
        def follow_forks(state):
            if state < len(state_chars) and state_chars[state] is None:
                return {s for t in state_transitions[state] for s in follow_forks(t)}
            else:
                return {state}
        def next_states(state, char):
            if state == len(state_chars) or state_chars[state] != '.' and state_chars[state] != char:
                return {}
            else:
                return follow_forks(state_transitions[state][0])
        states = follow_forks(0)
        for c in s:
            states = {ns for state in states for ns in next_states(state, c)}
        return len(state_chars) in states
