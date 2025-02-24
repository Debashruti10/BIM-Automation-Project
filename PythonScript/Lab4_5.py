import re
import json

def check_project_name(name):
    # Below is a regular expression string. It lists all values that are NOT (^) in the range a-z, A-Z, 0-9, -, .
    reference_pattern = r'[^a-zA-Z0-9\-.]'
    if re.search(reference_pattern, name):
        # Return True if string has anything outside pattern
        return True
    return False

def check_file_name(name):
    reference_pattern = r'^-[A-Za-z]{1,2}-\d{2,4}-[A-Za-z]-\d{7}'
    if re.match(reference_pattern, name):
        # Return False if pattern is matched
        return False
    return True

def get_file_details(name = "projectName-"):
    file_name = name.split('.')[0]
    separations = file_name.split('-')
    name_categories = {}
    if len(separations)==5:
        name_categories['project_name'] = separations[0]
        name_categories['responsible_party'] = separations[1]
        name_categories['content'] = separations[2]
        name_categories['presentation'] = separations[3]
        name_categories['building_number'] = str(separations[4])[:2]
        name_categories['level'] = str(separations[4])[2:4]
        name_categories['consecutive_number'] = str(separations[4])[4:]
    else:
        print("Invalid File name")
    return name_categories

def get_responsible_party(party_name):
    responsible_party = []
    for item in party_name:
        if item=='A' and item not in responsible_party:
            responsible_party.append('Architect')
        if item=='E' and item not in responsible_party:
            responsible_party.append('Electrical')
        if item=='V' and item not in responsible_party:
            responsible_party.append('HVAC')
        if item=='W' and item not in responsible_party:
            responsible_party.append('Plumbing')
        if item=='K' and item not in responsible_party:
            responsible_party.append('Structural')
        if item=='P' and item not in responsible_party:
            responsible_party.append('Projects Common')
    return responsible_party

def get_model_and_base_files(char):
    if len(char)==1:
        if char=='V':
            return '3D Models'
        if char=='P':
            return 'Plans'
        if char=='S':
            return 'Sections'
        if char=='F':
            return 'Facades'
        if char=='U':
            return 'Interior Elevations'
        if char=='D':
            return 'Details'
        if char=='X':
            return 'Non-Graphical Models'
        if char=='C':
            return 'Schedules'
    else:
        print("Invalid File name")
    return ''

def get_drawings_and_definitions(char):
    if len(char)==1:
        char_int = int(char)
        if char_int==0:
            return 'Composite Drawings'
        if char_int==1:
            return 'Plan Drawings'
        if char_int==2:
            return 'Sectional Drawings'
        if char_int==3:
            return 'Facade Drawings'
        if char_int==4:
            return 'Layout Drawings'
        if char_int==5:
            return 'List Drawings'
        if char_int==6:
            return 'Detail Drawings'
        if char_int==7:
            return 'Collaboration Drawings'
        if char_int==8:
            return 'Schematic Drawings'
        if char_int==9:
            return 'Text'
    else:
        print("Invalid File name")
    return ''

def print_file_data(data = {}):
    keys = list(data.keys())
    ref = ['project_name', 'responsible_party', 'content', 'presentation', 'building_number', 'level', 'consecutive_number']
    flag = True
    for i in ref:
        if i not in keys:
            flag = False
    if flag:
        
        print("Project name : ", data['project_name'])
        
        responsibles = get_responsible_party(str(data['responsible_party']))
        print("\tResponsible Party : ", str(responsibles).replace('[','').replace(']',''))

        contents = []
        for item in str(data['content']):
            value = get_drawings_and_definitions(str(item))
            if value not in contents:
                contents.append(value)
        print("\tBuilding Components : ", str(contents).replace('[','').replace(']',''))
        
        print("\tInformation Presentation style : ", get_model_and_base_files(str(data['presentation'])))

        print('\tBuilding Number : ', str(data['building_number']))
        
        print('\tLevel : ', str(data['level']))
        
        print('\tConsecutive File Number : ', str(data['consecutive_number']))
    else:
        print("Invalid File name")

def check_names(fullname):
    project_name = fullname.split('-')[0]
    remaining = ""
    for item in fullname.split('-')[1:]:
        remaining = remaining+'-'+item
    # print('Project name : ', project_name)
    # print('Remaining : ', remaining)
    if check_project_name(project_name):
        print("Invalid project name")
        return False
    if check_file_name(remaining):
        print('Invalid remaining name')
        return False
    return True

sample_name = "MIN3HUS4-A-40-V-010000000.rvt"

if(check_names(sample_name)):
    file_data = get_file_details(sample_name)
    # print("File data : ",json.dumps(file_data, indent=4))
    print_file_data(file_data)
else:
    print("Invalid full file name")