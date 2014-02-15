# This file is part of quicklauncher.
# Copyright (C) 2014  Cesar Saez

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation version 3.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages

setup(
    name="quicklauncher",
    version="0.1.4",
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    package_data={"quicklauncher.layout": ["ui/*.*", "ui/images/*.*"]},
    author="Cesar Saez",
    author_email="cesarte@gmail.com",
    description="A simple menu to find and execute Softimage commands/scripts.",
    url="http://www.github.com/csaez/quicklauncher",
    license="GNU General Public License (GPLv3)",
    install_requires=["wishlib>=0.3.0"]
)
