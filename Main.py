# from label import NetworkFunction,Interfaces_Protocols
# from Interfaces import service_based_interface,non_service_based_interface
# import re
# from rich.console import Console
# from rich.text import Text
# filter=["Not specified by 3GPP","NA"]
# network_functions=NetworkFunction()
# Service_interface=service_based_interface
# NonService_interface=non_service_based_interface
# _,Protocols=Interfaces_Protocols()
# file_path = r'D:\NER\3gpp.txt'  # Corrected file path
# with open(file_path, 'r', encoding='utf-8') as file:
#     content = file.read()
# console = Console()
# # Annotate network functions
# for word in network_functions:
#     content = re.sub(rf"(\b{word}\b)", rf"\1 (Network Function)", content)

# # Annotate service-based interfaces
# for word in Service_interface:
#     content = re.sub(rf"(\b{word}\b)", rf"\1 (Service-based Interface)", content)

# # Annotate non-service-based interfaces
# for word in NonService_interface:
#     content = re.sub(rf"(\b{word}\b)", rf"\1 (Non-service-based Interface)", content)
# #Annotate Protocols 
# for word in Protocols:
#     if word not in filter:
#         content = re.sub(rf"(\b{word}\b)", rf"\1 (Protocol)", content)

# styled_text = Text(content)
# console.print(styled_text)



# from label import NetworkFunction, Interfaces_Protocols
# from Interfaces import service_based_interface, non_service_based_interface
# import re
# from rich.console import Console
# from rich.text import Text

# # Define the list of filters
# filter_list = ["Not specified by 3GPP", "NA"]

# # Load network functions, interfaces, and protocols
# network_functions = NetworkFunction()
# service_interface = service_based_interface
# non_service_interface = non_service_based_interface
# _, protocols = Interfaces_Protocols()

# # Load the content from the file
# file_path = r'D:\NER\3gpp.txt'  # Corrected file path
# with open(file_path, 'r', encoding='utf-8') as file:
#     content = file.read()

# # Initialize Rich console
# console = Console()

# # Annotate network functions
# for word in network_functions:
#     content = re.sub(rf"(\b{word}\b)(?! \(Network Function\))", rf"\1 (Network Function)", content)

# # Annotate service-based interfaces
# for word in service_interface:
#     content = re.sub(rf"(\b{word}\b)(?! \(Service-based Interface\))", rf"\1 (Service-based Interface)", content)

# # Annotate non-service-based interfaces
# for word in non_service_interface:
#     content = re.sub(rf"(\b{word}\b)(?! \(Non-service-based Interface\))", rf"\1 (Non-service-based Interface)", content)

# # Annotate protocols, excluding filtered words
# for word in protocols:
#     if word not in filter_list:
#         content = re.sub(rf"(\b{word}\b)(?! \(Protocol\))", rf"\1 (Protocol)", content)

# # Create and print styled text
# styled_text = Text(content)
# print(styled_text)


from label import NetworkFunction, Interfaces_Protocols
from Interfaces import service_based_interface, non_service_based_interface
import re
from rich.console import Console
from rich.text import Text

# Define the list of filters
filter_list = ["Not specified by 3GPP", "NA"]

# Load network functions, interfaces, and protocols
network_functions = NetworkFunction()
service_interface = service_based_interface
non_service_interface = non_service_based_interface
_, protocols = Interfaces_Protocols()

# Load the content from the file
file_path = r'D:\NER\3gpp.txt'  # Corrected file path
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Initialize Rich console
console = Console()

# Define colors for different annotations
colors = {
    'Network Function': 'blue',
    'Service-based Interface': 'green',
    'Non-service-based Interface': 'yellow',
    'Protocol': 'red'
}

# Annotate network functions
for word in network_functions:
    content = re.sub(
        rf"(\b{word}\b)(?! \(Network Function\))",
        rf"[{colors['Network Function']}]\1 (Network Function)[/]",
        content
    )

# Annotate service-based interfaces
for word in service_interface:
    content = re.sub(
        rf"(\b{word}\b)(?! \(Service-based Interface\))",
        rf"[{colors['Service-based Interface']}]\1 (Service-based Interface)[/]",
        content
    )

# Annotate non-service-based interfaces
for word in non_service_interface:
    content = re.sub(
        rf"(\b{word}\b)(?! \(Non-service-based Interface\))",
        rf"[{colors['Non-service-based Interface']}]\1 (Non-service-based Interface)[/]",
        content
    )

# Annotate protocols, excluding filtered words
for word in protocols:
    if word not in filter_list:
        content = re.sub(
            rf"(\b{word}\b)(?! \(Protocol\))",
            rf"[{colors['Protocol']}]\1 (Protocol)[/]",
            content
        )

# Create styled text
styled_text = Text.from_markup(content)

# Print styled text in the console
console.print(styled_text)

# Save the final output to a text file without color annotations
output_file_path = r'D:\NER\annotated_output.txt'
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    plain_text = styled_text.plain
    output_file.write(plain_text)

print(f"Annotated content saved to {output_file_path}")
