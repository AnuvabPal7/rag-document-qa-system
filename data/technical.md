# Technical Q&A Knowledge Base
> Placement-oriented interview preparation across Java, Python, DBMS, OS, DSA, and Networking.

---

# Java

## What is Java?
Java is a high-level, class-based, object-oriented programming language designed to have as few implementation dependencies as possible. It follows the principle of "Write Once, Run Anywhere" (WORA) using the Java Virtual Machine (JVM).

## What is the JVM?
JVM (Java Virtual Machine) is an abstract machine that provides a runtime environment to execute Java bytecode. It converts bytecode into machine-specific code and handles memory management, garbage collection, and security.

## What is the difference between JDK, JRE, and JVM?
JDK (Java Development Kit) includes tools for developing Java programs like compiler (javac) and JRE. JRE (Java Runtime Environment) provides libraries and JVM needed to run Java applications. JVM (Java Virtual Machine) is the runtime engine that executes bytecode.

## What is inheritance in Java?
Inheritance allows one class to acquire the properties and methods of another class using the `extends` keyword. It promotes code reusability. The class that is inherited is called the parent or superclass, and the inheriting class is called the child or subclass.

## What is polymorphism?
Polymorphism means "many forms". In Java it comes in two types: compile-time (method overloading) and runtime (method overriding). It allows the same method name to behave differently based on the object or arguments.

## What is method overloading?
Method overloading is when multiple methods in the same class have the same name but different parameters (different number, type, or order). It is resolved at compile time and is an example of static polymorphism.

## What is method overriding?
Method overriding is when a subclass provides its own implementation of a method already defined in the parent class. The method name, return type, and parameters must be the same. It is resolved at runtime and is an example of dynamic polymorphism.

## What is encapsulation?
Encapsulation is the bundling of data (variables) and methods that operate on the data into a single unit (class), and restricting direct access to internal data using access modifiers like private. Getters and setters are used to access or modify private fields.

## What is abstraction?
Abstraction hides implementation details and only shows essential features to the user. In Java, abstraction is achieved using abstract classes and interfaces.

## What is the difference between abstract class and interface?
An abstract class can have both abstract and concrete methods, can have instance variables, and supports single inheritance. An interface can only have abstract methods (before Java 8), all fields are public static final, and a class can implement multiple interfaces. From Java 8, interfaces can have default and static methods.

## What is the difference between == and equals() in Java?
`==` compares object references (memory addresses). `equals()` compares the content or logical equality of objects. For Strings, `==` checks if both point to the same memory location, while `equals()` checks if the characters are the same.

## What is a constructor in Java?
A constructor is a special method that is automatically called when an object is created. It has the same name as the class and no return type. Constructors initialize the object's state. Java provides a default no-argument constructor if no constructor is defined.

## What is the difference between String, StringBuilder, and StringBuffer?
String is immutable; every modification creates a new object. StringBuilder is mutable and faster but not thread-safe. StringBuffer is mutable and thread-safe but slower than StringBuilder due to synchronization.

## What is exception handling in Java?
Exception handling is a mechanism to handle runtime errors gracefully using try, catch, finally, throw, and throws keywords. It prevents abnormal termination of programs. Exceptions are of two types: checked (must be handled at compile time) and unchecked (runtime exceptions).

## What is the difference between checked and unchecked exceptions?
Checked exceptions are compile-time exceptions that must be declared using throws or handled using try-catch (e.g., IOException, SQLException). Unchecked exceptions are runtime exceptions that are not checked at compile time (e.g., NullPointerException, ArrayIndexOutOfBoundsException).

## What is multithreading in Java?
Multithreading is the ability of a CPU to execute multiple threads concurrently. In Java, threads can be created by extending the Thread class or implementing the Runnable interface. It improves application performance by utilizing CPU efficiently.

## What is synchronization in Java?
Synchronization is a mechanism to control access of multiple threads to shared resources to prevent data inconsistency. The `synchronized` keyword can be applied to methods or blocks to allow only one thread to execute them at a time.

## What is the Collections Framework in Java?
The Java Collections Framework provides a set of interfaces and classes to store and manipulate groups of objects. Key interfaces include List, Set, Queue, and Map. Common implementations are ArrayList, LinkedList, HashSet, TreeSet, HashMap, and LinkedHashMap.

## What is the difference between ArrayList and LinkedList?
ArrayList is backed by a dynamic array; it provides fast random access (O(1)) but slow insertion/deletion in the middle (O(n)). LinkedList is backed by a doubly linked list; it provides slow random access (O(n)) but fast insertion/deletion (O(1)) at known positions.

