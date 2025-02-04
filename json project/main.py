import json
import os


def read_json_file(file_path):
    """Reads a JSON file and returns its content."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: The file {file_path} does not contain valid JSON.")
        return []


def filter_by_company_id(data, company_id):
    """Filters the list of JSON documents by company_id."""
    return [doc for doc in data if doc.get('company_id') == company_id]


def write_json_file(file_path, data):
    """Writes the filtered data to a JSON file."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def main():
    input_file = 'data/input.json'  # path to input JSON file
    output_file = 'output/filtered_output.json'  # path to output JSON file

    company_id_to_filter = "12345"  # change this to the desired company ID

    # read the input JSON file
    data = read_json_file(input_file)

    if not data:
        print("No data to process.")
        return

    # filter data by company_id
    filtered_data = filter_by_company_id(data, company_id_to_filter)

    if not filtered_data:
        print(f"No records found with company_id {company_id_to_filter}.")
        return

    # write the filtered data to the output file
    write_json_file(output_file, filtered_data)

    print(f"Filtered data written to {output_file}")


if __name__ == "__main__":
    main()
