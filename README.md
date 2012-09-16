Name
----
    Creeper - open source Python web crawler

Installation
------------
    Clone repository git://github.com/ricco386/creeper.git and execute
    file: ```python creeper.py```

Synopsis
--------
    creeper [-u|--url <value>] [-d|--depth] [-h|--help]

Description
-----------
    Simple web crwaler written in Python.

Options
-------
    -u, --url <value>
        The <value> is mandatory argument, with website url that starts the
        crawling.
    -d, --depth <value>
        Define depth how far should Creeper crawl from the root url. The
        <value> is mandatory argumnet and can be any positive integer. If not
        specified default value 100 is used.
    -v, --verbose
        Cause Creeper to be verbose, showing url crawled, with some statistical
        data that has been retrieved.
    -h, --help
        Prints the synopsis and a list of the most commonly used commands.

Licence
-------
    Creeper - Python web crawler
    Copyright (C) 2012  Richard Kellner

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
