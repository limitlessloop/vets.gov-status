# Name: Digital Veterans Platform (AWS)

Business and Application Owers:  Shamen Singh Drew Myklegard

Migrate to Cloud: Yes

Cutover Completed: Yes



### (Pre-Intake) Modernization and Decommission Planning
Task                                              | Status   | Comments (only if yellow or red)
------------                                      | -------- | ------------- 
Identify VA application owner                    | Complete  |  Dr. Shamen Singh (Business Owner) Drew Myklegard (Application Owner) Tim Robinson PM 
Initial cloud suitability 6 questions completed   |  No    | Early migration; not yet deployed
ITOPs to review if "obsolete" system based on usage     | Complete    | New system was approved by ITOPs
ECSO Migration wave planning started              | Complete    |  Wave 1
Baseline costs (pre-cloud) documented             |  N/A    | No baseline (pre-cloud) costs because this is a new system
Validated ACTIVE users / traffic analytics for past 12 months   | Complete    | 100,000 estimated users projected for steady state; no users at this time; planning to onboard users in spring 2019
ROM and funding information provided (e.g., UFR, research vs. OIT dollars, etc. | Complete     | Yes funded for cloud for FY18 OIT dollars; not complete for FY19
VIPR Epics completed                              | Complete     | 
Routing tab in VIPR workbook completed            | No    | Early migration; intake workbook not yet deployed
100% complete pre-intake checklist                |  No   | Checklist under development by CAS; not yet available 
COMPLETED ALL (PRE Intake) Tasks                  | Complete   | Early migration; many ECSO processes, tools, and exit criteria not yet in place.

### OIT Unified Intake (VIPR)
Task                                                          | Status   | Comments (only if yellow or red)
------------                                                  | -------- | -------------
VIPR ID created                                         |   Complete   | V17-01347-000
VIPR workbook (tab for cloud) 100% completed              | No     | Early migration; workbook not yet deployed.
EPMO IA analysis completed                          | Green     | Confirmed they worked with Rushika's team, but not clear on the output or artivact of this work.
ECSO wave migration designated                      |   Complete   | Wave 1
EPMO PM assigned                                     |  Complete    | Tim Robinson
Confirmed adequate funding and resources in place for migration based on ROM       | Complete   | no ROM; funding for FY18 complete (OIT dollars); need funding FY19; need to know what project team will fund and what ECSO will fund
Decision finalized: migrate to cloud, decommission obsolete / duplicate system, or waiver (stay as is)    | Complete     | 
Architecture review completed (proposed plan to refactor, rearchitect, etc.)        | Complete     | completed with Osama Lel-Zorkani (ITOPs)
Approved architecture by ITOPs              |  Complete    | Chris Cardella's team to do; CAS to coordinate with Chris
Intake checklist 100% completed               | No     | Checklist under development by CAS; not yet available                                       
COMPLETED ALL OIT Intake Tasks                 | Complete     | This platform supports API development and deployment; for internal and external users.

### ECSO / VAEC Detailed Migration Planning 
Task                                              | Status    | Comments (only if yellow or red)
------------                                      | --------- | ------------- 
ISSO assigned                                     | Complete | Charles Solomon-Jackson
Application workload and compute / network requirements documented       | Complete      | All docs are in DVP Sharepoint portal.
ITOPs (Chris) validates workload compute / network requirements                 |  Yellow     | Unsure if applicable given this is a new system?
Confirmed RACI and roles (per the ECSO CONOPS)                 | Yellow    | ECSO CONOPS currently being updated; some questions about what project teams will do vs. ECSO.
CSP selection criteria (analysis for AWS versus Azure)          |  No    | Early migration; not yet implemented
Support contracts for application teams awarded (as needed) / resource onboarding completed | Complete   |   Liberty IT, Mulesoft, CGS are support vendors               
Cloud credits purchased (do not expire)                 |   Complete    |
ATO plan started and entered GRC tool                | Complete      |
Decommission plan completed (incl. contracting, security, etc.)               |   NA    | Not applicable because new system
SLAs for applications defined and approved                 | Yellow     | using AWS SLAs; unsure if application level SLAs are needed; also unsure of exactly what AWS SLAs include 
SLAs for operations defined and approved with ITOPs        |  No     | see note above
CSP accounts and sub accounts created                 | Complete    | 
CD1 decision made                                   | Complete      | Date: June 30, 2017
Planning checklist 100% completed                 | No      | Checklist under development by CAS; not yet available
COMPLETED ALL Migration Planning and Onboarding Tasks        | Complete    | 


### Provisioning
Task                                                    | Status    | Comments (only if yellow or red)
------------                                            | --------- | ------------- 
ATO actions started; must demonstrate progress          | Complete      | ATO approved 8.16.18
Apps code assigned in coordination with ITOPs           | Complete      |
Identify and apply tagging and billing                 |  Complete     | 
Dev/Test/Staging/Prod environment set up completed     | Complete      | 
Provided inherited controls for CSP                    | Complete      | 
Operational security tools onboarding completed          |Complete  | 
Billing and reporting set up                          | Complete     | 
Team has access to all required tools and environments          |  Complete   | 
Working session to complete operations handoff with ITOPs                 |  No     | Unclear what ITOPs role is for new systems
Provisioning checklist 100% completed                 |  No     | Checklist under development by CAS; not yet available
COMPLETED ALL Provisioning Tasks                       | Complete     | 



### BUILD OUT, OPERATIONS HANDOFF, & CUTOVER
Task                                                    | Status    | Comments (only if yellow or red)
------------                                            | --------- | ------------- 
Application team environment, configuration and build out complete           | Complete      | 
Change management and comms plan approved (incl. VA training requirements)    |       | 
ECSSB decisions / tasks completed if applicable for connections         |  Complete     | ATO completed 8.16.18
Monitoring tools in place                | Complete      | 
Decommission plan approved                |  N/A     | not applicable b/c new system stood up in AWS
ATO approved                           |  Complete     | 8.16.18 Handoff planned for next summer
Operations handoff completed (per ATO approval)                | N/A      | New system
CD2 decision                                 |       | Date: March 2018
Build out and cutover checklist 100% complete                | No      | Checklist under development by CAS; not yet available
COMPLETED ALL Build Out and Cutover Tasks                   | Complete    | PATS-R Integration project is already migrated; larger rollout to 6-8 projects planned  spring 2019


### Cloud Operations
Task                                                    | Status    | Comments (only if yellow or red)
------------                                            | --------- | ------------- 
Go-live / production              |  Complete    | Has been cutover to production, but only a few users planned until Spring/Summer 2019
Go live operational kickoff with ITOPs              |   No    | is this applicable? Does ITOPS have role on this applicaiton?
Closeout session with Risk Vision working group              | Green      | ATO just completed 8/16/18
ECSO ongoing governing / operational processes in place              | Yellow      | Need to define roles and processes for operation
Validation that all SLAs being met              |Yellow       | Are there application-level SLAs other than infrastructure (AWS) that need to be defined? Would like to see the AWS SLAs.
Continuous monitoring of security, compute usage, performance, availability, etc. fully operational   | Green      | AWS does this
Complete any outstanding contract actions (including cancellations, mods, etc.)         |  N/A     | 
Implemented operational RACIs with VA staff              |       | 
Begin decommission plan tasks              |  N/A     | Not applicable
100% post-cutover checklist completed              | No      | Checklist under development by CAS; not yet available
COMPLETED ALL Operations Tasks              | Yellow     | Unsure about funding for FY19; application SLA's need to be developed.

### Retire / Decommission Legacy System
Task                                                    | Status    | Comments (only if yellow or red)
------------                                            | --------- | ------------- 
Systems identified as obsolete are retired and decommissioned immediately            |       | 
Contracts modified or cancelled            |       | 
Cost savings report delivered            |       | 
Archiving completed / data transferring completed            |       | 
100% ITOPs decommission checklist completed            |       | 
COMPLETED ALL Decommission Tasks              | N/A      | Not applicable (new system in AWS)

