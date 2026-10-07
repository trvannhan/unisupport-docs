import os

def update_readmes():
    # M01 README
    m01_path = 'd:/docs/03-modules/M01-student-portal/README.md'
    with open(m01_path, 'r', encoding='utf-8') as f:
        m01_content = f.read()
    
    old_m01_table = """| **FR-STU-01** | Đăng nhập tài khoản | Đăng nhập bằng tài khoản Sinh viên cấp sẵn |
| **FR-STU-02** | Gửi yêu cầu hỗ trợ | Form tạo Ticket, đính kèm file |
| **FR-STU-03** | Xem danh sách & theo dõi | Danh sách Ticket của sinh viên |
| **FR-STU-04** | Phản hồi & bổ sung | Bổ sung file/trả lời câu hỏi khi có yêu cầu |
| **FR-STU-05** | Đánh giá CSAT | Chấm điểm & nhận xét kết quả hỗ trợ |"""
    new_m01_table = """| **FR-STU-01** | Tra cứu hướng dẫn & FAQ | Xem FAQ theo nhóm vấn đề |
| **FR-STU-02** | Tạo & gửi yêu cầu hỗ trợ | Form tạo Ticket, đính kèm file |
| **FR-STU-03** | Xem & theo dõi yêu cầu | Danh sách Ticket của sinh viên |
| **FR-STU-04** | Nhận thông báo trạng thái | Nhận thông báo in-app (M04) |
| **FR-STU-05** | Bổ sung thông tin & phản hồi | Nhập trả lời bổ sung & Đánh giá CSAT |"""
    if old_m01_table in m01_content:
        m01_content = m01_content.replace(old_m01_table, new_m01_table)
        with open(m01_path, 'w', encoding='utf-8') as f:
            f.write(m01_content)

    # M02 README
    m02_path = 'd:/docs/03-modules/M02-staff-operations/README.md'
    with open(m02_path, 'r', encoding='utf-8') as f:
        m02_content = f.read()

    old_m02_table = """| **FR-STF-01** | Đăng nhập tài khoản Nhân viên | Xác thực Role và tải Ticket theo Phòng ban |
| **FR-STF-02** | Tiếp nhận & Phân công (Claim/Assign) | Nhận Ticket mới hoặc phân công cho đồng nghiệp |
| **FR-STF-03** | Phân loại & Ưu tiên | Cập nhật nhóm vấn đề và gán độ ưu tiên |
| **FR-STF-04** | Chuyển phòng ban (Transfer) | Điều phối Ticket sang phòng ban khác (kèm lý do) |
| **FR-STF-05** | Yêu cầu bổ sung hồ sơ | Yêu cầu sinh viên cấp thêm thông tin |
| **FR-STF-06** | Cập nhật kết quả & Đóng | Xử lý hoàn tất, trả kết quả và đóng Ticket |"""
    new_m02_table = """| **FR-STF-01** | Tiếp nhận, tìm kiếm & lọc yêu cầu | Lọc theo trạng thái, phòng ban, mức ưu tiên |
| **FR-STF-02** | Phân loại & phân công xử lý | Claim/Assign Ticket và chuẩn hóa nhóm vấn đề |
| **FR-STF-03** | Quản lý ưu tiên & thời hạn | Thiết lập mức ưu tiên và tính SLA |
| **FR-STF-04** | Xử lý & cập nhật yêu cầu | Yêu cầu bổ sung hồ sơ và lưu lịch sử xử lý |
| **FR-STF-05** | Chuyển xử lý, Escalation & hoàn tất | Chuyển phòng ban/người phụ trách và cập nhật kết quả |
| **FR-STF-06** | Đóng & mở lại yêu cầu | Đóng yêu cầu hoặc mở lại khi sinh viên phản hồi |"""
    if old_m02_table in m02_content:
        m02_content = m02_content.replace(old_m02_table, new_m02_table)
        with open(m02_path, 'w', encoding='utf-8') as f:
            f.write(m02_content)

    # M03 README
    m03_path = 'd:/docs/03-modules/M03-management-dashboard/README.md'
    with open(m03_path, 'r', encoding='utf-8') as f:
        m03_content = f.read()

    old_m03_table = """| **FR-MGT-01** | Đăng nhập tài khoản Quản lý | Đăng nhập bằng tài khoản có vai trò Quản lý (`MANAGER`). |
| **FR-MGT-02** | Dashboard tổng quan KPI | Xem các thẻ chỉ số (KPI Cards) và biểu đồ trực quan về khối lượng công việc, tình trạng quá hạn theo phòng ban. |
| **FR-MGT-03** | Báo cáo thời gian xử lý & Xu hướng | Báo cáo thời gian giải quyết trung bình (Average Resolution Time), xu hướng nhóm vấn đề và điểm CSAT trung bình. |
| **FR-MGT-04** | Quản lý tài khoản người dùng | Tạo mới, cập nhật thông tin, kích hoạt hoặc khóa/mở khóa tài khoản Sinh viên, Nhân viên và Quản lý. |
| **FR-MGT-05** | Phân quyền vai trò & Phòng ban | Gán vai trò (`STUDENT`, `STAFF`, `MANAGER`) và gán Phòng ban chuyên trách cho tài khoản. |
| **FR-MGT-06** | Tra soát nhật ký hệ thống (Audit Log) | Xem danh sách nhật ký ghi nhận các hành động quan trọng (Đổi trạng thái, Phân công, Chuyển phòng ban, Khóa tài khoản). |
| **FR-MGT-07** | Quản lý thời hạn lưu trữ | Cấu hình và quản lý thời hạn lưu trữ dữ liệu Ticket, File và Audit Log. |
| **FR-MGT-08** | Quản lý danh mục & xuất dữ liệu | Quản lý phòng ban/danh mục Ticket và xuất dữ liệu báo cáo theo quyền. |"""
    new_m03_table = """| **FR-MGT-01** | Quản lý tài khoản, vai trò & RBAC | Tạo/sửa/khóa tài khoản, gán vai trò, kiểm soát quyền truy cập theo vai trò. |
| **FR-MGT-02** | Quản lý phòng ban & danh mục | Quản lý phòng ban, nhóm vấn đề/danh mục Ticket và dữ liệu cấu hình. |
| **FR-MGT-03** | Kiểm soát quyền truy cập & Audit Trail | Áp dụng kiểm soát truy cập, bảo vệ dữ liệu/file theo quyền và ghi nhận nhật ký thao tác. |
| **FR-MGT-04** | Quản lý thời hạn lưu trữ | Xác định thời hạn lưu trữ dữ liệu Ticket, file đính kèm, log. |
| **FR-MGT-05** | Dashboard & thống kê quản trị | Dashboard KPI, tổng số Ticket, Ticket đang xử lý, quá hạn. |
| **FR-MGT-06** | Báo cáo, mức độ hài lòng & xuất dữ liệu | Báo cáo thời gian xử lý, xu hướng nhóm vấn đề, CSAT, phản hồi sinh viên. |"""
    if old_m03_table in m03_content:
        m03_content = m03_content.replace(old_m03_table, new_m03_table)
        with open(m03_path, 'w', encoding='utf-8') as f:
            f.write(m03_content)

update_readmes()
print("Updated READMEs")
