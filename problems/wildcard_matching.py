class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        class State:
            def __init__(self):
                self.char = None
                self.repeat = None
                self.next = None
                self.prev = None
                self.shortest = None
        initial = State()
        final = initial
        for c in p:
            next = State()
            if c == '*':
                final.repeat = State()
                final.repeat.char = '?'
                final.repeat.next = final
            else:
                final.char = c
            final.next = next
            next.prev = final
            final = next
        final.shortest = 0
        state = final.prev
        while state is not None:
            if state.repeat is None:
                state.shortest = state.next.shortest + 1
            else:
                state.shortest = state.next.shortest
            state = state.prev
        def follow_forks(state):
            if state.repeat is None:
                return {state}
            else:
                return follow_forks(state.repeat) | follow_forks(state.next)
        states = follow_forks(initial)
        for i, c in enumerate(s):
            rem = len(s) - i
            next_states = set()
            for state in states:
                if (state.char == '?' or state.char == c) and state.shortest <= rem:
                    next_states |= follow_forks(state.next)
            states = next_states
        return final in states
