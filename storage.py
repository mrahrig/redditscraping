import tsdb


def save_data(data, dataset_name):
    tsdb.pickle_dump(data, f"{dataset_name}.pkl")


def load_data(dataset_name):
    return tsdb.pickle_load(f"{dataset_name}.pkl")
