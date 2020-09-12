import sys
input = sys.stdin.readline

def del_special(new_id):
    special = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5',
               '6', '7', '8', '9', '-', '_', '.']
    new_id = list(new_id)
    new_id = [e for e in new_id if e in special]
    return ''.join(new_id)

def del_dot(new_id):
    result = []
    for idx, e in enumerate(new_id):
        if idx == len(new_id) - 1:
            result.append(e)
            return result
        if e == '.' and new_id[idx + 1] == '.': continue
        else: result.append(e)

def del_dot2(new_id):
    if len(new_id) != 0:
        if new_id[0] == '.':
            new_id = new_id[1:]
    if len(new_id) != 0:
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    if len(new_id) == 0:
        new_id.append('a')
    return new_id

def limit_len(new_id):
    new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    return new_id

def dupli(new_id):
    if len(new_id) <= 2:
        l = new_id[-1]
        while len(new_id) != 3:
            new_id.append(l)
    return new_id

def main(new_id):
    new_id = new_id.lower()
    new_id = del_special(new_id)
    new_id = del_dot(new_id)
    new_id = del_dot2(new_id)
    new_id = limit_len(new_id)
    new_id = dupli(new_id)
    answer = ''.join(new_id)
    print(answer)
    return answer

if __name__ == '__main__':
    ex = ["...!@BaT#*..y.abcdefghijklm", "z-+.^.", 	"=.=", "123_.def", "abcdefghijklmn.p"]
    for new_id in ex:
        main(new_id)
        # break