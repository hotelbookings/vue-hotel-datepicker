import subprocess
import sys


def open_read_file(file):
    """Opens the given file, reads and returns the file as a string"""

    # open the given file in read mode
    f = open(file, "r")

    file = f.read()
    f.close()

    return file


def open_write_file(file, data):
    """Opens the given file, and saves with the new data."""

    # open the given file in read mode
    f = open(file, "w")

    file = f.write(data)
    f.close()

    return file


if __name__ == '__main__':
    filename = './current-version'
    currentEnv = open_read_file(filename)
    print("Current Version:", currentEnv)
    nextEnv = int(currentEnv) + 1
    tag = 'v0.'
    hundreds = int(nextEnv / 100)
    tag += str(hundreds).zfill(2) + "."
    tens = nextEnv - (hundreds * 100)
    tag += str(tens).zfill(2)
    git_message = sys.argv[2]
    bashCmd = []
    bashCmd.append('./build.sh')
    bashCmd.append('-m')
    bashCmd.append(git_message)
    bashCmd.append('-v')
    bashCmd.append(tag)
    process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(output)
    open_write_file(filename, str(nextEnv))
    print("New tag:", tag)

