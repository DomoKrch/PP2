class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alts = []
        val = 0
        alts.append(val)

        for i in range(len(gain)):
            val = val + gain[i]
            alts.append(val)

        val = 0
        for i in range(len(alts)):
            if val < alts[i]:
                val = alts[i]

        return val
