# Postmortem
Postmortem: Outage Incident on Web Stack Servers

![484ce00708289fc3c138e4973746c68a](https://github.com/MundiaNderi/alx-system_engineering-devops/assets/98798719/b14578ae-eec6-4609-83ee-63e0dcc96f9d)



## Issue Summary:
Duration: June 8, 2023, 10:00 PM - June 9, 2023, 08:30 AM (EAT)

Impact: The user-facing website was intermittently unavailable, resulting in slow response times and errors for approximately 30% of the users during the incident.
Timeline:
1. 10:30 PM: Reboot begins
2. 12:26 AM: Outage begins
3. 12:26 AM: Alerts sent to teams via Datadog
4. 12:30 AM: Oncall SRE silenced all subsequent alerts due to server behaviour being “normal”
5. 2:30 AM: Server down and customers can’t reach the site
6. 2:30 AM: Alerts sent to teams via Datadog metrics and team engineering email, 
7. 2:35 AM: A ticket was opened on JIRA and a meeting was started to look at AWS Cloudwatch, AWS Config and AWS CloudTrail logs.
8. 3:15 AM: Team is able to assess the situation and understand the error cause.
9. 4:30 AM: Server restarts begin.
10. 8:30 AM: 100% of traffic back online.

## Root Cause 
The attempt to reboot the load balancer or cache server repeatedly failed, and the failover server (secondary server) remained offline for a duration of 3 hours.  We had not anticipated that the scheduled reboot would impact our systems. Although the software update went smoothly, it had an adverse effect on the overall performance of the website. 
The site failed to reconnect to the secondary server, and the database service provider's personnel discovered that the server's data did not automatically mount upon booting. 

Our Oncall  Site Reliability Engineer (SRE) classified this incident as a routine behaviour of a server reboot, resulting in automatic suppression of any further alerts.

## Corrective and Preventative Measures
1. Review Reboot Procedures: Conduct a thorough review of the reboot procedures for critical servers, such as the load balancer and cache  server. Ensure that the process is well-documented and includes steps to verify connectivity and data integrity after the reboot.
2. Test Failover Mechanisms: Regularly test the failover mechanisms, especially for the secondary server. Verify that the failover server can seamlessly take over in case of a primary server failure and ensure it reconnects to the necessary components properly.
3. Perform Risk Assessments: Prior to scheduling any reboots or software updates, conduct risk assessments to identify potential impacts on system performance and user experience. Consider all possible scenarios and devise mitigation strategies accordingly.
4. Implement Automated Monitoring and Alerts: Set up robust monitoring systems, like Datadog or AWS CloudWatch, to proactively detect and alert teams about any anomalies or performance issues. Configure alerts to be sent to relevant teams promptly, ensuring quick response and investigation.
5. Document Incident Response Procedures: Maintain a well-documented incident response plan that clearly outlines the steps to be taken during an outage or performance degradation. This should include the escalation process, responsibilities of team members, and procedures for analysing logs and metrics.
6. Improve Communication Channels: Establish efficient communication channels between teams involved in incident response. Ensure that alerts and notifications reach the appropriate personnel promptly, and provide clear lines of communication to collaborate effectively during troubleshooting and resolution.
7. Regularly Review System Configuration: Regularly review and validate the system configuration, including settings related to server reboots, auto-mounting of data, and failover mechanisms. Verify that all configurations are properly aligned with the desired behaviour of the system.
8. Conduct Post-Incident Reviews: After every incident, perform thorough post-incident reviews to identify root causes and determine necessary improvements. Share the findings with the relevant teams, and incorporate lessons learned into future prevention strategies and best practices.






