facts = {"has_hair", "gives_birth"}

rules = [
    ({"has_hair", "gives_birth"}, "mammal"),
    ({"mammal"}, "animal"),
    ({"mammal", "has_barks"}, "dog")
]

changed = True

while changed:
    changed = False

    for conditions, conclusion in rules:
        if conditions.issubset(facts) and conclusion not in facts:
            facts.add(conclusion)
            changed = True

print("Final facts:")

for fact in sorted(facts):
    print("-", fact)