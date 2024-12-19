Manage software project
=======================

.. section::
    :layout-type: two_right_sidebar

    .. panel::
        :title: ITO.02.42.05.01.01 MANAGE SOFTWARE PROJECT
        :titlecolor: #2471A3
        :bordercolor: #2471A3

        <h3><strong>PROCESS STEP DESCRIPTION</strong></h3>

        The 'Manage software project' process step includes the typical project management aspects of any project, like setting up the project management plan, defining and monitoring schedules, resources, risks and opportunities, managing stakeholders and suppliers, performing regular project status reports etc.
        <p></p>
        Within this process step also the project method is decided on and maintained, e.g. whether an agile or a test-driven software development approach is chosen.
        
        <h3><strong>PROCESS STEP OBJECTIVES</strong></h3>
        The process objectives are derived from the norms and standards, this process step is compliant to (see 'Regulations' box for details). Achievement of the process objectives is monitored based on controls (see 'Controls' box for details).
        

        .. expand::
            :title: Click here to expand...

            .. tablemacro::
                :header:
                    - ID
                    - Objective
                
                - PM_OBJ.1
                * To define the approach to planning progress, managing required resources, scheduling activities and monitoring project achievements.

                - PM_OBJ.2
                * To define project objectives, project constraints and project scope.
                
                - PM_OBJ.3
                * To prove feasibility of achieving the objectives of the project with available resources and the given constraints
                
                - PM_OBJ.4
                * To estimate the expected effort and cost to derive the amount of required resources.
                
                - PM_OBJ.5
                * To assign all relevant roles to project team members to cover the responsibilities for all relevant activities and to assure that the assignees have the skills required for the roles assigned to them.
                
                - PM_OBJ.6
                * To define interfaces, dependencies and interaction between involved parties.
                
                - PM_OBJ.7
                * To schedule project activities with clear responsibilities assigned to project team members across the complete project lifecycle and to refine the schedule to more detailed levels as progress is made.
                
                - PM_OBJ.8
                * To adjust schedules if they can systematically not be implemented as planned.
                
                - PM_OBJ.9
                * To implement the defined approach to identifying, analysing and prioritizing risks and deriving appropriate mitigation measures.
                
                - PM_OBJ.10
                * To track mitigation measures to managed risks to closure.
                
                - PM_OBJ.11
                * To define project management reports and to provide these reports at pre-defined intervals and whenever needed.
                
                - PM_OBJ.12
                * To monitor project progress against project objectives and project schedules.
                
                - SM_OBJ.1
                * To define interactions with and dependencies to (including the exchange of work products and information between all parties involved) suppliers for development activities.
                
                - SM_OBJ.2
                * To establish and maintain an agreement on joint processes, responsibilities and interfaces.
                
                - SM_OBJ.3
                * To review the technical development with the supplier and the progress regarding schedule, quality, and cost.
                
                - SM_OBJ.4
                * To monitor progress of project partners and to perform or supervise corrective actions mitigating deviations from schedule or expected quality.
                
                - SM_OBJ.5
                * To define supplier monitoring reports and to provide these reports at pre-defined intervals and whenever needed.
                
                - TrM_OBJ.1
                * To enable and to manage traceability and consistency checks between the different elements of the technical specifications and to achieve agreement that it is appropriate and complete.
                
    Break

    .. panel::
        :title: RESPONSIBILITIES
        :titlecolor: #707B7C
        :bordercolor: #707B7C

        .. user-profile::
            :profile_title: PROCESS OWNER
            :username: marinasastierstorfer

        <hr />

        .. user-profile::
            :profile_title: PROCESS MANAGER
            :username: thomasdonner

