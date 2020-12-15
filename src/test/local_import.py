import os
import sys

# Get the current directory
current_path = os.path.dirname(__file__)

# Get the parent directory
parent_path = os.path.dirname(current_path)

# Add the parent directory to sys.path
sys.path.append(parent_path)
