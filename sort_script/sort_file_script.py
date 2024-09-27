from operator import itemgetter

def main():
    first_data = read_file("sort_file_script.txt")
    handled_data, last = handle_data(first_data,2)
    handled_data = sort_numbers(handled_data)
    finder(handled_data)
    write_file("sort_file_script_new.txt", handled_data, last)

def read_file(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            return file.read().replace("\n", " ").replace(",", "").split()
    except IOError:
        print("File not found: " + file_name)

def handle_data(data, n):
    names_of_parameters = []
    list_of_dicts = []
    try:
        for p in range(n):
            parameter = input("Enter a parameter: ")
            names_of_parameters.append(parameter)
        for iteration in range(int(len(data)/n)):
            temp_dict = {}
            for y in range(n):
                temp_dict[names_of_parameters[y]] = data[iteration*n + y]
            list_of_dicts.append(temp_dict)
        print("Information was handled")
    except Exception as e:
        print(e)
    return list_of_dicts, names_of_parameters[-1]


def sort_by_letters(data):
    try:
        def casting():
            s = input("Enter a column to sort: ")
            print("1 - Ascending")
            print("2 - Descending")
            print("3 - Exit")
            b = True
            if s == 1:
                b = False
            elif s == 2:
                b = True
            elif s == 3:
                return
            else:
                casting()
            return s, b
        column, reversing = casting()
        list_for_bubble = sorted(data, key=itemgetter(column),reverse=reversing)
        return list_for_bubble
    except Exception as e:
        print(e)



def sort_numbers(data):
    try:
        s = input("Enter a column name: ")
        list_for_bubble = sorted(data, key=itemgetter(s), reverse=True)
        return list_for_bubble
    except Exception as e:
        print(e)



def finder(data):
    print("Input what you want to find: ")
    input_data = input()
    found = False
    for line in data:
        for key, value in line.items():
            if input_data in str(value):
                print(f"Found in line: {data.index(line) + 1}")
                found = True
    if not found:
        print(f"No {input_data} found")


def write_file(file_name,data, last):
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            for line in data:
                for key, value in line.items():
                    file.write(value + ", ") if key != last else file.write(value)
                file.write("\n")
        file.close()
        print("File saved")
    except IOError:
        print("File not found: " + file_name)




if __name__ == "__main__":
    main()