import os
import re

def replace_in_file(filepath, replacements):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    for old, new in replacements:
        if isinstance(old, re.Pattern):
            new_content = old.sub(new, content)
            if new_content != content:
                content = new_content
                modified = True
        else:
            if old in content:
                content = content.replace(old, new)
                modified = True
                
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

# 1. ADMIN references
replace_in_file('d:/docs/08-project/glossary.md', [
    (re.compile(r'\(`STUDENT`, `STAFF`, `MANAGER`, `ADMIN`\)'), '(`STUDENT`, `STAFF`, `MANAGER`)'),
    (re.compile(r"\('STUDENT', 'STAFF', 'MANAGER', 'ADMIN'\)"), "('STUDENT', 'STAFF', 'MANAGER')")
])

replace_in_file('d:/docs/07-architecture/system-context.md', [
    (re.compile(r'\(`STUDENT`, `STAFF`, `MANAGER`, `ADMIN`\)'), '(`STUDENT`, `STAFF`, `MANAGER`)')
])

replace_in_file('d:/docs/08-project/resource-and-cost.md', [
    ('TỔNG M3 – Admin', 'TỔNG M3 – Quản lý'),
    ('M3 – Admin Dashboard', 'M3 – Management Dashboard')
])

replace_in_file('d:/docs/08-project/open-questions.md', [
    ('Admin nhập tay', 'Quản lý nhập tay')
])

replace_in_file('d:/docs/08-project/milestones-and-timeline.md', [
    ('Quản lý/Admin', 'Quản lý')
])

replace_in_file('d:/docs/07-architecture/api-design.md', [
    ('Quản lý/Admin', 'Quản lý'),
    ('Manager/Admin', 'Manager')
])

replace_in_file('d:/docs/04-workflows/WF-05-complete-and-resolve.md', [
    ('Quản lý (Admin/Manager)', 'Quản lý (Manager)'),
    ('Admin/Manager', 'Manager')
])

replace_in_file('d:/docs/03-modules/M05-rbac-security/README.md', [
    ('MANAGER/ADMIN', 'MANAGER')
])

replace_in_file('d:/docs/03-modules/M05-rbac-security/prd.md', [
    ('Admin)', 'Quản lý)')
])

replace_in_file('d:/docs/03-modules/M03-management-dashboard/prd.md', [
    (re.compile(r'Admin'), 'Quản lý'),
    (re.compile(r'ADMIN'), 'MANAGER')
])

# 2. ADR-001
replace_in_file('d:/docs/07-architecture/technical-decisions/README.md', [
    ('TK-YYYYMM-XXXX', 'TK-YYYYMMDD-XXXX')
])

# 3. WF-06
replace_in_file('d:/docs/04-workflows/WF-06-close-and-rate.md', [
    ('### [FR-STU-03]', '### [FR-STU-05]')
])

# 4. RTM - Add Login traceback
rtm_path = 'd:/docs/06-acceptance/traceability-matrix.md'
with open(rtm_path, 'r', encoding='utf-8') as f:
    rtm_content = f.read()

new_req = "| **REQ-SEC-01** | Xác thực & Đăng nhập hệ thống (Sinh viên, Nhân viên, Quản lý) | M05-rbac-security | N/A | TS-SEC-01 | Chờ UAT |\n"
if "REQ-SEC-01" not in rtm_content:
    rtm_content = rtm_content.replace("| **REQ-MNG-01**", new_req + "| **REQ-MNG-01**")
    with open(rtm_path, 'w', encoding='utf-8') as f:
        f.write(rtm_content)

print("Fixes applied.")
