import os 
import subprocess
import json 

ESCAPE_KEY = b'0x1b'

def run_ast_metrics(project_directory, date):
    project_name = project_directory.split("/")[-1]
    report_name = 'metrics-reports/' + project_name + "_" + date + '.json'
    print(project_name)
    results = subprocess.run(['./ast-metrics', 'a', '-i', '--report-json=' + report_name, project_directory])
    print(results)
    print("saved report:" + report_name)
    return report_name

def roster_between_two_dates(project_name, date1, date2):
    with open('metrics-reports/' + project_name + "_" + date1 + '.json', 'r') as openfile1: 
        read_json1 = json.load(openfile1)
        roster1 = read_json1['rosterInformation']
        with open('metrics-reports/' + project_name + "_" + date2 + '.json', 'r') as openfile2 :
            read_json2 = json.load(openfile2)
            roster2 = read_json2['rosterInformation']
            roster3 = {}
            for type in roster2.keys():
                subroster1 = roster1[type]
                subroster2 = roster2[type]
                subroster3 = {}
                for individual in subroster2:
                    #default inclusive if individual was not in the roster group the first time
                    if individual in subroster1:
                        commits_in_window = subroster2[individual]['commits'] - subroster1[individual]['commits']
                        if commits_in_window != 0:
                            subroster3[individual] = subroster2[individual]
                            subroster3[individual]['commits'] = commits_in_window
                            subroster3[individual]['added_lines'] = subroster2[individual]['added_lines'] - subroster1[individual]['added_lines']
                            subroster3[individual]['removed_lines'] = subroster2[individual]['removed_lines'] - subroster1[individual]['removed_lines']
                            subroster3[individual]['files_changed'] = subroster2[individual]['files_changed'] - subroster1[individual]['files_changed']
                    else:
                        subroster3[individual] = subroster2[individual]
                roster3[type] = subroster3
    #done 
    print(len(subroster3))
    print(len(subroster2))
    out_filename = "metrics-reports/" + project_name + "_activity_roster_" + date1 + "_to_" + date2 + ".json"
    out_file = open(out_filename, "w")
    json.dump(roster3, out_file, indent = 6)
    out_file.close()

if __name__ == "__main__":
    roster_between_two_dates("ConfirmEdit", "2022-07-01", "2024-08-01")
