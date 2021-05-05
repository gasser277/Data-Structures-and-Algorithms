import heapq
from math import pow, sqrt
from collections import namedtuple

Cost = namedtuple('Cost', ['total', 'journey', 'to_goal'])
Path = namedtuple('Path', ['cost', 'intersections', 'previous', 'frontier'])

def euclidean_distance(origin_point: [float, float], destination_point: [float, float]) -> float: #input is two points and output is their euclidean distance :var origin_point is the origin point, in the 2D cartesian space :param destination_point: destination point, in the 2D cartesian space. return is: euclidean distance between the two points
    return sqrt(pow((origin_point[0] - destination_point[0]), 2) + pow((origin_point[1] - destination_point[1]), 2))#return is: euclidean distance between the two points


#Estimates the distance between the current path frontier point and the taret. Accomplished the A* optimization requirement of having an estimating function that underestimates. As in a 2D-Cartesian space, the straight line is always the smallest possible distance between two points; guaranteeing the "underestimation" requirement :
def estimated_distance(path_frontier_point: [float, float], goal_point: [float, float]) -> float:
    return euclidean_distance(origin_point=path_frontier_point, destination_point=goal_point)#varibable path_frontier_point: path frontier point :variable goal_point: goal point :return: estimated euclidean distance


#Given a path and a next point, this function updates the path :
def update_path(map: object, path: Path, new_frontier: int, goal: int) -> Path:
    distance_traversed = euclidean_distance(origin_point=map.intersections[path.frontier],destination_point=map.intersections[new_frontier])
    new_path_cost_journey = path.cost.journey + distance_traversed
    new_cost_path_goal= estimated_distance(path_frontier_point=map.intersections[new_frontier],goal_point=map.intersections[goal])
    new_path_cost_total = new_path_cost_journey + new_cost_path_goal
    new_path_intersections = path.intersections + [new_frontier]
    new_path = Path(Cost(new_path_cost_total, new_path_cost_journey, new_cost_path_goal),new_path_intersections, path.frontier, new_frontier)
    return new_path #param map: map of the current 2D space :param path: current traversed path :param new_frontier: coordinates of next point to add to the path :param goal: coordinates of the goal intersection :return: path costs and intersections updated with new point
#Given a map and a start and end point, returns the shortest path, based on A* algorithm :param map: map of the current 2D space :param start: coordinates of the original intersection :param goal: coordinates of the goal intersection :return:
def shortest_path(map: object, start: int, goal: int) -> list:
    paths = list()
    min_goal_path_val = float('inf')
    min_goal_path = None    
     
    if start == goal:# Check if already in goal
        return [start]
    
    goal_initial_distance = estimated_distance(path_frontier_point=map.intersections[start],goal_point=map.intersections[goal])# Initialize paths
    path = Path(Cost(goal_initial_distance, 0, goal_initial_distance), [start], start, start)
    heapq.heappush(paths, path)
    while len(paths) >= 1:
        nearest_frontier_path = heapq.heappop(paths)
        for neighbor_road in map.roads[nearest_frontier_path.frontier]:
            if neighbor_road == nearest_frontier_path.previous:  
                continue  # Avoid returning to backwards
            else:
                new_path = update_path(map=map, path=nearest_frontier_path, new_frontier=neighbor_road, goal=goal)
                if neighbor_road == goal:  # Reached destination with a path
                    if new_path.cost.total < min_goal_path_val:  # Better than previous path
                        min_goal_path_val = new_path.cost.total
                        min_goal_path = new_path.intersections
                    else:# Reached destination, with higher cost -> disregard
                        pass
                else:
                    if min_goal_path is not None:# Already found the goal with a path
                        if new_path.cost.total >= min_goal_path_val:# Path not reached goal and already costly
                            pass
                        else: # Cheaper path, keep exploring
                            heapq.heappush(paths, new_path)
                    else:# Not yet found the goal, keep exploring
                        heapq.heappush(paths, new_path)
    if min_goal_path is not None:
        return min_goal_path
    else:
        return -1