
import json
import csv
import re 
import os
from typing import List, Dict, Union
import pandas as pd
from docx import Document
from langchain_ollama import ChatOllama
from tqdm import tqdm
from openai import AzureOpenAI
from dotenv import load_dotenv

system_prompt = """
You are an AI assistant specializing in 3GPP telecommunications specifications. Your primary responsibility is to classify abbreviations into their correct entity types based **strictly on the context** provided. You must adhere exactly to the predefined categories and output format. Deviate from these rules only if absolutely necessary.

### Key Rules to Follow:
1. **Strict Category Matching**: Only use the predefined categories. Do not classify any abbreviation into a category not listed below.
2. **Exact Output Format**: Return the response in the exact format provided in the instructions without adding extra fields or text.
3. **Contextual Classification**: Rely solely on the context given to determine the correct classification. Avoid assumptions beyond what the context explicitly states.

### Output Format (strictly return the following fields):
- **entity_type**: The category of the abbreviation based on the context.
- **description**: A detailed, accurate description of the entity type and its relevance to the 3GPP specification.
- **explanation**: A short explanation of how the provided context justifies the classification.

### Predefined Categories:
Classify the abbreviation into one of the following entity types based on its role within the 3GPP specification:

1. **Protocol**:
   Data transmission rules used in telecommunications, e.g., NAS (Non-Access Stratum), SIP, IP, UDP.

2. **Network**:
   A collective set of interconnected network functions delivering telecommunications capabilities, e.g., EPC, 5GC, GSM/EDGE, UTRA, E-UTRA, NR radio access, Wi-Fi, WiMAX.

3. **Network Function**:
   Refers to both virtualized and dedicated hardware components within telecommunications, e.g., RNC, BSC, MSC, MME. "Network Element" and "Network Node" are synonymous with "Network Function."

4. **Interface**:
   Communication pathways between Network Functions, e.g., N1 Interface.

5. **Service**:
   Telecommunication offerings, e.g., VoLTE (Voice over LTE).

6. **Technology**:
   Standards governing telecommunications operations, e.g., 5G, LTE, GPS, 5G system architecture,TDD,FDD,.

7. **Parameter**:
   Critical network attributes for operation, including identifiers and timers, e.g., IMSI (International Mobile Subscriber Identity), T311 Timer.

8. **Connection**:
   Communication links between network endpoints, including DRBs, SRBs, and channels for data transmission, e.g., PDSCH, PRACH.

9. **Procedure**:
   Sequences of network operations, e.g., handover procedures, PDU sessions.

10. **Message**:
   Signaling data exchanged between network components, including control, user data, and signaling messages.

11. **Specification**:
   Technical 3GPP documents outlining standards and protocols, e.g., 3GPP TS 23.501.

12. **Organization**:
   Entities defining telecommunications standards, e.g., 3GPP.

13. **State**:
   Conditions/statuses of a network element or procedure, e.g., active, idle, error state.

14. **Mode**:
   Operational modes, e.g., Circuit Switched (CS), Packet Switched (PS).

15. **Measurement**:
   Network performance metrics, e.g., RSRP (Reference Signal Received Power), QoS (Quality of Service), QoE (Quality of Experience).

16. **Cause Code**:
   Codes identifying reasons for telecom events/issues, e.g., cause#5.

17. **Device**:
   Devices connecting to the network, including user equipment (e.g., smartphones, IoT devices) and network hardware (e.g., routers, switches).

18. **Working Group (WG)**:
   3GPP Working Groups for specific work areas, e.g., RAN1, SA2, SA4, CT1.

19. **Item**:
   Refers to Study Items (SI) and Work Items (WI) in 3GPP standardization.

20. **Miscellaneous**:
   Terms relevant to telecommunications but not fitting other categories.

### Input Format:
Input will be given in JSON format as follows:
```json
{
  "abbreviation": "<Abbreviation>",
  "full_form": "<Full Form>",
  "context": "<Context>"
}

#### Output:
entity_type: Network Function
description: The Access and Mobility Management Function (AMF) is responsible for managing access and mobility of user equipment (UE) in the 5G core network. It handles user authentication, session management, and connection establishment, enabling smooth transitions of users across network regions.
explanation: AMF is classified as a Network Function based on its role in controlling UE access and mobility within the network, as highlighted by the context.

DO NOT CLASSIFY THE ENTITIES OTHER THEN GIVEN LIST IN ### Predefined Categories ### I WILL PAY YOU 3000$
"""

