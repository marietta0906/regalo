import streamlit as st
from PIL import Image
# Everything is accessible via the st.secrets dict:
# streamlit_app.py
def check_password():
    """Returns `True` if the user had the correct password."""
    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["db_password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False
    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True
if check_password():
    st.write("Le soleil se couche et la nuit tombe sur Paris, le bateau vient de larguer les amarres et le quai s’éloigne doucement. Nous venons d’embarquer pour un dîner croisière d’exception avec la compagnie des Bateaux Mouches… La ville lumière se dévoile peu à peu alors que nous glissons doucement sur la Seine scintillante. L’instant est romantique, la magie opère … Nous sommes les acteurs de cette magnifique pièce qui ne se joue que pour nous. Le raffinement de la carte fait écho à ce cadre exceptionnel et illustre un art culinaire guidé par l’excellence. Un diner croisière qui restera un moment privilégié de notre vie à Paris. Une manière élégante et romantique de découvrir ou redécouvrir Paris depuis la Seine. Rendez-vous le samedi 10 septembre pour vivre cette expérience! Je t'aime")
    image = Image.open('photo maria arques.jpg')
    st.image(image)