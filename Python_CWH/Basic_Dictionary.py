print("**** Basic Geometric Shape Definition dictionary ****")

definitions = {"Triangle": "A plane figure with three straight sides and three angles",
               "Square": "A plane figure with four equal straight sides and four right angles",
               "Rectangle": "A plane figure with four straight sides and four right angles,\n"
                            "especially one with unequal adjacent sides, in contrast to a square",
               "Circle": "A round, two-dimensional shape"}

print("Available definitions: Triangle, Square, Rectangle, Circle")
defn_required = input("Enter your choice: ")

print(definitions.get(defn_required.capitalize()))