.. section::
    :layout-type:

    .. panel:: 
        :title: (i) TOOLS
        :titlecolor: #2471A3
        :bordercolor: #2471A3

        .. expand::
            :title: Click here for details

            <strong><h3>SW Factory tools</h3></strong>

            .. bulletlist::

                JIRA (CodeCraft):  .. link:: title=Tool address=https://cc.bmwgroup.net/ | .. link:: title=Access address=https://cc.bmwgroup.net/ | .. link:: title=Manual address=https://cc.bmwgroup.net/ 
            
            <strong><h3>Other tools</h3></strong>

            .. bulletlist::

                iP3: .. link:: title=Tool address=https://cc.bmwgroup.net/ | Access | Manual
                    
    Break

    .. panel:: 
        :title: (*r) REGULATIONS
        :titlecolor: #2471A3
        :bordercolor: #2471A3

        .. expand::
            :title: Click here for details

            <strong><h3>ASPICE PAM3.1</h3></strong>

            .. bulletlist::

                ACQ.4
                MAN.3
                MAN.5
                SUP.1
                SUP.10
                SWE.1-6
            
            <strong><h3>ISO 26262:2018</h3></strong>

            .. bulletlist::

                ISO 26262-2, Clause 5
                ISO 26262-2, Clause 6
                ISO 26262-6, Clause 6
                ISO 26262-8, Clause 5
                ISO 26262-8, Clause 9

    Break

    .. panel:: 
        :title: (off) METHODS
        :titlecolor: #2471A3
        :bordercolor: #2471A3

        .. expand::
            :title: Click here for details

            .. content-by-label::
                :label: esdf_methods_project_management
                :space: ESDFDEV

    Break
    
    .. panel::
        :title: (*y) GOOD &amp; BAD PRACTICES
        :titlecolor: #2471A3
        :bordercolor: #2471A3

        .. expand::
            :title: Click here for details

            
