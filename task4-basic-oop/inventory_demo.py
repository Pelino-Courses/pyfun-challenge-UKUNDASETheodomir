from product import Product

def main():
    try:
        apple = Product("Apple", 0.5, 100)
        print(apple.display_info())

        print("\nAdding 50 apples...")
        apple.add_inventory(50)

        print("\nRemoving 30 apples...")
        apple.remove_inventory(30)

        print("\nFinal Inventory:")
        print(apple.display_info())

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
