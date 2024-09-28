from operator import itemgetter





def read_file(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            columns = file.readline().replace("\n", " ").replace(",", "").split()
            return columns, file.read().replace("\n", " ").replace(",", "").split()
    except IOError:
        print("File not found: " + file_name)

def handle_data(data, columns):
    list_of_dicts = []
    try:
        for iteration in range(int(len(data)/len(columns))):
            temp_dict = {}
            for y in range(len(columns)):
                temp_dict[columns[y]] = data[iteration*len(columns) + y]
            list_of_dicts.append(temp_dict)
        print("Information was handled")
    except Exception as e:
        print(e)
    return list_of_dicts, columns[-1]


def get_params_to_sort():
    print("Enter the type of data to sort: ")
    print("1 - String")
    print("2 - Numeric")
    print("3 - Exit")
    datatype = int(input())
    if datatype == 1:
        datatype = True
    elif datatype == 2:
        datatype = False
    elif datatype == 3:
        return
    else:
        print("Invalid input")
        get_params_to_sort()
    print("Pick the order of the data")
    print("1 - Ascending")
    print("2 - Descending")
    print("3 - Exit")
    order = int(input())
    if order == 1:
        order = True
    elif order == 2:
        order = False
    elif order == 3:
        return
    else:
        print("Invalid input")
        get_params_to_sort()
    return datatype, order



def sort(data,list_columns,datatype,order):
    try:
        possible_to_sort = []
        numbers_possible_to_sort = []
        for line in data:
            for key, value in line.items():
                if datatype:
                    if not value.isnumeric():
                        possible_to_sort.append(key)
                else:
                    if not value.isnumeric():
                        possible_to_sort.append(key)
        for x in list_columns:
            if x in possible_to_sort:
                numbers_possible_to_sort.append(list_columns.index(x))
        for x in numbers_possible_to_sort:
            print(f"{x} - {possible_to_sort[x]}")

        s = input("Enter a column name: ")
        if s not in possible_to_sort:
            print("Invalid column name")
            return None
        list_for_bubble = sorted(data, key=itemgetter(s), reverse=order)
        return list_for_bubble
    except Exception as e:
        print(e)

def filter_by_columns(data, columns, last):
    for x in range(len(columns)):
        print(f"{x} - {columns[x]}")
    print("Enter -1 to exit: ")
    print("Enter any number to write filtered file: ")
    num = int(input())
    if 0<=num<len(columns):
        columns.remove(columns[int(num)])
        filter_by_columns(data, columns, last)
    elif num == -1:
        return
    else:
        try:
            file_name = input("Enter file name: ")
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(', '.join(columns) + '\n')
                for line in data:
                    for key, value in line.items():
                        if key in columns:
                            file.write(value + ", ") if key != last else file.write(value)
                    file.write("\n")
                file.close()
            print("File saved")
        except IOError:
            print("File not found: " + file_name)


def finder(data):
    print("Input what you want to find: ")
    input_data = input()
    found = False
    for line in data:
        for key, value in line.items():
            if input_data in str(value):
                print(f"Found: Line: {data.index(line) + 1}, Column: {(list(line.keys()).index(key))+1}")
                found = True
    if not found:
        print(f"No {input_data} found")


def write_file(file_name,data, last, columns):
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(', '.join(columns) + '\n')
            for line in data:
                for key, value in line.items():
                    file.write(value + ", ") if key != last else file.write(value)
                file.write("\n")
            file.close()
        print("File saved")
    except IOError:
        print("File not found: " + file_name)


def menu(file, handled_data, columns, last):
    print("What u want to do next?")
    print("1 - Filter by columns")
    print("2 - Sort by columns")
    print("3 - Find samples")
    print("4 - Exit")
    num = int(input())
    if num == 1:
        filter_by_columns(handled_data, columns, last)
        menu(file, handled_data, columns, last)
    elif num == 2:
        datatype, order = get_params_to_sort()
        handled_data = sort(handled_data, columns, datatype, order)
        menu(file, handled_data, columns, last)
    elif num == 3:
        finder(handled_data)
        menu(file, handled_data, columns, last)
    elif num == 4:
        print("Thank you for using Sorter!")
        write_file(f"new_{file}", handled_data, last, columns)
        return
    else:
        print("Invalid input")
        menu(file, handled_data, columns, last)


def main():
    print("Welcome to Sorter!")
    file = input("Enter file name to start work with: ")
    columns, first_data = read_file(file)
    handled_data, last = handle_data(first_data, columns)
    menu(file, handled_data, columns, last)

if __name__ == "__main__":
    main()