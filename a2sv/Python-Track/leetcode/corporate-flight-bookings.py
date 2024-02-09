class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        seats=[0]*(n+1)
        for first,last,seat in bookings:
            seats[first-1]+=seat
            seats[last]-=seat
        for i in range(1,n):
            seats[i]+=seats[i-1]
        return seats[0:n]