## What is the difference between HashMap and Hashtable?
HashMap is not synchronized and allows one null key and multiple null values. Hashtable is synchronized, does not allow null keys or values, and is slower. HashMap is preferred in single-threaded environments.

## What is the final keyword in Java?
`final` can be applied to variables (value cannot change), methods (cannot be overridden), and classes (cannot be subclassed). It is used to create constants and prevent modification.

## What is the static keyword in Java?
`static` means a member belongs to the class rather than any instance. Static variables are shared across all objects. Static methods can be called without creating an object. The static block is executed when the class is loaded.

## What is garbage collection in Java?
Garbage collection is the automatic process of reclaiming memory used by objects that are no longer reachable. The JVM handles this automatically. Developers can suggest garbage collection using `System.gc()` but cannot force it.

## What is Java 8 Stream API?
The Stream API introduced in Java 8 allows functional-style operations on sequences of elements. It supports operations like filter, map, reduce, collect, sorted, and forEach. Streams can be sequential or parallel and are lazy by nature.

## What are lambda expressions in Java?
Lambda expressions are anonymous functions introduced in Java 8. They provide a concise way to implement functional interfaces (interfaces with a single abstract method). Syntax: `(parameters) -> expression` or `(parameters) -> { statements; }`.

---

# Python

## What is Python?
Python is a high-level, interpreted, dynamically typed, and general-purpose programming language known for its simple and readable syntax. It supports multiple programming paradigms including procedural, object-oriented, and functional programming.

## What is list comprehension in Python?
List comprehension is a concise way to create lists using a single line of code. Syntax: `[expression for item in iterable if condition]`. Example: `[x**2 for x in range(10) if x % 2 == 0]` creates a list of squares of even numbers.

## What is the difference between a list and a tuple?
A list is mutable (can be changed after creation) and uses square brackets `[]`. A tuple is immutable (cannot be changed) and uses parentheses `()`. Tuples are faster and can be used as dictionary keys.

## What is a dictionary in Python?
A dictionary is an unordered collection of key-value pairs. Keys must be unique and immutable. Defined using curly braces `{}`. Common operations: `dict[key]`, `dict.get(key)`, `dict.keys()`, `dict.values()`, `dict.items()`.

## What are Python decorators?
Decorators are functions that modify the behavior of another function without changing its source code. They are applied using the `@decorator` syntax. Common use cases include logging, authentication, and memoization.

## What is the difference between deep copy and shallow copy?
A shallow copy creates a new object but inserts references to the same nested objects. A deep copy creates a completely independent clone including all nested objects. Use `copy.copy()` for shallow and `copy.deepcopy()` for deep copy.

## What are *args and **kwargs in Python?
`*args` allows a function to accept any number of positional arguments as a tuple. `**kwargs` allows any number of keyword arguments as a dictionary. They provide flexibility in function definitions.

## What is a generator in Python?
A generator is a function that uses the `yield` keyword to return values lazily, one at a time. It saves memory because it does not store all values in memory at once. Generators are useful for large or infinite data sequences.

## What is the difference between `is` and `==` in Python?
`is` checks for identity (whether two variables point to the same object in memory). `==` checks for equality (whether the values are the same). Two separate objects can be equal but not identical.

## What is exception handling in Python?
Python uses try, except, else, and finally blocks for exception handling. `try` contains code that might raise an error, `except` handles specific exceptions, `else` runs if no exception occurred, and `finally` always runs regardless of exceptions.

## What is a virtual environment in Python?
A virtual environment is an isolated environment for Python projects where you can install project-specific dependencies without affecting the global Python installation. Created using `python -m venv env_name`.

## What is Pandas?
Pandas is an open-source Python library for data manipulation and analysis. It provides two main data structures: Series (1D) and DataFrame (2D). Common operations include reading CSV/Excel files, filtering, grouping, merging, and handling missing values.

## What is NumPy?
NumPy is a Python library for numerical computing. It provides the ndarray object for efficient multi-dimensional array operations. It is faster than Python lists for mathematical operations and is the foundation for libraries like Pandas and Scikit-learn.

## What is Scikit-learn?
Scikit-learn is a Python machine learning library built on NumPy and SciPy. It provides simple tools for classification, regression, clustering, dimensionality reduction, model selection, and preprocessing.

---

# DBMS

## What is a Database Management System (DBMS)?
A DBMS is software that enables users to create, manage, and interact with databases. It provides an organized way to store, retrieve, and manipulate data. Examples include MySQL, PostgreSQL, Oracle, and SQLite.

