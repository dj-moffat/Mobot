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
include CMakeFiles/x_pigpiod_if.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/x_pigpiod_if.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/x_pigpiod_if.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/x_pigpiod_if.dir/flags.make

CMakeFiles/x_pigpiod_if.dir/x_pigpiod_if.c.o: CMakeFiles/x_pigpiod_if.dir/flags.make
CMakeFiles/x_pigpiod_if.dir/x_pigpiod_if.c.o: /home/mobot/ROS2/workspace/pigpio/x_pigpiod_if.c
CMakeFiles/x_pigpiod_if.dir/x_pigpiod_if.c.o: CMakeFiles/x_pigpiod_if.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/home/mobot/ROS2/workspace/build/pigpio/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/x_pigpiod_if.dir/x_pigpiod_if.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT CMakeFiles/x_pigpiod_if.dir/x_pigpiod_if.c.o -MF CMakeFiles/x_pigpiod_if.dir/x_pigpiod_if.c.o.d -o CMakeFiles/x_pigpiod_if.dir/x_pigpiod_if.c.o -c /home/mobot/ROS2/workspace/pigpio/x_pigpiod_if.c

CMakeFiles/x_pigpiod_if.dir/x_pigpiod_if.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing C source to CMakeFiles/x_pigpiod_if.dir/x_pigpiod_if.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/mobot/ROS2/workspace/pigpio/x_pigpiod_if.c > CMakeFiles/x_pigpiod_if.dir/x_pigpiod_if.c.i

CMakeFiles/x_pigpiod_if.dir/x_pigpiod_if.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling C source to assembly CMakeFiles/x_pigpiod_if.dir/x_pigpiod_if.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/mobot/ROS2/workspace/pigpio/x_pigpiod_if.c -o CMakeFiles/x_pigpiod_if.dir/x_pigpiod_if.c.s

# Object files for target x_pigpiod_if
x_pigpiod_if_OBJECTS = \
"CMakeFiles/x_pigpiod_if.dir/x_pigpiod_if.c.o"

# External object files for target x_pigpiod_if
x_pigpiod_if_EXTERNAL_OBJECTS =

x_pigpiod_if: CMakeFiles/x_pigpiod_if.dir/x_pigpiod_if.c.o
x_pigpiod_if: CMakeFiles/x_pigpiod_if.dir/build.make
x_pigpiod_if: libpigpiod_if.so
x_pigpiod_if: /usr/lib/aarch64-linux-gnu/librt.a
x_pigpiod_if: CMakeFiles/x_pigpiod_if.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/home/mobot/ROS2/workspace/build/pigpio/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable x_pigpiod_if"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/x_pigpiod_if.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/x_pigpiod_if.dir/build: x_pigpiod_if
.PHONY : CMakeFiles/x_pigpiod_if.dir/build

CMakeFiles/x_pigpiod_if.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/x_pigpiod_if.dir/cmake_clean.cmake
.PHONY : CMakeFiles/x_pigpiod_if.dir/clean

CMakeFiles/x_pigpiod_if.dir/depend:
	cd /home/mobot/ROS2/workspace/build/pigpio && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/mobot/ROS2/workspace/pigpio /home/mobot/ROS2/workspace/pigpio /home/mobot/ROS2/workspace/build/pigpio /home/mobot/ROS2/workspace/build/pigpio /home/mobot/ROS2/workspace/build/pigpio/CMakeFiles/x_pigpiod_if.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : CMakeFiles/x_pigpiod_if.dir/depend

