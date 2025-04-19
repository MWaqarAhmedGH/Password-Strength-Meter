#  Password Strength Meter

#  hum Streamlit library ko import kar rahe hain aur uska short name st rakh rahe hain.
import streamlit as st

#  Yeh built-in re module hai aur ye regular expressions ke liye hota hai, jis se aap strings ko match, search, replace, ya validate kar sakte ho
import re

#  My App Title
st.title("💻Password Strength Meter")

#  Description
st.markdown("""
    👍Welcome to the **Password Strength Meter!**
    Ensure your password is secure by checking: 
    -  ✔  Length
    -  ✔  Uppercase letters
    -  ✔  Lowercase letters
    -  ✔  Numbers
    -  ✔  Special characters *Improve Your Online Security by Creating Strong Password!*    
            """)

#  Check Password Strength Function
def check_password_strength(password):
    """Check the strength of a password and return a score and message."""
    score = 0
    tips = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        tips.append("🟥Password should be at least 8 characters long.\n")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        tips.append("🟨Password should contain at least one uppercase letter.\n")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        tips.append("🟩Password should contain at least one lowercase letter.\n")

    # Check for numbers
    if re.search(r'\d', password):
        score += 1
    else:
        tips.append("🟪Password should contain at least one number.\n")

    # Check for special characters
    if re.search(r'[@$!%*?&]', password):
        score += 1
    else:
        tips.append("🟫Password should contain at least one special character (@$!%*?&).\n")

    return score, tips

def main():
    password = st.text_input("🔐Enter your password:", type="password")
    if password:
        score, tips = check_password_strength(password)
        if score == 5:
            st.success("✅ Strong Password!")
        elif score >= 3:
            st.warning("⚠️ Moderate Password - Consider adding more security features.")
        else:
            st.error("❌ Weak Password - Improve it using the suggestions below.")
        
        # Display score and suggestions
        st.write(f"🔊Password Strength Score: {score}/5")
        st.write("🎤Suggestions to improve your password:")
        for tip in tips:
            st.write(f"- {tip}")

main()

