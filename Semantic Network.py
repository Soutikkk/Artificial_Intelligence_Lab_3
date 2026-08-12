network = {
    "Dog": [("IS-A", "Mammal"), ("HAS-A", "Tail")],
    "Mammal": [("IS-A", "Animal")],
    "Animal": [],
    "Bird": [("IS-A", "Animal")]
}

def show_relations(node):
    print("Relations of", node)

    for relation, target in network.get(node, []):
        print(node, relation, target)


def find_ancestor(node):
    current = node

    while True:
        isa_links = [
            target
            for relation, target in network.get(current, [])
            if relation == "IS-A"
        ]

        if not isa_links:
            return current

        current = isa_links[0]


show_relations("Dog")

print("Highest IS-A concept:", find_ancestor("Dog"))