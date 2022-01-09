# HL7crawler
This program was intended to collect data from specific HL7 segments from outbound HL7 logs.
While at work we already had in our software logging of outgoing data from DICOM images, we did not have this for HL7 messages.
I've created this program to be able to find some data customer has asked about.

The input for this program is the directory of HL7 log files. Since they contain PHI (protected health information) I cannot provide those, but here it is an anonymized HL& message just so you have an idea of the format
````
"MSH|^~\\&||Imagecast RIS|||20201101154710||ORM^O01|LAI.HL7SND.0000044|P|2.3|||||||
PID|||patid||patient name||patient dob|patient sex||||||||||||||||||||||
PV1||O|^GNHL^GREEN HILLS INTER MED||||id^name referring physican|id^name referring physican|||||||||||230026059566|||||||||||||||||||||||||||||||||
ORC|NW|230026059566|||||||||||||||BC||||||||||||||
OBR|||51746953|MMAMSD^BILATERAL DIGITAL SCREENING MAMMOGRAM W/ CAD|N||||||||v76.12 -  - ||^^^Breast|id^name referring physican||||||20130816155000|||F||^^^^^N||||v76.12 -  - |||||20130816155000||||||||||||||
OBX||TX|R^ORDER^L||||||||||||||||||||||
ZDS|1.2.124.113532.80.22016.3.20130816.155121.932898098||
"
````

So this program is supposed to scan a directory that contains thousands of logifiles, that in turn contain thousands of such messages as presented above.
The .bat file also has instructions on how to create it in order to get the needed data.
If you want for example to get all the patient ids for which HL7 messages have been sent, you'd request the program to output the PID3 segment and so on.

The output of the program is a file that has as a header the columns requested and if the output files exceed a certain GB limit, they get split in multiple files (since notepad works best with visualizing files of ~max 600Gb)
This has been a great way to learn how to work with regular expressions and pattern matching.

