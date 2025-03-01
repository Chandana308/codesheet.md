import pandas as pd
import re
from collections import Counter

def extract_group_counts(file_path, sheet_name="Input Data sheet", column_name="Additional comments"):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    
    comments = df[column_name].dropna().astype(str)
    
    pattern = r"Groups\s*:\s*\[code\]<I>(.*?)</I>\[/code\]"
    
    group_list = []

    for comment in comments:
        matches = re.findall(pattern, comment, re.IGNORECASE)
        for match in matches:
            group_list.extend([group.strip() for group in match.split(",")])
    
    group_counts = Counter(group_list)

    result_df = pd.DataFrame(group_counts.items(), columns=["Group name", "Number of occurrences"])

    result_df = result_df.sort_values(by="Number of occurrences", ascending=False).reset_index(drop=True)

    return result_df

file_path = "coding challenge test (1).xlsx"  
result_df = extract_group_counts(file_path)

result_df.to_excel("group_counts.xlsx", index=False)

print(result_df)



