# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.28

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/mobot/ROS2/workspace/pigpio

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/mobot/ROS2/workspace/build/pigpio

# Include any dependencies generated for this target.
include CMakeFiles/pig2vcd.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/pig2vcd.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/pig2vcd.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/pig2vcd.dir/flags.make

CMakeFiles/pig2vcd.dir/pig2vcd.c.o: CMakeFiles/pig2vcd.dir/flags.make
CMakeFiles/pig2vcd.dir/pig2vcd.c.o: /home/mobot/ROS2/workspace/pigpio/pig2vcd.c
CMakeFiles/pig2vcd.dir/pig2vcd.c.o: CMakeFiles/pig2vcd.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/home/mobot/ROS2/workspace/build/pigpio/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/pig2vcd.dir/pig2vcd.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT CMakeFiles/pig2vcd.dir/pig2vcd.c.o -MF CMakeFiles/pig2vcd.dir/pig2vcd.c.o.d -o CMakeFiles/pig2vcd.dir/pig2vcd.c.o -c /home/mobot/ROS2/workspace/pigpio/pig2vcd.c

CMakeFiles/pig2vcd.dir/pig2vcd.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing C source to CMakeFiles/pig2vcd.dir/pig2vcd.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/mobot/ROS2/workspace/pigpio/pig2vcd.c > CMakeFiles/pig2vcd.dir/pig2vcd.c.i

CMakeFiles/pig2vcd.dir/pig2vcd.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling C source to assembly CMakeFiles/pig2vcd.dir/pig2vcd.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/mobot/ROS2/workspace/pigpio/pig2vcd.c -o CMakeFiles/pig2vcd.dir/pig2vcd.c.s

CMakeFiles/pig2vcd.dir/command.c.o: CMakeFiles/pig2vcd.dir/flags.make
CMakeFiles/pig2vcd.dir/command.c.o: /home/mobot/ROS2/workspace/pigpio/command.c
CMakeFiles/pig2vcd.dir/command.c.o: CMakeFiles/pig2vcd.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/home/mobot/ROS2/workspace/build/pigpio/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object CMakeFiles/pig2vcd.dir/command.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT CMakeFiles/pig2vcd.dir/command.c.o -MF CMakeFiles/pig2vcd.dir/command.c.o.d -o CMakeFiles/pig2vcd.dir/command.c.o -c /home/mobot/ROS2/workspace/pigpio/command.c

CMakeFiles/pig2vcd.dir/command.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing C source to CMakeFiles/pig2vcd.dir/command.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/mobot/ROS2/workspace/pigpio/command.c > CMakeFiles/pig2vcd.dir/command.c.i

CMakeFiles/pig2vcd.dir/command.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling C source to assembly CMakeFiles/pig2vcd.dir/command.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/mobot/ROS2/workspace/pigpio/command.c -o CMakeFiles/pig2vcd.dir/command.c.s

# Object files for target pig2vcd
pig2vcd_OBJECTS = \
"CMakeFiles/pig2vcd.dir/pig2vcd.c.o" \
"CMakeFiles/pig2vcd.dir/command.c.o"

# External object files for target pig2vcd
pig2vcd_EXTERNAL_OBJECTS =

pig2vcd: CMakeFiles/pig2vcd.dir/pig2vcd.c.o
pig2vcd: CMakeFiles/pig2vcd.dir/command.c.o
pig2vcd: CMakeFiles/pig2vcd.dir/build.make
pig2vcd: CMakeFiles/pig2vcd.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/home/mobot/ROS2/workspace/build/pigpio/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking C executable pig2vcd"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/pig2vcd.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/pig2vcd.dir/build: pig2vcd
.PHONY : CMakeFiles/pig2vcd.dir/build

CMakeFiles/pig2vcd.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/pig2vcd.dir/cmake_clean.cmake
.PHONY : CMakeFiles/pig2vcd.dir/clean

CMakeFiles/pig2vcd.dir/depend:
	cd /home/mobot/ROS2/workspace/build/pigpio && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/mobot/ROS2/workspace/pigpio /home/mobot/ROS2/workspace/pigpio /home/mobot/ROS2/workspace/build/pigpio /home/mobot/ROS2/workspace/build/pigpio /home/mobot/ROS2/workspace/build/pigpio/CMakeFiles/pig2vcd.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : CMakeFiles/pig2vcd.dir/depend

