def can_build_string(s):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for word in ["aa", "aaa", "bb", "bbb"]:
            if i >= len(word) and dp[i - len(word)] and s[i - len(word):i] == word:
                dp[i] = True
    return dp[n]
t = int(input())
for _ in range(t):
    s = input()
    if can_build_string(s):
        print("YES")
    else:
        print("NO")