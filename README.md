# 🛍️ Optimart - Smart Price Comparison & Recommendation Engine

> **Find the Best Deals Instantly using Advanced Data Structures**

## 🚀 Overview
**Optimart** is a high-performance e-commerce simulation tool built for a **Hackathon** to demonstrate the practical application of **Data Structures and Algorithms (DSA)** in real-world scenarios. 

Unlike typical price comparison tools that rely solely on APIs, Optimart implements core algorithms from scratch to solve common e-commerce problems:
*   **Instant Search** via Tries
*   **Price Comparison** via Min-Heaps
*   **Product Recommendations** via Graph Traversal (BFS)
*   **Fast Lookups** via HashTables

## ✨ Key Features
*   **⚡ Lightning Fast Search**: Auto-complete and prefix search for instant product discovery.
*   **💰 Smart Price Comparison**: Automatically aggregates prices from multiple "sellers" and highlights the cheapest option.
*   **🤝 Intelligent Recommendations**: Suggests similar products based on specifications and price range using graph algorithms.
*   **📊 Interactive Dashboard**: A beautiful, dark-themed UI built with Streamlit for seamless user experience.

## 🛠️ Technology Stack
*   **Frontend**: Streamlit (Python)
*   **Backend Logic**: Python
*   **Data Structures**: Custom implementations of Heap, Graph, Trie, and HashMap.
*   **Styling**: Custom CSS (Glassmorphism & Dark Mode)

## 🧠 Data Structures & Algorithms (The Core)

This project showcases the power of choosing the *right* data structure for the *right* problem:

| Feature | Data Structure | Time Complexity | Why it was used? |
| :--- | :--- | :--- | :--- |
| **Product Lookup** | **HashMap (Dictionary)** | **O(1)** | Instant access to product details by name without iterating through lists. |
| **Lowest Price** | **Min-Heap (Priority Queue)** | **O(log N)** | Efficiently extracts the minimum price from multiple sellers; faster than sorting **O(N log N)**. |
| **Auto-Complete** | **Trie (Prefix Tree)** | **O(M)** | Enables fast prefix-based search suggestions, independent of the total number of products. |
| **Recommendations** | **Graph + BFS** | **O(V + E)** | Models products as nodes and similarities as edges to find "nearest neighbors" (alternatives) dynamically. |

### Implementation Details
*   **`dsa/hashmap.py`**: Custom wrapper around Python's dictionary to manage product-seller relationships.
*   **`dsa/heap_utils.py`**: A binary heap implementation to maintain a sorted order of prices for quick retrieval.
*   **`dsa/tree_search.py`**: A full Trie implementation where every node represents a character, enabling efficient prefix matching.
*   **`dsa/graph_recommend.py`**: Builds an adjacency list where edges represent product similarity (specs/price). Uses Breadth-First Search (BFS) to traverse and find related items.

## 📸 Screenshots
![Architecture Diagram](architecture_diagram.png)

## 📦 How to Run
1.  **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/optimart.git
    cd optimart
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Application**:
    ```bash
    streamlit run app.py
    ```

61:     ```
62: 
63: ## 🚀 How is Optimart Better? (DSA Advantage)
64: 
65: | Feature | ❌ Traditional Approach | ✅ Optimart (DSA Optimized) |
66: | :--- | :--- | :--- |
67: | **Search** | **O(N)** scan (slow with large data) | **O(M)** Trie Search (instant regardless of db size) |
68: | **Best Price** | **O(N log N)** Sorting (computational heavy) | **O(1)** Min-Heap Extraction (instant access) |
69: | **Recommendations** | Static category lists | **Graph + BFS** smart traversal of specs/price |
70: | **History** | Database queries (slower) | **Stack** (LIFO) for immediate undo/backtrack |
71: | **Trend Analysis** | Complex BI tools | **Queue** (FIFO) for sliding window price tracking |
72: 
73: ## 🔮 Future Scope
*   **Real-time API Integration**: Connect to Amazon/Flipkart APIs for live data.
*   **Machine Learning**: Use collaborative filtering for personalized user recommendations.
*   **Visual Search**: Integrate image processing to find products by photo.

---
*Built with ❤️ for the Hackathon*
