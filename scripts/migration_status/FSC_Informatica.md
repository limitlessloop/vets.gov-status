# Name: Financial Service Center (FCS) Informatica (MAG)

Business and Application Owers: Wallace French Jonathan Lindow

Migrate to Cloud: Yes

Cutover Completed: 



### (Pre-Intake) Modernization and Decommission Planning
Task                                              | Status   | Comments (only if yellow or red)
------------                                      | -------- | ------------- 
Identify VA application owner                     |Complete     | Wallace French Business Owner; Jonathan Lindow PM
Initial cloud suitability 6 questions completed   | No    | Early migration; not yet deployed
ITOPs to review if "obsolete" system based on usage     |      | Need to confirm w/ Chris / ITOPS
ECSO Migration wave planning started              | N/A   |  Explanation of the waves was confusing; customers need to understand this.
Baseline costs (pre-cloud) documented             |Complete      |
Validated ACTIVE users / traffic analytics for past 12 months   |N/A      | B2B tool PaaS; data Analytics for FMBT tools to manage data and data cleanse
ROM and funding information provided (e.g., UFR, research vs. OIT dollars, etc. | Complete     |Under FMBT program
VIPR Epics completed                              | Complete |Did epics but not in VIPR; Sharepoint system used by OIT (Austin); follows VIPR process but different reporting system (franchise fund at VA); lack of business ID from ITOPs  
Routing tab in VIPR workbook completed            | No   | Early migration; intake workbook not yet deployed
100% complete pre-intake checklist                | No     | Checklist in development by CAS
COMPLETED ALL (PRE Intake) Tasks                  | Complete   | Early migration; many ECSO processes, tools, and exit criteria not yet in place.

### OIT Unified Intake (VIPR)
Task                                                          | Status   | Comments (only if yellow or red)
------------                                                  | -------- | -------------
VIPR ID created                                          |  Yellow   |  Confusion about "IDs" (VIPR ID, VASI ID, etc.) 
VIPR workbook (tab for cloud) 100% completed              |     | Ken/Intake has not deployed this yet
EPMO IA analysis completed                               |      | Rushika's team just starting this; unsure of what this is
ECSO wave migration designated                        | Yellow    |unsure of wave designation; wasn't in place yet
EPMO PM assigned                                      | Complete     | Jonathan Lindow
Confirmed adequate funding and resources in place for migration based on ROM     | Complete     | Funded at the portfolio level
Decision finalized: migrate to cloud, decommission obsolete / duplicate system, or waiver (stay as is)       | Complete| 
CAS architecture review completed (proposed plan to refactor, rearchitect, etc.)              |      | in progress
Approved architecture by ITOPs                          |      | 
Intake checklist 100% completed                          |      |  Checklist in development by CAS                                      
COMPLETED ALL OIT Intake Tasks                           | Yellow     | process question about Unified Intake and VIPR process for projects that are part of larger VA portfolios (FMBT)

### ECSO / VAEC Detailed Migration Planning 
Task                                              | Status    | Comments (only if yellow or red)
------------                                      | --------- | ------------- 
ISSO assigned                                     |  Complete        | Joe Fourcade and Lee Zierbel ECSO ISSO; Leigh Taylor ISSO
Application workload and compute / network requirements documented       | Complete  |
ITOPs (Chris) validates workload compute / network requirements                 | N/A      |B2B tool
Confirmed RACI and roles (per the CONOPS)                                |       |
CSP selection criteria (analysis for AWS versus Azure)                 | Complete      | MAG
Support contracts for application teams awarded (as needed) / resource onboarding completed  | Complete   |                   
Cloud credits purchased (expire at end of contract)        | Complete      | 924 credits purchased 
ATO plan started (inherited controls, documentation, etc.) ; entered GRC tool (Risk Vision Working Group)    | Complete   |IFAM ATO Sept / Oct 2018
ESCCB decisions completed (if applicable)         | Red      | Blocker; was previously online now manual; process is broken (forms don't exist, missing documentation, no guidance on how to fill out forms. need a list of connection IDs, need examples)
SLAs for applications defined and approved                 | Yellow   |They have application levels SLAs, but they need to know the MAG SLAs
SLAs for operations defined and approved with ITOPs        | Yellow      | See note above
CSP accounts and sub accounts created                 | Complete | Sub account of FBMT
CD1 decision made                                   |  Green     | In progress; aligning with IFAMS
Planning checklist 100% completed                 |  No     |Checklist in development by CAS
COMPLETED ALL Migration Planning and Onboarding Tasks                 | Red   | Blocker ESCCB decision


### Provisioning
Task                                                    | Status    | Comments (only if yellow or red)
------------                                            | --------- | ------------- 
ATO actions started; must demonstrate progress                 | Yellow      | Need consistent info; VAEC, cloud ISO group, IA, and other security groups provide different, sometimes conflicting informatin. 
Apps code assigned in coordination with ITOPs                 | Red    | Issue with ITOPs and getting a VASI ID for NSD system
Identify and apply tagging and billing                 | Complete    | 
Dev/Test/Staging/Prod environment set up completed                 | Yellow      | Resource groups for environment are set up blocked on setting up VMs (can't do backups themselves, MS team trying to solve but unable to date, etc)
Provided inherited controls from CSP                 |Yellow  | Might be complete (IFAMS team would know) need better documentation
Operational security tools onboarding completed                 |       | 
Billing and reporting set up                           | Red     | Power BI reporting tool VA needs to request access; no access to reports yet; would like visibility into the process (credits used, consumption rate)
Team has access to all required tools and environments               | Red      | Hurting productivity; have access tools but not active directory portion (IO controlling; VA teams used to have access control but no longer)
Working session to complete operations handoff with ITOPs                 |       | 
Provisioning checklist 100% completed                 |  No     | Checklist in development by CAS
COMPLETED ALL Provisioning Tasks                 | Yellow      | (Need to validate this section w/ Johnny)



### BUILD OUT, OPERATIONS HANDOFF, & CUTOVER
Task                                                    | Status    | Comments (only if yellow or red)
------------                                            | --------- | ------------- 
Application team environment, configuration and build out complete      |  Yellow     | Access to POC environment; duplicate work as a result of access issues
Change management and comms plan approved (incl. VA training requirements)                |       | 
All testing cheklists have been completed / met acceptance criteria (security and operations)                |       | 
ECSSB decisions complete (if applicable               | Red      | Validate with Johnny
Monitoring tools in place                |       | 
Decommission plan approved                |       | 
ATO approved                |       | 
Operations handoff completed (per ATO approval)                |       | 
EPMO / Application PM role handoff completed (e.g, CSP account set up, etc.)                |       | 
Validate Disaster Recovery (DR) and Backup                |       | 
CD2 decision                |       | Date:
Build out and cutover checklist 100% complete                |       | 
COMPLETED ALL Build Out and Cutover Tasks                   | Red      |  


### Cloud Operations
Task                                                    | Status    | Comments (only if yellow or red)
------------                                            | --------- | ------------- 
Go-live / production              |       | 
Go live operational kickoff with ITOPs              |       | 
Closeout session with Risk Vision working group              |       | 
ECSO ongoing governing / operational processes in place (per plan)              |       | 
Validation that all SLAs being met              |       | 
Continuous monitoring of security, compute usage, performance, availability, etc. fully operational              |       | 
Complete any outstanding contract actions (including cancellations, mods, etc.)              |       | 
Implemented operational RACIs with VA staff              |       | 
Begin decommission plan tasks              |       | 
100% post-cutover checklist completed              |       | 
COMPLETED ALL Operations Tasks              |       | Checklist in development by CAS

### Retire / Decommission Legacy System
Task                                                    | Status    | Comments (only if yellow or red)
------------                                            | --------- | ------------- 
Systems identified as obsolete are retired and decommissioned immediately            |       | 
Contracts modified or cancelled            |       | 
Cost savings report delivered            |       | 
Archiving completed / data transferring completed            |       | 
100% ITOPs decommission checklist completed            |       | Checklist in development by CAS
COMPLETED ALL Decommission Tasks              |       | 

