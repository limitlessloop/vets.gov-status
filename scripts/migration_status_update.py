import datetime
import os
import re
import textwrap
import time
import pdb
import json
from urllib.parse import quote

import github3

MARKDOWN_DIR = "migration_status"
IGNORE_LIST = [item.casefold() for item in [
               "readme.md",
               "project status template.md",
               "link to launch guide.md",
               "use this template.md",
               "OLD Service and Facility Locator.md",
               "OLD USE THIS TEMPLATE.md",
               "OLD Vocational Rehabilitation and Employment.md"
               "TEMPLATE.md"
               ]
               ]


def createDashboardCSV(repo, markdown_files):
    output_file = os.path.join(os.environ['DATA_DIR'], 'migration_status.csv')
    with open(output_file, 'w') as migration_status:
        migration_status.write('name,link,lead,pre_intake,oit_intake,migrate_to_cloud,migration_planning,migration_cutover,cutover_complete,decom\n')
        product_rows = []
        for md in markdown_files:
            if md.casefold() not in IGNORE_LIST:
                full_path = MARKDOWN_DIR + '/' + md,
                document = open(full_path).read().decode('utf8')
                #full_path = MARKDOWN_DIR + '/' + md
                #doc_path = repo.html_url + '/blob/master/' + quote(full_path)
                #document = repo.file_contents(full_path).decoded.decode('utf-8')
                product_rows.append(docToRow(document, doc_path))
        product_rows.sort()
        for row in product_rows:
            migration_status.write(row + "\n")


def docToRow(document, doc_path):
    lines = document.splitlines()
    lines = list(filter(lambda x: not re.match(r'^\s*$', x), lines))
    product_name = lines[0].split(":")[1].strip()
    product_lead = lines[1].split(":")[1].strip()
    migrate_to_cloud = lines[2].split(":")[1].strip()
    cutover_complete = lines[3].split(":")[1].strip()

    for line in lines:
        if "COMPLETED ALL (PRE Intake) Tasks" in line:
            pre_intake = get_status(line)
        elif "COMPLETED ALL OIT Intake Tasks" in line:
            oit_intake = get_status(line)
        elif "COMPLETED ALL Migration Planning and Onboarding Tasks" in line:
            migration_planning = get_status(line)
        elif "COMPLETED ALL Provisioning Tasks" in line:
            provisioning_tasks = get_status(line)
        elif "COMPLETED ALL Build Out and Cutover Tasks" in line:
            migration_cutover = get_status(line)
        elif "COMPLETED ALL Operations Tasks" in line:
            operations_tasks = get_status(line)
        elif "COMPLETED ALL Decommission Tasks" in line:
            decom = get_status(line)

    product_link = "\"" + doc_path + "\""

    return ",".join((product_name, product_link, product_lead, pre_intake,
                     oit_intake, migrate_to_cloud, migration_planning,provisioning_tasks,
                     migration_cutover, operations_tasks,cutover_complete, decom))


def get_status(string):
    """remove everything before first | and after last |"""
    return string.split("|")[1].title().strip()


def main():
    gh_client = github3.GitHub(os.environ["GH_USER"],
                               token=os.environ["GH_TOKEN"])
    repo = gh_client.repository("department-of-veterans-affairs",
                                "vets.gov-status")
    #markdown_files = repo.directory_contents(MARKDOWN_DIR, return_as=dict)
    print(os.getcwd())
    markdown_files = os.listdir(MARKDOWN_DIR)

    createDashboardCSV(repo, markdown_files)


if __name__ == "__main__":
    main()
