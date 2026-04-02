def is_safe(district, color, assignment, graph):
    """Checks if the assigned color is valid (no adjacent districts share it)."""
    for neighbor in graph.get(district, []):
        if assignment.get(neighbor) == color:
            return False
    return True

def map_coloring_csp(districts, colors, graph, assignment=None):
    """Solves the map coloring problem using Backtracking Search."""
    if assignment is None:
        assignment = {}

    # Base case: all districts are assigned a valid color
    if len(assignment) == len(districts):
        return assignment

    # Select an unassigned district
    unassigned = [d for d in districts if d not in assignment]
    current_district = unassigned[0]

    # Try assigning available colors
    for color in colors:
        if is_safe(current_district, color, assignment, graph):
            assignment[current_district] = color
            
            # Recursively color the rest of the map
            result = map_coloring_csp(districts, colors, graph, assignment)
            if result:
                return result
            
            # Backtrack if the color leads to a dead end
            del assignment[current_district]

    return None

# 33 Districts of Telangana
telangana_districts = [
    "Adilabad", "Bhadradri Kothagudem", "Hyderabad", "Jagtial", "Jangaon",
    "Jayashankar Bhupalpally", "Jogulamba Gadwal", "Kamareddy", "Karimnagar",
    "Khammam", "Kumuram Bheem", "Mahabubabad", "Mahabubnagar",
    "Mancherial", "Medak", "Medchal-Malkajgiri", "Mulugu", "Nagarkurnool",
    "Nalgonda", "Narayanpet", "Nirmal", "Nizamabad", "Peddapalli",
    "Rajanna Sircilla", "Ranga Reddy", "Sangareddy", "Siddipet", "Suryapet",
    "Vikarabad", "Wanaparthy", "Warangal", "Hanumakonda", "Yadadri Bhuvanagiri"
]

# By the Four Color Theorem, 4 colors are sufficient for any planar map
available_colors = ["Red", "Green", "Blue", "Yellow"]

# Adjacency Graph (Add the remaining physical borders to complete the model)
adjacency_graph = {
    "Hyderabad": ["Medchal-Malkajgiri", "Ranga Reddy"],
    "Ranga Reddy": ["Hyderabad", "Medchal-Malkajgiri", "Sangareddy", "Vikarabad", "Mahabubnagar", "Nagarkurnool", "Nalgonda", "Yadadri Bhuvanagiri"],
    "Medchal-Malkajgiri": ["Hyderabad", "Ranga Reddy", "Sangareddy", "Medak", "Siddipet", "Yadadri Bhuvanagiri"],
    "Vikarabad": ["Sangareddy", "Ranga Reddy", "Mahabubnagar", "Narayanpet"],
    "Sangareddy": ["Vikarabad", "Ranga Reddy", "Medchal-Malkajgiri", "Medak", "Kamareddy"],
    # ... Populate remaining district neighbors here
}

# Ensure all districts are present in the graph dictionary to prevent KeyErrors
for d in telangana_districts:
    if d not in adjacency_graph:
        adjacency_graph[d] = []

# Execute
solution = map_coloring_csp(telangana_districts, available_colors, adjacency_graph)

if solution:
    for district, color in solution.items():
        print(f"{district}: {color}")
else:
    print("No valid coloring found. Check adjacency graph constraints.")