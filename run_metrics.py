import os 
import subprocess

ESCAPE_KEY = b'0x1b'

def run_ast_metrics(project_directory):
    project_name = project_directory.split("/")[-1]
    report_name = project_name + '.json'
    print(project_name)
    #TODO: fork own branch of the project and then work from there, don't need 'too high' things
    results = subprocess.run(['php', '../phploc.phar', project_directory], capture_output=True, text=True).stdout.strip("\n")
    print(results)
    results_file = open("metrics-reports/" + project_name + ".txt", "w")
    results_file.write(results)
    results_file.close()
    #os.chdir('/Users/mgone/Desktop/git/ast-metrics-main/ast-metrics')
    #subprocess.run(['go', 'run', '.', 'a', '-i', '--report-markdown=/Users/mgone/Desktop/git/mw-data-coll/metrics-reports/report.md', project_directory])
    #subprocess.run(['go', 'run', '.', 'a', '-i', '--report-json=' + report_name, project_directory])
    #subprocess.run(['mv', report_name, 'Users/mgone/Desktop/git/mw-data-coll/metrics-reports/' + report_name])
    #subprocess.run(['ast-metrics', 'a', '--non-interactive', '--report-markdown=report.md', project_directory])

if __name__ == "__main__":
    run_ast_metrics("../ConfirmEdit")
