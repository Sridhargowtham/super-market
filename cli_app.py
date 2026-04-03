from grocery_store.cli import GroceryStoreCLI
from grocery_store.database import initialize_database


if __name__ == "__main__":
    initialize_database()
    print("\n🚀 GMS CLI MODE ACTIVATED")
    print("=" * 54)
    GroceryStoreCLI().run()
