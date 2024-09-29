from pathlib import Path


def total_salary(path):
    salary_list = list()
    try:
        with open(path, 'r') as file:
            for line in file:
                salary = line.split(',')[1]
                salary_list.append(int(salary))

        if len(salary_list) == 0:
            print('err: file us empty')
            return None, None

        total = sum(salary_list)
        avarage = total / len(salary_list)
        return total, avarage
    except Exception as e:
        print(f"{e} with file file")



total, average = total_salary("C:/PyHomeWork/HomeWorks/path.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
