# import dependencies
import os
import MBDVidia
import CheckMate

# parse input params and put in object called 'inputs'
with open('in.txt') as f:
    lines = f.readlines()

    inputs = {}

    for line in lines:
        kv = line.rstrip().split("=")
        key = kv.pop(0).strip()
        value = "=".join(kv).strip()
        inputs[key] = value

# download the input file to the local dir
import filemanagement
filemanagement.download_data(inputs["inputFile"], "input.prt")

# call MBDVidia and CheckMate to generate output data
MBDVidia.run_mbdvidia("input.prt", "input.qif")
CheckMate.run_checkmate("input.qif", "output.dmi")
dmis_output = "./output.dmi"

# upload report to s3 bucket and write location to out.txt
final_name = upload_report(dmis_output)

outputs = "\noutputFile="+final_name
outputs += "\noutputTemplate=<div class=\"project-run-services padding-10\" ng-if=\"!runHistory\" layout=\"column\">          <style>            #custom-dome-UI {             margin-top: -30px;           }          </style>            <div id=\"custom-dome-UI\">             <div layout=\"row\" layout-wrap style=\"padding: 0px 30px\">               <h2>Report Created Successfully:</h2>               <p><a href=\"{{outputFile}}\">{{outputFile}}</a></p>             </div>           </div>        </div>   <script> </script>"

target = open("out.txt", 'w')
target.write(outputs)
target.close