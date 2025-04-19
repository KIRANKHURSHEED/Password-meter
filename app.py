import string
import streamlit as st

st.title("Password Strength Meter Kiran Khursheed")

password = st.text_input("Enter Your Password", type="password")

score = 0

if st.button("Check Password Strength"):

    if len(password) >= 8:
        score += 1
        st.success("✔️ Password length is good.")
    else:
        st.error("❌ Password should be at least 8 characters long.")

    if any(char.isupper() for char in password):
        score += 1
        st.success("✔️ Contains uppercase letter.")
    else:
        st.error("❌ Add at least one uppercase letter.")

    if any(char.islower() for char in password):
        score += 1
        st.success("✔️ Contains lowercase letter.")
    else:
        st.error("❌ Add at least one lowercase letter.")

    if any(char.isdigit() for char in password):
        score += 1
        st.success("✔️ Contains a digit.")
    else:
        st.error("❌ Add at least one digit.")

    if any(char in string.punctuation for char in password):
        score += 1
        st.success("✔️ Contains special character.")
    else:
        st.error("❌ Add at least one special character.")

    st.write(f"🔒 Your password score is: *{score}/5*")

    if score == 5:
        st.success("✅ Strong password 💪")
    elif score == 4:
        st.warning("⚠️ Good password, but could be stronger.")
    else:
        st.error("❌ Weak password. Please improve it.")

    st.subheader("🔐 Password Suggestions for Stronger Security")
    st.markdown("""
- Must be at least 8 characters long  
- Include at least one uppercase letter (A–Z)  
- Include at least one lowercase letter (a–z)  
- Include at least one number (0–9)  
- Include at least one special character (e.g., !@#$%^&*)  
""")
