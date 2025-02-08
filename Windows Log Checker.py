import win32evtlog
import win32evtlogutil
import win32con
import datetime

def get_event_logs(server, log_type, num_records=10):
    try:
        hand = win32evtlog.OpenEventLog(server, log_type)
        flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
        events = win32evtlog.ReadEventLog(hand, flags, 0)
        
        print(f"\nFetching {num_records} latest events from {log_type}...")
        count = 0
        
        for event in events:
            if count >= num_records:
                break
            
            event_time = event.TimeGenerated.Format() if event.TimeGenerated else "Unknown"
            event_id = event.EventID & 0x1FFFFFFF  # Mask higher bits
            event_type = event.EventType
            event_source = event.SourceName
            
            print(f"Time: {event_time}, ID: {event_id}, Type: {event_type}, Source: {event_source}")
            count += 1
        
        win32evtlog.CloseEventLog(hand)
    except Exception as e:
        print(f"Error reading {log_type}: {e}")

if __name__ == "__main__":
    server = "localhost"  # Change this if checking logs on a remote machine
    log_types = [
        "Security", "System", "Application", "Setup", "Microsoft-Windows-Firewall-With-Advanced-Security/Firewall",
        "Microsoft-Windows-NetworkProfile/Operational", "Microsoft-Windows-GroupPolicy/Operational"
    ]
    
    for log in log_types:
        get_event_logs(server, log)
