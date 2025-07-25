# install the stil
use a debin vm or the real thing 



        sudo apt-get update

        sudo apt-get install git

        sudo apt-get install gitk git-gui

        git clone https://github.com/ArduPilot/ardupilot.git

        Tools/environment_install/install-prereqs-ubuntu.sh -y

        reboot




# install Gazebo 

Gazebo Harmonic is the one that u need to use https://gazebosim.org/docs/harmonic/install
pase in to the terminal 

**For Gazebo Harmonic**

sudo apt update
sudo apt install libgz-sim8-dev rapidjson-dev
sudo apt install libopencv-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev gstreamer1.0-plugins-bad gstreamer1.0-libav gstreamer1.0-gl

mkdir -p gz_ws/src && cd gz_ws/src
git clone https://github.com/ArduPilot/ardupilot_gazebo

export GZ_VERSION=harmonic
cd ardupilot_gazebo
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=RelWithDebInfo
make -j4


### Configure the Gazebo environment

Gazebo uses a number of environment variables to locate plugins and models at run time. These may be set in the terminal used to run Gazebo, or set in your .bashrc or .zshrc files:
export GZ_SIM_SYSTEM_PLUGIN_PATH=$HOME/gz_ws/src/ardupilot_gazebo/build:$GZ_SIM_SYSTEM_PLUGIN_PATH
export GZ_SIM_RESOURCE_PATH=$HOME/gz_ws/src/ardupilot_gazebo/models:$HOME/gz_ws/src/ardupilot_gazebo/worlds:$GZ_SIM_RESOURCE_PATH

# run it 


Using Gazebo with ArduPilot¶

Two models are provided as examples with the plugin: an Iris quadcopter and a Zephyr delta-wing.
Iris quadcopter¶

    Run Gazebo

        gz sim -v4 -r iris_runway.sdf

    Run SITL

        sim_vehicle.py -v ArduCopter -f gazebo-iris --model JSON --map --console

    Arm and takeoff

        STABILIZE> mode guided
        GUIDED> arm throttle
        GUIDED> takeoff 5

Zephyr delta-wing¶

The Zephyr is positioned for vertical takeoff.

    Run Gazebo

        gz sim -v4 -r zephyr_runway.sdf

    Run SITL

        sim_vehicle.py -v ArduPlane -f gazebo-zephyr --model JSON --map --console

    Arm, takeoff and circle

        MANUAL> mode fbwa
        FBWA> arm throttle
        FBWA> rc 3 1800
        FBWA> mode circle

