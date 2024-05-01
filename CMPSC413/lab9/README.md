# Lab 9 - Arrival Route Planning for the Philadelphia Int'l Airport 

# Graph Model
**nodes**: nodes of the graph represent waypoints or runways  
**edges**: represent the flight time in minutes between waypoints

# Flight Generation
flights with source and destination points are generated and added to the airspace.
The user may select to either have `can_hold` set to true or false in the ATC() class.
This is how we switch between allowing negative edges into the graph or using only positive
edges. This also controls which algorithm is used for finding the paths. 
If Using postive edges only, we can save time be running the more efficient
Dijkstras Algorithm. However, with negative edges, we must use the Bellman-Ford
Algorithm which is a bit slower. 

# Negative Weights
in order to assist in sequencing flights during times with congested airspace.
ATC will request that aircraft enter a holding pattern to allow some arriving
aircraft to land. Flights that elected to do so are rewarded with an expedited
vector to the runway which I model with a negative edge cost.

# Time Complexities 

### Dijkstra's 
for my implementation I am using a priority queue (heap) and this allows 
me to get the best possible efficiency out of this algorithm. In all cases,
Dijkstras with this implementation has a time complexity of
- O(|V|+|E|log|V|)

### Bellman Ford
Since we have essentially added a for-loop to dijkstras (to check over every edge
after each iteration), we get a time complexiy of 
- O(|V||E|) 

Since the edges are directed only in one direction (aircraft shouldnt be flying directly
towareds each other), and since the graph is rather sparse, this time complexity should not
be expected to be the worst case of O(|v|^2).

# Conclusion
In conclusion, path finding algorithms are extremely important as 
many problems and scenarios can be modeled well using graphs. These 
algorithms lends themselves well to path palnning on a network of aircraft.
