import time

n = int(input())

counts = {0: 0, 1: 0}
def get_count(i):
  if i in counts:
    return counts[i]
  # counts[i] = min(get_count(i // 3) + i % 3, get_count(i // 2) + i % 2, get_count(i-1)) + 1

  li = [i-1, 0, 0]
  if i % 3 == 0:
    li[2] = i/3
  if i % 2 == 0:
    li[1] = i/2

  if li[1] == 0 and li[2] == 0:
    counts[i] = get_count(li[0]) + 1
  elif li[1] == 0:
    counts[i] = min(get_count(li[2]), get_count(li[0])) + 1
  elif li[2] == 0:
    counts[i] = min(get_count(li[1]), get_count(li[0])) + 1
  else:
    counts[i] = min(get_count(i // 3) + i % 3, get_count(i // 2) + i % 2, get_count(i-1)) + 1

  return counts[i]
'''
counts = {0: 0, 1: 0}
def get_count(i):
  if i in counts:
    return counts[i]
  counts[i] = min(get_count(i // 3) + i % 3, get_count(i // 2) + i % 2, get_count(i-1)) + 1
  return counts[i]
'''
start = time.time()
print(get_count(n))
end = time.time()
print((end - start)*1000)