## What is a primary key?
A primary key is a column or set of columns that uniquely identifies each row in a table. It cannot contain NULL values and must be unique across all rows. Each table can have only one primary key.

## What is a foreign key?
A foreign key is a column in one table that references the primary key of another table. It establishes a relationship between two tables and enforces referential integrity.

## What is normalization?
Normalization is the process of organizing a database to reduce redundancy and improve data integrity. It involves dividing a large table into smaller related tables. The main normal forms are 1NF, 2NF, 3NF, and BCNF.

## What is 1NF (First Normal Form)?
A table is in 1NF if all columns contain atomic (indivisible) values, each column contains values of a single type, and each row is unique. There should be no repeating groups or arrays.

## What is 2NF (Second Normal Form)?
A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the entire primary key. It eliminates partial dependencies (applies only to tables with composite primary keys).

## What is 3NF (Third Normal Form)?
A table is in 3NF if it is in 2NF and there are no transitive dependencies (no non-key column depends on another non-key column). Each non-key attribute depends only on the primary key.

## What is the difference between TRUNCATE, DELETE, and DROP?
DELETE removes specific rows based on a WHERE condition and can be rolled back. TRUNCATE removes all rows from a table without logging individual row deletions; it is faster but cannot be easily rolled back. DROP deletes the entire table structure and data permanently.

## What is a JOIN in SQL?
A JOIN combines rows from two or more tables based on a related column. Types: INNER JOIN (returns matching rows from both tables), LEFT JOIN (all rows from left + matching from right), RIGHT JOIN (all rows from right + matching from left), FULL OUTER JOIN (all rows from both tables).

## What is the difference between WHERE and HAVING?
WHERE filters rows before grouping and cannot use aggregate functions. HAVING filters groups after the GROUP BY clause and can use aggregate functions like COUNT, SUM, AVG.

## What is an index in a database?
An index is a data structure that improves the speed of data retrieval operations. It works like a book index, allowing the database engine to find rows faster without scanning the entire table. However, indexes slow down INSERT, UPDATE, and DELETE operations.

