# 0x0C. Web server

# Description
This project focuses on configuring a web server according to specific requirements. The tasks involve setting up an Ubuntu machine to fit the given specifications through automated Bash scripts.

## Concepts
For this project, understanding the concept of "Child Process" is essential.

## Background Context

In this project, some of the tasks will be graded on 2 aspects:

1. Is your web-01 server configured according to requirements?
2. Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)?

For example, if I need to create a file /tmp/test containing the string hello world and modify the configuration of Nginx to listen on port 8080 instead of 80, I can use emacs on my server to create the file and to modify the Nginx configuration file /etc/nginx/sites-enabled/default.

But my answer file would contain:

```bash
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world > /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
```

## Learning Objectives
At the end of this project, you should be able to explain:
- The main role of a web server
- What a child process is and why web servers usually have parent and child processes
- The main HTTP requests
- The role of DNS, what it stands for, and its record types (A, CNAME, TXT, MX)

## Requirements
- Allowed editors: vi, vim, emacs
- All files interpreted on Ubuntu 16.04 LTS
- All files ending with a new line
- README.md file at the root is mandatory
- All Bash scripts must be executable
- Bash scripts must pass Shellcheck (version 0.3.7) without errors
- The first line of all Bash scripts should be #!/usr/bin/env bash
- The second line of all Bash scripts should be a comment explaining the script's purpose
- systemctl cannot be used for restarting a process

