def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    
    return file_content

def get_num_words(book_content):
    return len(book_content.split())

def count_letters(book_content):
    lower_book_content = book_content.lower()
    instance_count = {}

    for char in lower_book_content:
        if char in instance_count:
            instance_count[char] += 1
        else:
            instance_count[char] = 1
    
    return instance_count

def sort_by(list):
    return list["num"]

def sort_on(instance_count):
    sorted_list = []

    for key, value in instance_count.items():
        new_dict = {"char": key, "num": value}
        sorted_list.append(new_dict)
    
   
    sorted_list.sort(reverse=True, key=sort_by)
    return sorted_list



    