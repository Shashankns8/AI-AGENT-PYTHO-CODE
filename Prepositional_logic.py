def implies(p, q):
    return (not p) or q


def check_all(kb, query, symbols, model):

    if len(symbols) == 0:

        if kb(model):
            return query(model)
        else:
            return True

    p = symbols[0]
    rest = symbols[1:]

    model1 = model.copy()
    model1[p] = True

    model2 = model.copy()
    model2[p] = False

    return (check_all(kb, query, rest, model1)
            and
            check_all(kb, query, rest, model2))


def tt_entails(kb, query, symbols):

    return check_all(kb, query, symbols, {})


# Knowledge Base: (P -> Q) AND P

def kb(model):
    return implies(model['P'], model['Q']) and model['P']


# Query: Q

def query(model):
    return model['Q']


symbols = ['P', 'Q']

result = tt_entails(kb, query, symbols)

if result:
    print("KB entails the query")
else:
    print("KB does not entail the query")
    def implies(p, q):
        return (not p) or q

def kb(m):
    return implies(m['P'], m['Q']) and m['P']

def query(m):
    return m['Q']

# TT-Check-All code
def check_all(kb, query, symbols, model):
    if len(symbols) == 0:
        return query(model) if kb(model) else True
    p = symbols[0]
    rest = symbols[1:]
    m1 = model.copy()
    m1[p] = True
    m2 = model.copy()
    m2[p] = False
    return check_all(kb, query, rest, m1) and check_all(kb, query, rest, m2)

symbols = ['P', 'Q']
result = check_all(kb, query, symbols, {})

print("Knowledge Base: P -> Q and P")
print("Query: Q")
print("Checking all possible models")
print("Result:", result)
print("KB entails Query" if result else "KB does not entail Query")