from itertools import permutations
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    eq = input().strip()
    op = ['+', '-', '*']
    op_li = list(permutations(op))
    max_ = 0
    for f, s, t in op_li:
        eq_s = eq.split(t)
        for idx, e in enumerate(eq_s):
            eq_s[idx] = e.split(s)
        for i in range(len(eq_s)):
            for j in range(len(eq_s[i])):
                eq_s[i][j] = eval(eq_s[i][j])
            eq_s[i] = eval(s.join(map(str, eq_s[i])))
        eq_s = abs(eval(t.join(map(str, eq_s))))
        if max_ < eq_s: max_ = eq_s
    print(max_)
'''
+ - *
+ * -
- + *
- * +
* + -
* - +
'''