# Name: VBMS Track 1 Document Upload Transition (AWS)

Business and Application Owners: Kenneth Wimsatt, Gary Dameron

Migrate to Cloud: Yes

Cutover Completed: 



### (Pre-Intake) Modernization and Decommission Planning
Task                                              | Status   | Comments (only if yellow or red)
------------                                      | -------- | ------------- 
Identify VA application owner                     |  Complete     | Gary Dameron is System Owner; Kenneth Winsat is business owner; PM for migration Dwayne Wirfel. 
Initial cloud suitability 6 questions completed   |  No     | Early migration; not yet deployed
ITOPs to review if "obsolete" system based on usage   |  Complete   | 
ECSO Migration wave planning started              | Complete   |  Wave 2
Baseline costs (pre-cloud) documented             |  Complete   | Need to refine baseline costs to calculate accurate cost savings; some cost analysis already completed
Validated ACTIVE users / traffic analytics for past 12 months   |      |
ROM and funding information provided (e.g., UFR, research vs. OIT dollars, etc. | Complete     | Cost analysis for IBM 
VIPR Epics completed                              |      | VBMS has VIPR; but did not go through a specific process for migration
Routing tab in VIPR workbook completed            |    | Did not go through VIPR; does info need to be entered?
100% complete pre-intake checklist                |  N/A    | Checklist in development by CAS
COMPLETED ALL (PRE Intake) Tasks                  | Complete | This track 1 is specific to VBMS data migration out of Terremark using AWS snowball.

### OIT Unified Intake (VIPR)
Task                                          | Status   | Comments (only if yellow or red)
------------                                 | -------- | -------------
VIPR ID created                               | Yellow     | No VIPR ID found
VIPR workbook (tab for cloud) 100% completed   |  No    | Early migration; not deployed yet.
EPMO IA analysis completed              | Yellow     | Unsure what this is
ECSO wave migration designated              |Complete      | Wave 2
EPMO PM assigned              |  Complete    | Gary Dameron 
Confirmed adequate funding and resources in place for migration based on ROM              |Complete      | 
Decision finalized: migrate to cloud, decommission obsolete / duplicate system, or waiver (stay as is)     | Complete     | 
Architecture review completed (proposed plan to refactor, rearchitect, etc.)          | Green     | in progress; Checking if TIC can handle bandwidth; architecture adjustments are small.
Approved architecture by ITOPs              | N/A   | ITOPS not involved in architecture
Intake checklist 100% completed               | No    | Checklist in development by CAS                                       
COMPLETED ALL OIT Intake Tasks                 | Complete   | No VIPR ID referenced in ECSO tracker

### ECSO / VAEC Detailed Migration Planning 
Task                                              | Status    | Comments (only if yellow or red)
------------                                      | --------- | ------------- 
ISSO assigned                                      |  Complete    | James Boring and Eguardo Rivera
Application workload and compute / network requirements documented    | Complete  |Confirm with Dwayne
ITOPs (Chris) validates workload compute / network requirements       |       | Unsure; not sure if this is relevant
Confirmed RACI and roles                            | Green      | Gary and Dwayne are managing the four tracks; Gary is backup 
CSP selection criteria (analysis for AWS versus Azure)        | Complete       | AWS
Support contracts for application teams awarded (as needed) / resource onboarding completed (GFE, PIV, VA account set up, etc.) |  Complete  |                  
Cloud credits purchased (do not expire)                 | Complete   |
ATO plan started (inherited controls, documentation, etc.) ; entered GRC tool (Risk Vision Working Group)  |  Complete     | ATO for production for 150; ATO for test not required
Decommission plan completed (incl. contracting, security, etc.)        | N/A      |  Not part of this track of work.
SLAs for applications defined and approved                 | Complete      | SLAs with the business
SLAs for operations defined and approved with ITOPs        | Complete      |
CSP accounts and sub accounts created                 |Complete     | 
CD1 decision made                                   |N/A       | Not relevant for this track of work
Planning checklist 100% completed                 | No      | Checklist in development by CAS
COMPLETED ALL Migration Planning and Onboarding Tasks     |  Green     | 


### Provisioning
Task                                                    | Status    | Comments (only if yellow or red)
------------                                            | --------- | ------------- 
ATO actions started; must demonstrate progress          |  Complete     | 
Apps code assigned in coordination with ITOPs           | Yellow      | Unsure what this is? Need info from ITOPS.
Identify and apply tagging and billing                  | Green      | In progress VAEC ID tag set up; unsure what has been provisioned.
Dev/Test/Staging/Prod environment set up completed       | Green      | In progress; no blockers
Provided inherited controls for CSP                      |  Complete     | 
Operational security tools onboarding completed          | Green       | Early stages of this work
Billing and reporting set up                             | Complete    | 
Team has access to all required tools and environments                 |  Green     | In progress; unsure of comprehensive tools
Working session to complete operations handoff with ITOPs         | Yellow     | Don't work w/ ITOPs; unsure of role if ITOPs for migration.
Provisioning checklist 100% completed                 |  No     | Checklist in development by CAS
COMPLETED ALL Provisioning Tasks                 | Yellow    | Need clarity of ITOPs role here (if any)



### BUILD OUT, OPERATIONS HANDOFF, & CUTOVER
Task                                                    | Status    | Comments (only if yellow or red)
------------                                            | --------- | ------------- 
Application team environment, configuration and build out complete        |  Green     | In progress
Change management and comms plan approved (incl. VA training requirements)    | N/A      | Not applicable
ESCCB decisions complete (if applicable)                |  Green     | In progess
Monitoring tools in place                |   Green    | In progress; depends on what AWS offers
Decommission plan approved                |       | relevant, but not started yet
ATO approved                | Green      | 150 day ATO (Jan 2019); 45 days prior to end new authorization starts
Operations handoff completed (per ATO approval)                |       | 
EPMO / Application PM role handoff completed (e.g, CSP account set up, etc.)             |Complete       | Gary and Dwayne
Validate Disaster Recovery (DR) and Backup                |       | 
CD2 decision                | N/A      | Not relevant
Build out and cutover checklist 100% complete                |       | Checklist in development by CAS
COMPLETED ALL Build Out and Cutover Tasks                   | Red  | VBMS be out of IBM/Terremark by March 2019 (not end of calendar year 2018)


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
100% post-cutover checklist completed              |       | Checklist in development by CAS
COMPLETED ALL Operations Tasks              |      | 

### Retire / Decommission Legacy System
Task                                                    | Status    | Comments (only if yellow or red)
------------                                            | --------- | ------------- 
Systems identified as obsolete are retired and decommissioned immediately            |       | 
Contracts modified or cancelled            |       | 
Cost savings report delivered            |       | 
Archiving completed / data transferring completed            |       | 
100% ITOPs decommission checklist completed            |       | Checklist in development by CAS
COMPLETED ALL Decommission Tasks              |      | 

