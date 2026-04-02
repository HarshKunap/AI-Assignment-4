import networkx as nx
import matplotlib.pyplot as plt

# 1. Variables: The 33 Districts of Telangana
districts = [
    "Adilabad", "Bhadradri Kothagudem", "Hyderabad", "Jagtial", "Jangaon",
    "Jayashankar Bhupalpally", "Jogulamba Gadwal", "Kamareddy", "Karimnagar",
    "Khammam", "Kumuram Bheem Asifabad", "Mahabubabad", "Mahabubnagar", "Mancherial",
    "Medak", "Medchal Malkajgiri", "Mulugu", "Nagarkurnool", "Nalgonda", "Narayanpet",
    "Nirmal", "Nizamabad", "Peddapalli", "Rajanna Sircilla", "Rangareddy",
    "Sangareddy", "Siddipet", "Suryapet", "Vikarabad", "Wanaparthy",
    "Warangal Rural", "Warangal Urban", "Yadadri Bhuvanagiri"
]

# 2. Constraints: Adjacent districts (Add the rest of your borders here!)
edges = [
    ("Hyderabad", "Rangareddy"),
    ("Hyderabad", "Medchal Malkajgiri"),
    ("Rangareddy", "Vikarabad"),
    ("Rangareddy", "Sangareddy"),
    ("Rangareddy", "Mahabubnagar"),
    # ... add all other district neighbors here to complete the map!
]

# 3. Domain: The colors we can use
colors = ['red', 'green', 'blue'] 

# Create the Graph using NetworkX
G = nx.Graph()
G.add_nodes_from(districts)
G.add_edges_from(edges)

# Function to check if a color is safe to use
def is_safe(node, color, graph, color_assignment):
    for neighbor in graph.neighbors(node):
        if color_assignment.get(neighbor) == color:
            return False
    return True

# 4. Method: Backtracking Algorithm
def solve_map_coloring(nodes, graph, colors, color_assignment, index=0):
    # If we reached the end, all districts are colored successfully!
    if index == len(nodes):
        return True 

    current_node = nodes[index]
    
    # Try out each color
    for color in colors:
        if is_safe(current_node, color, graph, color_assignment):
            color_assignment[current_node] = color  # Assign the color
            
            # Move to the next district
            if solve_map_coloring(nodes, graph, colors, color_assignment, index + 1):
                return True
                
            # If it led to a dead end, remove the color (Backtrack!)
            color_assignment[current_node] = None 
            
    return False

# Initialize empty assignments
color_assignment = {node: None for node in districts}

# 5. Visualization: Run the solver and draw the graph
if solve_map_coloring(districts, G, colors, color_assignment):
    print("Map successfully colored!")
    
    # Get the colors in the right order for the nodes
    node_colors = [color_assignment[node] for node in G.nodes()]
    
    # Draw the map as a graph
    plt.figure(figsize=(15, 12))
    nx.draw(G, with_labels=True, node_color=node_colors, node_size=3000, 
            font_size=8, font_weight="bold", edge_color="gray")
    plt.title("Telangana District Map Coloring", fontsize=20)
    plt.show()
else:
    print("Could not find a solution with the given colors. Try adding a 4th color!")