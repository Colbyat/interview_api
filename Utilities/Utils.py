import pandas


def verticaljsontopandasdf(json):
    return pandas.DataFrame(json[1:], columns=json[0])

verticaljsontopandasdf.__doc__ = """Takes a given json in the format of: [[column_labels], [row_1], [row_2],...[row_n]]
                                     and outputs a pandas dataframe with the given data."""