import os

def check_file_name(file_name):
    parts = file_name.split('-')
    
    if len(parts) != 7:
        return False

    project_name = parts[0]
    responsible_party = parts[1]
    content = parts[2]
    presentation = parts[3]
    building_number = parts[4]
    level = parts[5]
    consecutive_and_format = parts[6].split('.')

    if len(consecutive_and_format) != 2:
        return False
    consecutive_number, file_format = consecutive_and_format

    if project_name.startswith("BIM") and project_name[3:].isalnum():
        pass
    else:
        return False

    if len(responsible_party) == 2 and responsible_party[0] in "AEVWKPC" and responsible_party[1].isdigit():
        pass
    else:
        return False

  
    if content.isdigit():
        pass
    else:
        return False
   
    if presentation in "VPSFUDEXC0123456789":
        pass
    else:
        return False

    if len(building_number) == 2 and building_number.isdigit():
        pass
    else:
        return False

    if len(level) == 2 and level.isdigit():
        pass
    else:
        return False

    if not consecutive_number.isdigit():
        return False

    if file_format != "rvt":
        return False

    return True

def check_files_in_directory(directory_path):
    for file_name in os.listdir(directory_path):
        if check_file_name(file_name):
            print(str(file_name) + ":" + "VALID" + ".")
        else:
            print(str(file_name)+ ":" + "INVALID"+ ".")

directory_path = "G:\\Python\\python"
check_files_in_directory(directory_path)
