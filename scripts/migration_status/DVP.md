# Name: Digital Veterans Platform (AWS)

Business and Application Owers:  Drew Myklegard 

Migrate to Cloud: Yes

Cutover Completed: Yes



### (Pre-Intake) Modernization and Decommission Planning
Task                                              | Status   | Comments (only if yellow or red)
------------                                      | -------- | ------------- 
Identify VA application owner                    | Complete  |  Dr. Shamen Singh (Business Owner) Drew Myklegard (Application Owner) Tom Robinson PM 
Initial cloud suitability 6 questions completed   |  N/A    | Ken/Intake team have not yet deployed these in VIPR intake process
ITOPs to review if "obsolete" system based on usage     | N/A     | New system was approved by ITOPs
ECSO Migration wave planning started              | Complete    |  Wave 1
Baseline costs (pre-cloud) documented             |  N/A    | No baseline (pre-cloud) costs because this is a new system
Validated ACTIVE users / traffic analytics for past 12 months   | Complete    | 100,000 users projected and provided to ECSO in steady state; no users at this time
ROM and funding information provided (e.g., UFR, research vs. OIT dollars, etc. | Complete     | Yes funded for cloud for FY18 OIT dollars; not complete for FY19
VIPR Epics completed                              | Complete     | confirm w/ Tim
Routing tab in VIPR workbook completed            | N/A     | Team began work before Ken/Intake team deployed workbook
100% complete pre-intake checklist                |  N/A    | Checklist under development by CAS; not yet available 
COMPLETED ALL (PRE Intake) Tasks                  | Complete   | Usage data needed; confirm what is VA / user demand for this system

### OIT Unified Intake (VIPR)
Task                                                          | Status   | Comments (only if yellow or red)
------------                                                  | -------- | -------------
VIPR ID created               |   Complete   | V17-01347-000
VIPR workbook (tab for cloud) 100% completed              | N/A     | Workbook not yet deployed / available by Ken/Intake team.
EPMO IA analysis completed              | Green     | Confirmed workign with Rushika's team; need to confirm with Ruchika if an IA analysis was completed
ECSO wave migration designated              |   Complete   | Wave 1
EPMO PM assigned              |  Complete    | Tim Robinson
Confirmed adequate funding and resources in place for migration based on ROM              | Complete   | no ROM; funding for FY18; need funding FY19; need to know what project team will fund and what ECSO will fund
Decision finalized: migrate to cloud, decommission obsolete / duplicate system, or waiver (stay as is)         | Complete     | 
CAS architecture review completed (proposed plan to refactor, rearchitect, etc.)        | Complete     | worked with ITOPS; completed Osama Lel-Zorkani (ITOPs)
Approved architecture by ITOPs              |      | Chris Cardella's team to do; CAS to coordinate with Chris
Intake checklist 100% completed               | N/A     | Checklist under development by CAS; not yet available                                       
COMPLETED ALL OIT Intake Tasks                 | Complete     | Need to make sure project is APPROVED

### ECSO / VAEC Detailed Migration Planning 
Task                                              | Status    | Comments (only if yellow or red)
------------                                      | --------- | ------------- 
ISSO assigned                                     | Complete | Charles Solomon-Jackson
Application workload and compute / network requirements documented       | Complete      | All docs DVP Share portal; ECSO does not require this of all project teams
ITOPs (Chris) validates workload compute / network requirements                 |       | 
Confirmed RACI and roles (per the CONOPS)                 | Complete      | 
CSP selection criteria (analysis for AWS versus Azure)                 |  NA     | Not yet implemented
Support contracts for application teams awarded (as needed) / resource onboarding completed (GFE, PIV, VA account set up, etc.) | Complete   |   Liberty IT, Mulesoft, CGS               
Cloud credits purchased (do not expire)                 |   Complete    |
ATO plan started (inherited controls, documentation, etc.) ; entered GRC tool (Risk Vision Working Group)   | Complete      |
Decommission plan completed (incl. contracting, security, etc.)               |   NA    | Not applicable because new system
SLAs for applications defined and approved                 | Complete      | using AWS SLAs 
SLAs for operations defined and approved with ITOPs        |       | 
CSP accounts and sub accounts created                 | Complete    | 
Release agent identified or waiver                 |       |
Sustainment organization identified                 |       |
CD1 decision made                 | Complete      | Date: June 30, 2017
Planning checklist 100% completed                 |       | Checklist under development by CAS; not yet available
COMPLETED ALL Migration Planning and Onboarding Tasks                 | Complete    | 


### Provisioning
Task                                                    | Status    | Comments (only if yellow or red)
------------                                            | --------- | ------------- 
ATO actions started; must demonstrate progress          | Complete      | ATO approved 8.15.18
Apps code assigned in coordination with ITOPs           | Complete      |
Identify and apply tagging and billing                 |  Complete     | 
Dev/Test/Staging/Prod environment set up completed     | Complete      | 
Provided inherited controls for CSP                    | Complete      | 
Operational security tools onboarding completed          |Complete  | 
Billing and reporting set up                          | Complete     | 
Team has access to all required tools and environments                 |  Complete   | 
Working session to complete operations handoff with ITOPs                 |       | 
Provisioning checklist 100% completed                 |       | Checklist under development by CAS; not yet available
COMPLETED ALL Provisioning Tasks                       | Complete     | 



### BUILD OUT, OPERATIONS HANDOFF, & CUTOVER
Task                                                    | Status    | Comments (only if yellow or red)
------------                                            | --------- | ------------- 
Application team environment, configuration and build out complete           | Complete      | 
Change management and comms plan approved (incl. VA training requirements)    |       | Operations planning
All testing cheklists have been completed / met acceptance criteria (security and operations)     | Complete      | 
Cutover checklist approved                |       | do teams use a checklist? is this applicable for a new sytem in cloud? would it be helpful?
Monitoring tools in place                | Complete      | specific tools for DVP?
Decommission plan approved                |  N/A     | not applicable b/c new system stood up in AWS
ATO approved                |  Complete     | 8.15.18 Handoff planned for next summer
Operations handoff completed (per ATO approval)                | Green      | 
EPMO / Application PM role handoff completed (e.g, CSP account set up, etc.)        |       | is this applicable?
Validate Disaster Recovery (DR) and Backup                |  Complete     | part of ATO; (can this be deleted--is it already covered in ATO?)
CD2 decision                                 |       | Date: March 2018
Build out and cutover checklist 100% complete                |       | Checklist under development by CAS; not yet available
COMPLETED ALL Build Out and Cutover Tasks                   | Green     |  


### Cloud Operations
Task                                                    | Status    | Comments (only if yellow or red)
------------                                            | --------- | ------------- 
Go-live / production              |  Complete    | No users yet
Go live operational kickoff with ITOPs              |       | is this applicable? Does ITOPS have role on this applicaiton?
Closeout session with Risk Vision working group              |       | 
ECSO ongoing governing / operational processes in place              |       | ? ESCO - what is this process?
Validation that all SLAs being met              |       | are there SLAs other than AWS ones? how are these being monitored and reported to VA?
Continuous monitoring of security, compute usage, performance, availability, etc. fully operational   |       | AWS does this?
Complete any outstanding contract actions (including cancellations, mods, etc.)         |       | 
Implemented operational RACIs with VA staff              |       | 
Begin decommission plan tasks              |  N/A     | Not applicable
100% post-cutover checklist completed              |       | Checklist under development by CAS; not yet available
COMPLETED ALL Operations Tasks              | Green     | 

### Retire / Decommission Legacy System
Task                                                    | Status    | Comments (only if yellow or red)
------------                                            | --------- | ------------- 
Systems identified as obsolete are retired and decommissioned immediately            |       | 
Contracts modified or cancelled            |       | 
Cost savings report delivered            |       | 
Archiving completed / data transferring completed            |       | 
100% ITOPs decommission checklist completed            |       | 
COMPLETED ALL Decommission Tasks              |       | Not applicable (new system in AWS)

