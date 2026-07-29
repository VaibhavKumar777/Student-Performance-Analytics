import analytics
import pandas as pd
import sys
def value_error():
    print("Please enter a valid numeric value\n")
text = input("Please enter csv filename with extension: ")
dataset = analytics.load_file(text)
cleaned_dataset = None
filtered_data = None
sorted_data= None
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
        "5. Filter Students\n" \
        "6. Sort Students\n" \
        "7. Subject Wise Statistics\n" \
        "8. Overall Statistics\n" \
        "9. Group and Summarize\n" \
        "10. Performers\n" \
        "11. Export File\n" \
        "12. Exit\n"))

        if user == 1:
            print("Dataset Overview\n")
            if dataset is not None:
                if cleaned_dataset is not None:
                    row,col,datatype = analytics.dataset_overview(cleaned_dataset)
                    print(f"Rows: {row}\nColumns: {col}\nData Type: {datatype}\n")
                    duplicates = cleaned_dataset.duplicated().sum()
                    print(f"Total Duplicates: {duplicates}\n")
                else:
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
            print("Column wise Statistics\n")
            if dataset is not None:
                column = input("Please enter the column name to get statistics\n")
                stats = analytics.column_wise_stats(dataset, column)
                print(stats)
            else:
                print("No dataset loaded yet\n")
        elif user == 5:
            print("Filter Students\n")
            if dataset is not None:
                column = input("Please enter the column name to filter\n")
                value = input("Please enter the value to filter\n")
                filtered_data = analytics.filter(dataset, column, value)
                print(filtered_data)
            else:
                print("No dataset loaded yet\n")
        elif user == 6:
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
                    sorted_data = analytics.sort_dataset(dataset, columns=None, ascending=True, what="index")
                else:
                    column = input("Please enter the column name to sort\n")
                    order = input("Please enter 'asc' for ascending or 'desc' for descending order\n")
                    ascending = True if order.lower() == 'asc' else False
                    sorted_data = analytics.sort_dataset(dataset, column, ascending)
                print(sorted_data)
            else:
                print("No dataset loaded yet\n")
        elif user == 7:
            print("Subject Wise Statistics\n")
            if dataset is not None:
                subject = input("Please enter the subject name to get statistics\n")
                stats = analytics.subject_wise_stats(dataset, subject)
                print(stats)
        elif user == 8:
            print("Overall Statistics\n")
            if dataset is not None:
                if cleaned_dataset is not None:
                    overall_stats = analytics.overall(cleaned_dataset)
                else:
                    overall_stats = analytics.overall(dataset)
                print(overall_stats)
            else:
                print("No dataset loaded yet\n")
        elif user == 9:
            print("Group and Summarize\n")
            if dataset is not None:
                if cleaned_dataset is not None:
                    col1 = input("Please enter the first column name to group by\n")
                    col2 = input("Please enter the second column name to summarize\n")
                    grouped_data = analytics.group_and_summarize(cleaned_dataset, col1, col2)
                    print(grouped_data)
                else:
                    col1 = input("Please enter the first column name to group by\n")
                    col2 = input("Please enter the second column name to summarize\n")
                    grouped_data = analytics.group_and_summarize(dataset, col1, col2)
                    print(grouped_data)
            else:
                print("No dataset loaded yet\n")
        elif user == 10:
            print("Performers\n")
            if dataset is not None:
                subject = input("Please enter the subject name to analyze performers\n")
                try:
                    threshold = float(input("Please enter the threshold marks to categorize performers\n"))
                except ValueError:
                    value_error()
                    continue
                if cleaned_dataset is not None:
                    performance = analytics.performers(cleaned_dataset,subject, threshold)
                    if performance is not None:
                        highest,lowest,above_avg,below_avg = performance
                        print(f"Highest Marks: {highest}\nLowest Marks: {lowest}\nAbove Average: {above_avg}\nBelow Average: {below_avg}\n")
                else:
                    performance = analytics.performers(dataset,subject, threshold)
                    if performance is not None:
                        highest,lowest,above_avg,below_avg = performance
                        print(f"Highest Marks: {highest}\nLowest Marks: {lowest}\nAbove Average: {above_avg}\nBelow Average: {below_avg}\n")
            else:
                print("No dataset loaded yet\n")
        elif user == 11:
            print("Export File\n")
            if dataset is not None:
                try:
                    user2 = int(input("Please choose: \n" \
                    "1. Export Filtered Dataset\n" \
                    "2. Export Sorted Dataset\n" \
                    "3. Cleaned Dataset\n"))
                    if user2 == 1 and filtered_data is not None:
                        filename = input("Please enter the filename to export (with .csv extension)\n")
                        analytics.export_file(filtered_data, filename)
                    elif user2 == 2 and sorted_data is not None:
                        filename = input("Please enter the filename to export (with .csv extension)\n")
                        analytics.export_file(sorted_data, filename)
                    elif user2 == 3 and cleaned_dataset is not None:
                        filename = input("Please enter the filename to export (with .csv extension)\n")
                        analytics.export_file(cleaned_dataset, filename)
                    else:
                        print("Please choose a valid option and ensure the corresponding dataset is loaded.\n")
                except ValueError:
                    value_error()
                    continue
            else:
                print("No dataset loaded yet\n")
        elif user == 12:
            print("Thanks,Rooting to see you again\n")
            break
        else:
            print("Please choose a valid option\n")
    except ValueError:
        value_error()