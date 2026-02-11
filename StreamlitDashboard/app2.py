import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Sortable Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.sidebar-title {
    font-size: 20px;
    font-weight: bold;
    color: #2563EB;
}
.menu-item {
    font-size: 16px;
    padding: 6px 0;
}
.dashboard-box {
    padding: 20px;
    border-radius: 12px;
    background-color: #F9FAFB;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
}
.icon-blue { color:#2563EB; }
.icon-green { color:#16A34A; }
.icon-red { color:#DC2626; }
.icon-orange { color:#F59E0B; }
.icon-purple { color:#7C3AED; }
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.markdown("<div class='sidebar-title'>📊 Sortable App</div>", unsafe_allow_html=True)

menu = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "📋 Sortable List",
        "🔲 Sortable Grid",
        "💾 Saved Layouts",
        "⚙️ Admin Panel",
        "❓ Help"
    ]
)

# ---------------- DASHBOARD ----------------
if menu == "🏠 Dashboard":
    st.title("📊 Sortable Management Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="dashboard-box">
        <h4 class="icon-blue">📋 Sortable List</h4>
        <p>Drag & reorder list items interactively.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="dashboard-box">
        <h4 class="icon-purple">🔲 Sortable Grid</h4>
        <p>Arrange items in grid-based layout.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="dashboard-box">
        <h4 class="icon-green">💾 Saved Orders</h4>
        <p>View and restore saved item layouts.</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------- SORTABLE LIST ----------------
elif menu == "📋 Sortable List":
    st.title("📋 Sortable List Panel")

    st.info("This section simulates sortable list behavior (UI demo).")

    items = st.multiselect(
        "Drag simulation (select order):",
        ["Item One", "Item Two", "Item Three", "Item Four", "Item Five"],
        default=["Item One", "Item Two", "Item Three"]
    )

    st.success("Current Order:")
    st.write(items)

    if st.button("🔄 Reset Order"):
        st.warning("Order reset to default (simulation).")

# ---------------- SORTABLE GRID ----------------
elif menu == "🔲 Sortable Grid":
    st.title("🔲 Sortable Grid Panel")

    cols = st.columns(3)
    labels = ["A", "B", "C", "D", "E", "F"]

    for i, label in enumerate(labels):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="dashboard-box icon-orange" style="text-align:center;">
            <h3>{label}</h3>
            </div>
            """, unsafe_allow_html=True)

    st.caption("Grid sorting can be enabled using JS integration later.")

# ---------------- SAVED LAYOUTS ----------------
elif menu == "💾 Saved Layouts":
    st.title("💾 Saved Layouts")

    st.table({
        "Layout Name": ["Default Layout", "Custom Order 1"],
        "Status": ["Active", "Saved"],
        "Last Updated": ["Today", "Yesterday"]
    })

    st.button("♻️ Restore Default")

# ---------------- ADMIN PANEL ----------------
elif menu == "⚙️ Admin Panel":
    st.title("⚙️ Admin Control Panel")

    st.subheader("Item Management")

    col1, col2 = st.columns(2)

    with col1:
        st.text_input("Add New Item")
        st.button("➕ Add Item")

    with col2:
        st.selectbox("Delete Item", ["Item One", "Item Two", "Item Three"])
        st.button("🗑️ Delete Item")

    st.subheader("System Settings")
    st.checkbox("🔒 Lock Item Positions")
    st.checkbox("🖱️ Enable Dragging")

# ---------------- HELP ----------------
elif menu == "❓ Help":
    st.title("❓ Help & Support")

    st.markdown("""
    ### How to Use
    - Navigate using sidebar
    - Drag & reorder items (simulation)
    - Save or reset layouts
    - Admin can manage items

    📧 Support: support@example.com
    """)

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("© 2026 Sortable UI Demo | Built with Streamlit")
