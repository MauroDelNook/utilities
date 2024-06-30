import yaml

def read_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def write_yaml(data, file_path):
    with open(file_path, 'w') as file:
        yaml.safe_dump(data, file)

def insert_specific_parameters(source_file, target_file, new_file, param_key):
    # Read the source and target YAML files
    source_data = read_yaml(source_file)
    target_data = read_yaml(target_file)

    # Check if the specific parameter exists in the source data
    if param_key in source_data:
        # Insert the specific parameter into the target data
        target_data[param_key] = source_data[param_key]

    # Write the updated data to a new file
    write_yaml(target_data, new_file)

# Example usage: only pass the param1 parameter from source_file
source_file = 'source.yaml'
target_file = 'target.yaml'
new_file = 'updated_target.yaml'
param_key = 'param1'

insert_specific_parameters(source_file, target_file, new_file, param_key)
