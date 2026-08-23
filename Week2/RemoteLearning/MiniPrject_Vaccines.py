from hashids import Hashids

class Human():
    _blood_type_list = ["A", "B", "AB", "O"]
    _human_count = 0

    def __init__(self, name:str, age:int, priority:bool, blood_type:int):
        Human._human_count += 1
        hashids = Hashids(salt="my_secret_salt", min_length=8)
        my_int = Human._human_count

        self.id_number:str = hashids.encode(my_int)
        self.name = name
        self.age = age
        self.priority = priority
        if 0 <= blood_type <= 3:
            self.blood_type = Human._blood_type_list[blood_type]
        else:
            raise ValueError


class Queue():
    def __init__(self, humans = None):
        self.humans = [] if humans == None else list(humans)

    def add_person(self, person:Human):
        if person.age >= 60 or person.priority:
            self.humans = [person] + self.humans 
        else:
            self.humans.append(person)

    def _find_index(self, person:Human)->int:
        for i in range(len(self.humans)):
            if self.humans[i] == person:
                return i

    def find_in_queue(self, person:Human)->int:
        return Queue._find_index(self, person)

    def swap(self, person1:Human, person2:Human):
        index1 = self.find_in_queue(person1)
        index2 = self.find_in_queue(person2)
        self.humans[index1], self.humans[index2] = self.humans[index2], self.humans[index1]

    def get_next(self)->Human:
        a_humain = self.humans[0]
        if a_humain:
            # self.humans.pop(0)
            self.humans = self.humans[1:]
            return a_humain
        else:
            return None

    def get_next_blood_type(self, blood_type:str)->Human:
        a_human = list(filter(lambda h : h.blood_type == blood_type, self.humans))[0]
        if a_human:
            index = Queue._find_index(self, a_human)
            self.humans = self.humans[0:index] + self.humans[index:]
            return list(filter(lambda h : h.blood_type == blood_type, self.humans))[0]
        else:
            return None

    def sort_by_age(self):
        priority_humans = list(filter(lambda h: h.priority, self.humans))
        older_humans = list(filter(lambda h: h.age >= 60, self.humans))
        other_humans = list(filter(lambda h: h.age < 60 and h.priority == False, self.humans))

        self.humans = priority_humans + older_humans + other_humans

human_list = [
    Human("Bob", 66, False, 0),
    Human("Henri", 32, True, 1),
    Human("Caroline", 28, False, 2),
    Human("Charlie", 45, False, 3),
    Human("Robert", 62, False, 2),
    Human("Bernad", 65, True, 1),
    Human("Roger", 58, True, 0),
    Human("Momo", 12, False, 2),
    Human("Albert", 20, False, 1),
]

a_queue = Queue()

for human in human_list:
    a_queue.add_person(human)
    
for human in human_list:
    print(a_queue.find_in_queue(human))

for h in a_queue.humans:
    print(f"{h.name} - {h.age} - {h.priority}")

a_queue.swap(human_list[2], human_list[4])
a_queue.get_next()
a_queue.get_next_blood_type("A")
# a_queue.sort_by_age()
# print("*****")
# for h in a_queue.humans:
#     print(f"{h.name} - {h.age} - {h.priority}")