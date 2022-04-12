# Pothole-Hunter
First steps towards a 'pothole hunter' as practice in designing, building and programming with sensor feedback

Pothole Hunter was developed for practice in designing, building and programming with sensor feedback. Developed in a 'Hardware' module of the MRAC course, the bot requires also python and other software programming to get the hardware to work as a roving bot capable of responding to specific objects detected by its sensors. 
The initial concept was to build a small mobile robot to simulate detecting and filling potholes, which would require the ability to:
● recognize and detect potholes
● navigate to the closest pothole
● manoeuvre correctly to position an end effector directly over the pothole (althought this is done without the pothole remaining in the field of vision)
● fill the pothole
● continue to next pothole
In practice, the goals were scaled back while maintaining the core goal of learning to build and program a complete bot with sensor feedback. In practice the desired ability of recognizing and detecting potholes was simplified to recognizing and detecting 'blobs' within a colour range - in fact oranges as can be seen in the videos below! This simplification was mainly due to time constraints, brought about mainly by an unfortunate situation in which the timing of the develpment of the project came immediately after the release of the updated Raspberry Pi IV microcomputers but before any new software for the new 'camera stack' was generally available. This resulted in quite a lot of time being spent unsuccessfully trying to use the Raspberry Pi IV and the new official Raspberry Pi camera module together, which had to be abandoned due to the lack of software available at the time, and having to opt for an alternative object-recognition hardware/software solution, in a reduced timeframe. This is why the blog post contains some images with the Raspberry Pi camera module mounted in the bot, but the videos in fact use a mobile phone attached to the bot in order to use its camera instead.
Hardware Overview
The bot uses a simple rectangular aluminium frame (universally available 20mm x 20mm extrusion) below which are mounted two motorized wheels (DC motors with encoders, and motor drivers) and a castor wheel and above which is mounted the remaining hardware: an Arduino Uno R3 microprocessor (blue in image below) controls the motion system, a Raspberry Pi 4 microprocessor was intended to control the vision system, a Raspberry Pi V2 camera (both green in image below) but in the end a mobile phone was used as a camera (and off-board image processing was used instead of the Rapsberry Pi 4). A 12V solenoid controlled the release of a liquid from a recipient to a tube which deposited it where the 'pothole' was. A distance sensor was positioned to detect when the liquid filled the 'pothole' to the required level. Screw couplings, 5V regulators, 3S Lipo batteries and some 3D printed parts completed the set up.
