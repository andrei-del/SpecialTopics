
import tkinter as tk
import requests  

class RecipeSearchApp:
    def __init__(self, master):
        self.master = master
        master.title("Recipe Search App")

        # Welcome Label
        self.label = tk.Label(master, text="Welcome to the online cookingbook!", font=("Helvetica", 16))
        self.label.pack(pady=10)

        # Search Entry
        self.entry_label = tk.Label(master, text="Enter keyword:")
        self.entry_label.pack(pady=5)
        self.entry = tk.Entry(master, width=30)
        self.entry.pack(pady=5)

        # Search Button
        self.search_button = tk.Button(master, text="Search", command=self.search_recipes)
        self.search_button.pack(pady=10)

        # Recipe Result Text Area
        self.result_text = tk.Text(master, height=10, width=50)
        self.result_text.pack(pady=10)

    def search_recipes(self):
        keyword = self.entry.get()

        #  API endpoint
        recipes = self.query_api(keyword)
        self.display_results(recipes)

    def query_api(self, keyword):
        
        api_url = "http://localhost:8000/api/recipes"

        # Use the GET request to search for recipes
        response = requests.get(api_url, params={"name": keyword})

        if response.status_code == 200:
            return response.json()
        else:
            # Handle error
            return []

    def display_results(self, recipes):
        self.result_text.delete(1.0, tk.END)  # Clear previous results
        for recipe in recipes:
            print(recipe)  # Add this line to print the structure of each recipe
            self.result_text.insert(tk.END, f"Title: {recipe.get('title', 'N/A')}\n")
            self.result_text.insert(tk.END, f"Description: {recipe.get('description', 'N/A')}\n")
            self.result_text.insert(tk.END, f"Cooking Time: {recipe.get('cooking_time', 'N/A')} minutes\n")

        # Check if 'ingredients' is present and is a list
            ingredients = recipe.get('ingredients', [])
            if isinstance(ingredients, list):
                self.result_text.insert(tk.END, f"Ingredients:\n")
                for ingredient in ingredients:
                    name = ingredient.get('ingredient_name', 'N/A')
                    quantity = ingredient.get('quantity', 'N/A')
                    self.result_text.insert(tk.END, f"  - {name}: {quantity}\n")
            else:
                self.result_text.insert(tk.END, "Ingredients: N/A\n")

            self.result_text.insert(tk.END, "\n")



root = tk.Tk()
app = RecipeSearchApp(root)

root.mainloop()


