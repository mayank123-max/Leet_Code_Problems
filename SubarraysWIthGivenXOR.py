def solve(array, k):
    count = 0
    prefix_xor = [array[0]]
    freq = {}
    for i in array[1:]:
        prefix_xor.append(prefix_xor[-1] ^ i)
    for i in range(len(array)):
        if prefix_xor[i] == k:
            count += 1
        if freq.get(prefix_xor[i]):
            freq[prefix_xor[i]] += 1
        else:
            freq[prefix_xor[i]] = 1
        if freq.get(prefix_xor[i] ^ k):
            count += freq.get(prefix_xor[i] ^ k)
    return count

array = list(map(int,input().split()))
k = int(input())
print(solve(array, k))