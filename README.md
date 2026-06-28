# Pushdown Automaton & Turing Machine Simulators
Language: Python

---

Faiz Adli Nugraha - 5025231174 (in charge of the turing machine)

Ali Ridho - 5025231162 (in charge of the push-down automata)

## Files

| File | Description |
|------|-------------|
| `pda_simulator.py` | Simulates a Pushdown Automaton |
| `turing_machine_simulator.py` | Simulates a Turing Machine |

Both programs accept strings of the language **a^n b^n**, equal numbers of `a`'s followed by equal numbers of `b`'s.

---

## How to run

```bash
python pda_simulator.py
python turing_machine_simulator.py
```

Type a string when prompted, press Enter to see the result. Type `exit` to quit.

---

## Example output

```
Enter string: aabb
Result: ACCEPTED

Enter string: aab
Result: REJECTED
```

---

## How they work

### PDA
A Pushdown Automaton uses a **stack** alongside its states. This PDA pushes an `A` onto the stack for every `a` it reads, then pops an `A` for every `b`. If the stack is empty at the end, the string is accepted.

### Turing Machine
A Turing Machine has an infinite **tape** and a read/write head that moves one cell at a time. This TM uses a mark-and-sweep approach, it marks one `a` as `X`, scans right to mark one `b` as `Y`, scans back left, and repeats. When all `a`'s are marked, it checks that no `b`'s remain.
