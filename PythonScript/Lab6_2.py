import xml.etree.ElementTree as ET
import os

class Construction_Entity:
    def __init__(self, xml_file):
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # Extract values from XML file
        self.id = root.attrib['id']
        self.CoClassCode = root.find('CoClassCode').text
        self.PropertyName = root.find('PropertyName').text
        self.SpaceArea = float(root.find('SpaceArea').text)
        self.CostAssessment = float(root.find('CostAssessment').text)
        self.EnergyConsumption = float(root.find('EnergyConsumption').text)
        self.CarbonDioxideEquivalency = float(root.find('CarbonDioxideEquivalency').text)

    def get_LCC(self, r, n):
        # Calculate the value factor
        value_factor = (1 - (1 + r) ** -n) / r

        # Calculate LCC based on provided formula
        d = 0.1 * self.CostAssessment
        ic = self.CostAssessment
        kWh = self.EnergyConsumption
        e = 1 * kWh
        o = 250 * self.SpaceArea
        m = 100 * self.SpaceArea
        s = 0  # You may want to adjust this if downtime costs are provided elsewhere
        env = self.CarbonDioxideEquivalency * 0.72

        # LCC calculation
        LCC = (ic + e + o + m + s + env + d) + value_factor
        return LCC

def calculate_average_LCC(co_class_code, folder_path, r, n):
    # Collect all objects with the given CoClassCode
    total_LCC = 0
    count = 0

    # Go through all XML files in the folder
    for xml_file in os.listdir(folder_path):
        if xml_file.endswith('.xml'):
            full_path = os.path.join(folder_path, xml_file)
            entity = Construction_Entity(full_path)

            if entity.CoClassCode == co_class_code:
                total_LCC += entity.get_LCC(r, n)
                count += 1

    # Calculate the average LCC per space area
    if count > 0:
        average_LCC_per_area = total_LCC / count
        print(f"The average LCC/SpaceArea for CoClassCode {co_class_code} is: {average_LCC_per_area}")
    else:
        print(f"No entities found with CoClassCode {co_class_code}.")

# Main program
def main():
    # Ask the user for the folder path
    folder_path = input("Enter the folder path containing the XML files: ")
    
    # Validate folder path
    if not os.path.isdir(folder_path):
        print("Invalid folder path. Please ensure the path exists.")
        return

    # Ask for other inputs
    r = float(input("Enter the net discount rate: "))
    n = float(input("Enter the number of years: "))
    co_class_code = input("Enter the CoClassCode to filter by: ")

    # Calculate and print the average LCC per space area
    calculate_average_LCC(co_class_code, folder_path, r, n)

if __name__ == "__main__":
    main()