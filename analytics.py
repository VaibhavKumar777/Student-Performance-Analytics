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
    except pd.errors.ParserError:
        print("The file is not a valid CSV\n")
        return

def dataset_overview(dataset):
    return dataset.shape[0],dataset.shape[1],dataset.dtypes

def statistics(dataset):
    return dataset.describe()
def subject_wise_stats(dataset,subject):
    if subject not in dataset.columns:
        print(f"The subject {subject} doesn't exist\n")
        return
    return dataset[subject].describe()
def column_wise_stats(dataset,column):
    if column not in dataset.columns:
        print(f"The column {column} doesn't exist\n")
        return
    return dataset[column].describe()

def sort_dataset(dataset,columns,ascending=True,what="values"):
    if what == "values":
        return dataset.sort_values(by=columns,ascending=ascending)
    elif what == "index": 
        return dataset.sort_index(ascending=ascending)

def filter(dataset,column,value):
    if column not in dataset.columns:
        print(f"The column {column} doesn't exist\n")
        return
    return dataset[dataset[column] == value]
    
def overall(dataset):
    return dataset.mean(numeric_only=True), dataset.sum(numeric_only=True), dataset.median(numeric_only=True)
def performers(dataset,subject,threshold):
    if subject not in dataset.columns:
        print(f"The subject {subject} doesn't exist\n")
        return 
    highest = dataset[subject].max()
    highest_students = dataset[dataset[subject] == highest]
    lowest = dataset[subject].min()
    lowest_students = dataset[dataset[subject] == lowest]
    above_avg = dataset[dataset[subject] >= threshold]
    below_avg = dataset[dataset[subject] < threshold]
    return highest_students,lowest_students,above_avg,below_avg
def group_and_summarize(dataset,col1,col2):
    if col1 not in dataset.columns:
        print(f"The column {col1} doesn't exist\n")
        return
    if col2 not in dataset.columns:
        print(f"The column {col2} doesn't exist\n")
        return
    grouped = dataset.groupby([col1,col2])
    return grouped.describe()
def export_file(dataset,txt):
    try:
        dataset.to_csv(txt)
        print(f"File exported successfully as {txt}\n")
    except FileExistsError:
        print(f"File with {txt} already exists Try another name\n")