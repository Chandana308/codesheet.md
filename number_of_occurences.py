import pandas as pd
import re
from collections import Counter

def extract_group_counts(file_path, sheet_name="Input Data sheet", column_name="Additional comments"):
    # Load the Excel file
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    
    # Extract the relevant column and drop missing values
    comments = df[column_name].dropna().astype(str)
    
    # Regex pattern to capture groups inside <I> </I> within the [code] tags after "Groups :"
    pattern = r"Groups\s*:\s*\[code\]<I>(.*?)</I>\[/code\]"
    
    # List to store extracted group names
    group_list = []

    # Extract groups from each comment
    for comment in comments:
        matches = re.findall(pattern, comment, re.IGNORECASE)
        for match in matches:
            # Groups may be comma-separated, so we split and strip them
            group_list.extend([group.strip() for group in match.split(",")])
    
    # Count occurrences of each unique group
    group_counts = Counter(group_list)

    # Convert result to a DataFrame
    result_df = pd.DataFrame(group_counts.items(), columns=["Group name", "Number of occurrences"])

    # Sort the results by the number of occurrences in descending order
    result_df = result_df.sort_values(by="Number of occurrences", ascending=False).reset_index(drop=True)

    return result_df

# Usage
file_path = "coding challenge test (1).xlsx"  # Update this to the correct file path
result_df = extract_group_counts(file_path)

# Save results to a new Excel file
result_df.to_excel("group_counts.xlsx", index=False)

# Display results
print(result_df)



