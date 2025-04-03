# log-analyzer
This project is a Python-based log analyzer that automates log processing by parsing log files, generating a summary of log levels, and displaying formatted output with colored text for improved readability.

## Overview

The log analyzer performs the following tasks:

- **Parsing Log Files:**  
  Reads log entries and extracts the date, log level, and message using regular expressions.

- **Color-coded Output:**  
  Displays log entries with color coding (e.g., errors in red, warnings in yellow, info in green) to quickly identify issues.

- **Log Summary:**  
  Provides a count of occurrences for each log level, making it easier to gauge the overall health of your application.

- **Filtering:**  
  Optionally filters logs by a specified log level.

## Prerequisites

- Python 3.x installed on your system.
- A log file in the expected format (e.g., `"YYYY-MM-DD HH:MM:SS,ms LEVEL Message"`).

## Installation

Clone this repository and navigate to the project directory:

```bash
git clone <repository-url>
cd <repository-directory>
```
Run the log analyzer from the command line by specifying the path to your log file:

```bash
python log_analyzer.py --logfile path/to/your/logfile.log
```

o filter the log output by a specific log level (e.g., ERROR), use the --level option:
```bash
python log_analyzer.py --logfile path/to/your/logfile.log --level ERROR
```

## Customization

Log Format:
Adjust the regular expression in the log analyzer code if your log file format differs.

Color Scheme:
Modify the color settings in the code to use different colors or styling for log levels.

## Contributing

If you have suggestions or improvements, feel free to fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
```sql
Simply copy everything above into your `README.md` file, and you’re all set!
