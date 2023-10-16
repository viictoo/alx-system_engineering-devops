## 0x13. Firewall

DevOps		SysAdmin	Security

1. Configure ufw so that it blocks all incoming traffic,
	except the following TCP ports:

	22 (SSH)
	443 (HTTPS SSL)
	80 (HTTP)
100. Configure web-01 so that its firewall redirects port
	8080/TCP to port 80/TCP


useful addons
[enable netwroking on docker]

```docker run --cap-add=NET_ADMIN -it ubuntu:16.04```

[uncomplicated firewall rules]
``` sudo ufw status verbose ```

```iptables -L ```
