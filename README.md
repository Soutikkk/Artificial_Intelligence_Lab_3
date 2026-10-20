# Artificial Intelligence Lab - Knowledge Representation

This repository contains Python implementations of foundational **Knowledge Representation (KR)** paradigms developed for the Artificial Intelligence Laboratory (5th Semester).

---

## 📌 Repository Overview

Knowledge Representation is a fundamental subfield of Artificial Intelligence (AI) concerned with representing real-world knowledge in a machine-readable format so that computer systems can reason, infer new information, and solve problems.

This repository includes practical implementations of five important Knowledge Representation techniques:

1. **Semantic Networks** (`Semantic Network.py`)
2. **Conceptual Graphs** (`Conceptual Graph.py`)
3. **Rule-Based Systems** (`Rule-Based System.py`)
4. **Frame-Based Systems** (`Frame-Based System.py`)
5. **Bayesian Networks** (`Bayesian Network.py`)

---

## 📁 Included Implementations

### 1. Semantic Network (`Semantic Network.py`)

- **Description:** Represents concepts and objects as nodes connected by directed, labeled edges that describe relationships such as `IS-A` and `HAS-A`.
- **Key Features:**
  - Node and relationship lookup.
  - Hierarchical knowledge representation.
  - Ancestor resolution through iterative `IS-A` traversal.
- **Execution:**

  ```bash
  python "Semantic Network.py"
  ```

### 2. Conceptual Graph (`Conceptual Graph.py`)

- **Description:** Represents structured knowledge using concepts and relationships. For example, `Riya` borrows `Book1` from `Library1`.
- **Key Features:**
  - Explicit concept type definitions, such as `Person`, `Book`, and `Library`.
  - Labeled relationships between concepts.
  - Relationship querying for target entities.
- **Execution:**

  ```bash
  python "Conceptual Graph.py"
  ```

### 3. Rule-Based System (`Rule-Based System.py`)

- **Description:** Implements a forward-chaining inference engine that derives new conclusions from an initial set of facts using production rules in the form `IF condition THEN conclusion`.
- **Key Features:**
  - Iterative rule matching against known facts.
  - Automatic deduction of new facts.
  - Repeated inference until no additional facts can be derived.
- **Execution:**

  ```bash
  python "Rule-Based System.py"
  ```

### 4. Frame-Based System (`Frame-Based System.py`)

- **Description:** Represents knowledge using frames, which organize information about objects or concepts into attributes (slots) and their corresponding values.
- **Key Features:**
  - Creation of frames for real-world entities.
  - Storage and retrieval of attributes and values.
  - Inheritance of properties from parent frames.
  - Support for overriding inherited values in child frames.
- **Execution:**

  ```bash
  python "Frame-Based System.py"
  ```

### 5. Bayesian Network (`Bayesian Network.py`)

- **Description:** Demonstrates probabilistic reasoning by representing dependencies among variables such as cloudy weather, rain, sprinklers, and wet grass.
- **Key Features:**
  - Conditional probability calculations.
  - Probabilistic inference based on observed conditions.
  - Estimation of the likelihood of events.
  - Decision-making based on calculated probabilities.
- **Execution:**

  ```bash
  python "Bayesian Network.py"
  ```

---

## 🚀 Prerequisites and Execution

### Requirements

- Python 3.6 or higher.
- Standard Python library only; no external dependencies are required.

### Running Individual Scripts

Run any implementation from the repository directory:

```bash
python "Semantic Network.py"
python "Conceptual Graph.py"
python "Rule-Based System.py"
python "Frame-Based System.py"
python "Bayesian Network.py"
```

### Running All Scripts

On Linux or macOS, you can execute all five programs sequentially:

```bash
python "Semantic Network.py" && \
python "Conceptual Graph.py" && \
python "Rule-Based System.py" && \
python "Frame-Based System.py" && \
python "Bayesian Network.py"
```

**Note:** The Bayesian Network program requires interactive input. Enter the requested values when prompted.

---

## 🎯 Learning Outcomes

By completing these practical implementations, students can understand:

- Graph-based knowledge representation.
- Concepts, entities, and semantic relationships.
- Forward-chaining inference and rule-based reasoning.
- Frame structures, inheritance, and attribute overriding.
- Probabilistic reasoning and conditional probability.
- The role of knowledge representation in Artificial Intelligence.

---

## 📝 License

This project is open-source and intended for educational and academic practical coursework. You may use and modify the implementations for learning and experimentation.
