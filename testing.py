import pandas as pd


def load_election_data(file_path):
    """Load election data from a CSV file."""
    return pd.read_csv(file_path)


def aggregate_votes(data):
    """Aggregate votes by party across all polling stations."""
    return data.groupby('parti').sum().drop(columns='krets').rename(columns={'stemmer': 'votes'})


def lesValg(year, file_path, existing_ledger=None):
    """
    Given a year and the file with validated data from that year, returns the election ledger.
    Can build upon an existing election ledger when it is provided.

    Args:
    year (int): The election year.
    file_path (str): The path to the CSV file containing the election data.
    existing_ledger (dict, optional): The existing election ledger to update.

    Returns:
    dict: Updated or new election ledger.
    """
    # Load the election data from the specified file
    data = pd.read_csv(file_path)

    # Aggregate the votes by party
    aggregated_data = data.groupby('parti').sum().drop(columns='krets').rename(columns={'stemmer': 'votes'})

    # Convert aggregated data to dictionary
    year_data = aggregated_data.to_dict('index')

    # If an existing ledger is provided, update it
    if existing_ledger is not None:
        existing_ledger[year] = year_data
        return existing_ledger

    # If no existing ledger is provided, create a new ledger
    else:
        return {year: year_data}


# Example usage of the function to load and process data
file_path_2013 = '/mnt/data/stemmer2013.txt'
file_path_2017 = '/mnt/data/stemmer2017.txt'
file_path_2021 = '/mnt/data/stemmer2021.txt'

data_2013 = load_election_data(file_path_2013)
data_2017 = load_election_data(file_path_2017)
data_2021 = load_election_data(file_path_2021)

aggregated_data_2013 = aggregate_votes(data_2013)
aggregated_data_2017 = aggregate_votes(data_2017)
aggregated_data_2021 = aggregate_votes(data_2021)

election_ledger = {
    2013: aggregated_data_2013.to_dict('index'),
    2017: aggregated_data_2017.to_dict('index'),
    2021: aggregated_data_2021.to_dict('index')
}

# Using the function to create an example ledger
example_ledger = lesValg(2013, file_path_2013)
print(example_ledger)
