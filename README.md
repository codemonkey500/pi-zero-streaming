# pi-zero-streaming

This repo can be used to easily transform your Raspberry Pi Zero into a security cam.
It features CPU temperature monitoring.

Run on boot:

```bash
crontab -e
```

Add

```bash
@reboot python3 /home/admin/Pi-Zero-Streaming/main.py &
```
