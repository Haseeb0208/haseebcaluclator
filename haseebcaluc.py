import streamlit as st

def main():
    st.title("Simple Calculator")
    
    # Input fields for numbers
    num1 = st.number_input("Enter the first number", value=0.0, step=0.1, format="%.2f")
    num2 = st.number_input("Enter the second number", value=0.0, step=0.1, format="%.2f")

    # Dropdown for selecting operation
    operation = st.selectbox("Choose an operation", ["Add", "Subtract", "Multiply", "Divide"])

    # Perform calculation based on selected operation
    if operation == "Add":
        result = num1 + num2
        st.write(f"**Result:** {num1} + {num2} = {result}")
    elif operation == "Subtract":
        result = num1 - num2
        st.write(f"**Result:** {num1} - {num2} = {result}")
    elif operation == "Multiply":
        result = num1 * num2
        st.write(f"**Result:** {num1} * {num2} = {result}")
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
            st.write(f"**Result:** {num1} / {num2} = {result}")
        else:
            st.error("Division by zero is not allowed.")

if __name__ == "__main__":
    main()
