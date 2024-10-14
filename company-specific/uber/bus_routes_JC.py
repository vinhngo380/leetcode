class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # Utilize graph (in the form of defaultdict with sets), queue (deque with tuple)
        graph = defaultdict(set)
        queue = deque([(source, 0)])

        # here, bus would be the index of route
        for bus, route in enumerate(routes):
            # each stop in route, add the corresponding bus... will be useful in a bit
            for stop in route:
                graph[stop].add(bus)

        visited_stops = set()
        visited_buses = set()
        
        while queue:
            stop, route_len = queue.popleft() # unpacked due to tuple

            if stop == target: # return if stop == target.
                return route_len
            
            # graph utilized here. we want to perform bfs on this
            for bus in graph[stop]:
                # IF BUS NOT visited yet, we have to go through the process of adding it to the queue, along with its stops.
                if bus not in visited_buses:
                    visited_buses.add(bus)
                    for stop in routes[bus]:
                        if stop not in visited_stops:
                            visited_stops.add(stop)
                            queue.append((stop, route_len + 1))

        return -1

  '''
  TLDR: Use bfs with graphs and queue. In the queue, we would be using tuples in the form (source, route_len). 
  So first, we would iterate through all the routes, adding to our graph (in the form of dict with sets) each stop along with the buses that go to it.
  Note that the "bus" is the index of each route in routes. 

  Then, we also need a set each for visited_stops, visited_buses to avoid cycles. Finally, we start popping/appending to our queue until we get our answer (or not)
  To do so, we first pop from the queue, unpacking into stop and route_len. Compare, and if stop == target, we return the route_len (our answer). If not,
  we have to check EVERY bus in the stop to see if there is a bus that does arrive at our final target. So, we have a for loop to iterate through the graph,
  checking if the bus is in visited_buses and THEN, if the stop is in visited_stops. If both are false, then we append to our queue the stop, with route_len, in a tuple.
  Note that at each step where bus and stop is false, we have to mark them as visited after we handle them.

  If we went through the queue and have not yet found our answer, then we return -1 (Not found).

  TC O(n^2) due to going through every bus, then every stop and also buses from that stop.
  SC O(n^2) due to same reasons as TC
  '''
