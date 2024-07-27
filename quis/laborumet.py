import xml.etree.ElementTree as ET

# Example XML string
xml_data = """
<root>
    <study_first_submitted>2024-06-22</study_first_submitted>
</root>
"""

# Parse the XML
root = ET.fromstring(xml_data)

# Find the element and get its text
first_submission_date = root.find('study_first_submitted').text

print(first_submission_date)  # Output: 2024-06-22
