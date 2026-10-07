import os
import re

def replace_in_file(filepath, replacements):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements:
        content = content.replace(old, new)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# 1. Role Inconsistency
replace_in_file('d:/docs/08-project/glossary.md', [
    ("('STUDENT', 'STAFF', 'MANAGER', 'ADMIN')", "('STUDENT', 'STAFF', 'MANAGER')")
])

replace_in_file('d:/docs/07-architecture/api-design.md', [
    ('Staff, Manager/Admin', 'Staff, Manager'),
    ('Quản lý & Admin', 'Quản lý'),
    ('Manager/Admin', 'Manager'),
    ('Admin', 'Manager')
])

replace_in_file('d:/docs/07-architecture/data-model.md', [
    ("'STUDENT', 'STAFF', 'MANAGER', 'ADMIN'", "'STUDENT', 'STAFF', 'MANAGER'")
])

replace_in_file('d:/docs/07-architecture/security-design.md', [
    ('| Quản trị viên (`ADMIN`) |', '|')
])

replace_in_file('d:/docs/07-architecture/system-context.md', [
    ('Quản lý / Quản trị viên (Manager & Admin)', 'Quản lý (Manager)'),
    ("('STUDENT', 'STAFF', 'MANAGER', 'ADMIN')", "('STUDENT', 'STAFF', 'MANAGER')"),
    ('|  Quản lý / Admin  |', '|  Quản lý  |'),
    ('|  (Manager/Admin)  |', '|  (Manager)  |')
])

replace_in_file('d:/docs/03-modules/M05-rbac-security/prd.md', [
    ('Sinh viên, Nhân viên, Quản lý, Admin', 'Sinh viên, Nhân viên, Quản lý'),
    ('Admin gửi request -> Hệ thống cho phép', 'Quản lý gửi request -> Hệ thống cho phép'),
    ('Người dùng là Quản trị viên (Admin)', 'Người dùng là Quản lý (Manager)'),
    ('Tài khoản Admin thử gửi lệnh', 'Tài khoản Quản lý thử gửi lệnh')
])

replace_in_file('d:/docs/03-modules/M05-rbac-security/README.md', [
    ('Quản lý/Admin', 'Quản lý'),
    ('(`STUDENT`, `STAFF`, `MANAGER`/`ADMIN`)', '(`STUDENT`, `STAFF`, `MANAGER`)'),
    ('MANAGER/ADMIN', 'MANAGER'),
    ('| Quản Trị Viên (`ADMIN`) |', '|')
])

replace_in_file('d:/docs/03-modules/M03-management-dashboard/README.md', [
    ('Phân Hệ Quản Lý / Admin', 'Phân Hệ Quản Lý'),
    ('Ban Giám hiệu, Trưởng/Phó các Phòng ban chức năng và Quản trị viên hệ thống', 'Ban Giám hiệu và Trưởng/Phó các Phòng ban chức năng'),
    ('Quản trị viên hệ thống', 'Quản lý hệ thống'),
    ('Tổng M3 - Admin', 'Tổng M3 - Quản lý'),
    ('| **FR-MGT-07** | Quản lý danh mục, lưu trữ & xuất dữ liệu | Quản lý phòng ban/danh mục Ticket, thời hạn lưu trữ và xuất dữ liệu báo cáo theo quyền. |', '| **FR-MGT-07** | Quản lý thời hạn lưu trữ | Cấu hình và quản lý thời hạn lưu trữ dữ liệu Ticket, File và Audit Log. |\n| **FR-MGT-08** | Quản lý danh mục & xuất dữ liệu | Quản lý phòng ban/danh mục Ticket và xuất dữ liệu báo cáo theo quyền. |'),
    ('[Danh mục/Lưu trữ/Xuất dữ liệu FR-MGT-07]', '[Lưu trữ FR-MGT-07] / [Danh mục/Xuất dữ liệu FR-MGT-08]')
])

