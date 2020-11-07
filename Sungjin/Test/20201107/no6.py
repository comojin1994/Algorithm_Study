def organize(logs):
    results = dict()
    for log in logs:
        user_id, no, score = log.split(' ')
        if user_id not in results.keys():
            results[user_id] = dict()
        results[user_id][no] = score

    return results


def preprocess(scores):
    users = dict()
    for user_id in scores:
        solved = len(scores[user_id].items())
        if solved >= 5:
            if solved not in users.keys():
                users[solved] = []
            users[solved].append(user_id)
    return users


def checkCheat(users, scores):
    result = set()
    for idx, user in enumerate(users):
        check = scores[user].items()
        for jdx, user_ in enumerate(users):
            if jdx <= idx: continue
            if check == scores[user_].items():
                result.add(user)
                result.add(user_)
    return list(result)


def solution(logs):
    cheater = []
    scores = organize(logs)
    users = preprocess(scores)
    for solved in users.keys():
        same_solved_users = users[solved]
        cheat = checkCheat(same_solved_users, scores)
        cheater += cheat
    if len(cheater) == 0: cheater = ["None"]
    return cheater


if __name__ == '__main__':
    LOGS = [
        ["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80", "0001 10 90", "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"],
        ["1901 1 100", "1901 2 100", "1901 4 100", "1901 7 100", "1901 8 100", "1902 2 100", "1902 1 100", "1902 7 100",
         "1902 4 100", "1902 8 100", "1903 8 100", "1903 7 100", "1903 4 100", "1903 2 100", "1903 1 100", "2001 1 100",
         "2001 2 100", "2001 4 100", "2001 7 95", "2001 9 100", "2002 1 95", "2002 2 100", "2002 4 100", "2002 7 100",
         "2002 9 100"],
        ["1901 10 50", "1909 10 50"]
    ]
    for logs in LOGS:
        print(solution(logs))
        break
