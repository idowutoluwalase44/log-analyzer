#!/usr/bin/env python3
import argparse
import re
import sys
from collections import defaultdict

def parse_log_line(line):
    """
    Parses a single log line.
    Expected log format: "YYYY-MM-DD HH:MM:SS,ms LEVEL Message"
    For example: "2023-04-15 10:34:23,123 INFO Starting application..."
    """
    pattern = r'^(?P<date>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}),\d+\s+(?P<level>[A-Z]+)\s+(?P<message>.*)$'
    match = re.match(pattern, line)
    if match:
        return match.groupdict()
    return None

def color_text(text, color):
    """
    Returns text wrapped in ANSI escape sequences for colored terminal output.
    """
    colors = {
        'red': '\033[91m',
        'yellow': '\033[93m',
        'green': '\033[92m',
        'blue': '\033[94m',
        'reset': '\033[0m'
    }
    return f"{colors.get(color, '')}{text}{colors['reset']}"

def analyze_log_file(logfile, filter_level=None):
    """
    Reads the log file, parses the lines, and outputs a summary and formatted entries.
    """
    log_entries = []
    level_counts = defaultdict(int)

    try:
        with open(logfile, 'r') as f:
            for line in f:
                parsed = parse_log_line(line.strip())
                if parsed:
                    # Filter entries if a log level filter is specified
                    if filter_level and parsed['level'] != filter_level.upper():
                        continue
                    log_entries.append(parsed)
                    level_counts[parsed['level']] += 1
                else:
                    # Print lines that don't match the expected format.
                    print(f"Unparsed: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File {logfile} not found.")
        sys.exit(1)

    # Print summary of log levels
    print("\nLog Summary:")
    for level, count in level_counts.items():
        print(f"{level}: {count}")

    # Print formatted log entries with color coding
    print("\nFormatted Log Entries:")
    for entry in log_entries:
        level = entry['level']
        # Apply colors based on log level
        if level == "ERROR":
            colored_level = color_text(level, 'red')
        elif level == "WARNING":
            colored_level = color_text(level, 'yellow')
        elif level == "INFO":
            colored_level = color_text(level, 'green')
        else:
            colored_level = level

        print(f"{entry['date']} {colored_level} {entry['message']}")

def main():
    parser = argparse.ArgumentParser(description="Automated Log Analyzer")
    parser.add_argument("--logfile", required=True, help="Path to the log file to analyze")
    parser.add_argument("--level", help="Optional: Filter logs by level (e.g., ERROR, INFO, WARNING)")
    args = parser.parse_args() --parse_log_line

    analyze_log_file(args.logfile, args.level)

if __name__ == "__main__":
    main()