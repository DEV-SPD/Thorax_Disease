import streamlit as st   


def main():
    st.title('THORAX DISEASE DIAGNOSIS')
    uploaded_file = st.file_uploader("UPLOAD X-RAY IMAGE", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
    # Display the uploaded image
     st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)

if __name__ == '__main__':
    main()
