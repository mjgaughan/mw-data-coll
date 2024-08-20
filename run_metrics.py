import os 
import subprocess

ESCAPE_KEY = b'0x1b'

def run_ast_metrics(project_directory, date):
    project_name = project_directory.split("/")[-1]
    report_name = 'metrics-reports/' + project_name + "_" + date + '.json'
    print(project_name)
    results = subprocess.run(['./ast-metrics', 'a', '-i', '--report-json=' + report_name, project_directory])
    print(results)
    print("saved report:" + report_name)

if __name__ == "__main__":
    run_ast_metrics("../ConfirmEdit")
