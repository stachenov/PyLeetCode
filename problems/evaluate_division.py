from collections import defaultdict


class Solution(object):
    def calcEquation(self, equations, values, query):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type query: List[List[str]]
        :rtype: List[float]
        """
        eqs_for = dict((x, {x: 1})
                       for eq in equations
                       for x in eq)
        eqs_for.update(dict((eq[0], {eq[1]: float(val)})
                            for eq, val in zip(equations, values)))
        eqs_for.update(dict((eq[1], {eq[0]: 1 / float(val)})
                            for eq, val in zip(equations, values) if val != 0))
        zeroes = set(eq[0] for eq, val in zip(equations, values) if val == 0)

        def expand(x, y):
            if any(z in zeroes for z in eqs_for[y]):
                zeroes.add(x)
            for z in set(eqs_for[y].keys()) - set(eqs_for[x].keys()):
                eqs_for[x][z] = eqs_for[x][y] * eqs_for[y][z]
                expand(x, z)

        for x in eqs_for:
            for y in eqs_for[x].keys():
                expand(x, y)
        res = []
        for x, y in query:
            if x in zeroes:
                res.append(0)
            elif x not in eqs_for or y not in eqs_for:
                res.append(-1)
            else:
                common = set(eqs_for[x].keys()) & set(eqs_for[y].keys())
                if not common:
                    res.append(-1)
                else:
                    z = common.pop()
                    res.append(eqs_for[x][z] / eqs_for[y][z])
        return res
