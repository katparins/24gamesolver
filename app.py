import streamlit as st
import pathlib
from solver import solve_24_game

# Page config
st.set_page_config(page_title="24 Game Solver", page_icon="🩷", layout="centered")

# Load external CSS
def load_css(file_path):
    with open(file_path) as file:
        st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)

css_path = pathlib.Path("styles.css")
load_css(css_path)

# Title
st.title("24 Game Solver")
st.markdown("Give me 4 numbers and let's find all the ways to make **24** 💅")

# User inputs
col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("1️⃣ FIRST number", min_value=1, max_value=100, step=1, key="num1")
with col2:
    num2 = st.number_input("2️⃣ SECOND number", min_value=1, max_value=100, step=1, key="num2")

col3, col4 = st.columns(2)
with col3:
    num3 = st.number_input("3️⃣ THIRD number", min_value=1, max_value=100, step=1, key="num3")
with col4:
    num4 = st.number_input("4️⃣ FOURTH number", min_value=1, max_value=100, step=1, key="num4")

# Solve button
solve_clicked = st.button("✨Solve it!")

# Solver logic
if solve_clicked:
    input_list = [num1, num2, num3, num4]
    solutions = solve_24_game(input_list)

    st.markdown("---")
    if solutions:
        st.success("🎉 Yay! We've found solutions:")
        unique_solutions = list(set(solutions))
        for solution in unique_solutions:
            st.write(f"🌟 {solution}")
    else:
        st.error("😢 No solution found. Try different numbers!")
        
    st.markdown("---")
    st.markdown(
        """
        <div class='message'>
        <b>This solver was built with pure big brain energy 🧠</b>  
        <br><br>
        It all started when a girl got dumped, took an intro to programming class out of heartbreak and boredom,  
        and <u>wrote 4000 lines of for loops to cope</u> 😭  
        <br><br>
        After some procrastination, healing, landing a tech internship, and getting a new boyfriend (love u 💖),  
        she realized she actually <i>likes</i> coding. Now she's doing a second degree in CS and finally refactored  
        those 4000 lines down to 300 💪  
        <br><br>
        Shoutout to her current bf for the push to finish this project so she could finally share it.  
        She promises no other solver online handles edge cases like this one — and yes,  
        she once beat the entire 24 game app with her own code.  
        <br><br>
        ✨ Girl math, but make it computer science ✨  
        <br><br>
        <b>Thanks for playing 🩷</b>
        <br>
        Try different numbers — and if something breaks, DM <a href='https://instagram.com/katparins' target='_blank'>@katparins</a> 🫶
        </div>
        """,
        unsafe_allow_html=True
    )