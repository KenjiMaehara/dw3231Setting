#!/bin/sh
sudo modprobe -c | grep 3231
sudo hwclock -r
#echo ds3231 0x68 | sudo tee /sys/class/i2c-adapter/i2c-1/new_device
#sudo lsmod | grep rtc_ds
#sudo hwclock -r





#sudo hwclock -r > checkTime.txt
#date
#sudo hwclock -w
#sudo hwclock -r


