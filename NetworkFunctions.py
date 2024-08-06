functions=[
    {"Abbreviation": "5G-EIR", "Role": "Enables authentication of devices in the network. Protects networks and revenues against the use of stolen and unauthorized devices."},
    {"Abbreviation": "AMF", "Role": "Performs most of the functions that the MME performs in a 4G network."},
    {"Abbreviation": "AUSF", "Role": "Performs the authentication function of 4G HSS."},
    {"Abbreviation": "CBCF", "Role": "Supports public warning system functionality."},
    {"Abbreviation": "CCS", "Role": "Provides account management, rating, and charging functions."},
    {"Abbreviation": "DN", "Role": "e.g. Internet access or 3rd party services."},
    {"Abbreviation": "EASDF", "Role": "Registers to the NRF for EASDF discovery and selection. Handles the DNS messages according to the instructions from the SMF, exchanges DNS messages from the UE. Forwards DNS messages to C-DNS or L-DNS for DNS Queries."},
    {"Abbreviation": "GMLC", "Role": "Provides functionality required to support location-based services (LBS). The GMLC is the first node an external LBS client accesses in a PLMN. AFs and NFs may access GMLC directly or via the NEF."},
    {"Abbreviation": "I-NEF", "Role": "Intermediate Network Exposure Function."},
    {"Abbreviation": "I-UPF", "Role": "Examples of these are a Wi-Fi, and DSL network."},
    {"Abbreviation": "LMF", "Role": "Supports location-based services (LBS) for a UE."},
    {"Abbreviation": "MBSF", "Role": "Multicast/Broadcast Service Function."},
    {"Abbreviation": "MB-SMF", "Role": "Handles MBS session management (including QoS control), configures the MB-UPF for multicast and broadcast data transport and allocates/de-allocates TMGIs."},
    {"Abbreviation": "MBSTF", "Role": "Multicast/Broadcast Service Transport Function."},
    {"Abbreviation": "MB-UPF", "Role": "Handles packet filtering of incoming downlink packets for multicast and broadcast flows. QoS enforcement (MFBR) and interactions with MB-SMF for receiving multicast and broadcast data."},
    {"Abbreviation": "MFAF", "Role": "The messaging framework in which the analytics or event notifications (carrying raw data for the NWDAF to process) can be distributed around the network. Its operation is not standardized by the 3GPP."},
    {"Abbreviation": "N3IWF", "Role": "Non-3GPP Interworking Function."},
    {"Abbreviation": "NAF", "Role": "Identifies a Service-based Interface for the Application Function."},
    {"Abbreviation": "NF", "Role": "Network Function."},
    {"Abbreviation": "Non-3GPP Network", "Role": "Networks not defined by 3GPP. Examples of these are a Wi-Fi, and DSL network."},
    {"Abbreviation": "NRF", "Role": "Allows every network function to discover the services offered by other network functions."},
    {"Abbreviation": "NSACF", "Role": "Monitors and controls the number of registered UEs per network slice and/or the number of PDU Sessions per network slice for the network slices that are subject to Network Slice Admission Control (NSAC)."},
    {"Abbreviation": "NSSAAF", "Role": "Provides slice-specific authentication and authorization for a given UE. The NSSAAF acts as a NF Service Producer, while the AMF is the NF Service Consumer."},
    {"Abbreviation": "NSSF", "Role": "Redirects traffic to a network slice."},
    {"Abbreviation": "NSWOF", "Role": "Interfaces to the WLAN access network using the SWa interface and interfaces to the AUSF using the Nausf Service Based Interface (SBI) to support WLAN connection using 5G credentials without 5GS registration."},
    {"Abbreviation": "NWDAF", "Role": "Responsible for providing network analysis information upon request from network functions."},
    {"Abbreviation": "PCF", "Role": "Governs the network behavior by supporting a unified policy framework. Also, provides policy rules to Control Plane functions."},
    {"Abbreviation": "PSA", "Role": "PDU Session Anchor. The user plane function that terminates the N6 interface of a PDU session within a 5G core network."},
    {"Abbreviation": "RAN", "Role": "Radio Access Network. Using radio technology provides access to the core network."},
    {"Abbreviation": "SEPP", "Role": "Protects control plane traffic that is exchanged between different 5G operator networks."},
    {"Abbreviation": "SMF", "Role": "Session Management Function. Handles management of UE sessions."},
    {"Abbreviation": "SMSF", "Role": "Short Message Service Function. Supports the transfer of SMS over NAS."},
    {"Abbreviation": "TNGF", "Role": "Trusted Non-3GPP Gateway Function. Enables the UE to connect to the 5G Core over WLAN access technology."},
    {"Abbreviation": "TSCTSF", "Role": "Time Sensitive Communication Time Synchronization Function. Controls the DS-TT(s) and NW-TT for the (g)PTP based time synchronization service. In addition, TSCTSF supports TSC assistance container related functionalities."},
    {"Abbreviation": "TSN AF", "Role": "Time-Sensitive Networking Application Function. Stores the binding relationship between a port on UE/DS-TT side and a PDU Session during reporting of 5GS TSN bridge information. The TSN AF also stores the information about ports on the UPF/NW-TT side."},
    {"Abbreviation": "TWIF", "Role": "Trusted WLAN Interworking Function. A new 5G function for interoperability with legacy devices. Some devices may support 5G SIM authentication but do not support 5G NAS signaling over trusted Wi-Fi access. TWIF contains the NAS protocol stack and exchanges NAS messages with the AMF on behalf of these types of devices."},
    {"Abbreviation": "UCMF", "Role": "UE radio Capability Management Function. Allows NF service consumers to create, update and delete UCMF dictionary entries for Manufacturer-assigned UE Radio Capability IDs."},
    {"Abbreviation": "UDM", "Role": "Unified Data Management. Performs parts of the 4G HSS function."},
    {"Abbreviation": "UDR", "Role": "Unified Data Repository. A converged repository of subscriber information that can be used to service a number of network functions."},
    {"Abbreviation": "UDSF", "Role": "Unstructured Data Storage Function. Part of the UDM entity. Network Functions (NFs) can store/retrieve unstructured data from an Unstructured Data Storage Function (UDSF)."},
    {"Abbreviation": "UE", "Role": "User Equipment. Any device used directly by an end-user to communicate (a handheld phone, laptop, etc.)."},
    {"Abbreviation": "UPF", "Role": "User Plane Function. A combination of the data plane parts of the SGW and PGW in 4G."},
    {"Abbreviation": "W-AGF", "Role": "Wireline Access Gateway Function. Enables wireline access to the 5G Core."},
    {"Abbreviation": "5G DDNMF", "Role": "Direct Discovery Name Management Function. The logical function handling network-related actions required for dynamic 5G ProSe Direct Discovery."},
    {"Abbreviation": "AAnF", "Role": "AKMA Anchor Function. The anchor function in the HPLMN that generates the key material to be used between the UE and the AF and maintains UE AKMA contexts."},
    {"Abbreviation": "AF", "Role": "Application Function. Performs the same function as the EPC AF."},
    {"Abbreviation": "AKMA", "Role": "Authentication and Key Management for Applications. Similar to the Generic Bootstrapping Architecture (GBA) in earlier generations, this function leverages an operator authentication infrastructure to secure the communication between the UE and an Application Function (AF)."},
    {"Abbreviation": "CHF", "Role": "Charging Function. Allows charging services to be offered to authorized network functions."},
    {"Abbreviation": "DCCF", "Role": "Data Collection Coordination Function. Coordinates data collection to avoid duplicate requests for the same data."},
    {"Abbreviation": "NEF", "Role": "Network Exposure Function. Provides a mechanism for securely exposing services and features of the 5G core."},
    {"Abbreviation": "AnLF", "Role": "Analytical Logical Function. Responsible for collecting the analytical request and sending the response to the consumer. AnLF requires the model endpoints, which are provided by the MTLF (Model Training Logical Function)."},
    {"Abbreviation": "MTLF", "Role": "Model Training Logical Function. The MTLF trains and deploys the model inference microservice."},
    {"Abbreviation": "SCP", "Role": "Service Communication Proxy. A new network function enabling dynamic scaling and management of communication and services in the 5G network."},
    {"Abbreviation": "ADRF", "Role": "Analytical Data Repository Function. Stores and retrieves analytics generated by NWDAFs and other collected data."},
    {"Abbreviation": "NSWOF", "Role": "Non-Seamless WLAN Offload Function. Interfaces to the WLAN access network and supports WLAN connection using 5G credentials without 5GS registration."},
    {"Abbreviation": "CAPIF", "Role": "Common API Framework. Provides a unified and standardized northbound API framework across several 3GPP functions."},
    {"Abbreviation": "PFDF", "Role": "Packet Flow Description Function. A repository that stores Packet Flow Descriptions (PFDs) that can be managed and updated by third-party service providers."},
    {"Abbreviation": "RE-NWDAF", "Role": "Roaming Exchange NWDAF. NWDAF with roaming exchange capability, used as an exchange point to exchange analytics and to collect input data for analytics with other PLMNs."},
    {"Abbreviation": "BSF", "Role": "Binding Support Function. Used for binding an application-function request."},
    {"Abbreviation":"5G DDNMF"}
]