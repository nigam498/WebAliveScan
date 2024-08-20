import csv
from typing import List, Dict, Union
from lib.common.output import Output

def save_result(path: str, headers: List[str], results: List[Dict[str, Union[str, int]]]) -> bool:
    """
    Save results to a CSV file with specified headers.

    Args:
        path (str): Path to the file where results will be saved.
        headers (List[str]): List of header names for the CSV file.
        results (List[Dict[str, Union[str, int]]]): List of dictionaries containing the data to be saved.

    Returns:
        bool: True if the file was written successfully, False otherwise.
    """
    try:
        with open(path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=headers, quoting=csv.QUOTE_MINIMAL)
            writer.writeheader()
            writer.writerows(results)
        return True
    except Exception as e:
        Output().error(f"Failed to save results to {path}: {e}")
        return False
