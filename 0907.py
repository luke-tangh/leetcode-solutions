class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        arr = [0] + arr
        result = [0]*len(arr)
        st = [0]
        for i in range(len(arr)):
            while arr[st[-1]] > arr[i]:
                st.pop()
            j = st[-1]
            result[i] = result[j] + (i-j)*arr[i]
            st.append(i)
        return sum(result) % (10**9+7)
