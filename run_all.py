import subprocess

# Define the commands to run each script
commands = [
    "python packet_logger.py",
    "python traffic_simulator.py",
    "python threat_detection_agent.py"
]

# Run all scripts in separate processes
processes = []
for command in commands:
    processes.append(subprocess.Popen(command, shell=True))

# Wait for all processes to finish
for process in processes:
    process.wait()
