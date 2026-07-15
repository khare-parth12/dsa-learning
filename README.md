# DSA Learning Notes

This repository is used for learning Data Structures and Algorithms using Python and Java.

## Languages Used
- Python
- Java

## What is DSA?
Data Structures are ways to organize and store data efficiently. Algorithms are step-by-step procedures to solve problems using that data.

## Core Data Structures

### 1. Array
- Definition: A collection of elements stored in contiguous memory locations.
- Structure Representation: [10, 20, 30, 40]
- Basic Operations: access, update, insert, delete, traverse, search

### 2. String
- Definition: A sequence of characters used to store and process text.
- Structure Representation: "hello"
- Basic Operations: length, concatenate, substring, compare, search

### 3. Linked List
- Definition: A linear data structure where each node contains data and a reference to the next node.
- Structure Representation: 10 -> 20 -> 30 -> null
- Basic Operations: insert, delete, search, traverse

### 4. Stack
- Definition: A linear structure that follows the Last In, First Out (LIFO) principle.
- Structure Representation: top -> 10 -> 20 -> 30
- Basic Operations: push, pop, peek, isEmpty

### 5. Queue
- Definition: A linear structure that follows the First In, First Out (FIFO) principle.
- Structure Representation: front -> 10 -> 20 -> 30 -> rear
- Basic Operations: enqueue, dequeue, peek, isEmpty

### 6. Deque
- Definition: A double-ended queue that allows insertion and deletion from both ends.
- Structure Representation: front [10, 20, 30] rear
- Basic Operations: addFront, addRear, removeFront, removeRear, peek

### 7. Hash Table / Hash Map / Dictionary
- Definition: A data structure that stores data as key-value pairs using hashing.
- Structure Representation: {"name": "Alice", "age": 21}
- Basic Operations: insert, update, search, delete

### 8. Set
- Definition: A collection of unique values with no duplicate elements.
- Structure Representation: {1, 2, 3, 4}
- Basic Operations: add, remove, contains, union, intersection

### 9. Tree
- Definition: A hierarchical data structure made of nodes connected by edges.
- Structure Representation:
  - root
    - left child
    - right child
- Basic Operations: insert, delete, search, traverse

### 10. Binary Search Tree (BST)
- Definition: A binary tree where the left subtree contains smaller values and the right subtree contains larger values.
- Structure Representation:
  - 20
    - 10
    - 30
- Basic Operations: insert, search, delete, inorder traversal

### 11. Heap
- Definition: A complete binary tree that satisfies the heap property, usually used for priority queues.
- Structure Representation: [10, 5, 7, 2, 1]
- Basic Operations: insert, extractMin/extractMax, peek, heapify

### 12. Graph
- Definition: A collection of vertices connected by edges to represent relationships.
- Structure Representation: A -> B, B -> C, A -> C
- Basic Operations: add vertex, add edge, traverse, search, shortest path

### 13. Trie
- Definition: A tree-like structure used to store strings efficiently by prefix.
- Structure Representation:
  - root
    - c
      - a
        - t
- Basic Operations: insert, search, delete, prefix search

## Common Topics in This Repository
- Arrays
- Sorting
- Recursion
- Hashing
- Patterns

## Study Goal
Understand each data structure, learn its properties, and practice implementing it in Python and Java.
