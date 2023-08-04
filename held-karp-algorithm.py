def tsp_held_karp(distances):
    n = len(distances)
    memo = {}

    def dp(mask, pos):
        if mask == (1 << n) - 1:
            return distances[pos][0]
        
        if (mask, pos) in memo:
            return memo[(mask, pos)]

        ans = float('inf')
        for nxt in range(n):
            if not mask & (1 << nxt):
                ans = min(ans, distances[pos][nxt] + dp(mask | (1 << nxt), nxt))
        
        memo[(mask, pos)] = ans
        return ans

    min_distance = dp(1, 0)  # Start from node 0
    return min_distance

# Example usage
distances = [
    [0, 29, 20, 21],
    [29, 0, 15, 26],
    [20, 15, 0, 27],
    [21, 26, 27, 0]
]

min_distance = tsp_held_karp(distances)
print("Minimum distance:", min_distance)
