import os
import subprocess

from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a Python file located within the working directory with optional arguments and returns its output",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Python file path relative to the working directory to execute along with optional arguments",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Array of string arguments to pass to the Python file",
                items=types.Schema(type=types.Type.STRING),
            ),
        },
        required=["file_path"],
    ),
)


def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = (
            os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        )
        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not target_file.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file]
        if args is not None:
            command.extend(args)

        process = subprocess.run(
            command,
            cwd=working_dir_abs,
            capture_output=True,
            text=True,
            timeout=30,
        )

        output = []

        if process.returncode != 0:
            output.append(f"Process exited with code {process.returncode}")

        if len(process.stdout) == 0 and len(process.stderr) == 0:
            output.append("No output produced")

        if len(process.stdout) > 0:
            output.append(f"STDOUT: {process.stdout}")

        if len(process.stderr) > 0:
            output.append(f"STDERR: {process.stderr}")

        return "\n".join(output)
    except Exception as e:
        return f"Error: executing Python file: {e}"