.. panel::
    :title: (/) CONTROLS
    :titlecolor: #2471A3
    :bordercolor: #2471A3

    The following controls must be performed as they are the basis for the overall project KPIs to be reported.

    .. expand::
        :title: Click here for details:

        .. tablemacro::
            :header:
                - ID
                - Control
                - Target Purpose
                - Relationship to objectives
                - Frequency
                - Calculation Measurement
                - Evaluation
                
            - <strong>PM_CON.1</strong>
            * <b>Project management approach</b>
            * Ensure the .. link:: title=Project Management Plan address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Project+Management+Plan+Description document (incl. supplier management) has been reviewed and any findings from reviews have been mitigated within 12 weeks after the review. <p></p>Reviews of the .. link:: title=Project Management Plan address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Project+Management+Plan+Description document must be conducted as follows:
            -- Before milestone   G2 "Project setup confirmed"  (see:  .. link:: title=Defining the project lifecycle address=https://confluence.cc.bmwgroup.net/display/esdfdev/Defining+the+project+lifecycle ):Anytime the project management plan is determined to be in a reviewable state, yet latest at the milestone G2.
            -- After milestone G2 "Project setup confirmed" (see:  .. link:: title=Defining the project lifecycle address=https://confluence.cc.bmwgroup.net/display/esdfdev/Defining+the+project+lifecycle ):Reviews must be repeated each time the plan document is changed  content wise  (e.g. not after correction of spelling /  grammar errors or broken links).
            * PM_OBJ.1, PM_OBJ.2, PM_OBJ.5, PM_OBJ.6, PM_OBJ.9, SM_OBJ.1
            * At least once per software release cycle (e.g., in the context of each i-step's SAb milestone).
            * X = Depending on all unmitigated findings from all reviews:
            -- 0 if any review has not been conducted as described OR if the review at milestone G2 "Project setup confirmed" was not successful, meaning the review resulted in one or more findings.
            -- 1 if at least one unmitigated finding form any review  has been open for ≥ 12 weeks.
            -- 2 if all unmitigated findings from all reviews have been for open for 12 weeks.
            -- 3 if there are no unmitigated findings from any reviews.
            * Followed::
            -- .. status:: title=RED color=Red 
            -- To → Escalation to line management required.
            -- .. status:: title=YELLOW color=Yellow
            -- → Escalation to project management ( .. link:: title=Software Project Lead address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Project+Lead ) required.
            -- .. status:: title=GREEN color=Green

            - <strong>PM_CON.2</strong>
            * <b>Project management process adherence</b>
            * Ensure project management audits (incl. supplier monitoring) have been held.<p></p>Audits of the project management process must be conducted as follows:
            -- first audit between 6 and 10 months after project start, and
            -- at least a second audit between 6 and 12 months after the first audit, yet latest 8 months before SOP.
            * PM_OBJ.3, PM_OBJ.4, PM_OBJ.5, PM_OBJ.7, PM_OBJ.8, SM_OBJ.1, SM_OBJ.2, SM_OBJ.3, SM_OBJ.4, SM_OBJ.5
            * At least once per software release cycle (e.g., in the context of each i-step's SAb milestone).
            * X = Depending on all unmitigated findings from all audits:
            * Followed::
            -- .. status:: title=RED color=Red
            -- →  Escalation to line management required.
            -- .. status:: title=YELLOW color=Yellow
            -- →  Escalation to project management ( .. link:: title=Software Project Lead address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Project+Lead ) required.
            -- .. status:: title=GREEN color=Green

            - <strong>PM_CON.3</strong>
            * <b>Risk control</b>
            * Ensure mitigation measures for identified risks are closed in time.
            * PM_OBJ.10
            * At least once per software release cycle (e.g., in the context of each i-step's SAb milestone).
            * X = Depending on overdue mitigation measures to identified risks:
            -- 0 if a risk overview does not exist, is incomplete or outdated later than 12 weeks after project start.
            -- 1 if at least one mitigation measures is overdue.
            -- 2 if no mitigation measures is overdue.
            * Followed::
            -- .. status:: title=RED color=Red X = 0 → Escalation to line management required.
            -- .. status:: title=YELLOW color=Yellow → Escalation to project management ( .. link:: title=Software Project Lead address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Project+Lead ) required.
            -- .. status:: title=GREEN color=Green

            - <strong>PM_CON.4</strong>
            * <b>Project status reporting</b>
            * Ensure a .. link:: title=Project Status Report address=https://confluence.cc.bmwgroup.net/display/esdfdev/Project+Status+Report+Description for the latest reporting period (as of frequency) is available and complete.
            * PM_OBJ.11, PM_OBJ.12
            * At least once per software release cycle (e.g., in the context of each i-step's SAb milestone).
            * X = Availability and completeness of the .. link:: title=Project Status Report address=https://confluence.cc.bmwgroup.net/display/esdfdev/Project+Status+Report+Description for the latest reporting period.
            -- 0 if the .. link:: title=Project Status Report address=https://confluence.cc.bmwgroup.net/display/esdfdev/Project+Status+Report+Description for the latest reporting period is not available.
            -- 1 if the .. link:: title=Project Status Report address=https://confluence.cc.bmwgroup.net/display/esdfdev/Project+Status+Report+Description for the latest reporting period is available but incomplete or contains outdated information.
            -- 2 if the .. link:: title=Project Status Report address=https://confluence.cc.bmwgroup.net/display/esdfdev/Project+Status+Report+Description for the latest reporting period is available, up-to-date and complete.
            * Followed::
            -- .. status:: title=RED color=Red X = 0 → Escalation to line management required.
            -- .. status:: title=YELLOW color=Yellow → Escalation to project management ( .. link:: title=Software Project Lead address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Project+Lead ) required.
            -- .. status:: title=YELLOW color=Yellow X = 2

            - <strong>TrM_CON.1</strong>
            * <b>Traceability management approach</b>
            * Ensure the approach to enable and manage traceability has been reviewed and any findings from reviews have been mitigated within 12 weeks after the review .<p></p>Reviews of the approach to enable and manage traceability must be conducted as follows:
            -- Before milestone   G2 "Project setup confirmed"  (see:  .. link:: title=Defining the project lifecycle address=https://confluence.cc.bmwgroup.net/display/esdfdev/Defining+the+project+lifecycle ):<p></p>Anytime the project management plan is determined to be in a reviewable state, yet latest at the milestone G2.
            -- After milestone G2 "Project setup confirmed" (see: .. link:: title=Defining the project lifecycle address=https://confluence.cc.bmwgroup.net/display/esdfdev/Defining+the+project+lifecycle ):<p></p>Reviews must be repeated each time the plan document is changed  content wise  (e.g. not after correction of spelling /  grammar errors or broken links).
            * TrM_OBJ.1
            * At least once per software release cycle (e.g., in the context of each i-step's SAb milestone).
            * X = Depending on all unmitigated findings from all reviews:
            -- 0 if any review has not been conducted as described OR if the review at milestone .. link:: title=G2 "Project setup confirmed" address=https://asc.bmwgroup.net/wiki/pages/tinyurl.action?urlIdentifier=e4wpKw was not successful, meaning the review resulted in one or more findings.
            -- 1 if at least one unmitigated finding form any review  has been open for ≥ 12 weeks.
            -- 2 if all unmitigated findings from all reviews have been for open for 12 weeks.
            -- 3 if there are no unmitigated findings from any reviews.
            * Followed::
            -- .. status:: title=RED color=Red → Escalation to line management required.
            -- .. status:: title=YELLOW color=Yellow 1 ≤ X ≤ 2  → Escalation to project management ( .. link:: title=Software Project Lead address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Project+Lead ) required .
            -- .. status:: title=GREEN color=Green 

        
**CORE Activities**

.. section::
    :layout-type:

    .. tablemacro::
        :header:
            - Activity 
            - 01. Define project.
            - 02. Instantiate processes.
            - 03. Schedule project.
            - 04. Monitor and maintain ongoing project.	
            - 05. Monitor supplier performance.	
            - 06. Report project progress and results.

        - <b>Description</b><p>The activity descriptions to the right only give a brief outline of the required process work in a project. For the complete and normative description refer to the project's plan documents.Activities do not have to be performed in sequential order.</p>
        * Define project scope, initial team and a rough timeline. Identify standards and norms which must be adhered to. Setup initial project timelines and milestones.<p></p>Refine and document supplier agreements and contracted supplier deliverables. Align supplier performance with project timelines.<p></p>Define the escalation approach for all potentially relevant forms of conflicts (e.g., conflicts between project delivery and quality management, conflicts with suppliers, ...)
        * Tailor the BMW ESDF processes to the project's needs. Provide a work product overview for the tailored process. Define project goals, process goals. Identify and specify corresponding KPIs measuring goal conformance.<p></p>Document tracing relationships and tracing implementation between software architectural elements, requirements and  development and verification artefacts.<p></p>Setup plan documents, specifying the approach to the various process areas (like configuration management, requirements engineering, etc.).<p></p>Check whether open source software is used in the project. If so, initiate the Open Source Software Process by obtaining Open Source Software General Approval.
        * Create an initial project schedule. Initiate ticket generation for the work products as they were tailored in the WPO. Lay down the strategy for schedule refinement through-out the project (e.g., agile methods for backlog refinement and sprint planning)
        * Monitor schedule adherence through-out the project lifecycle. In case of deviations: specify and agree on corrective actions (as defined in the escalation approach).
        * Monitor adherence of supplier performance with valid agreements and contractual documents. In case of deviations: specify and agree on corrective actions (as defined in the escalation approach).<p></p>Also, collect updates of agreed deliverables (e.g., Safety Manuals).
        * Conduct measurement of project-management-related KPIs. Relate observed versus expected progress. Summarize as a status report and communicate results.

        - <h3>Involved role</h3> colspan=7

        - <b>Roles</b><p></p>The roles to the right are the main roles involved in the activities. <p></p>There may be other roles involved, see the work product table below.
        * .. link:: title=Software Project Lead address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Project+Lead <br /><p></p> .. link:: title=Software Security Engineer address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Security+Engineer
        * .. link:: title=Software Configuration Manager address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Configuration+Manager <br /><p></p> .. link:: title=ECU_Software Requirements Manager address=https://confluence.cc.bmwgroup.net/display/esdfdev/ECU_Software+Requirements+Manager <br /><p></p> .. link:: title=Software Project Lead address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Project+Lead <br /><p></p> .. link:: title=Free and Open Source Project Manager address=https://confluence.cc.bmwgroup.net/display/esdfdev/Free+and+Open+Source+Project+Manager <br />
        * .. link:: title=Software Project Lead address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Project+Lead
        * .. link:: title=Software Project Lead address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Project+Lead
        * Project Partner<p></p> .. link:: title=Software Project Lead address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Project+Lead
        * .. link:: title=Software Project Lead address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Project+Lead

        - <h3>Relevant work products</h3> colspan=7

        - <p>Work products</p>The work products to the right are the main results of the activities. There may be additional relevant work products, see the work product table below.
        * Work products in project depot:
        -- .. link:: title=Software Project Management Plan address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Project+Management+Plan+Description
        -- .. link:: title=Supplier Management Plan address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Project+Management+Plan+Description <br /><p></p>Work products in other tools:
        -- .. link:: title=Supplier Selection Report address=https://confluence.cc.bmwgroup.net/display/esdfdev/Supplier+Selection+Report+Description
        -- .. link:: title=Supplier Agreements address=https://confluence.cc.bmwgroup.net/display/esdfdev/Supplier+Agreements+Description
        -- .. link:: title=Internal Interface Agreement address=https://confluence.cc.bmwgroup.net/display/esdfdev/Internal+Interface+Agreement+Description
        -- .. link:: title=Software Security Interface Agreement address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Security+Interface+Agreement+Description
        -- .. link:: title=Team Assignment List address=https://confluence.cc.bmwgroup.net/display/esdfdev/Team+Assignment+List+Description
        -- .. link:: title=Training Plan address=https://confluence.cc.bmwgroup.net/display/esdfdev/Training+Plan+Description
        -- .. link:: title=Risk and Opportunity List address=https://confluence.cc.bmwgroup.net/display/esdfdev/Risk+and+Opportunity+List+Description
        * Work products in other tools:
        -- .. link:: title=Software Project Management Plan address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Project+Management+Plan+Description
        -- .. link:: title=Supplier Management Plan address=https://confluence.cc.bmwgroup.net/display/esdfdev/Supplier+Management+Plan+Description <br/><p></p>Work products in other tools:
        -- .. link:: title=Work Product Overview address=https://confluence.cc.bmwgroup.net/display/esdfdev/Work+Product+Overview+Description
        -- .. link:: title=Traceability Concept address=https://confluence.cc.bmwgroup.net/display/esdfdev/Traceability+Concept+Description
        -- .. link:: title=Open Source Software General Approval address=https://confluence.cc.bmwgroup.net/display/esdfdev/Open+Source+Software+General+Approval+Description
        * Work products in other tools: 
        -- .. link:: title=Project Schedule address=https://confluence.cc.bmwgroup.net/display/esdfdev/Project+Schedule+Description
        * Work products in other tools:
        -- .. link:: title=Project Status Report address=https://confluence.cc.bmwgroup.net/display/esdfdev/Project+Status+Report+Description
        -- .. link:: title=Supplier Management Status Report address=https://confluence.cc.bmwgroup.net/display/esdfdev/Supplier+Management+Status+Report+Description
        -- .. link:: title=Risk and Opportunity List address=https://confluence.cc.bmwgroup.net/display/esdfdev/Risk+and+Opportunity+List+Description
        -- .. link:: title=Project Schedule address=https://confluence.cc.bmwgroup.net/display/esdfdev/Project+Schedule+Description
        -- .. link:: title=Team Assignment List address=https://confluence.cc.bmwgroup.net/display/esdfdev/Team+Assignment+List+Description
        -- .. link:: title=Training Plan address=https://confluence.cc.bmwgroup.net/display/esdfdev/Training+Plan+Description
        * Work products in other tools:
        -- .. link:: title=Supplier Documents address=https://confluence.cc.bmwgroup.net/display/esdfdev/Supplier+Documents+Description
        -- .. link:: title=Supplier Management Status Report address=https://confluence.cc.bmwgroup.net/display/esdfdev/Supplier+Management+Status+Report+Description
        * Work products in other tools:
        -- .. link:: title=Project Status Report address=https://confluence.cc.bmwgroup.net/display/esdfdev/Project+Status+Report+Description
        -- .. link:: title=Lessons Learned Rep address=https://confluence.cc.bmwgroup.net/display/esdfdev/Lessons+Learned+Report+Description

**WORK PRODUCTS**

.. panel::
    :title: WORK PRODUCT RESPONSIBILITIES
    :titlecolor: #00777A 

    Who is responsible to create, review etc. each work product.

    .. tablemacro::
        :header:
            - Work Product
            - Responsible
            - Review
            - Alignment
            - Mandatories
        
        - .. link:: title=Internal Interface Agreement address=https://confluence.cc.bmwgroup.net/display/esdfdev/Internal+Interface+Agreement+Description
        * .. link:: title=Software Project Lead address=https://confluence.cc.bmwgroup.net/display/esdf/Software+Project+Lead
        * .. link:: title=Systems and Software Quality Engineer address=https://confluence.cc.bmwgroup.net/display/esdfdev/Systems+and+Software+Quality+Engineer
        * .. link:: title=Software Safety Manager address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Safety+Manager <br/> .. link:: title=Software Security Engineer address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Security+Engineer
        * .. status:: title=MANDATORY color=Red

        - .. link:: title=Lessons Learned Report address=https://confluence.cc.bmwgroup.net/display/esdfdev/Lessons+Learned+Report+Description
        * .. link:: title=Software Project Lead address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Project+Lead
        * &nbsp;
        * .. link:: title=Systems and Software Quality Engineer address=https://confluence.cc.bmwgroup.net/display/esdfdev/Systems+and+Software+Quality+Engineer
        * .. status:: title=MANDATORY color=Red

        - .. link:: title=Open Source Software General Approval address=https://confluence.cc.bmwgroup.net/display/esdfdev/Open+Source+Software+General+Approval+Description
        * .. link:: title=Free and Open Source Project Manager address=https://confluence.cc.bmwgroup.net/display/esdfdev/Free+and+Open+Source+Project+Manager 
        * &nbsp;
        * .. link:: title=Software Architect address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Architect <br/> .. link:: title=Software Project Lead address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Project+Lead
        * .. status:: title=OSS color=Yellow
        
        - .. link:: title=Project Schedule address=https://confluence.cc.bmwgroup.net/display/esdfdev/Project+Schedule+Description
        * .. link:: title=Software Project Lead address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Project+Lead
        * &nbsp;  
        * .. link:: title=Software Safety Manager address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Safety+Manager <br/> .. link:: title=Software Security Engineer address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Security+Engineer
        * .. status:: title=MANDATORY color=Red

        - .. link:: title=Project Status Report address=https://confluence.cc.bmwgroup.net/display/esdfdev/Project+Status+Report+Description
        * .. link:: title=Software Project Lead address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Project+Lead
        * &nbsp;  
        * .. link:: title=Systems and Software Quality Engineer address=https://confluence.cc.bmwgroup.net/display/esdfdev/Systems+and+Software+Quality+Engineer 
        * .. status:: title=MANDATORY color=Red
        
        - .. link:: title=Risk and Opportunity List address=https://confluence.cc.bmwgroup.net/display/esdfdev/Risk+and+Opportunity+List+Description
        * .. link:: title=Software Project Lead address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Project+Lead
        * &nbsp;  
        * .. link:: title=Software Safety Manager address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Safety+Manager <br/> .. link:: title=Software Security Engineer address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Security+Engineer
        * .. status:: title=MANDATORY color=Red
        
        - .. link:: title=Software Project Management Plan address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Project+Management+Plan+Description
        * .. link:: title=Software Project Lead address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Project+Lead
        * .. link:: title=Systems and Software Quality Engineer address=https://confluence.cc.bmwgroup.net/display/esdfdev/Systems+and+Software+Quality+Engineer  
        * .. link:: title=Software Safety Manager address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Safety+Manager <br/> .. link:: title=Software Security Engineer address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Security+Engineer
        * .. status:: title=MANDATORY color=Red
        
        - .. link:: title=Software Security Interface Agreement address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Security+Interface+Agreement+Description
        * .. link:: title=Software Security Engineer address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Security+Engineer
        * .. link:: title=Software Project Lead address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Project+Lead
        * .. link:: title=Software Safety Manager address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Safety+Manager <br/> .. link:: title=Systems and Software Quality Engineer address=https://confluence.cc.bmwgroup.net/display/esdfdev/Systems+and+Software+Quality+Engineer
        * .. status:: title=SECURITY color=Yellow
        
        - .. link:: title=Supplier Agreements address=https://confluence.cc.bmwgroup.net/display/esdfdev/Supplier+Agreements+Description
        * .. link:: title=Software Project Lead address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Project+Lead
        * .. link:: title=Systems and Software Quality Engineer address=https://confluence.cc.bmwgroup.net/display/esdfdev/Systems+and+Software+Quality+Engineer
        * .. link:: title=Software Safety Manager address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Safety+Manager <br/> .. link:: title=Software Security Engineer address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Security+Engineer
        * .. status:: title=MANDATORY color=Red
        
        - .. link:: title=Supplier Documents address=https://confluence.cc.bmwgroup.net/display/esdfdev/Supplier+Documents+Description
        * .. link:: title=Software Project Lead address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Project+Lead (external input by Project Partner)
        * &nbsp;
        * &nbsp;
        * .. status:: title=MANDATORY color=Red

        - .. link:: title=Supplier Management Plan address=https://confluence.cc.bmwgroup.net/display/esdfdev/Supplier+Management+Plan+Description
        * .. link:: title=Software Project Lead address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Project+Lead
        * .. link:: title=Systems and Software Quality Engineer address=https://confluence.cc.bmwgroup.net/display/esdfdev/Systems+and+Software+Quality+Engineer
        * .. link:: title=Software Safety Manager address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Safety+Manager <br/> .. link:: title=Software Security Engineer address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Security+Engineer
        * .. status:: title=MANDATORY color=Red

        - .. link:: title=Supplier Management Status Report address=https://confluence.cc.bmwgroup.net/display/esdfdev/Supplier+Management+Status+Report+Description
        * .. link:: title=Software Project Lead address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Project+Lead
        * &nbsp;
        * .. link:: title=Systems and Software Quality Engineer address=https://confluence.cc.bmwgroup.net/display/esdfdev/Systems+and+Software+Quality+Engineer
        * .. status:: title=MANDATORY color=Red

        - .. link:: title=Supplier Selection Report address=https://confluence.cc.bmwgroup.net/display/esdfdev/Supplier+Selection+Report+Description
        * .. link:: title=Software Project Lead address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Project+Lead
        * &nbsp;
        * &nbsp;
        * .. status:: title=MANDATORY color=Red
        
        - .. link:: title=Team Assignment List address=https://confluence.cc.bmwgroup.net/display/esdfdev/Team+Assignment+List+Description
        * .. link:: title=Software Project Lead address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Project+Lead
        * &nbsp;
        * &nbsp;
        * .. status:: title=MANDATORY color=Red

        - .. link:: title=Traceability Concept address=https://confluence.cc.bmwgroup.net/display/esdfdev/Traceability+Concept+Description
        * .. link:: title=ECU_Software Requirements Manager address=https://confluence.cc.bmwgroup.net/display/esdfdev/ECU_Software+Requirements+Manager
        * .. link:: title=Software Architect address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Architect
        * .. link:: title=Software Safety Architect address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Safety+Architect <br/> .. link:: title=Software Security Engineer address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Security+Engineer <br/> .. link:: title=Software Test Engineer address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Test+Engineer
        * .. status:: title=MANDATORY color=Red

        - .. link:: title=Training Plan address=https://confluence.cc.bmwgroup.net/display/esdfdev/Training+Plan+Description
        * .. link:: title=Software Project Lead address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Project+Lead
        * &nbsp;
        * &nbsp;
        * .. status:: title=MANDATORY color=Red
        
        - .. link:: title=Work Product Overview address=https://confluence.cc.bmwgroup.net/display/esdfdev/Work+Product+Overview+Description
        * .. link:: title=Software Configuration Manager address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Configuration+Manager
        * .. link:: title=Systems and Software Quality Engineer address=https://confluence.cc.bmwgroup.net/display/esdfdev/Systems+and+Software+Quality+Engineer
        * .. link:: title=ECU_Software Requirements Manager address=https://confluence.cc.bmwgroup.net/display/esdfdev/ECU_Software+Requirements+Manager <br/> .. link:: title=Software Architect address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Architect <br/> .. link:: title=Software Integrator address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Integrator <br/> .. link:: title=Software Problem Manager address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Problem+Manager <br/> .. link:: title=Software Project Lead address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Project+Lead <br/> .. link:: title=Software Safety Manager address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Safety+Manager <br/> .. link:: title=Software Test Manager address=https://confluence.cc.bmwgroup.net/display/esdfdev/Software+Test+Manager
        * .. status:: title=MANDATORY color=Red
