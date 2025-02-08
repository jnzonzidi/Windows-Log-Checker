# Windows-Log-Checker

Python script checks and retrieves logs for authentication, authorization, system, application, network, firewall, database, security, and audit events in Windows. It uses the Windows Event Log (eventvwr.msc) via the win32evtlog module from pywin32.

This script retrieves and displays recent events from key Windows logs. You can adjust num_records to fetch more or fewer logs.
