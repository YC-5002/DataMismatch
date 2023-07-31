# If you encounter a ModuleNotFoundError, do this in the terminal: pip install pandas 
import pandas as pd

def compareCol(sheet1, sheet2):
    print("\nHere are the columns in the sheet - " + sheet1_name + ": ")
    sheet1_cols = sheet1.columns.values
    for number in range(len(sheet1_cols)):
        print(str(number) + ": " + sheet1_cols[number])
    selected_sheet1_col = int(input("\nColumn number from " + sheet1_name + " to compare: "))
    if selected_sheet1_col in range(len(sheet1_cols)): 
        print("\nHere are the columns in the sheet - " + sheet2_name + ": ")
        sheet2_cols = sheet2.columns.values
        for number in range(len(sheet2_cols)):
            print(str(number) + ": " + sheet2_cols[number])
        selected_sheet2_col = int(input("\nColumn number from " + sheet2_name + " to compare: "))
        
        if selected_sheet2_col in range(len(sheet2_cols)):
            sheet1_column_used = [str(each_row) for each_row in sheet1[sheet1_cols[selected_sheet1_col]]]
            sheet2_column_used = [str(each_row) for each_row in sheet2[sheet2_cols[selected_sheet2_col]]]
            diff_index = []
            for num in range(len(sheet1_column_used)):
                if sheet1_column_used[num] != sheet2_column_used[num]:
                    diff_index.append(num + 2)
            print("\n" + sheet1_name + "'s Column: " + sheet1_cols[selected_sheet1_col])
            print(sheet2_name + "'s Column: " + sheet2_cols[selected_sheet2_col])
            print("Columns Matching?: " + str(len(diff_index)==0))
            print("\nThese are the rows that are different: \n" + str(diff_index))
                
            
        else:
            print("You did not enter a valid column number in the sheet - " + sheet2_name + ".")
    else:
        print("You did not enter a valid column number in the sheet - " + sheet1_name + ".")
        
    return

def compareSheet(sheet1, sheet2):
    sheet1_cols = sheet1.columns.values
    sheet2_cols = sheet2.columns.values
    if len(sheet1_cols) != len(sheet2_cols):
        print("\nData Match?: " + str(False))
        print("The sheets do not have the same number of columns.")
        return
    
    columns_with_diff = []
    for num in range(len(sheet1_cols)):
        current_col_val1 = [str(each_row) for each_row in sheet1[sheet1_cols[num]]]
        current_col_val2 = [str(each_row) for each_row in sheet2[sheet2_cols[num]]]
        if current_col_val1 != current_col_val2:
            columns_with_diff.append(num + 1)
    print("\nData Match?: " + str(len(columns_with_diff) == 0))
    print("Columns Not Same: " + str(columns_with_diff))

    return

# main
path = input("The path to the Excel file: ")
sheet1_name = input("Name of Sheet 1: ")
try:
    sheet1 = pd.read_excel(path, sheet_name=sheet1_name)
    sheet2_name = input("Name of Sheet 2: ")
    sheet2 = pd.read_excel(path, sheet_name=sheet2_name)
    function_to_perform = int(input("\nDo you want to... \n(1) Compare Columns \n(2) Compare Sheets \nEnter Corresponding Number: "))
    if function_to_perform == 1:
        compareCol(sheet1, sheet2)
    elif function_to_perform == 2:
        compareSheet(sheet1, sheet2)
    else:
        print("The input was not valid")

except FileNotFoundError:
        print("The sheet can not be found")
        exit()