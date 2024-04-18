def extract_hex(input_file, output_file):
    # Open the input file in read mode
    with open(input_file, 'r') as f:
        # Read the content of the file and remove spaces
        hex_data = f.read().replace(" ", "")

    # Find the index of the first occurrence of 'ffd8'
    start_index = hex_data.find('ffd8')
    # Find the index of the last occurrence of 'ffd9'
    end_index = hex_data.rfind('ffd9')

    # If both 'ffd8' and 'ffd9' are found
    if start_index != -1 and end_index != -1:
        # Extract the hex data between 'ffd8' and 'ffd9'
        extracted_hex_data = hex_data[start_index:end_index+4]

        # Open the output file in write mode
        with open(output_file, 'w') as f:
            # Write the extracted hex data to the output file
            f.write(extracted_hex_data)
        # Print success message
        print("Hex data extracted successfully.")
    else:
        # If 'ffd8' or 'ffd9' is not found, print error message
        print("Hex data not found in the file.")


# Input and output file names
input_file = "hex.txt"
output_file = "extracted_hex_data.txt"

# Call the function to extract hex data
extract_hex(input_file, output_file)