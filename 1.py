file_name = "test_sort/market_data_2018/2018-01-01/BANKNIFTY04JAN1825700PE_2018-01-01.csv"

# Extracting the required portion using string manipulation
file_name_parts = file_name.split('/')
file_name_without_extension = file_name_parts[-1].split('.')[0]
data_parts = file_name_without_extension.split('_')

# Extracting instrument name (BANKNIFTY04JAN1825700PE)
instrument_name = data_parts[0]

# Adding spaces after 9th, 7th, and 5th characters
instrument_name_with_spaces = (
    instrument_name[:9]
    + ' '
    + instrument_name[9:16]
    + ' '
    + instrument_name[16:21]
    + ' '
    + instrument_name[21:]
)

# Print intermediate result for debugging
print("instrument_name_with_spaces:", instrument_name_with_spaces)
