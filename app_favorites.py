import streamlit as st

def run_favorites():
    if 'favorites' not in st.session_state:
        st.session_state.favorites = []

    st.title("Your Favorite Items")

    # Check if there are any favorite items
    if st.session_state.favorites:
        # Display items in a grid with 3 columns per row
        cols = st.columns(3)
        to_remove = []

        for i, item in enumerate(st.session_state.favorites):
            with cols[i % 3]:
                # Display item details: image, name, price
                st.image(item['image'], use_column_width=True)
                st.write(item['name'])
                st.write(f"Price: ${item['price']}")

                # Button to remove item from favorites
                if st.button("Remove from Favorites", key=f"remove_{item['name']}"):
                    to_remove.append(item)  # Mark item for removal

        # Remove items that were marked for deletion
        for item in to_remove:
            st.session_state.favorites.remove(item)
            st.success(f"Removed {item['name']} from favorites.")
    else:
        st.write("No favorite items yet. Start adding some!")
