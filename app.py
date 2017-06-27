# import dependencies
import os
import MBDVidia
import CheckMate

try:
    local_directory = os.getcwd()
    local_directory = local_directory + "\\"

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

    creo_input = r"input.prt"
    qif_file = r"input.qif"
    dmis_output = r"output.dmi"

    # call MBDVidia and CheckMate to generate output data
    # Launch MBDVidia with this input file
    print("Generating QIF model from Creo with MBDVidia", flush=True)
    MBDVidia.run_mbdvidia(local_directory + creo_input, local_directory + qif_file)

    # Launch CheckMate with the results from MBDVidia
    print("Generating DMIS program from QIF with CheckMate", flush=True)
    CheckMate.run_checkmate(local_directory + qif_file, local_directory + dmis_output)

    # upload report to s3 bucket and write location to out.txt
    final_name = filemanagement.upload_report(dmis_output)

    outputs = "outputFile="+final_name
    outputs += "\noutputTemplate=<div class=\"project-run-services padding-10\" ng-if=\"!runHistory\" layout=\"column\">          <style>            #custom-dome-UI {             margin-top: -30px;           }          </style>            <div id=\"custom-dome-UI\">             <div layout=\"row\" layout-wrap style=\"padding: 0px 30px\">               <h2>Report Created Successfully:</h2>               <p><a href=\"{{outputFile}}\">{{outputFile}}</a></p>             </div>           </div>        </div>   <script> </script>"

    target = open("out.txt", 'w')
    target.write(outputs)
    target.close
    
except:
    outputs = "outputFile=null"
    outputs += "\noutputTemplate=<div class=\"project-run-services padding-10\" ng-if=\"!runHistory\" layout=\"column\">          <style>            #custom-dome-UI {             margin-top: -30px;           }          </style>            <div id=\"custom-dome-UI\">             <div layout=\"row\" layout-wrap style=\"padding: 0px 30px\">               <h2>Error</h2>               <p>There was an error running this application</p>             </div>           </div>        </div>   <script> </script>"

    target = open("out.txt", 'w')
    target.write(outputs)
    target.close