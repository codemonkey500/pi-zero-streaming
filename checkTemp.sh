#!/bin/bash

temp=$(vcgencmd measure_temp | cut -d "=" -f2 | sed s/\'/°/g)

echo -n "Pi Temperatur: " > /home/admin/Pi-Zero-Streaming/temperature.txt
echo -n $temp >> /home/admin/Pi-Zero-Streaming/temperature.txt