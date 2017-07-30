import json

def open_class(class_file): 
    with open(class_file, "r") as json_file:
        return json.load(json_file)

def save_class(data, class_file):
    with open(class_file, "w") as json_file:
        json.dump(data, json_file)
 
def print_class(class_data):
    for student, assignments in class_data.items():
        print "{:-^25}".format(student)
        for assignment, grade in assignments.items():
            print "{}: {}".format(assignment, grade)
        print ""
    
if __name__ == "__main__":
    test_data = {
        "mandy":
            {"a1":90, "a2":87},
        "danny":
            {"a1":60, "a2":78},
        "margaret":
            {"a1":76, "a2":96}
    }
    
    save_class(test_data, "test_data.json")
    retrieved_data = open_class("test_data.json")
    print_class(retrieved_data)
    
