from setuptools import setup, find_packages
setup(
    name="hbmqtt_device_tracker",
    version=0.1,
    description="HASS device tracker based on connected clients",
    author="Mitko Masarliev",
    author_email='mitko@masarliev.net',
    url="https://github.com/masarliev/hbmqtt_device_tracker",
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    platforms='all',
    entry_points={
        'hbmqtt.broker.plugins': [
            'hbmqtt_device_tracker = hbmqtt_device_tracker:DeviceTracker',
        ]
    }
)