replace_in_file('d:/docs/03-modules/M03-management-dashboard/prd.md', [
    ('Phân Hệ Quản Lý / Admin', 'Phân Hệ Quản Lý'),
    ('Ban Giám hiệu, Trưởng/Phó phòng ban và Quản trị viên hệ thống', 'Ban Giám hiệu và Trưởng/Phó phòng ban'),
    ('TỔNG M3 - Admin', 'TỔNG M3 - Quản lý'),
    ('[FR-MGT-01] Đăng nhập tài khoản Quản lý / Quản trị viên', '[FR-MGT-01] Đăng nhập tài khoản Quản lý'),
    ("Quản lý (`MANAGER`) hoặc Quản trị viên (`ADMIN`)", "Quản lý (`MANAGER`)"),
    ('Quản lý phòng ban / Ban Giám hiệu / Quản trị viên kỹ thuật (Manager / Admin).', 'Quản lý phòng ban / Ban Giám hiệu (Manager).'),
    ('`MANAGER` hoặc `ADMIN`', '`MANAGER`'),
    ('`ADMIN`/Ban Giám hiệu', 'Ban Giám hiệu'),
    ('Quản trị viên (Admin)', 'Quản lý (Manager)'),
    ('Quản trị viên hệ thống (Admin).', 'Quản lý (Manager).'),
    ('vai trò `ADMIN`', 'vai trò `MANAGER`'),
    ('1. Admin truy cập', '1. Quản lý truy cập'),
    ('Admin nhấn', 'Quản lý nhấn'),
    ('Admin nhập', 'Quản lý nhập'),
    ('Admin chọn', 'Quản lý chọn'),
    ('2. Admin xem', '2. Quản lý xem'),
    ('3. Admin tạo', '3. Quản lý tạo'),
    ('4. Admin cấu hình', '4. Quản lý cấu hình'),
    ('5. Admin truy cập', '5. Quản lý truy cập'),
    ('### [FR-MGT-07] Quản lý phòng ban, danh mục, lưu trữ & xuất dữ liệu\n\n**Mô tả**\nCho phép Admin quản lý các dữ liệu cấu hình phục vụ vận hành hệ thống, bao gồm Phòng ban, Nhóm vấn đề/Danh mục Ticket, thời hạn lưu trữ dữ liệu và thao tác xuất dữ liệu báo cáo theo phạm vi đã chốt trong bảng chi phí nội bộ.', '### [FR-MGT-07] Quản lý thời hạn lưu trữ (Data Retention)\n\n**Mô tả**\nCho phép Quản lý thiết lập và kiểm soát thời hạn lưu trữ (retention policy) đối với Ticket đã đóng, file đính kèm và Audit Log để tối ưu dung lượng hệ thống theo chính sách của nhà trường.\n\n**Actor**\nQuản lý (Manager).\n\n**Preconditions**\n- Người dùng đăng nhập bằng tài khoản có vai trò `MANAGER`.\n\n**Luồng chính**\n1. Quản lý truy cập mục **Cấu hình lưu trữ**.\n2. Quản lý xem các mức thiết lập lưu trữ hiện tại (vd: Ticket lưu 3 năm, File lưu 1 năm, Log lưu 6 tháng).\n3. Quản lý điều chỉnh các mốc thời gian lưu trữ theo cấu hình cho phép.\n4. Quản lý nhấn **Lưu cấu hình**.\n5. Hệ thống cập nhật thời hạn lưu trữ và ghi nhận Audit Log.\n\n**Business Rules**\n- Chỉ tài khoản có thẩm quyền Quản lý hệ thống mới có thể chỉnh sửa cấu hình này.\n- Các quy định xóa dữ liệu tự động định kỳ (cron job) sẽ dựa trên cấu hình lưu trữ này.\n\n---\n\n### [FR-MGT-08] Quản lý phòng ban, danh mục & xuất dữ liệu\n\n**Mô tả**\nCho phép Quản lý quản lý các dữ liệu cấu hình phục vụ vận hành hệ thống, bao gồm Phòng ban, Nhóm vấn đề/Danh mục Ticket và thao tác xuất dữ liệu báo cáo theo phạm vi đã chốt trong bảng chi phí nội bộ.')
])

replace_in_file('d:/docs/04-workflows/WF-05-complete-and-resolve.md', [
    ('Admin/Manager', 'Manager')
])

