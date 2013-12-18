from setuptools import setup, find_packages

setup(
    name="quicklauncher",
    version="0.1.3",
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    package_data={"quicklauncher.layout": ["ui/*.*", "ui/images/*.*"]},
    author="Cesar Saez",
    author_email="cesarte@gmail.com",
    description="A simple menu to find and execute Softimage commands/scripts.",
    url="http://www.github.com/csaez/quicklauncher",
    license="GNU General Public License (GPLv3)",
    install_requires=["wishlib >= 0.1.4"],
    scripts=["QuickLauncherPlugin.py"]
)
