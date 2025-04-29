# 🎬 Neo4j Movie Graph Project using Python

This project demonstrates how to use Neo4j's **graph database** with Python to explore and query movie data using **Cypher queries**.

---

## 🛠 Setup Instructions

### 1. Install Neo4j Desktop  
- Download Neo4j Desktop from the [official site](https://neo4j.com/download/).
- Install and activate with the license key provided.
- Create or open a project and use the **preloaded Movie database**.

### 2. Python Setup  
Install the required package:

```bash
pip install neo4j
```

---

## 💡 Project Overview

This project uses the `neo4j` Python driver to connect with the Neo4j database and run Cypher queries. The queries help analyze relationships between **People** and **Movies**—like roles, number of collaborations, and more.

---

## 🔍 Key Features / Queries

- List people and their roles in movies (actor, director, producer, etc.)
- List of all movies with release year and tagline
- Top 5 directors by number of movies directed
- People who directed and produced the same movie
- People who worked in more than 6 movies
- Actors who also wrote or directed the same movie
- Get all roles of a given person
- Get all people involved in a given movie
- Calculate actor’s age at the time of the movie (work age)

---

## 📁 File Structure

- `Neo4jConnection` class: handles connection and query execution
- `result_to_dataframe()`: converts query results to pandas DataFrame
- `graphs_to_csv()`: utility to extract and structure data by labels and properties

---

## ✅ Requirements

- Neo4j Desktop (with Movie database)
- Python 3.x
- Packages: `neo4j`, `pandas`

---

 
