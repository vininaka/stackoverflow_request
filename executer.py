import subprocess
import re
import argparse
from fetcher import show_solutions, get_and_print_first_solution

def run_script(script_name):
    try:
        # Runs external script and checks if it returns an error
        command = ["python", script_name]
        subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)

    except subprocess.CalledProcessError as e:
        error_name = e.output.strip().splitlines()[-1]
        match = re.match(r'(\w+Error):\s(.+$)', error_name)

        if match:
            error_type, error_details = match.groups()
        else:
            error_type = error_name
            error_details = None

        print(f"Error Type: {error_type}")
        print(f"Error Details: {error_details}")

        show_solutions(error_type)
        get_and_print_first_solution(error_type)

if __name__ == "__main__":
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Script parser to execute")
    # Define command-line arguments
    parser.add_argument("--script_name", type=str, required=True, help="Script to execute")
    # Parse the command-line arguments
    args = parser.parse_args()

    run_script(args.script_name)