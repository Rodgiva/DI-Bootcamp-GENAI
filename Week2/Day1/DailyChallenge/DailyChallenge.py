class Farm():
    def __init__(self, farm_name, animals = None):
        self.farm_name = farm_name
        self.animals = {} if animals == None else dict(animals)

    def add_animal(self, **kwargs):
        for animal_type, count in kwargs.items():
            if animal_type in self.animals:
                self.animals[animal_type] += count
            else:
                self.animals[animal_type] = count
        return self

    def get_info(self)->str:
        info = f"{self.farm_name}'s farm\n\n"
        for k,v in self.animals.items():
            info += f"{k}: {v}\n"
        info += "\nE-I-E-I-0!"
        return info

    def get_animal_types(self)->list:
        sorted_animals = list(self.animals.keys())
        sorted_animals.sort()
        return sorted_animals

    def get_short_info(self)->str:
        animals_list = self.get_animal_types()
        for i in range(len(animals_list)):
            if self.animals[animals_list[i]] > 1:
                animals_list[i] += "s"
        animals_str = ", ".join(animals_list)
        short_info = f"{self.farm_name}'s farm has {animals_str}"
        return short_info

macdonald = Farm("McDonald")
add = {
    "cow":5,
    "sheep":1,
    "sheep":1,
    "goat":12
}
macdonald.add_animal(**add)
print(macdonald.get_info())

print(macdonald.get_animal_types())
print(macdonald.get_short_info())