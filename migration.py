import sys
import subprocess

def convert_to_text_hwp(file_path):
    """
    Uses hwp5proc to attempt to parse a file and return its text content.
    """
    try:
        # The command to run. We're trying to extract the preview text stream.
        command = ["hwp5proc", "cat", "--vstreams", file_path, "PrvText.utf8"]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except FileNotFoundError:
        return "Error: hwp5proc command not found. Make sure pyhwp is installed and in your PATH."
    except subprocess.CalledProcessError as e:
        return f"An error occurred while running hwp5proc: {e}\nStderr: {e.stderr}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        content = convert_to_text_hwp(file_path)
        print(content)
    else:
        print("Usage: python migration.py <file_path>")