def get_text_format(text):
  llm=llm = ChatOllama(model='llama3.1:70b', temperature=0, format='json')
  message=[
  ("system",system_prompt),("human",f"context:{text}")
]
  ai_msg=llm.invoke(message)
  print("AI Message Content:", ai_msg.content.strip())
  return ai_msg.content.strip()


def get_json_out(text):
    system_json="""You are tasked with extracting structured information from the provided text. Please read the text carefully and extract the following three components:

1. **entity_type**: The category of the telecommunications concept mentioned.
2. **description**: A detailed description of the concept, including its role and functionality.
3. **explanation**: A brief explanation of why the concept is classified under the selected entity type.

### Output Format:
The extracted information should be formatted as a JSON object with the following structure:

```json
{
    "entity_type": "string",
    "description": "string",
    "explanation": "string"
}
DO NOT GIVE ANY OTHER FORMAT GIVE ONLY JSON I WILL PAY YOU 4000$ PLEASE!!!
"""

    llm=ChatOllama(model='gemma2:9b',temperature=0,format='json')
    message=[
    ("system",system_json),("human",f"context:{text}")
  ]
    ai_msg=llm.invoke(message)
    try:
        json_str = json.loads(ai_msg.content.strip())
        print("Parsed JSON:", json_str)
        return json_str
    except json.JSONDecodeError as e:
        print(f"JSON decoding error: {e}. Response content: {ai_msg.content}")
        return None, "Error decoding JSON response.", None
    

# # Function to read and update the progress index in 'progress.txt'
# def read_progress(file_path: str) -> int:
#     if os.path.exists(file_path):
#         with open(file_path, 'r') as f:
#             last_index = f.read().strip()
#             return int(last_index) if last_index else 0
#     else:
#         return 0

# def write_progress(file_path: str, index: int):
#     with open(file_path, 'w') as f:
#         f.write(str(index))


# def process_csv_and_save(input_csv: str, output_csv: str, progress_file: str):
#     # Read input CSV
#     df = pd.read_csv(input_csv)
#     # Read the last processed index from the progress file
#     last_index = read_progress(progress_file)
#     print(f"Resuming from index {last_index}")

#     # Check if the output CSV already exists and is non-empty
#     file_exists = os.path.isfile(output_csv) and os.path.getsize(output_csv) > 0
    
#     # Open the output CSV in append mode
#     with open(output_csv, 'a', newline='', encoding='utf-8') as csvfile:
#         fieldnames = ["name", "full_form", "entity_type", "description", "explanation", "context", "section_title", "doc_number"]
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
#         # Write the header if the file is new or empty
#         if not file_exists:
#             writer.writeheader()

#         # Iterate over rows in the CSV file from the last index
#         for index, row in tqdm(df.iloc[last_index:].iterrows(), total=len(df) - last_index):
#             name = row['name']
#             full_form = row['full_form']
#             content = row['context']
#             doc_number = row['doc_number']
#             section_title = row['section_title']
#             context = f"[ Text extracted from : {doc_number}) \n Paragraph taken from section title : {section_title}] \n Generate only using Paragraph : {content}"
            
#             input_text = str({
#                 'abbreviation': name,
#                 'full_form': full_form,
#                 'context': context
#             })
           
#             # Get the classification from LLaMA model
#             entity_data = get_text_format(input_text)  # Replace "model_name" with your actual model name
#             generated = get_json_out(entity_data)
#             if 'entity_type' in generated:

