import streamlit as st
from cryptography.fernet import Fernet

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="File Encryptor ", layout="centered")

st.title(" File Encryption & Decryption System")
st.write("Secure your files using encryption!")

# -------------------------------
# Functions
# -------------------------------
def generate_key():
    return Fernet.generate_key()

def encrypt_file(file_data, key):
    f = Fernet(key)
    return f.encrypt(file_data)

def decrypt_file(file_data, key):
    f = Fernet(key)
    return f.decrypt(file_data)

# -------------------------------
# Session State Initialization
# -------------------------------
if "encrypted_data" not in st.session_state:
    st.session_state.encrypted_data = None

if "filename" not in st.session_state:
    st.session_state.filename = None

# -------------------------------
# Tabs
# -------------------------------
tab1, tab2 = st.tabs([" Encrypt", " Decrypt"])

# ===============================
# ENCRYPTION TAB
# ===============================
with tab1:
    st.subheader("Encrypt Your File")

    uploaded_file = st.file_uploader("Upload a file")

    if uploaded_file is not None:
        file_data = uploaded_file.read()

        if st.button("Encrypt File"):
            key = generate_key()
            encrypted_data = encrypt_file(file_data, key)

            # Store in session
            st.session_state.encrypted_data = encrypted_data
            st.session_state.filename = uploaded_file.name

            st.success("File Encrypted Successfully!")

            # Download only key
            st.download_button(
                label="Download Secret Key ",
                data=key,
                file_name="secret.key"
            )

# ===============================
# DECRYPTION TAB
# ===============================
with tab2:
    st.subheader("Decrypt Your File")

    key_file = st.file_uploader("Upload secret key")

    if key_file is not None and st.session_state.encrypted_data is not None:
        key = key_file.read()

        if st.button("Decrypt File"):
            try:
                decrypted_data = decrypt_file(st.session_state.encrypted_data, key)

                st.success("File Decrypted Successfully!")

                st.download_button(
                    label="Download Decrypted File",
                    data=decrypted_data,
                    file_name=st.session_state.filename
                )

            except:
                st.error("Invalid Key!")

    else:
        st.info("Please encrypt a file first and upload the correct key.")