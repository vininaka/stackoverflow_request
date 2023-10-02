import subprocess
import re
import argparse
from fetcher import show_solutions, get_and_print_first_solution

if __name__ == "__main__":
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Script parser to execute")
    # Define command-line arguments
    parser.add_argument("--script_name", type=str, help="Script to execute")
    # Parse the command-line arguments
    args = parser.parse_args()
    # Access and use the argument values
    value = args.script_name
    
    assert value is not None, "Argument 'script_name' is required and cannot be None."

    try:
        # Runs external script and checks if returns an error
        command = ["python", value]
        subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)

    except subprocess.CalledProcessError as e:
        # Process error format to split in error type and error details
        error_name = e.output.strip().splitlines()
        error_name = error_name[-1]

        match = re.match(r'(\w+Error):\s(.+$)', error_name)
        if match:
            error_type, error_details = match.groups()
            print(f"Error Type: {error_type}")
            print(f"Error Details: {error_details}")

            show_solutions(error_type)
            get_and_print_first_solution((error_type))
        else:
            show_solutions(error_name)
            get_and_print_first_solution((error_name))

