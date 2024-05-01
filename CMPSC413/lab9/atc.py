# airtraffic control class
import random

from graph import kphl_graph, wpts, full_wpts, runway_entry_points, hold_entry_points
import networkx as nx
import heapq

class ATC:
    def __init__(self, can_hold=True):
        self.flights = {}
        self.can_hold = can_hold  # holding off by default
        self.airspace : nx.DiGraph = self.create_airspace()


    def create_airspace(self):
        wpts = [
            # normal wpts
            ("MOD", "PTW", 40),
            ("PTW", "BRIG", 50),
            ("BRIG", "DUP", 45),
            ("DUP", "CTR", 25),
            ("CTR", "MOD", 35),
            ("MOD", "OPK", 75),
            ("ACL", "MOD", 39),
            ("KBR", "BRIG", 35),
            ("MOD", "YIT", 15),
            ("OPK", "PTW", 49),

            # rwy entry points
            ("BRIG", "RWY-27L", 10),
            ("BRIG", "RWY-35", 6),
            ("PTW", "RWY-17", 12),
        ]

        if self.can_hold:
            hold_pts = [
            # hold enter possible
            ("KBR", "HOLD_ENTER", 20),
            ("OPK", "HOLD_ENTER", 20),

            # hold exit
            ("HOLD_ENTER", "HOLD_EXIT", 20),

            ("HOLD_EXIT", "RWY-27L", -12),
            ("HOLD_EXIT", "RWY-09R", -12),
            ("HOLD_EXIT", "RWY-35", -12),
            ("HOLD_EXIT", "RWY-17", -12)]

            wpts.extend(hold_pts)

        g = nx.DiGraph()
        for start, end, cost in wpts:
            g.add_edge(start, end, weight=cost)
        return g

    def add_flight(self, flight_num, src, dst):
        if flight_num not in self.flights.keys():
            if src in self.airspace.nodes and dst in self.airspace.nodes:
                self.flights[flight_num] = (src, dst)
                print(f"Added Flight {flight_num} | {src} -> {dst}")
    def del_flight(self, flight_num):
        if flight_num in self.flights.keys():
            del self.flights[flight_num]
            print(f"Removed Flight {flight_num}")
    def find_routing_no_hold(self, flight_num):
        if flight_num in self.flights.keys():
            # dijkstras

            # lookup flight
            src, dst = self.flights[flight_num]

            # for reconstruction
            visited = {n: None for n in self.airspace.nodes}

            # copy of edge list
            dist = {v : float('infinity') for v in self.airspace.nodes} # contains distances from src to all other wpts
            dist[src] = 0 # set src -> src distance to 0

            # append to priority queue
            pq = [(dist[node], node) for node in dist]
            heapq.heapify(pq) # turn into min heap

            while pq:
                cur_dist, cur_wpt = heapq.heappop(pq)
                cur_neighbors = list(self.airspace.neighbors(cur_wpt))

                # get distances and names
                neighbor_costs = [(n, self.airspace.get_edge_data(cur_wpt, n)['weight'])
                                  for n in cur_neighbors if 'weight' in self.airspace.get_edge_data(cur_wpt, n)]

                # relaxation
                for neigh_name, neigh_cost in neighbor_costs:
                    candidate_dist = cur_dist + neigh_cost
                    if candidate_dist < dist[neigh_name]:  # compare to the best known distance
                        dist[neigh_name] = candidate_dist  # update distance
                        visited[neigh_name] = cur_wpt # for path reconstruction
                        new_tup = (candidate_dist, neigh_name)
                        heapq.heappush(pq, new_tup)

            # reconstructing path
            path = []
            step = dst
            while visited[step] is not None:
                path.append(step)
                step = visited[step]

            path.append(step)  # add the source
            total_cost = sum(self.airspace[u][v]['weight'] for u, v in zip(path[:-1], path[1:])) # total cost
            return {'path' : list(reversed(path)),
                    'dist' : total_cost} # return reversed path -> ([path], total_dist)

    def find_routing_with_hold(self, flight_num):
        # bellman-ford (negative weights after hold)
        if flight_num in self.flights.keys():
            # lookup flight
            src, dst = self.flights[flight_num]

            # for reconstruction
            visited = {n: None for n in self.airspace.nodes}

            # initialize distances
            dist = {v: float('infinity') for v in self.airspace.nodes}
            dist[src] = 0

            # relax all edges (|V|-1) times
            for _ in range(len(self.airspace.nodes) - 1):
                for u, v, data in self.airspace.edges(data=True):
                    if dist[u] + data['weight'] < dist[v]:
                        dist[v] = dist[u] + data['weight']
                        visited[v] = u

            # check for negative cycles
            for u, v, data in self.airspace.edges(data=True):
                if dist[u] + data['weight'] < dist[v]:
                    print("Negative cycle detected!")
                    return None  # handling negative cycle by exiting

            # reconstruct path
            path = []
            step = dst
            while step is not None:
                path.append(step)
                step = visited[step]

            path.reverse()  # reverse the path to start from the source
            total_cost = sum(self.airspace[u][v]['weight'] for u, v in zip(path[:-1], path[1:]))

            return {'path': path, 'dist': total_cost}


# testing
if __name__ == '__main__':
    kphl = ATC(can_hold=True)
    can_hold = True

    airlines = ["AA", "UA", "BA", "DA", "FF", "AF", "JA", "WZ"]
    active_runway = random.sample(runway_entry_points, 1)[0][1]
    print(f"\nACTIVE RUNWAY: {active_runway} | Hold Avialable: {can_hold}\n")
    airspace = [tup for tup in kphl.airspace.edges]

    # testing flights
    for i in range(50):
        src = random.sample(airspace, 1)[0][0]

        dst = active_runway
        airline = random.sample(airlines,1)[0]
        fnum = random.randint(0,1000)

        callsign = airline + str(fnum)
        kphl.add_flight(callsign, src, dst)

        if can_hold:
            rt = kphl.find_routing_with_hold(callsign)
        else:
            rt = kphl.find_routing_no_hold(callsign)
        print(rt)








