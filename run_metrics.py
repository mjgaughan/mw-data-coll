import os 
import subprocess

ESCAPE_KEY = b'0x1b'

def run_ast_metrics(project_directory):
    project_name = project_directory.split("/")[-1]
    report_name = project_name + '.json'
    print(project_name)
    #os.chdir('/Users/mgone/Desktop/git/ast-metrics')
    #subprocess.run(['go', 'run', '.', 'a', '-i', '--report-json=' + report_name, project_directory])
    #subprocess.run(['mv', report_name, 'Users/mgone/Desktop/git/mw-data-coll/metrics-reports/' + report_name])
    subprocess.run(['ast-metrics', 'a', '--non-interactive', '--report-markdown=report.md', project_directory])

if __name__ == "__main__":
    run_ast_metrics("../ConfirmEdit")
