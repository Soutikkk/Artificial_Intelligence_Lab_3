# Artificial Intelligence Lab - Knowledge Representation

This repository contains Python implementations of foundational **Knowledge Representation** paradigms created for the Artificial Intelligence Laboratory (5th Semester).

---

## 📌 Repository Overview

Knowledge Representation (KR) is a fundamental subfield of Artificial Intelligence dedicated to representing information about the real world in a machine-readable form so that a computer system can solve complex tasks.

This repository features practical implementations of three key KR paradigms:
1. **Semantic Networks** (`Semantic Network.py`)
2. **Conceptual Graphs** (`Conceptual Graph.py`)
3. **Rule-Based Systems** (`Rule-Based System.py`)

---

## 📁 Included Implementations

### 1. Semantic Network (`Semantic Network.py`)
* **Description:** Represents objects/concepts as nodes in a graph, connected by directed labeled edges representing relationships such as `IS-A` (inheritance/taxonomical) and `HAS-A` (property/part-whole).
* **Key Features:**
  - Node relation lookup.
  - Hierarchical ancestor resolution via iterative `IS-A` traversal to locate root concepts.
* **Execution:**
  ```bash
  python "Semantic Network.py"
  ```

---

### 2. Conceptual Graph (`Conceptual Graph.py`)
* **Description:** Implements a bipartite graph structure to capture structured semantic meanings with explicit concepts and relation nodes (e.g., entity `Riya` `BORROWS` `Book1` `FROM` `Library1`).
* **Key Features:**
  - Explicit concept type definitions (`Person`, `Book`, `Library`).
  - Labeled relationship tuples.
  - Target entity relationship querying.
* **Execution:**
  ```bash
  python "Conceptual Graph.py"
  ```

---

### 3. Rule-Based System (`Rule-Based System.py`)
* **Description:** Implements a **Forward-Chaining Inference Engine** that derives new conclusions from an initial set of facts using a knowledge base of production rules (`IF condition THEN conclusion`).
* **Key Features:**
  - Iterative rule matching against active fact sets.
  - Automatic fact deduction until a fixpoint state (no new facts derived) is reached.
* **Execution:**
  ```bash
  python "Rule-Based System.py"
  ```

---

## 🚀 Prerequisites & Execution

### Requirements
- Python 3.6 or higher (uses standard library modules only).

### Running All Scripts
You can execute each script directly using Python:
```bash
python "Semantic Network.py"
python "Conceptual Graph.py"
python "Rule-Based System.py"
```

---

## 📝 License
This project is open-source and maintained for educational and academic practical coursework.