#                 # Prepare row data to be saved
#                 row_data = {
#                     "name": name,
#                     "full_form": full_form,
#                     "entity_type": generated['entity_type'],
#                     "description": generated['description'],
#                     "explanation": generated['explanation'],
#                     "context": content,
#                     "section_title": section_title,
#                     "doc_number": doc_number
#                 }
                
#                 # Save the processed row to CSV immediately
#                 writer.writerow(row_data)
                
#                 # Update the progress file after processing each row
#                 write_progress(progress_file, index + 1)
#     print(f"Processed data saved to {output_csv}")


# input_csv = '/home/sunny/Desktop/SunnyKG/prev_method/data_32_38_34.csv'  
# output_csv = 'output_data_32_38_34.csv'   
# progress_file = '/home/sunny/Desktop/SunnyKG/prev_method/progress.txt'  
# process_csv_and_save(input_csv, output_csv, progress_file)



# def write_progress(file_path: str, index: int):
#     with open(file_path, 'w') as f:
#         f.write(str(index))

# def process_csv_and_save(input_csv: str, output_csv: str, progress_file: str, batch_size: int = 10):
#     df = pd.read_csv(input_csv)
#     last_index = read_progress(progress_file)
#     print(f"Resuming from index {last_index}")
#     file_exists = os.path.isfile(output_csv) and os.path.getsize(output_csv) > 0
    
#     with open(output_csv, 'a', newline='', encoding='utf-8') as csvfile:
#         fieldnames = ["name", "full_form", "entity_type", "description", "explanation", "context", "section_title", "doc_number"]
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         if not file_exists:
#             writer.writeheader()
        
#         rows_to_save = []
#         for index, row in tqdm(df.iloc[last_index:].iterrows(), total=len(df) - last_index):
#             try:
#                 name = row['name']
#                 full_form = row['full_form']
#                 content = row['context']
#                 doc_number = row['doc_number']
#                 section_title = row['section_title']
#                 context = f"[Text from {doc_number}, section {section_title}]: {content}"
                
#                 input_text = {
#                     'abbreviation': name,
#                     'full_form': full_form,
#                     'context': context
#                 }
#                 entity_data = get_text_format(input_text)
#                 generated = get_json_out(entity_data)

#                 if generated and 'entity_type' in generated:
#                     row_data = {
#                         "name": name,
#                         "full_form": full_form,
#                         "entity_type": generated['entity_type'],
#                         "description": generated['description'],
#                         "explanation": generated['explanation'],
#                         "context": content,
#                         "section_title": section_title,
#                         "doc_number": doc_number
#                     }
#                     rows_to_save.append(row_data)
                
#                 if len(rows_to_save) >= batch_size:
#                     writer.writerows(rows_to_save)
#                     write_progress(progress_file, index + 1)
#                     rows_to_save.clear()
                    
#             except Exception as e:
#                 print(f"Error at index {index}: {e}")

#         if rows_to_save:
#             with open("out_34_38_32.txt", "w") as file:
#                 json.dump(rows_to_save, file, indent=4)
#             writer.writerows(rows_to_save)
#             write_progress(progress_file, len(df))
#     print(f"Processed data saved to {output_csv}")
# def process_csv_and_save(input_csv: str, output_csv: str, progress_file: str, batch_size: int = 10):
#     df = pd.read_csv(input_csv)
#     last_index = read_progress(progress_file)
#     print(f"Resuming from index {last_index}")
#     file_exists = os.path.isfile(output_csv) and os.path.getsize(output_csv) > 0
    
#     with open(output_csv, 'a', newline='', encoding='utf-8') as csvfile:
#         fieldnames = ["name", "full_form", "entity_type", "description", "explanation", "context", "section_title", "doc_number"]
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         if not file_exists:
#             writer.writeheader()
        
#         rows_to_save = []
#         for index, row in tqdm(df.iloc[last_index:].iterrows(), total=len(df) - last_index):
#             try:
#                 name = row['name']
#                 full_form = row['full_form']
#                 content = row['context']
#                 doc_number = row['doc_number']
#                 section_title = row['section_title']
#                 context = f"[Text from {doc_number}, section {section_title}]: {content}"
                
