def find_common_participants(string1, string2, separator=',') :
    common = list(set(string1.split(separator)).intersection(string2.split(separator)))
    common.sort()
    return common

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_second_group, participants_second_group, separator='|'))

