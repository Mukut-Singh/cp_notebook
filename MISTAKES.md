## Some common mistakes
Concept,The Wrong Way (Trap),The Right Way (Efficient),Why?
2D Matrix,[[0]*m]*n,        [[0 for _ in range(m)] for _ in range(n)],        Avoids linked rows.
Adding Front,"list.insert(0, x)",        collections.deque.appendleft(x),        O(N) vs O(1) speed.
String Build,"s += ""new""",        "list.append(""new"") then """".join(list)",        Avoids O(N2) string copying.
