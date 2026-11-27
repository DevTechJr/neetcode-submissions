class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total = 0
        start = 0

        for station_ind in range(len(gas)):
            total += (gas[station_ind]-cost[station_ind])

            if total <0:
                start = station_ind+1
                total = 0
        return start