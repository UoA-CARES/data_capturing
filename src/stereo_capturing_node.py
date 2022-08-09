#! /usr/bin/env python3
import rospy
from datetime import datetime
from cares_lib_ros.data_sampler import DataSamplerFactory#StereoDataSampler, DepthDataSampler, ZividDepthDataSampler

import os
from os.path import expanduser

home = expanduser("~")

def run_loop(sensor_samplers,filepath):
    rate = rospy.Rate(10.0) #10.0
    count = 0
    while not rospy.is_shutdown():
        for sensor, sensor_sampler in sensor_samplers.items():
            sensor_filepath = filepath+sensor_sampler.sensor_name+"/"
        # Capture data at this pose
            sensor_sampler.sample_multiple_streams()
            file_name = sensor_filepath+str(count)
            sensor_sampler.save(file_name)
            count = count+1
        rate.sleep()

def get_filepath():
    now = datetime.now()
    now = now.strftime("%Y-%m-%d-%H-%M-%S")
    scans_directory = home +"/canopy_scans/"

    number_of_scans = len(list(os.listdir(scans_directory)))
    filepath = scans_directory+str(number_of_scans+1)+"_"+now+"/"

    return filepath

def main():
    print("You can start capturing data: ")

    sensors      = rospy.get_param('~sensors') # 'zivid' 'realsense' 'stereo'

    filepath = get_filepath()

    sensor_samplers = {}
    if len(sensors) == 0:
      print("Sensor topics not set - exiting")
      return
    else:
      print("Capturing data with sensors:")
      for sensor in sensors:
        print(sensor)
        sensor_sampler = DataSamplerFactory.create_datasampler(sensor)

        if sensor_sampler == None:
            print("Undefined depth sensor type selected: "+str(sensor)+" exiting")
            return

        sensor_samplers[sensor] = sensor_sampler

        sensor_filepath = filepath + sensor
        if not os.path.exists(sensor_filepath):
            os.makedirs(sensor_filepath)
        print("Saving data too: "+sensor_filepath)

    sensor_filepath = filepath+sensor_sampler.sensor_name+"/"
    run_loop(sensor_samplers, filepath)

if __name__ == '__main__':
    rospy.init_node('canopy_mapping')
    main()
