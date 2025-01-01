import subprocess
import os

def exec(command):
    try:
        result = subprocess.run(command.split(), capture_output = True, text = True)
        print(result.stdout)
        if result.stderr:
            print(f"Error : {result.stderr}")
    except Exception as e:
        print(f"Exception : {e}")

def file_to_process(command):
    try:
        # split and clear each part
        parts = command.split('<')
        cmd = parts[0].strip()
        input_file = parts[1].strip()

        with open(input_file, 'r') as infile:
            result = subprocess.run(cmd.split(), stdin=infile, capture_output=True, text=True)
            print(result.stdout)
            if result.stderr:
                print(f"Error: {result.stderr}")
    except Exception as e:
        print(f"An exception occurred: {e}")


def process_to_file(command):
    try:
        # split and clear each part
        parts = command.split('>')
        cmd = parts[0].strip()
        output_file = parts[1].strip()

        with open(output_file, 'w') as outfile:
            result = subprocess.run(cmd.split(), capture_output = True, text = True)
            outfile.write(result.stdout)
            if result.stderr:
                print(f"Error : {result.stderr}")
    except Exception as e:
        print(f"Exception : {e}")
        
def main():
    print("Custom Shell: Type 'exit' to quit.")
    while True:
        command = input(">> ").strip()
        if command.lower() == "exit":
            break
        elif "<" in command:
            file_to_process(command)
        elif ">" in command:
            process_to_file(command)
        elif command == "pwd":
            print(os.getcwd())
        elif command.startswith("cd"):
            subprocess.run(["cd", command[3:]])
        else:
            exec(command)

if __name__ == "__main__":
    main()