class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        count = 0
        for price in sorted(costs):
            if price <= coins:
                count += 1
                coins -= price
            else:
                break
        return count
