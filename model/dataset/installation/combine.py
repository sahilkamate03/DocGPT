import json, os

# List of input JSONL file paths
# input_files = ['file1.jsonl', 'file2.jsonl', 'file3.jsonl']
input_dir = 'model/dataset/installation'

# Get a list of all files in the input directory
files = os.listdir(input_dir)

# Filter the list to include only JSONL files
jsonl_files = [f for f in files if f.endswith('.jsonl')]

# Construct the full paths to the input files
input_files = [os.path.join(input_dir, f) for f in jsonl_files]

# Output JSONL file path
output_file = 'merged.jsonl'

# Open the output file for writing
with open(output_file, 'w') as f_out:

    # Iterate over the input files
    for input_file in input_files:

        # Open the input file for reading
        with open(input_file, 'r') as f_in:

            # Iterate over the lines in the input file
            for line in f_in:

                # Parse the JSON object from the line
                obj = json.loads(line)

                # Write the JSON object to the output file
                f_out.write(json.dumps(obj) + '\n')
