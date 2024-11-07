import streamlit as st
import random


tab1, tab2 = st.tabs(["Portfolio", "Guessing Game"])

# Portfolio tab content
with tab1:
    # Page title and intro
    st.title("ANAND's Portfolio")
    st.write("Welcome to my portfolio! I am a BTech student specializing in Artificial Intelligence and Data Science.")
    
    # Contact Information
    st.header("Contact Information")
    st.write("📧 Email: [vishnuanand0775@gmail.com](mailto:your.email@example.com)")
    st.write("💼 LinkedIn: [linkedin.com/in/ANAND](https://www.linkedin.com/in/anand-p-2490b0315?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)")
    st.write("💻 GitHub: [github.com/ANAND](https://github.com/Vishnu-beep-code)")
    
    # Education
    st.header("Education")
    st.write("**Bachelor of Technology in Artificial Intelligence and Data Science**")
    st.write("KITE, Expected Graduation: [2028]")
    
    # Skills
    st.header("Skills")
    st.write("- Programming Languages: Python, JavaScript")
    st.write("- Frameworks: , Streamlit")
    st.write("- Tools: Git, Visual Studio Code, Jupyter Notebook")
    
    
    
    # Extracurriculars
    st.header("Extracurricular Activities")
    st.write("like to play piano -Musical keyboard,esports")
    
    # Footer
    st.write(" ")
    st.write("Thank you for visiting my portfolio!")

with tab2:
    # Initialize or reset the game state
    if "target_number" not in st.session_state:
        st.session_state.target_number = random.randint(1, 100)
        st.session_state.attempts = 0

    # App title
    st.title("Guess the Number Game")

    # Instructions
    st.write("I'm thinking of a number between 1 and 100. Can you guess what it is?")

    # Input from the user
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

    # Button to check the guess
    if st.button("Submit Guess"):
        st.session_state.attempts += 1

        # Check if the guess is correct, too high, or too low
        if guess < st.session_state.target_number:
            st.write("Too low! Try again.")
        elif guess > st.session_state.target_number:
            st.write("Too high! Try again.")
        else:
            st.write(f"Congratulations! You guessed it in {st.session_state.attempts} attempts.")
            # Reset game
            st.session_state.target_number = random.randint(1, 100)
            st.session_state.attempts = 0
            st.write("I've picked a new number. Let's play again!")

    # Optional: display the number of attempts
    st.write(f"Attempts: {st.session_state.attempts}")

