"""pdok-mirror.

Copyright (C) 2017  Max Maass

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from controller import scraper, uploader

max_period = 18

for i in range(1, 19, 1):
    # scraper.scrape_period(i, max_period)
    uploader.upload_legislaturperiode(i)


# max_period = 18
# for i in range(1, max_period + 1):
#     scraper.scrape_period(i, max_period)
