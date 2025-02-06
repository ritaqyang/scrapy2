import json
import os


current_path = os.path.abspath(__file__)
json_path = os.path.join(os.path.dirname(current_path), "results.json")
with open(json_path, "r", encoding="utf-8") as file:
    products = json.load(file)

categories = {}
for product in products:
    code, category, description, amount, imageURL = product.values()
    if category not in categories:
        categories[category] = []
    product['image'] = imageURL.strip()
    product['unitPrice'] = 8.99
    categories[category].append(product)

category_map = []
for category, items in categories.items():

    category_code = category.split(" ")[0].lower()

    # create a category map for the react redux store 
    category_items = {
        "category": category_code,
        "products": items
    }
    category_map.append(category_items)


# Create an output directory if it doesn't exist
output_dir = "categories"
os.makedirs(output_dir, exist_ok=True)

filename = f"{output_dir}/category_map.json"

with open(filename, "w", encoding="utf-8") as file:
    json.dump(category_map, file, indent=4, ensure_ascii=False)
# # Save each category's products into separate JSON files
# for category, items in categories.items():
#     filename = f"{output_dir}/category_{category.replace(' ', '_').replace('/', '_')}.json"
#     with open(filename, "w", encoding="utf-8") as file:
#         json.dump(items, file, indent=4, ensure_ascii=False)
#     print(f"Created file: {filename}")

print("Separation complete!")