# 2. ADR-001 format
replace_in_file('d:/docs/07-architecture/technical-decisions/ADR-001-ticket-id-generation.md', [
    ('TK-202610-A89F', 'TK-20261004-A89F'),
    ('TK-202610-8F3A', 'TK-20261004-8F3A'),
    ('TK + [YYYYMM]', 'TK + [YYYYMMDD]')
])

# 4. Escalation in M02
replace_in_file('d:/docs/03-modules/M02-staff-operations/prd.md', [
    ('### [FR-STF-04] Chuyển phòng ban chuyên trách (Transfer Department)', '### [FR-STF-04] Chuyển phòng ban chuyên trách & Escalation (Transfer & Escalation)'),
    ('Khi phát hiện sinh viên gửi nhầm phòng ban hoặc nội dung cần sự giải quyết của đơn vị khác, nhân viên có quyền chuyển Ticket sang Phòng ban chuyên trách kèm theo lý do chuyển.', 'Khi phát hiện sinh viên gửi nhầm phòng ban hoặc nội dung cần sự giải quyết của đơn vị/cấp quản lý khác, nhân viên có quyền chuyển (Transfer) hoặc leo thang (Escalate) Ticket sang Phòng ban/Người phụ trách chuyên trách kèm theo lý do.'),
    ('Nhân viên chọn chức năng **Chuyển phòng ban**', 'Nhân viên chọn chức năng **Chuyển phòng ban / Escalation**')
])

# 5. Timeline UAT contradiction and SRS removal
replace_in_file('d:/docs/08-project/milestones-and-timeline.md', [
    ('Tài liệu PRD, Wireframe/SRS hoàn chỉnh', 'Tài liệu PRD, Wireframe hoàn chỉnh'),
    ('| **Giai đoạn 5: Kiểm thử & Nghiệm thu** | Tuần 12–13 | Kiểm thử chức năng, kiểm thử tích hợp, kiểm thử hồi quy, UAT với client và sửa lỗi thuộc phạm vi. | Báo cáo kiểm thử/UAT, danh sách lỗi và kết quả khắc phục |\n| **Giai đoạn 6: Hoàn thiện & Bàn giao** | Tuần 14 | Sửa lỗi cuối, triển khai hệ thống, hoàn thiện tài liệu, mã nguồn và bàn giao chính thức. | Hệ thống triển khai, tài liệu bàn giao, biên bản bàn giao |', '| **Giai đoạn 5: Kiểm thử nội bộ** | Tuần 12–13 | Kiểm thử chức năng, kiểm thử tích hợp, kiểm thử hồi quy và sửa lỗi nội bộ thuộc phạm vi. | Báo cáo kiểm thử nội bộ, danh sách lỗi và kết quả khắc phục |\n| **Giai đoạn 6: Hoàn thiện & Bàn giao** | Tuần 14 | Sửa lỗi cuối, triển khai hệ thống, hoàn thiện tài liệu, mã nguồn và bàn giao chính thức phiên bản RC. | Hệ thống triển khai, tài liệu bàn giao, biên bản bàn giao |\n| **Giai đoạn sau Tuần 14: Nghiệm thu UAT** | +10 ngày | Khách hàng kiểm thử UAT và xác nhận nghiệm thu. | Biên bản nghiệm thu |'),
    ('* **Mốc 4 (Tuần 13):** Hoàn thành UAT và tổng hợp kết quả phản hồi từ client.\n* **Mốc 5 (Tuần 14):** Hoàn tất xử lý lỗi thuộc phạm vi, triển khai và bàn giao chính thức.', '* **Mốc 4 (Tuần 13):** Hoàn thành kiểm thử nội bộ và sửa các lỗi phát sinh.\n* **Mốc 5 (Tuần 14):** Bàn giao chính thức hệ thống phục vụ UAT.\n* **Mốc 6 (Sau Tuần 14):** Hoàn thành 10 ngày UAT và ký nghiệm thu chính thức.')
])
replace_in_file('d:/docs/08-project/team-charter.md', [
    ('lập đặc tả (SRS)', 'lập đặc tả (PRD)')
])

print("Files updated successfully.")
