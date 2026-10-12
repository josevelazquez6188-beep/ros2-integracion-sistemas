
from setuptools import setup
from glob import glob
import os

package_name = 'hardware_system_pkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),
        ('share/' + package_name, ['package.xml']),
        (
            os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.py')
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Estudiante',
    maintainer_email='alumno@example.com',
    description='Sistema de monitoreo de hardware con ROS 2',
    license='MIT',
    entry_points={
        'console_scripts': [
            'hardware_emulator = hardware_system_pkg.hardware_emulator:main',
            'monitor_node = hardware_system_pkg.monitor_node:main',
            'operator_node = hardware_system_pkg.operator_node:main',
        ],
    },
)
