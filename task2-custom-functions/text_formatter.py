def format_text(text: str, uppercase: bool = False, align: str = "left") -> str:
    # Validate input types
    if not isinstance(text, str):
        raise ValueError("Input text must be a string.")
    
    if align not in ("left", "center", "right"):
        raise ValueError("Alignment must be 'left', 'center', or 'right'.")

    # Convert to uppercase if specified
    formatted_text = text.upper() if uppercase else text

    # Apply alignment
    if align == "center":
        formatted_text = formatted_text.center(30)
    elif align == "right":
        formatted_text = formatted_text.rjust(30)
    else:  # Default "left" alignment (no need for an explicit check since "left" is default)
        formatted_text = formatted_text.ljust(30)
    
    return formatted_text

text=input(print("please Enter text to format"))
if __name__ == "__main__":
    try:
        print(format_text(text))  # Default formatting (left alignment)
        print(format_text(text, True))  # Uppercase formatting
        print(format_text(text, align="center"))  # Center alignment
        print(format_text(text, align="right"))  # Right alignment
        print(format_text(123))  
        
    except ValueError as e:
        print(f"Error: {e}")
