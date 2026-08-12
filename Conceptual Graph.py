concepts = {
    "Riya": "Person",
    "Book1": "Book",
    "Library1": "Library"
}

relations = [
    ("Riya", "BORROWS", "Book1"),
    ("Riya", "FROM", "Library1")
]

print("Concepts:")

for name, concept_type in concepts.items():
    print(name, ":", concept_type)

print("\nRelations:")

for source, relation, target in relations:
    print(source, "--", relation, "-->", target)

person = "Riya"

for source, relation, target in relations:
    if source == person:
        print("Query:", person, relation, target)