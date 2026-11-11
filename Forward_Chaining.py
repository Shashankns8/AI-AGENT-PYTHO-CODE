
import re
from itertools import count

# Convert input string into a predicate
def parse_atom(text):
    text = text.strip()
    match = re.fullmatch(r'(\w+)\s*\((.*?)\)', text)

    if not match:
        raise ValueError("Invalid predicate: " + text)

    name = match.group(1)
    args = [x.strip() for x in match.group(2).split(",")]

    # Variables start with lowercase letters
    args = [
        "?" + x if x[0].islower() else x
        for x in args
    ]

    return (name, tuple(args))


# Convert predicate back to string
def show(atom):
    name, args = atom
    return name + "(" + ", ".join(
        x[1:] if x.startswith("?") else x for x in args
    ) + ")"


# Apply substitution
def SUBST(theta, atom):
    name, args = atom

    def replace(x):
        while x.startswith("?") and x in theta:
            x = theta[x]
        return x

    return (name, tuple(replace(x) for x in args))


# Unification
def UNIFY(x, y, theta=None):
    if theta is None:
        theta = {}

    x = SUBST(theta, x)
    y = SUBST(theta, y)

    if x[0] != y[0] or len(x[1]) != len(y[1]):
        return None

    for a, b in zip(x[1], y[1]):

        if a == b:
            continue

        if a.startswith("?"):
            theta[a] = b

        elif b.startswith("?"):
            theta[b] = a

        else:
            return None

    return theta


# Standardize variables
def STANDARDIZE_VARIABLES(rule, number):
    mapping = {}

    def rename(atom):
        name, args = atom
        new_args = []

        for arg in args:
            if arg.startswith("?"):
                if arg not in mapping:
                    mapping[arg] = arg + "_" + str(number)
                new_args.append(mapping[arg])
            else:
                new_args.append(arg)

        return (name, tuple(new_args))

    premises, conclusion = rule

    return (
        [rename(p) for p in premises],
        rename(conclusion)
    )


# Find all substitutions that satisfy premises
def FIND_SUBSTITUTIONS(premises, KB):

    results = [{}]

    for premise in premises:
        new_results = []

        for theta in results:
            current = SUBST(theta, premise)

            for fact in KB:
                phi = UNIFY(current, fact, theta.copy())

                if phi is not None:
                    new_results.append(phi)

        results = new_results

        if not results:
            break

    return results


# Forward Chaining Algorithm
def FOL_FC_ASK(KB, rules, alpha):

    new = set()
    rule_counter = count(1)

    while True:

        new = set()

        for rule in rules:

            # Standardize variables
            rule = STANDARDIZE_VARIABLES(
                rule, next(rule_counter)
            )
            premises, conclusion = rule
            for theta in FIND_SUBSTITUTIONS(premises, KB):
                q = SUBST(theta, conclusion)
                if q not in KB and q not in new:
                    new.add(q)
                    # Unify q with query
                    phi = UNIFY(q, alpha)
                    if phi is not None:
                        return phi
        if not new:
            return False
        KB.update(new)
print("FORWARD REASONING ALGORITHM")
print("---------------------------")
KB = set()
print("\nEnter initial facts.")
print("Example: Parent(Ram,Ravi)")
print("Press ENTER when finished.")
while True:
    line = input("Fact: ").strip()
    if line == "":
        break
    KB.add(parse_atom(line))
rules = []
print("\nEnter rules.")
print("Example: Parent(x,y) -> Ancestor(x,y)")
print("Use & for multiple conditions.")
print("Press ENTER when finished.")
while True:
    line = input("Rule: ").strip()
    if line == "":
        break
    left, right = line.split("->")
    premises = [
        parse_atom(x)
        for x in left.split("&")
    ]
    conclusion = parse_atom(right)
    rules.append((premises, conclusion))
print("\nEnter the query.")
alpha = parse_atom(input("Query: "))
result = FOL_FC_ASK(KB, rules, alpha)
print("\n---------------------------")
print("RESULT")

if result is not False:
    print("Query is TRUE")

    if result:
        print("Substitution:")

        for key, value in result.items():
            print(key[1:], "=", value)

else:
    print("Query is FALSE")

print("---------------------------")
