from pathlib import Path

def get_cats_info(path):
    cats_list = []
    try:
        with open(path, 'r') as file:
            for line in file:
                split1 = line.strip().split(',')
                if len(split1) >= 3:
                    cat_id = split1[0]
                    cat_name = split1[1]
                    cat_age = split1[2]
                    cats_list.append({'id' : cat_id, 'name': cat_name, 'age': cat_age})


    except Exception as e:
        print(f"{e} with file file")
    return cats_list

print(get_cats_info("C:/PyHomeWork/HomeWorks/CatNames.txt"))
