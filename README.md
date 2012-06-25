#PythonScripts

##LinkedIn resume scraper

### About

This script retrieves the information from a resume on LinkedIn, and creates an XML file with these information.  
The format of the output file is:  
```
<?xml version="1.0" encoding="UTF-8"?>
<resume>  
    <position>
        <title>Your title</title>
        <company>Your company</company>
        <from>From date</from>
        <to>To date (or Present)</to>
        <description>The job description</description>
    </position>
    <position>
        ...
    </position>
</resume>
```

### Installation

To install this script, you'll need (of course) to have Python installed.
The modules needed to run this script are:  
- codecs  
- urllib2  
- requests (to install: sudo pip install requests)  
- StringIO  
- sys  
- lxml (to install: sudo apt-get install python-lxml)  

### Usage

To use this script, just call it
`./linkedin.py <profile_address> <output_file>`

