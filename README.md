Radiation-serial
----------------------------

these are a handful of logging scripts for <a href="https://mightyohm.com/blog/products/geiger-counter/">MightyOhm's fantastic geiger counter</a>. <br><br>

broadly speaking the goal is to use the geiger counter as a source of <a href="https://en.wikipedia.org/wiki/Hardware_random_number_generator#Physical_phenomena_with_random_properties">truly random numbers</a> for my own ostensibly useful purposes. currently
the data is sourced mainly from background radiation here in my bedroom.

**geiger-daily** - writes serial output from geiger to .CSV file on desktop. intended to be run once a day via cron.
<br>

**metro-m4-serial-delay-logging** - records time between individual decays from geiger's pulse output and writes to internal flash memory on adafruit metro M4 express
<br>

**metro-m4-serial-delay** - same as above, but returns delay in serial
<br>

**serial-read** - simple serial reader for testing purposes etc
<br>

