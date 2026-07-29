import pandas as pd

def load_file(text):
    try:
        file = pd.read_csv(text)
        return file
    except FileNotFoundError:
        print(f"The file {text} doesn't exist\n")
        return
    except pd.errors.EmptyDataError:
        print("The file is empty\n")
        return

def dataset_overview(dataset):
    return dataset.shape[0],dataset.shape[1],dataset.dtypes

def statistics(dataset):
    return dataset.describe()

def column_wise_stats(dataset):
    pass
def sort(dataset,columns,ascending=True,what="values"):
    pass

def filter(dataset,columns):
    pass
def overall(dataset):
    pass

def group_and_summarize(dataset,col1,col2):
    pass


def export(dataset,txt):
    try:
        dataset.to_csv(txt)
        print(f"File exported successfully as {txt}\n")
    except FileExistsError:
        print(f"File with {txt} already exists Try another name\n")