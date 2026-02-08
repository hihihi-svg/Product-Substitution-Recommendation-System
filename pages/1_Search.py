# ==================== pages/1_Search.py (SEARCH & PRODUCT LISTING) ====================
import streamlit as st
import pandas as pd
from data.products import PRODUCT_DATA, get_products_by_category
from dsa.hashmap import ProductHashMap
from dsa.tree_search import TrieSearch
from utils.theme import apply_dark_theme

st.set_page_config(page_title="Search Products", page_icon="🔍", layout="wide")
apply_dark_theme()

# ==================== TOP NAVIGATION ====================
col1, col2, col3, col4, col5 = st.columns([3, 1, 1, 1, 1])

with col1:
    st.markdown("## 🛍️ **Price Comparison System**")

with col2:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("app.py")

with col3:
    if st.button("ℹ️ About", use_container_width=True):
        st.switch_page("pages/4_About.py")

with col4:
    if st.button("👤 Profile", use_container_width=True):
        st.switch_page("pages/3_Profile.py")

with col5:
    cart_count = len(st.session_state.get('cart', []))
    st.button(f"🛒 Cart ({cart_count})", use_container_width=True)

st.markdown("---")

# ==================== BACK BUTTON ====================
if st.button("⬅️ Back to Home"):
    st.switch_page("app.py")

# ==================== PAGE HEADER ====================
category = st.session_state.get('selected_category', 'Electronics')
st.markdown(f"## 🔍 Search in {category}")

# ==================== SEARCH BAR ====================
# Check if we need to clear search
if st.session_state.get('clear_search', False):
    st.session_state.clear_search = False
    search_query = ""
else:
    col1, col2 = st.columns([4, 1])

    with col1:
        search_query = st.text_input(
            "Search for products",
            placeholder=f"Type product name... (e.g., iPhone, Laptop, Watch)",
            key="search_input",
            label_visibility="collapsed"
        )

    with col2:
        search_button = st.button("🔍 Search", use_container_width=True, type="primary")

# ==================== DATA STRUCTURE IMPLEMENTATION ====================

# Initialize HashMap
product_hashmap = ProductHashMap()
all_products = get_products_by_category(category)

# Build HashMap: product_name -> list of seller entries
for product in all_products:
    product_hashmap.insert(product['name'], product)

# Initialize Trie for prefix search
trie = TrieSearch()
unique_names = list(set([p['name'] for p in all_products]))
for name in unique_names:
    trie.insert(name)

# ==================== SEARCH LOGIC ====================
# Check if a suggestion was clicked
if 'selected_suggestion' in st.session_state and st.session_state.selected_suggestion:
    search_query = st.session_state.selected_suggestion
    st.session_state.selected_suggestion = None

if search_query:
    # Using Trie for prefix-based suggestions
    suggestions = trie.search_prefix(search_query)
    
    if suggestions and len(suggestions) > 1:
        # Show inline dropdown suggestions (Google-style)
        st.markdown("""
        <style>
        .suggestion-box {
            background: #1e293b;
            border: 1px solid #334155;
            border-radius: 8px;
            padding: 10px;
            margin-top: -10px;
            margin-bottom: 20px;
        }
        .suggestion-item {
            padding: 8px 12px;
            cursor: pointer;
            border-radius: 4px;
            transition: background 0.2s;
        }
        .suggestion-item:hover {
            background: #334155;
        }
        </style>
        """, unsafe_allow_html=True)
        
        st.info(f"💡 **Trie Search:** Found {len(suggestions)} matching products")
        
        # Display suggestions as clickable items
        st.markdown("<div class='suggestion-box'>", unsafe_allow_html=True)
        st.markdown("**🔍 Did you mean:**")
        
        cols = st.columns(min(3, len(suggestions[:6])))
        for idx, suggestion in enumerate(suggestions[:6]):
            with cols[idx % 3]:
                if st.button(f"🔎 {suggestion}", key=f"suggest_{suggestion}", use_container_width=True):
                    st.session_state.selected_suggestion = suggestion
                    st.rerun()
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Using HashMap for fast lookup
    results = []
    for suggestion in suggestions:
        products = product_hashmap.get(suggestion)
        if products:
            results.extend(products)
    
    filtered_results = results
else:
    # Show all products in category
    filtered_results = all_products

# ==================== DISPLAY RESULTS ====================
st.markdown(f"### 📊 Found {len(filtered_results)} products from multiple sellers")

if filtered_results:
    # Group by product name
    product_groups = {}
    for p in filtered_results:
        if p['name'] not in product_groups:
            product_groups[p['name']] = []
        product_groups[p['name']].append(p)
    
    # Display in Queue order (FIFO - ordered display)
    st.info("📋 **Queue Data Structure:** Products displayed in ordered sequence (FIFO)")
    
    for idx, (product_name, variants) in enumerate(product_groups.items(), 1):
        st.markdown(f"#### {idx}. {product_name}")
        
        # Create DataFrame for table display
        df_data = []
        for v in variants:
            df_data.append({
                'Seller/Website': v['seller'],
                'Price': f"₹{v['price']:,}",
                'Rating': f"⭐ {v['rating']}",
                'Raw_Price': v['price']  # Hidden column for sorting
            })
        
        df = pd.DataFrame(df_data)
        
        # Sort by price (lowest first)
        df = df.sort_values('Raw_Price')
        df = df.drop('Raw_Price', axis=1)
        
        # Display table
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )
        
        # Compare button
        col1, col2, col3 = st.columns([2, 1, 1])
        
        with col1:
            if st.button(f"⚖️ Compare All Prices", key=f"compare_{product_name}", use_container_width=True):
                st.session_state.selected_products = variants
                st.session_state.selected_product_name = product_name
                st.switch_page("pages/2_Compare.py")
        
        with col2:
            min_price = min([v['price'] for v in variants])
            st.success(f"💰 Best: ₹{min_price:,}")
        
        with col3:
            max_rating = max([v['rating'] for v in variants])
            st.info(f"⭐ Top: {max_rating}")
        
        st.markdown("---")

else:
    st.warning("❌ No products found. Try a different search term or category.")
    
    if st.button("🔄 View All Products"):
        st.session_state.clear_search = True
        st.rerun()

# ==================== DATA STRUCTURE EXPLANATION ====================
st.markdown("<br>", unsafe_allow_html=True)

with st.expander("🔧 Data Structures in Action (Click to Expand)", expanded=False):
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### HashMap Implementation
        - **Purpose:** Fast product lookup
        - **Time Complexity:** O(1) average
        - **Usage:** `product_name → [seller_entries]`
        
        ### Trie (Prefix Tree)
        - **Purpose:** Auto-complete suggestions
        - **Time Complexity:** O(m) where m = query length
        - **Usage:** Prefix-based search as you type
        """)
    
    with col2:
        st.markdown("""
        ### Queue (FIFO)
        - **Purpose:** Ordered display of results
        - **Time Complexity:** O(1) enqueue/dequeue
        - **Usage:** Maintains sequential product loading
        
        ### Array/List
        - **Purpose:** Store product records
        - **Time Complexity:** O(n) for iteration
        - **Usage:** Base storage for seller data
        """)

st.markdown("<br>", unsafe_allow_html=True)