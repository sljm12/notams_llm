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
Below are 9 Notices to AIRMAN

0:
+ A3400/24 N TWY N2 BEHIND ACFT STANDS 509 AND 510 CLSD DUE WIP
From: 02 Oct 2024 02:00 To: 02 Oct 2024 08:00

1:
+ A3401/24 N JUNCTION OF TWY S/TWY W/TWY W10 CLSD DUE WIP
From: 01 Oct 2024 06:00 To: 01 Oct 2024 08:00

2:
+ A3414/24 N TWY S2 CLSD
From: 30 Sept 2024 16:00 To: 30 Nov 2024 15:59

3:
+ A3273/24 N DANGER AREA WSD14 ACTIVE
Lower: SFC Upper: FL400
From: 29 Sept 2024 16:00 To: 04 Oct 2024 15:59

4:
+ A3274/24 N DANGER AREA WSD15 ACTIVE
Lower: SFC Upper: FL400
From: 29 Sept 2024 16:00 To: 04 Oct 2024 15:59

5:
+ A3275/24 N DANGER AREA WSD44 ACTIVE
Lower: SFC Upper: FL400
From: 29 Sept 2024 16:00 To: 04 Oct 2024 15:59

6:
+ A3276/24 N DANGER AREA WSD45 ACTIVE
Lower: SFC Upper: FL400
From: 29 Sept 2024 16:00 To: 04 Oct 2024 15:59

7:
+ A3277/24 N MIL TRG AND EXER WILL TAKE PLACE WI THE FLW COORD:
023000.00N1051628.72E - 023000.00N1060000.00E -
013000.00N1060000.00E - 013000.00N1045219.20E -
021838.00N1052205.00E - 023000.00N1051628.72E
RMK/ALL TRAFFIC ON THE AFFECTED ATS ROUTES WILL BE SUBJECT TO ATC
CLEARANCE
Lower: SFC Upper: FL400
From: 29 Sept 2024 16:00 To: 04 Oct 2024 15:59

8:
+ A3421/24 N PARAMOTOR ACT WILL TAKE PLACE WI 010916.00N1040304.00E -
010732.00N1040034.00E - 010731.00N1040336.00E -
010916.00N1040304.00E.
RMK/ALL ACFT SUBJ ATC CLR
Lower: SFC Upper: 500FT AMSL
From: 02 Oct 2024 01:00 To: 05 Oct 2024 03:00

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