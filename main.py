import streamlit as st

def main():
    if 'page' not in st.session_state:
        st.session_state.page = "home"

    st.sidebar.title("Navigation")
    st.sidebar.button("Home", on_click=lambda: setattr(st.session_state, 'page', "home"), key="main_home_button")
    st.sidebar.button("Go to App", on_click=lambda: setattr(st.session_state, 'page', "app"), key="main_app_button")
    st.sidebar.button("Favorites", on_click=lambda: setattr(st.session_state, 'page', "favorites"), key="main_favorites_button")
    st.sidebar.button("About", on_click=lambda: setattr(st.session_state, 'page', "about"), key="main_about_button")

    if st.session_state.page == "app":
        import app
        app.run_app()
    elif st.session_state.page == "favorites":
        import app
        app.run_favorites()
    elif st.session_state.page == "about":
        import about
        about.run_about()
    else:
        import home
        home.show_home()

if __name__ == "__main__":
    main()