#                 input_text = {
#                     'abbreviation': name,
#                     'full_form': full_form,
#                     'context': context
#                 }
#                 entity_data = get_text_format(input_text)
#                 generated = get_json_out(entity_data)

#                 # Debug output
#                 print("Generated output:", generated)

#                 if generated and 'entity_type' in generated:
#                     row_data = {
#                         "name": name,
#                         "full_form": full_form,
#                         "entity_type": generated['entity_type'],
#                         "description": generated['description'],
#                         "explanation": generated['explanation'],
#                         "context": content,
#                         "section_title": section_title,
#                         "doc_number": doc_number
#                     }
#                     rows_to_save.append(row_data)
                
#                 # Save batch
#                 if len(rows_to_save) >= batch_size:
#                     with open("out_34_38_32.txt", "w") as file:
#                         json.dump(rows_to_save, file, indent=4)
#                     print(f"Saving batch of {len(rows_to_save)} rows")
#                     writer.writerows(rows_to_save)
#                     write_progress(progress_file, index + 1)
#                     rows_to_save.clear()
                    
#             except Exception as e:
#                 print(f"Error at index {index}: {e}")

#         # Save any remaining rows
#         if rows_to_save:
#             writer.writerows(rows_to_save)
#             write_progress(progress_file, len(df))
#     print(f"Processed data saved to {output_csv}")


# Function to read and update the progress index in 'progress.txt'
def read_progress(file_path: str) -> int:
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            last_index = f.read().strip()
            return int(last_index) if last_index else 0
    else:
        return 0

def write_progress(file_path: str, index: int):
    with open(file_path, 'w') as f:
        f.write(str(index))


def process_csv_and_save(input_csv: str, output_csv: str, progress_file: str, batch_size: int = 1):
    df = pd.read_csv(input_csv)
    last_index = read_progress(progress_file)
    print(f"Resuming from index {last_index}")

    file_exists = os.path.isfile(output_csv) and os.path.getsize(output_csv) > 0
    output_txt = "textdataset_34_38_32.txt"

    # Initialize the text file if it doesn't exist
    if not os.path.exists(output_txt):
        with open(output_txt, "w") as file:
            file.write("[\n")  # Start of a JSON array

    # Open the CSV file for writing
    with open(output_csv, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["name", "full_form", "entity_type", "description", "explanation", "context", "section_title", "doc_number"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()

        for index, row in tqdm(df.iloc[last_index:].iterrows(), total=len(df) - last_index):
            try:
                name = row['name']
                full_form = row['full_form']
                content = row['context']
                doc_number = row['doc_number']
                section_title = row['section_title']
                context = f"[Text from {doc_number}, section {section_title}]: {content}"

                input_text = {
                    'abbreviation': name,
                    'full_form': full_form,
                    'context': context
                }
                entity_data = get_text_format(input_text)
                generated = get_json_out(entity_data)

                if generated and 'entity_type' in generated:
                    row_data = {
                        "name": name,
                        "full_form": full_form,
                        "entity_type": generated['entity_type'],
                        "description": generated['description'],
                        "explanation": generated['explanation'],
                        "context": content,
                        "section_title": section_title,
                        "doc_number": doc_number
                    }

                    # Write to CSV immediately
                    writer.writerow(row_data)
                    write_progress(progress_file, index + 1)

                    # Append to text file
                    with open(output_txt, "a") as file:
                        json.dump(row_data, file, indent=4)
                        file.write(",\n")  # Separate entries with a comma and newline

            except Exception as e:
                print(f"Error at index {index}: {e}")

        # Close the JSON array after all processing
        with open(output_txt, "a") as file:
            file.write("\n]")  # Close the JSON array

    print(f"Processed data saved to {output_csv}")


input_csv = '/home/sunny/Desktop/SunnyKG/prev_method/data_22_31_33.csv'
output_csv = 'dataset_31_22_33.csv'
progress_file = '/home/sunny/Desktop/SunnyKG/prev_method/progress.txt'
process_csv_and_save(input_csv, output_csv, progress_file)


