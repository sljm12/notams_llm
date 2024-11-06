prompt_template = """
Below are {number} Notices to AIRMAN

{notams}

Study them so that you can extract the following information.
NOTAM Number
Event Name
Location_Names
Coordinates
Other information
Lower
Upper
From
To

The event name will be on the same line as the '+' character after the NOTAM number.
Please expand NOTAM short forms to their long forms. 

E.g TWY = Taxiway, WI = Within

Please extract them in JSON format.  
For coordinates, please do not convert them and use Longitude and Latitude Paris to represent them.
For Dates please use the ISO format.
If the information is not available, put in 'null' as the value.
"""

prompt_template1 = """
Below are {number} Notices to AIRMAN

{notams}

Study them so that you can extract the following information.
NOTAM Number
Event Name
Location_Names
Coordinates
Other information
Lower
Upper
From
To

The event name will be on the same line as the '+' character after the NOTAM number.
Please expand NOTAM short forms to their long forms. 

E.g TWY = Taxiway, WI = Within

Please extract them in JSON format.  
Coordinate will look like this '012019N1035813E' where everything before the 'N' or 'S'  is Latitude and after the 'N' or 'S' is Longitude.
For coordinates, please do not convert them and use Longitude and Latitude pairs to represent them.
For Dates please use the ISO format.
If the information is not available, put in 'null' as the value.

"""