import json
import xml.etree.ElementTree as ET
from pathlib import Path

class JSONDataExtractor:
    def __init__(self, filePath: Path):
        self.data = {}
        with open(filePath, 'r') as file:
            self.data = json.load(file)

    @property
    def parsed_data(self):
        return self.data
    
class XMLDataExtractor:
    def __init__(self, filePath: Path):
        self.tree = ET.parse(filePath)
    
    @property
    def parsed_data(self):
        return self.tree
    
# Factory function
def extract_factory(filePath: Path):
    ext = filePath.name.split(".")[-1]
    
    if ext == "json":
        return JSONDataExtractor(filePath)
    elif ext == "xml":
        return XMLDataExtractor(filePath)

def extract(case: str):
    dir_path = Path(__file__).parent

    if case == "json":
        path = dir_path / Path("movies.json")
        factory = extract_factory(path)
        data = factory.parsed_data

        for movie in data:
            print(f"Title: {movie["title"]}")
            print(f"Director: {movie["director"]}")
            print("___\n")
    elif case == "xml":
        path = dir_path / Path("person.xml")
        factory = extract_factory(path)
        data = factory.parsed_data

        search_xpath = ".//person[lastName='Liar']"
        items = data.findall(search_xpath)
        for item in items:
            first = item.find("firstName").text
            last = item.find("lastName").text
            print(f"{first} {last}")


if __name__ == "__main__":
    print("JSON Parser")
    extract(case="json")

    print("XML Parser")
    extract(case="xml")
