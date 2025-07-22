cmake_minimum_required(VERSION 3.8)
project(imu_utils)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(nav_msgs REQUIRED)
#find_package(code_utils REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(Ceres REQUIRED)
find_package(OpenCV REQUIRED)

find_package(OpenCV REQUIRED)
find_package(Eigen3 REQUIRED)
find_package(Ceres REQUIRED)

include_directories(
  ${CERES_INCLUDE_DIRS}
  ${EIGEN3_INCLUDE_DIR}
)

include_directories("../code_utils/include")

set(
  ACC_LIB_SOURCE_FILES
  ${PROJECT_SOURCE_DIR}/src/acc_lib/allan_acc.cpp
  ${PROJECT_SOURCE_DIR}/src/acc_lib/fitallan_acc.cpp
)

set(
  GYR_LIB_SOURCE_FILES
  ${PROJECT_SOURCE_DIR}/src/gyr_lib/allan_gyr.cpp
  ${PROJECT_SOURCE_DIR}/src/gyr_lib/fitallan_gyr.cpp
)

add_executable(
  imu_an
  src/imu_an.cpp
  ${ACC_LIB_SOURCE_FILES}
  ${GYR_LIB_SOURCE_FILES}
)

target_link_libraries(
  imu_an
  ${OpenCV_LIBRARIES}
  ${CERES_LIBRARIES}
)

ament_target_dependencies(
  imu_an
  rclcpp
  std_msgs
  geometry_msgs
  nav_msgs
  #code_utils
  sensor_msgs
)

install(
  TARGETS
  imu_an
  DESTINATION lib/${PROJECT_NAME}
)

install(
  DIRECTORY
  launch

  DESTINATION share/${PROJECT_NAME}
)





ament_package()
