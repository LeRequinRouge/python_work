def order_sandwich(*contents):
    print(f"\nYour sandwich contains the following ingredients:")
    for content in contents:
        print(f"- {content}")


order_sandwich("lettuce", "tomato")
order_sandwich("mayo", "pickle", "mustard", "turkey", "provolone")
