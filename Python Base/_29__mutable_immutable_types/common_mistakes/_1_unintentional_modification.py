from copy import deepcopy

# Присваивание не копирует словарь: обе переменные ссылаются на один объект.
original_dict = {"x": 1, "y": 2}
alias = original_dict
alias["x"] = 100

print(original_dict)  # {'x': 100, 'y': 2}: изменение через alias видно через original_dict
print(alias is original_dict)  # True: это один и тот же словарь

# dict.copy() создаёт поверхностную копию: новый внешний словарь,
# но вложенные изменяемые объекты остаются общими.
original_patient_data = {"heart_rate": [60, 61, 63, 60, 61]}
shallow_copy = original_patient_data.copy()

shallow_copy["heart_rate"].append(63)
print(original_patient_data)  # Список изменился и в оригинале
print(shallow_copy)  # Содержимое такое же: оба словаря ссылаются на один список
print(original_patient_data["heart_rate"] is shallow_copy["heart_rate"])  # True

# deepcopy() рекурсивно копирует вложенные объекты, поэтому списки независимы.
original_patient_data = {"heart_rate": [60, 61, 63, 60, 61]}
deep_copy = deepcopy(original_patient_data)

deep_copy["heart_rate"].append(63)
print(original_patient_data)  # Исходный список не изменился
print(deep_copy)  # Изменился только список в глубокой копии
print(original_patient_data["heart_rate"] is deep_copy["heart_rate"])  # False
