Title: Daemons - Background Processes that Power Your System

Introduction

In the world of computer systems, daemons (pronounced "dae-mons") are essential
but often invisible entities. These unassuming background processes are responsible 
for handling critical system-level tasks, providing crucial services, and quietly 
supporting the smooth operation of your computer. In this technical guide, we will
explore what daemons are, how they work, and their significance in various operating systems.

What is a Daemon?

A daemon is a type of process that operates in the background, detached from any
controlling terminal or user session. Unlike foreground processes that interact 
directly with users through a terminal, daemons run independently, diligently executing 
their designated tasks. Commonly initiated at system startup, daemons serve a wide range 
of purposes, from network services to hardware management and more.

The Origin of the Term "Daemon"

The name "daemon" has intriguing origins. It derives from an 1867 thought experiment
called "Maxwell's demon," proposed by physicist James Maxwell. In Greek mythology,
daemons were supernatural beings, existing between humans and gods, and they were
known for their divine knowledge and powers. Unlike their Judeo-Christian counterparts,
Greek daemons were not necessarily malevolent. Just as these mythical beings assisted
the gods, modern-day daemons aid in carrying out tasks that foreground users might prefer to avoid.

Characteristics of Daemons

Daemons possess distinct characteristics that set them apart from ordinary processes:

1. Longevity: Daemons are intended to be long-lived. They often start during
system boot and continue running until the system shuts down.

2. Background Execution: Unlike foreground processes that require a terminal,
	daemons operate in the background, free from direct user interaction.

Daemons in Linux

In Linux, daemons play a crucial role in system maintenance and operation.
They are organized in specific directories based on their importance:
1. /usr/sbin/: This directory houses system-related executables, including daemons
essential for system operation. Examples include sshd (SSH daemon) and httpd (web server daemon).

2. /sbin/: Similar to /usr/sbin/, /sbin/ contains system executables. 
However, the ones in /sbin/ are critical for system maintenance and recovery,
such as init and systemd.

3. /usr/bin/: Although less common, some daemons may reside in /usr/bin/ if they
are associated with specific applications and not required for system boot.

--the specific locations of daemon executables can vary depending on the Linux distribution and system configuration.--

Kernel Threads as Daemons

Some daemons are implemented as kernel threads, integrated into the kernel itself.
These daemons are created during system startup and managed by the kernel.
Examples include pdflush, which periodically flushes dirty pages to disk from the buffer cache.


Daemon vs Background Processes (&) - Comparison

To better understand daemons, let's compare them to background processes:

|               | Daemons                                       | Background Processes                                 |
|---------------|-----------------------------------------------|------------------------------------------------------|
| Controlling   | No controlling terminal or user session     | Connected to a terminal or user session             |
| Execution     | Long-lived, running until system shutdown   | Short-lived, dependent on user interaction           |
| Purpose       | System-level tasks and services             | User-specific tasks and interactions                 |
| Examples      | sshd, httpd, cron, dhcpd                    | Text editors, web browsers, shell scripts, etc.      |

Daemon Management and Activation

Daemons are launched during system boot or triggered based on specific events.
The initiation process varies based on the operating system and the init system used:

1. Boot Process: During system boot, the init system (e.g., SysV init, Upstart, or systemd) takes control and starts
various system services, including daemons. Init scripts are commonly used in SysV init systems, while systemd relies on unit files.

2. Triggered Activation: Some daemons are launched on-demand when certain events occur, like network activity or hardware detection.

3. User Initiated: Users can start daemons manually by running corresponding commands, like httpd or sshd.

4. Service Managers: Apart from the init system, service managers like systemctl or supervisord can manage daemons.

Creating Your Own Daemon - An Analogy

Creating a daemon process can be visualized using an analogy with the Space Shuttle Enterprise:

1. Space Shuttle Enterprise: Represents the daemon, designed for a specific service and operating independently in the background.

2. Pre-Launch Preparations: Define the daemon's purpose, plan its behavior, and adhere to system standards.

3. Carrier Plane: Represents the parent process, responsible for creating the daemon.

4. Assembling the Planes: Setting up signal handlers, closing standard file descriptors, and creating the PID file.

5. Forking the Space Shuttle Enterprise: Duplicating the process to create the daemon.

6. Detaching from the Carrier Plane: The daemon process detaches from the parent process to become independent.

7. Space Shuttle Enterprise's Mission: The daemon executes its specific mission autonomously.

8. Parent Process Cleanup: The parent process exits after forking the daemon.

9. Monitoring and Signal Handling: Implementing traps to respond to signals for graceful termination or restart.

10. Continuous Operation: The daemon keeps running without user intervention.

11. Termination and Cleanup: Graceful termination with any required cleanup actions.

Example Daemon and Daemon Manager Code

Below is an example of a simple daemon process that writes a number to /tmp/my_process every second.
The accompanying daemon manager script allows you to start, stop, restart, and check the status of the daemon:


(Daemon Script)

	```
#!/usr/bin/env bash
# Daemon that indefinitely writes a number every second to /tmp/my_process

# Trap SIGHUP to ignore the hangup signal
	trap '' SIGHUP

# Fork the process to create a daemon
	(
# Detach from the terminal by closing standard input, output, and error
	 exec 0<&-
	 exec 1>&-
	 exec 2>&-

# Continue running even if the parent script exits
	 disown

# Change the working directory to root to avoid locking any file system
	 cd /

	 i=0
	 while true; do
	 echo "$i" >> /tmp/my_process
	 (( i++ ))
	 sleep 1
	 done
	) &
	```

(Daemon Manager Script)

	```
#!/usr/bin/env bash
# Daemon manager
	DAEMON=my_daemon.sh
	PIDFILE=/var/run/my_process.pid

	case $1 in
	"start")
	if pidof -x $(basename "$DAEMON") >/dev/null; then
	echo "$DAEMON is already running."
	else
	nohup ./$DAEMON >/dev/null 2>&1 &
	echo "Starting log generator daemon."
	fi
	;;
	"stop")
	if test -f $PIDFILE; then
	kill "$(cat $PIDFILE)"
	rm $PIDFILE
	echo "Stopping log generator daemon."
	else
	echo "$DAEMON is not running."
	fi
	;;
	"restart")
	$0 stop
	sleep 1
	$0 start
	;;
	"status")
	if pidof -x $(basename "$DAEMON") >/dev/null; then
	echo "$DAEMON is running."
	exit 0;
	else
	echo "$DAEMON is not running."
	if test -f $PIDFILE; then exit 2; fi
	exit 3;
	fi


	;;
	"force-reload")
	$0 stop
	sleep 1
	$0 start
	;;
	*)
	echo "Usage: $0 {start|stop|restart|force-reload|status}"
	exit 1
	;;
	esac
	```

	Conclusion

	Daemons play a critical role in the unseen operations of modern computer systems. Operating in the background,
	these long-lived processes handle essential tasks and services, ensuring smooth system functioning. By understanding
	the principles of daemons and their management, system administrators and developers can harness their power to create
	efficient and reliable applications. So, next time you interact with your computer, remember that daemons are silently working to help you!
