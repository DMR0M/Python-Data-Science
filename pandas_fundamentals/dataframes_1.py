import numpy as np
import pandas as pd


def create_dataframe(x: int, y: int):
    np.random.seed(100)
    arr = np.random.randint(0, 100, (x, y))
    return arr


def programming_languages_df(key_lst: list, prog_langs: list,
                             year: list, is_static: list):
    try:
        # Initialize value lists into 1 2D list
        vals_list = np.array([prog_langs, year, is_static])

        # Create dynamic dictionary based on the keys parameters
        # and values parameters
        data_dict = {key: vals_list[idx] for idx, key in enumerate(key_lst)}

        # Define row length
        rows_length = len(list(data_dict['Prog Langs']))

        # Create list of row indices
        row_indices = [f'Prog Lang {n}' for n in range(1, rows_length+1)]

        # Create and return the dataframe
        df = pd.DataFrame(data_dict, index=row_indices)
        return df

    except ValueError:
        # Raise exception if the value lists does not match each of their sizes
        return 'The list sizes does not match'


def main():
    a = ['Java', 'Python', 'C#', 'Go', 'Javascript', 'Rust', 'C++']
    b = [1995, 2008, 2000, 2012, 1995, 2008, 1986]
    c = [True, False, True, True, False, True, True]
    data_keys = ['Prog Langs', 'Year', 'Static Typing']
    print(programming_languages_df(data_keys, a, b, c))

    # row_names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    # col_names = ['Jan', 'Feb', 'Mar']
    #
    # dict_sample = {
    #     'Prog Langs': ['Java', 'Python', 'C#', 'Go', 'Javascript'],
    #     'Year': [1995, 2008, 2000, 2012, 1995],
    #     'Static Typing': [True, False, True, True, False]
    # }
    #
    # # Determine length of row indices
    # row_size = len(list(dict_sample['Prog Langs']))+1
    #
    # # Create a list of row indices
    # prog_lang_idx = [f'Prog Lang {n}' for n in range(1, row_size)]
    #
    # # Print and assign dataframe
    # print(data := pd.DataFrame(dict_sample, index=prog_lang_idx))

    # Converting Numpy Matrix to Dataframe
    # You can pass in index as row names and columns as column names
    # df = pd.DataFrame(n_arr := create_dataframe(5, 3), index=row_names, columns=col_names)
    # print(df)
    # print(type(df))


if __name__ == '__main__':
    main()
