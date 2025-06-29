bird_species = {
    "sparrow": {"color": "brown", "pattern": "plain", "size": "small", "behavior": "gregarious", "habitat": "urban"},
    "eagle": {"color": "brown", "pattern": "mottled", "size": "large", "behavior": "solitary", "habitat": "mountains"},
    "northen cardinal":{"color":"bright red","pattern":"red tinged","size":"small","behavior":"territorial","habitat":"woodlands"},
    "bluejay":{"color":"vibrant blue","pattern":"perky crest","size":"small","behavior":"noisy","habitat":"forests"},
    "barn owl":{"color":"light tan","pattern":"golden buff","size":"small","behavior":"nocturnal hunters","habitat":"grasslands"},
    "atlantic puffin":{"color":"black and white","pattern":"cheek patches","size":"small","behavior":"excellent drivers","habitat":"coastal cliffs"},
    "peacock":{"color":"vibrant blue","pattern":"ocelli","size":"large","behavior":"display elaborate","habitat":"south asia"},
    "great horned owl":{"color":"mottled brown","pattern":"mottled","size":"small","behavior":"nocturnal hunters","habitat":"diverse"},
    "ruby-throated hummingbird":{"color":"bright green","pattern":"bright emerald","size":"tiny","behavior":"agilefliers","habitat":"eastern north america"},
    "atlantic canary":{"color":"yellow","pattern":"yellow breast","size":"small","behavior":"social birds","habitat":"canary islands"},
    "australian rainbow lorikeet":{"color":"vibrant rainbow","pattern":"yellow green collar","size":"small","behavior":"energetic","habitat":"rainforest"},
   
}

def identify_bird():
    color = input("Enter the color of the bird: ")
    pattern = input("Enter the pattern of the bird: ")
    size = input("Enter the size of the bird: ")
    behavior = input("Enter the behavior of the bird: ")
    habitat = input("Enter the habitat of the bird: ")

    for species, attributes in bird_species.items():
        if (
            attributes["color"] == color.lower()
            and attributes["pattern"] == pattern.lower()
            and attributes["size"] == size.lower()
            and attributes["behavior"] == behavior.lower()
            and attributes["habitat"] == habitat.lower()
        ):
            print(f"The bird is a {species}.")
            return

    print("Sorry, I couldn't identify that bird.")

identify_bird()
