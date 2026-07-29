import analytics
import pandas as pd
import sys
def value_error():
    print("Please enter a valid numeric value\n")
text = input("Please enter csv filename with extension: ")
dataset = analytics.load_file(text)
cleaned_dataset = None
if dataset is not None:
    print(f"Dataset {text} is loaded sucessfully\n")
else:
    sys.exit()

while True:
    print("=== Student Performance Analytics ===\n")
    try:
        user = int(input("Please choose: \n" \
        "1. Dataset Overview\n" \
        "2. Clean the Dataset\n" \
        "3. Generate Statistics\n" \
        "4. Column wise Statistics \n" \
        "5. Sort Dataset\n" \
        "6. Searching\n" \
        "7. Value Counts\n" \
        "8. Date Time Analysis\n" \
        "9. Export File\n" \
        "10. Exit\n"))

        if user == 1:
            print("Dataset Overview\n")
            if dataset is not None:
                row,col,datatype = analytics.dataset_overview(dataset)
                print(f"Rows: {row}\nColumns: {col}\nData Type: {datatype}\n")
                duplicates = dataset.duplicated().sum()
                print(f"Total Duplicates: {duplicates}\n")
            else:
                print("No dataset loaded yet\n")
        elif user == 2:
            print("Let's Clean the clutter\n")
            if dataset is not None:
                try:
                    ask = int(input("1. Delete the Student records with none/nan values\n2. Set marks as zero for nan/none values\n3. Keep the original dataset as is\nPlease enter(1-3): "))
                    if ask == 1:
                        cleaned_dataset = dataset.dropna()
                        print("Deleted the none values\n")
                    elif ask == 2:
                        cleaned_dataset = dataset.fillna(0)
                        print("The none values are now zero\n")
                    elif ask == 3:
                        cleaned_dataset = dataset
                    else:
                        print("Please choose a valid option\n")
                except ValueError:
                    value_error()
            else:
                print("No dataset loaded yet\n")
        elif user == 3:
            print("Generating Statistics\n")
            if dataset is not None:
                if cleaned_dataset is not None:
                    stats = analytics.statistics(cleaned_dataset)
                else:
                    stats = analytics.statistics(dataset)
                print(stats)
            else:
                print("No dataset loaded yet\n")
        elif user == 4:
            print("Filter Dataset\n")
            if dataset is not None:
                column = input("Please enter the column name to filter\n")
                value = input("Please enter the value to filter\n")
                filtered_data = analytics.filter_dataset(dataset, column, value)
                print(filtered_data)
            else:
                print("No dataset loaded yet\n")
        elif user == 5:
            print("Sort Dataset\n")
            try:
                ask = int(input("Please choose: \n" \
                "1. Sort by Index\n" \
                "2. Sort by Values\n"))
            except ValueError:
                value_error()
                continue
            if dataset is not None and ask in [1, 2]:
                if ask == 1:
                    sorted_data = analytics.sort_dataset(dataset, column=None, ascending=True, what="index")
                else:
                    column = input("Please enter the column name to sort\n")
                    order = input("Please enter 'asc' for ascending or 'desc' for descending order\n")
                    ascending = True if order.lower() == 'asc' else False
                    sorted_data = analytics.sort_dataset(dataset, column, ascending)
                print(sorted_data)
            else:
                print("No dataset loaded yet\n")
        elif user == 6:
            print("Search Dataset\n")
            if dataset is not None:
                column = input("Please enter the column name to search\n")
                value = input("Please enter the value to search\n")
                searched_data = analytics.search_dataset(dataset, column, value)
                print(searched_data)
        elif user == 7:
            print("Value Counts\n")
            if dataset is not None:
                column = input("Please enter the column name to get value counts\n")
                try:
                    counts = analytics.value_counts(dataset[column])
                    print(counts)
                except KeyError:
                    print(f"Column '{column}' does not exist in the dataset.\n")
            else:
                print("No dataset loaded yet\n")
        elif user == 8:
            print("Date Time Analysis\n")
            if dataset is not None:
                column = input("Please enter the column name for datetime analysis\n")
                datetime_data = analytics.datetime_analysis(dataset, column)
                if not datetime_data.empty:
                    print(datetime_data)
            else:
                print("No dataset loaded yet\n")
        elif user == 9:
            print("Export File\n")
            if dataset is not None:
                try:
                    user2 = int(input("Please choose: \n" \
                    "1. Export Filtered Dataset\n" \
                    "2. Export Sorted Dataset\n" \
                    "3. Export Searched Dataset\n" \
                    "4. Export Original Dataset\n"))
                    if user2 == 1 and filtered_data is not None:
                        filename = input("Please enter the filename to export (with .csv extension)\n")
                        analytics.export_file(filtered_data, filename)
                    elif user2 == 2 and sorted_data is not None:
                        filename = input("Please enter the filename to export (with .csv extension)\n")
                        analytics.export_file(sorted_data, filename)
                    elif user2 == 3 and searched_data is not None:
                        filename = input("Please enter the filename to export (with .csv extension)\n")
                        analytics.export_file(searched_data, filename)
                    elif user2 == 4 and dataset is not None:
                        filename = input("Please enter the filename to export (with .csv extension)\n")
                        analytics.export_file(dataset, filename)
                    else:
                        print("Please choose a valid option and ensure the corresponding dataset is loaded.\n")
                except ValueError:
                    value_error()
                    continue
            else:
                print("No dataset loaded yet\n")
        elif user == 10:
            print("Thanks,Rooting to see you again\n")
            break
        else:
            print("Please choose a valid option\n")
    except ValueError:
        value_error()