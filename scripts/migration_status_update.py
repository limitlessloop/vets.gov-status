import os
import re

MARKDOWN_DIR = os.environ["MARKDOWN_DIR"]
IGNORE_LIST = [item.casefold() for item in
               [
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
        migration_status.write('name,link,lead,pre_intake,oit_intake,migrate_to_cloud,migration_planning,provisioning_tasks,migration_cutover,operations_tasks,cutover_complete,decom\n')
        product_rows = []
        for md in markdown_files:
            if md.casefold() not in IGNORE_LIST:
                full_path = str(MARKDOWN_DIR + '/' + md)
                print('Adding: ' + full_path)
                document = open(full_path, 'r', encoding='utf8').read()
                doc_path = repo + '/blob/master/' + full_path
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
                     oit_intake, migrate_to_cloud, migration_planning,
                     provisioning_tasks, migration_cutover, operations_tasks,
                     cutover_complete, decom))


def get_status(string):
    """remove everything before first | and after last |"""
    return string.split("|")[1].title().strip()


def main():

    repo = 'https://github.com/department-of-veterans-affairs/vets.gov-status'
    markdown_files = os.listdir(MARKDOWN_DIR)

    createDashboardCSV(repo, markdown_files)


if __name__ == "__main__":
    main()
