import os
import json

def main():
    # Define the directory containing the JSON files
    json_dir = 'json'
    # Define the output manifest file path
    manifest_file = 'manifest.json'

    # List all files in the json directory
    try:
        all_files = os.listdir(json_dir)
        # Filter for files ending with .json
        json_files = [f for f in all_files if f.endswith('.json')]
        # Sort the list alphabetically (optional, but good practice)
        json_files.sort()
    except FileNotFoundError:
        print(f"Error: Directory '{json_dir}' not found.")
        exit(1)
    except Exception as e:
        print(f"An error occurred while listing files: {e}")
        exit(1)

    # Write the list of JSON filenames to the manifest file
    try:
        with open(manifest_file, 'w') as f:
            json.dump(json_files, f, indent=2) # Use indent=2 for pretty printing
        print(f"Successfully created '{manifest_file}' with {len(json_files)} entries.")
    except Exception as e:
        print(f"An error occurred while writing to '{manifest_file}': {e}")
        exit(1)

if __name__ == "__main__":
    main()
