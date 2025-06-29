install the rasbery pi 

| i found that i had to have the pcie to the ai hat disconeced to get wifi

# seting up the ai hat 
sudo apt upgrade
sudo apt full-upgrade 

**I losely followed the core electronks on the ai hat https://core-electronics.com.au/guides/yolo-object-detection-on-the-raspberry-pi-ai-hat-writing-custom-python/#KBNAKNI**

sudo apt install hailo-all

| atatch the pcie cable to the pi
reboot it 

# set pcie speeds to gen 3
sudo raspi-config
then go to option 6

git clone https://github.com/hailo-ai/hailo-rpi5-examples.git
cd hailo-rpi5-examples
./install.sh

once done reboot

