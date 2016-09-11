def expand(eqs_for, x, y, zeroes):
    for z in eqs_for[y].keys():
        if z in zeroes:
            zeroes.add(x)
        elif z not in eqs_for[x].keys():
            eqs_for[x][z] = eqs_for[x][y] * eqs_for[y][z]
            expand(eqs_for, x, z, zeroes)


class Solution(object):
    def calcEquation(self, equations, values, query):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type query: List[List[str]]
        :rtype: List[float]
        """
        eqs_for = {}
        zeroes = set()
        for i in xrange(0, len(equations)):
            eq = equations[i]
            val = float(values[i])
            if val == 0:
                zeroes += eq[0]
            else:
                eqf = eqs_for.get(eq[0], {eq[0]: 1})
                eqf[eq[1]] = val
                eqs_for[eq[0]] = eqf
                eqf = eqs_for.get(eq[1], {eq[1]: 1})
                eqf[eq[0]] = 1 / val
                eqs_for[eq[1]] = eqf
        for x in eqs_for:
            for y in eqs_for[x].keys():
                expand(eqs_for, x, y, zeroes)
        res = []
        for q in query:
            if q[0] in zeroes:
                res.append(0)
            elif q[0] not in eqs_for or q[1] not in eqs_for:
                res.append(-1)
            else:
                eq0 = eqs_for[q[0]]
                eq1 = eqs_for[q[1]]
                common = set(eq0.keys()).intersection(set(eq1.keys()))
                if not common:
                    res.append(-1)
                else:
                    k = common.pop()
                    res.append(eq0[k] / eq1[k])
        return res
