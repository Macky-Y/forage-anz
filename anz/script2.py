import base64

def base64_to_hex_from_file(input_file, output_file):
    # Read the Base64 string from the input file
    with open(input_file, 'r') as file:
        base64_str = file.read().strip()

    # Decode the Base64 string
    decoded_bytes = base64.b64decode(base64_str)
    
    # Convert the decoded bytes to hexadecimal
    hex_str = decoded_bytes.hex()

    # Write the hexadecimal string to the output file
    with open(output_file, 'w') as file:
        file.write(hex_str)

# Example usage
input_file = "base64_to_hex.txt"   # Input file containing Base64 string
output_file = "base64_hex_output.txt"     # Output file for hexadecimal representation
base64_to_hex_from_file(input_file, output_file)
