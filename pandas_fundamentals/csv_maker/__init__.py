from prog_langs import ProgLanguages, ManageData, CreateData

# Unstructured data file resource path
res_path_ = 'unstructured_data/res.txt'

# Path to save csv file or json file
csv_path_ = '../csv_files/prog_languages_2.csv'
json_path_ = '../json_files/prog_languages.json'

# Instantiate from resource path to organize data
md = ManageData(res_path_)
data_dict = md.organize()

# Instantiate from CreateData class with organized data variable as an instance attribute
d = CreateData(data_dict, save_path_csv=csv_path_, save_path_json=json_path_)
d.save_as_csv()
d.save_as_json()
d.json_to_csv()