## What is a transaction in DBMS?
A transaction is a sequence of operations performed as a single logical unit of work. Transactions follow the ACID properties: Atomicity (all or nothing), Consistency (data remains valid), Isolation (concurrent transactions don't interfere), Durability (committed changes persist).

## What are ACID properties?
ACID stands for Atomicity (transaction is fully completed or fully rolled back), Consistency (database moves from one valid state to another), Isolation (concurrent transactions are isolated from each other), Durability (committed transactions are permanently saved even after failures).

## What is a view in SQL?
A view is a virtual table based on the result of a SQL query. It does not store data physically. Views simplify complex queries, provide security by restricting access to specific columns, and present data in a customized format.

## What is a stored procedure?
A stored procedure is a prepared SQL code that can be saved and reused. It can accept parameters, perform operations, and return results. Stored procedures reduce network traffic, improve performance, and enforce business logic at the database level.

## What is the difference between SQL and NoSQL?
SQL databases are relational, use structured schemas and tables, and use SQL for querying. They are ACID-compliant and good for complex queries. NoSQL databases are non-relational, schema-less, and store data in formats like documents (MongoDB), key-value (Redis), or graphs. They scale horizontally and handle unstructured data better.

---

# Operating Systems

## What is an Operating System?
An Operating System (OS) is system software that manages hardware and software resources and provides common services for computer programs. Examples include Windows, Linux, macOS, and Android.

## What is a process?
A process is a program in execution. It includes the program code, current activity (program counter), stack, data section, and heap. Each process has its own memory space and is managed by the OS.

## What is the difference between a process and a thread?
A process is an independent program in execution with its own memory space. A thread is a lightweight unit of execution within a process that shares the same memory space. Threads are faster to create and context-switch than processes.

## What is context switching?
Context switching is the process of saving the state (context) of a currently running process or thread and restoring the state of another. It allows the CPU to switch between multiple processes to give the illusion of parallelism.

## What is deadlock?
Deadlock is a situation where two or more processes are waiting for each other to release resources, resulting in all of them being stuck indefinitely. The four necessary conditions (Coffman conditions) are: Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait.

## What are the conditions for deadlock?
The four Coffman conditions for deadlock are: (1) Mutual Exclusion — only one process can use a resource at a time; (2) Hold and Wait — a process holds at least one resource while waiting for more; (3) No Preemption — resources cannot be forcibly taken; (4) Circular Wait — processes form a circular chain of waiting.

## What is CPU scheduling?
CPU scheduling is the process of determining which process in the ready queue gets CPU time. Common algorithms: FCFS (First Come First Serve), SJF (Shortest Job First), Round Robin, Priority Scheduling, and Multilevel Queue Scheduling.

## What is Round Robin scheduling?
Round Robin is a CPU scheduling algorithm where each process gets a fixed time slice (quantum) in a cyclic manner. It is fair and widely used in time-sharing systems. After the quantum expires, the process is moved to the end of the ready queue.

## What is virtual memory?
Virtual memory is a memory management technique that allows processes to use more memory than physically available by using disk space as an extension of RAM. It uses paging or segmentation to map virtual addresses to physical addresses.

## What is paging?
Paging is a memory management scheme that eliminates fragmentation by dividing physical memory into fixed-size frames and logical memory into pages of the same size. The OS maintains a page table to map virtual pages to physical frames.

## What is thrashing?
Thrashing occurs when a system spends more time swapping pages in and out of memory than executing processes. It happens when the degree of multiprogramming is too high and processes do not have enough frames to hold their working set.

## What is a semaphore?
A semaphore is a synchronization tool used to control access to shared resources by multiple processes. A binary semaphore (mutex) has values 0 and 1. A counting semaphore can have any non-negative integer value. Operations: wait (P) decrements the value, signal (V) increments it.

## What is the difference between mutex and semaphore?
A mutex is a locking mechanism where only the process that locked it can unlock it. It is used for mutual exclusion. A semaphore is a signaling mechanism and can be used to control access by multiple threads. Semaphores don't have ownership.

## What is a file system?
A file system is a method used by the OS to organize and store files on storage devices. It manages file naming, storage, retrieval, access control, and directory structure. Common file systems: NTFS (Windows), ext4 (Linux), FAT32.

---

# Data Structures & Algorithms

## What is a data structure?
A data structure is a way of organizing and storing data in memory so that it can be accessed and modified efficiently. Examples include arrays, linked lists, stacks, queues, trees, graphs, and hash tables.

## What is the difference between a stack and a queue?
A stack follows LIFO (Last In First Out) — the last element added is the first to be removed. Operations: push and pop. A queue follows FIFO (First In First Out) — the first element added is the first removed. Operations: enqueue and dequeue.

## What is a linked list?
A linked list is a linear data structure where each element (node) contains data and a pointer to the next node. Types: singly linked list (one pointer), doubly linked list (two pointers: next and previous), circular linked list. Unlike arrays, linked lists do not require contiguous memory.

## What is a binary tree?
A binary tree is a hierarchical data structure where each node has at most two children, referred to as left and right child. The topmost node is the root. Common traversals: Inorder (Left, Root, Right), Preorder (Root, Left, Right), Postorder (Left, Right, Root).

## What is a Binary Search Tree (BST)?
A BST is a binary tree where the left subtree contains nodes with values less than the root, and the right subtree contains nodes with values greater. It allows efficient searching, insertion, and deletion in O(log n) average case.

## What is Big O notation?
Big O notation describes the upper bound of an algorithm's time or space complexity as the input size grows. Common complexities: O(1) constant, O(log n) logarithmic, O(n) linear, O(n log n) linearithmic, O(n²) quadratic, O(2ⁿ) exponential.

## What is recursion?
Recursion is a technique where a function calls itself with a smaller input to solve a problem. It requires a base case to stop the recursion. Examples: factorial, Fibonacci, tree traversal. Recursive solutions can usually be converted to iterative ones.

## What is dynamic programming?
Dynamic programming is an optimization technique that solves complex problems by breaking them into overlapping subproblems and storing the results (memoization or tabulation) to avoid redundant computation. Examples: longest common subsequence, knapsack problem, Fibonacci.

## What is hashing?
Hashing is a technique to map data to a fixed-size value (hash) using a hash function. It is used in hash tables for O(1) average-time lookup. Collisions (two keys mapping to the same index) are resolved using chaining (linked lists) or open addressing.

## What is a graph?
A graph is a non-linear data structure consisting of vertices (nodes) and edges. It can be directed or undirected, weighted or unweighted. Common algorithms: BFS (Breadth-First Search), DFS (Depth-First Search), Dijkstra's (shortest path), Kruskal's and Prim's (minimum spanning tree).

---

# Computer Networks

## What is a computer network?
A computer network is a collection of interconnected devices that can communicate and share resources such as data, files, and internet access. Networks can be wired or wireless and range from small LANs to the global internet.

## What is the OSI model?
The OSI (Open Systems Interconnection) model is a 7-layer conceptual framework for how data travels across a network: Physical, Data Link, Network, Transport, Session, Presentation, and Application. Each layer has a specific responsibility, from raw bit transmission to application-level communication.

## What is the TCP/IP model?
TCP/IP is a 4-layer practical networking model used in real-world systems: Network Interface, Internet, Transport, and Application. It is simpler than the OSI model and forms the basis of how the internet actually works.

## What is the difference between TCP and UDP?
TCP (Transmission Control Protocol) is connection-oriented, reliable, and ensures ordered delivery of data using acknowledgments and retransmission. UDP (User Datagram Protocol) is connectionless, faster, and does not guarantee delivery or order, making it suitable for real-time applications like video streaming or gaming.

## What is an IP address?
An IP address is a unique numerical identifier assigned to each device on a network, used to locate and communicate with that device. IPv4 addresses are 32-bit (e.g., 192.168.1.1), while IPv6 addresses are 128-bit, designed to handle the growing number of internet-connected devices.

## What is the difference between IPv4 and IPv6?
IPv4 uses 32-bit addresses, providing about 4.3 billion unique addresses, and is written in dotted decimal format. IPv6 uses 128-bit addresses, providing a vastly larger address space, and was introduced to solve IPv4 address exhaustion.

## What is DNS?
DNS (Domain Name System) translates human-readable domain names (like google.com) into IP addresses that computers use to identify each other on the network. It acts like a phonebook for the internet.

## What is the difference between HTTP and HTTPS?
HTTP (HyperText Transfer Protocol) transmits data between a client and server in plain text. HTTPS (HTTP Secure) encrypts this data using SSL/TLS, protecting it from eavesdropping and tampering. HTTPS is the secure standard used by most modern websites.

## What is a MAC address?
A MAC (Media Access Control) address is a unique hardware identifier assigned to a device's network interface card. Unlike an IP address, which can change, a MAC address is generally fixed and used for communication within a local network.

## What is the difference between a router, switch, and hub?
A hub broadcasts incoming data to all connected devices without any filtering. A switch intelligently forwards data only to the specific device it is intended for, using MAC addresses. A router connects different networks together and directs data between them using IP addresses.

## What is a firewall?
A firewall is a network security system that monitors and controls incoming and outgoing network traffic based on predefined security rules. It acts as a barrier between a trusted internal network and untrusted external networks like the internet.

## What is a three-way handshake in TCP?
The TCP three-way handshake is the process used to establish a reliable connection between a client and server: the client sends a SYN (synchronize) request, the server responds with a SYN-ACK, and the client replies with an ACK (acknowledgment), after which data transfer can begin.

## What is the difference between a LAN, MAN, and WAN?
A LAN (Local Area Network) covers a small area like a home or office. A MAN (Metropolitan Area Network) covers a city-wide area. A WAN (Wide Area Network) covers a large geographic area, such as a country or the entire globe — the internet is the largest example of a WAN.

## What is a port number?
A port number is a numerical identifier used alongside an IP address to specify a particular process or service on a device. For example, HTTP typically uses port 80, and HTTPS uses port 443.

## What is the difference between a static IP and a dynamic IP?
A static IP address is manually configured and does not change over time, commonly used for servers. A dynamic IP address is automatically assigned by a DHCP server and can change periodically, which is the common setup for most home and mobile devices.

## What is DHCP?
DHCP (Dynamic Host Configuration Protocol) automatically assigns IP addresses and other network configuration details to devices on a network, eliminating the need for manual configuration of each device.

---

## What is Git?
Git is a distributed version control system that tracks changes in source code. It allows multiple developers to collaborate, maintain history, branch, merge, and revert changes. Key concepts: repository, commit, branch, merge, pull request.

## What is the difference between git pull and git fetch?
`git fetch` downloads changes from the remote repository but does not merge them into the working branch. `git pull` fetches and then immediately merges the changes. `git pull` = `git fetch` + `git merge`.

## What is a merge conflict?
A merge conflict occurs when two branches have made different changes to the same part of a file and Git cannot automatically determine which version to keep. The developer must manually resolve the conflict by editing the file and then committing the resolution.

## What is a .gitignore file?
A `.gitignore` file specifies files and directories that Git should not track or commit. Common entries include `node_modules/`, `__pycache__/`, `.env`, and compiled files. It helps keep the repository clean and avoid exposing sensitive data.

---