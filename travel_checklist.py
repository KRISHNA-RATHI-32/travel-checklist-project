import streamlit as st

st.set_page_config(page_title="Travel Checklist", layout="centered")

st.title("🧳 Travel Checklist")

# Initialize session state for checklist and checked states
if 'checklist' not in st.session_state:
    st.session_state['checklist'] = []
if 'checked' not in st.session_state:
    st.session_state['checked'] = []

# Input for new item
with st.form(key='add_item_form', clear_on_submit=True):
    new_item = st.text_input("Add an item", placeholder="e.g., Passport, Toothbrush", key='new_item')
    add_clicked = st.form_submit_button("Add", use_container_width=True)
    if add_clicked and new_item.strip():
        st.session_state['checklist'].append(new_item.strip())
        st.session_state['checked'].append(False)

# Display checklist
st.subheader("Your Items:")
if st.session_state['checklist']:
    remove_indices = []
    for idx, item in enumerate(st.session_state['checklist']):
        col1, col2, col3 = st.columns([1, 7, 2])
        with col1:
            checked = st.checkbox("", value=st.session_state['checked'][idx], key=f'checkbox_{idx}')
            st.session_state['checked'][idx] = checked
        with col2:
            st.markdown(f"- {'~~' + item + '~~' if checked else item}")
        with col3:
            if st.button("Remove", key=f'remove_{idx}', use_container_width=True):
                remove_indices.append(idx)
    # Remove items after loop to avoid index errors
    for idx in sorted(remove_indices, reverse=True):
        st.session_state['checklist'].pop(idx)
        st.session_state['checked'].pop(idx)
    st.markdown("---")
    if st.button("Clear All", type="primary", use_container_width=True):
        st.session_state['checklist'].clear()
        st.session_state['checked'].clear()
else:
    st.info("Your checklist is empty. Add items to get started!")

st.markdown("<style>button, input, .stTextInput, .stButton {font-size: 1.2em !important;} .stButton>button {width: 100%;}</style>", unsafe_allow_html=True) 
