import xml.etree.ElementTree as ET

# Function to calculate the area of a room
def calculate_room_area(room):
    side_length_1 = int(room.find('side-length-1').text)
    side_length_2 = int(room.find('side-length-2').text)
    return side_length_1 * side_length_2

# Function to calculate the total area of the house
def calculate_total_area(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    total_area = 0
    for room in root.findall('room'):
        total_area += calculate_room_area(room)
    
    return total_area

# Main code
if __name__ == "__main__":
    xml_file = 'house.xml'
    total_area = calculate_total_area(xml_file)
    print(f"The total area of the house is: {total_area} square units")

