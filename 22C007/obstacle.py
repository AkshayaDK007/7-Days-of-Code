def shortest_path(t, test_cases):
    results = []

    for _ in range(t):
        xA, yA, xB, yB, xF, yF = test_cases[_]

        distance_AB = abs(xA - xB) + abs(yA - yB)

        if (xA == xB and xB == xF and min(yA, yB) < yF < max(yA, yB)) or \
           (yA == yB and yB == yF and min(xA, xB) < xF < max(xA, xB)):
            distance_AB += 2
        
        results.append(distance_AB)

    return results

t = int(input())

test_cases = []

# Process each test case
for _ in range(t):
    input()  # Consume empty line
    xA, yA = map(int, input().split())
    xB, yB = map(int, input().split())
    xF, yF = map(int, input().split())
    test_cases.append((xA, yA, xB, yB, xF, yF))

results = shortest_path(t, test_cases)

for result in results:
    print(result)
