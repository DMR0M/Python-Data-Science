import numpy as np
import csv
import json
import pandas as pd
from dataclasses import dataclass, asdict


@dataclass()
class ProgLanguages:
    """Data container class to create dictionary"""
    Programming_Language: list[str]
    Year: list[int]
    Statically_Typed: list[bool]


class ManageData:
    def __init__(self, target_path: str):
        self.target_file = target_path

    def aggregation(self) -> list:
        # Initialize data aggregation storage
        string_vals = []
        number_vals = []

        boolean_lookup = ['True', 'False']
        boolean_vals = []

        with open(self.target_file, 'r') as file:
            lines = file.readlines()
            stripped_data = map(lambda l: l.strip(), lines)
            undefined_data = ''.join(stripped_data).replace(' ', '').split(',')

            # Aggregate
            for d in undefined_data:
                if not d.isnumeric() and d not in boolean_lookup:
                    string_vals.append(d)
                if d.isnumeric():
                    number_vals.append(d)
                if d.title() in boolean_lookup:
                    boolean_vals.append(d)
        return [string_vals, list(map(int, number_vals)), boolean_vals]

    def organize(self) -> list[dict]:
        list_data: list[dict] = []
        md = ManageData(self.target_file)
        values = md.aggregation()
        date_arranged = sorted(values[1])
        languages = values[0]

        year = 0
        is_static = True
        # TODO: Add Lookups for match cases
        for idx, lang in enumerate(languages):
            match lang:
                case 'Java' | 'Javascript' | 'Ruby':
                    year = date_arranged[2]
                case 'Python' | 'Rust':
                    year = date_arranged[4]
                case 'C++':
                    year = date_arranged[1]
                case 'C':
                    year = date_arranged[0]
                case 'C#':
                    year = date_arranged[3]
                case 'Go':
                    year = date_arranged[5]
                case _:
                    year = 'Unknown'
            match lang:
                case 'Python' | 'Javascript' | 'Ruby':
                    is_static = False
                case _:
                    is_static = True
            data_ = {
                'Programming Language': lang,
                'Year Created': year,
                'Statically Typed': is_static
            }
            list_data.append(data_)
        return list_data


class CreateData:
    def __init__(self, data_object, *,
                 save_path_csv: str = '../csv_files/prog_languages.csv',
                 save_path_json: str = '../json_files/prog_languages.json'):
        self.data = data_object
        self.save_path_csv = save_path_csv
        self.save_path_json = save_path_json
        self.data_frame = pd.DataFrame(self.data)
        self.res_path = 'unstructured_data/res.txt'

        md = ManageData(self.res_path)
        self.structured_data = md.organize()

    def save_as_csv(self) -> None:
        self.data_frame.to_csv(self.save_path_csv)

    def save_as_json(self) -> None:
        json_str = json.dumps(self.structured_data, indent=4)
        with open(self.save_path_json, 'w') as json_f:
            json_f.write(json_str)

    def json_to_csv(self) -> None:
        self.data_frame = pd.DataFrame(self.structured_data)
        self.data_frame.to_csv(self.save_path_csv)


def main():
    a = ['Java', 'Python', 'C']
    b = [1995, 2008, 1972]
    c = [True, False, True]
    csv_path_ = '../csv_files/prog_languages.csv'
    json_path_ = '../json_files/prog_languages.json'

    # Instantiate from data container
    data_dclass = ProgLanguages(a, b, c)
    data_dict = asdict(data_dclass)

    d = CreateData(data_dict, json_path_)
    # d.save_as_csv(csv_path_)
    d.save_as_json()


if __name__ == '__main__':
    main()
