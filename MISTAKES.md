## Some common mistakes
### 🚩 Common Traps

| Concept | The Wrong Way (Trap) | The Right Way (Efficient) | Why? (The Logic) |
| :--- | :--- | :--- | :--- |
| **2D Matrix** | `[[0]*m]*n` | `[[0 for _ in range(m)] for _ in range(n)]` | **Avoids linked rows.** The trap creates $n$ references to the *same* list. Changing one row changes all of them. |
| **Adding Front** | `list.insert(0, x)` | `collections.deque.appendleft(x)` | **$O(N)$ vs $O(1)$ speed.** Shifting an entire list takes linear time; a `deque` handles ends in constant time. |
| **String Build** | `s += "new"` | `list.append("new")` then `"".join(list)` | **Avoids $O(N^2)$ copying.** Strings are immutable; every `+` creates a brand-new string in memory. |

---
##some more
**1.if all machine are A type means x-1 will take no. of a time ,and if a = big big no. time exceeds so answer should be a directly**  

**2.try not put any variable outside t cases loop**  

**3.odd even me use modulus % symbol**  

