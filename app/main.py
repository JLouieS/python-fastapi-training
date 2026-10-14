from products import load_products, available_products, products_by_category, total_inventory_value, build_summary, save_report, find_product, ProductNotFoundError

if __name__ == "__main__":
    products = load_products("data/products.json")
    print([p["name"] for p in available_products(products)])            # ['Keyboard', 'Monitor']
    print([p["name"] for p in products_by_category(products, "display")])  # ['Monitor']
    print(total_inventory_value(products))                              # 83000

    report = build_summary(products)
    print(report)
    save_report(report, "data/report.json")

    print(find_product(products, 3)["name"])   # Monitor

    try:
        find_product(products, 99)
    except ProductNotFoundError as e:
        print(f"Caught: {e}")                  # Caught: Product with id 99 not found
