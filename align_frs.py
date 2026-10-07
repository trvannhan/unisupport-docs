import os
import re

def align_m01():
    path = 'd:/docs/03-modules/M01-student-portal/prd.md'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Xóa FR-STU-01 Đăng nhập (từ dòng 49 đến dòng 87)
    content = re.sub(r'### \[FR-STU-01\] Đăng nhập tài khoản Sinh viên.*?---', '', content, flags=re.DOTALL)
    
    # Đổi FR-STU-00 thành FR-STU-01
    content = content.replace('### [FR-STU-00] Tra cứu hướng dẫn & FAQ', '### [FR-STU-01] Tra cứu hướng dẫn & FAQ')
    
    # Đổi tên FR-STU-02
    content = content.replace('### [FR-STU-02] Sinh viên gửi yêu cầu hỗ trợ', '### [FR-STU-02] Tạo & gửi yêu cầu hỗ trợ')
    
    # Đổi tên FR-STU-03
    content = content.replace('### [FR-STU-03] Xem danh sách & Theo dõi tiến độ xử lý Ticket', '### [FR-STU-03] Xem & theo dõi yêu cầu')

    # Đổi tên FR-STU-04 và gộp FR-STU-05
    # Thêm FR-STU-04 Nhận thông báo trạng thái
    notification_fr = """### [FR-STU-04] Nhận thông báo trạng thái

**Mô tả**
Nhận thông báo trong hệ thống khi Ticket được tiếp nhận, yêu cầu bổ sung, chuyển trạng thái hoặc hoàn tất (liên kết với Module Notification M04).

---

"""
    content = content.replace('### [FR-STU-04] Phản hồi & Bổ sung thông tin / Hồ sơ theo yêu cầu', notification_fr + '### [FR-STU-05] Bổ sung thông tin & phản hồi')
    
    # Gộp nội dung của CSAT vào FR-STU-05 thay vì tạo riêng FR-STU-06
    content = content.replace('### [FR-STU-05] Xem kết quả giải quyết & Đánh giá mức độ hài lòng (CSAT)', '#### Tích hợp: Xem kết quả giải quyết & Đánh giá mức độ hài lòng (CSAT)')

    # Sửa bảng Danh mục
    old_table = """| **FR-STU-00** | Tra cứu hướng dẫn & FAQ | Xem FAQ theo nhóm vấn đề, gợi ý phòng ban và tạo Ticket trực tiếp. |
| **FR-STU-01** | Đăng nhập tài khoản | Đăng nhập bằng Mã SV/Email + Mật khẩu. Hỗ trợ khóa 5 phút sau 5 lần sai. |
| **FR-STU-02** | Gửi yêu cầu hỗ trợ | Form tạo Ticket, đính kèm max 3 file (PDF/PNG/JPG). Sinh mã Ticket duy nhất. |
| **FR-STU-03** | Xem danh sách & theo dõi | Danh sách Ticket sắp xếp mới nhất, chi tiết timeline, file đính kèm, người thụ lý. |
| **FR-STU-04** | Phản hồi & bổ sung | Nhập câu trả lời + upload file. Tự động chuyển trạng thái để tiếp tục đếm SLA. |
| **FR-STU-05** | Đánh giá CSAT | Xem kết quả + Đánh giá 1-5 sao kèm nhận xét (1 lần duy nhất, hạn 7 ngày). |"""
    new_table = """| **FR-STU-01** | Tra cứu hướng dẫn & FAQ | Xem FAQ theo nhóm vấn đề, gợi ý phòng ban và tạo Ticket trực tiếp. |
| **FR-STU-02** | Tạo & gửi yêu cầu hỗ trợ | Form tạo Ticket, đính kèm max 3 file (PDF/PNG/JPG). Sinh mã Ticket duy nhất. |
| **FR-STU-03** | Xem & theo dõi yêu cầu | Danh sách Ticket sắp xếp mới nhất, chi tiết timeline, file đính kèm, người thụ lý. |
| **FR-STU-04** | Nhận thông báo trạng thái | Nhận thông báo in-app (M04) khi Ticket chuyển trạng thái, yêu cầu bổ sung. |
| **FR-STU-05** | Bổ sung thông tin & phản hồi | Nhập câu trả lời, upload file bổ sung. Xem kết quả và Đánh giá CSAT (1-5 sao). |"""
    content = content.replace(old_table, new_table)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def align_m02():
    path = 'd:/docs/03-modules/M02-staff-operations/prd.md'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Bỏ FR-STF-01 Đăng nhập
    content = re.sub(r'### \[FR-STF-01\] Đăng nhập tài khoản Nhân viên.*?---', '', content, flags=re.DOTALL)

    # Thêm FR-STF-01 Tìm kiếm & Lọc
    search_fr = """### [FR-STF-01] Tiếp nhận, tìm kiếm & lọc yêu cầu

**Mô tả**
Xem danh sách yêu cầu mới/được giao, tìm kiếm, lọc theo trạng thái, phòng ban, mức ưu tiên và người phụ trách.

---

"""
    content = content.replace('### [FR-STF-02] Tiếp nhận (Claim) & Phân công (Assign) Ticket', search_fr + '### [FR-STF-02] Phân loại & phân công xử lý')
    
    content = content.replace('### [FR-STF-03] Phân loại (Triage) & Quản lý độ ưu tiên', '### [FR-STF-03] Quản lý ưu tiên & thời hạn')
    
    content = content.replace('### [FR-STF-05] Yêu cầu bổ sung hồ sơ (Request Supplement)', '### [FR-STF-04] Xử lý & cập nhật yêu cầu')
    
    content = content.replace('### [FR-STF-04] Chuyển phòng ban chuyên trách & Escalation (Transfer & Escalation)', '### [FR-STF-05] Chuyển xử lý, Escalation & hoàn tất')
    
    content = content.replace('### [FR-STF-06] Cập nhật kết quả & Đóng / Mở lại Ticket', '### [FR-STF-06] Đóng & mở lại yêu cầu')

    old_table = """| **FR-STF-01** | Đăng nhập NV | Đăng nhập bằng Email/Mã NV + MK. Kiểm tra Role=STAFF/MANAGER. Chỉ nạp Ticket thuộc phòng ban được phân quyền. |
| **FR-STF-02** | Tiếp nhận & Phân công | Claim Ticket chưa có chủ hoặc Assign cho NV cùng phòng ban. Đảm bảo Race condition: chỉ 1 người nhận thành công. |
| **FR-STF-03** | Phân loại & Ưu tiên | Điều chỉnh Nhóm vấn đề, thiết lập Mức ưu tiên. SLA tính lại từ thời điểm tạo Ticket gốc theo mức ưu tiên mới. |
| **FR-STF-04** | Chuyển phòng ban | Chọn phòng ban đích + nhập lý do bắt buộc. Sau khi chuyển, NV cũ mất quyền chỉnh sửa. |
| **FR-STF-05** | Yêu cầu bổ sung | Nhập nội dung bổ sung -> trạng thái WAITING_STUDENT, SLA tạm dừng, thông báo cho sinh viên. |
| **FR-STF-06** | Cập nhật kết quả & Đóng | Nhập nội dung kết quả + file. Ticket chuyển RESOLVED. Sau 3 ngày không tương tác -> tự động CLOSED. |"""
    new_table = """| **FR-STF-01** | Tiếp nhận, tìm kiếm & lọc yêu cầu | Xem danh sách yêu cầu mới/được giao, tìm kiếm, lọc theo trạng thái, phòng ban, mức ưu tiên và người phụ trách. |
| **FR-STF-02** | Phân loại & phân công xử lý | Claim Ticket chưa có chủ hoặc Assign cho NV cùng phòng ban, chuẩn hóa phân loại. |
| **FR-STF-03** | Quản lý ưu tiên & thời hạn | Điều chỉnh Mức ưu tiên. SLA tính lại và cảnh báo quá hạn. |
| **FR-STF-04** | Xử lý & cập nhật yêu cầu | Ghi nhận tiến độ, trao đổi với sinh viên, yêu cầu bổ sung thông tin/hồ sơ và lưu lịch sử xử lý. |
| **FR-STF-05** | Chuyển xử lý, Escalation & hoàn tất | Chuyển phòng ban/người phụ trách khi cần, escalation các trường hợp khó và cập nhật kết quả. |
| **FR-STF-06** | Đóng & mở lại yêu cầu | Đóng yêu cầu sau khi hoàn tất hoặc mở lại khi sinh viên phản hồi/chưa hài lòng. |"""
    content = content.replace(old_table, new_table)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def align_m03():
    path = 'd:/docs/03-modules/M03-management-dashboard/prd.md'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Bỏ Đăng nhập
    content = re.sub(r'### \[FR-MGT-01\] Đăng nhập tài khoản Quản lý.*?---', '', content, flags=re.DOTALL)
    
    content = content.replace('### [FR-MGT-04] Quản lý tài khoản người dùng (User Management)', '### [FR-MGT-01] Quản lý tài khoản, vai trò & RBAC')
    content = content.replace('### [FR-MGT-05] Quản lý phân quyền vai trò & Phòng ban (RBAC & Department Assignment)', '#### Tích hợp: Phân quyền vai trò & Phòng ban')
    
    content = content.replace('### [FR-MGT-08] Quản lý phòng ban, danh mục & xuất dữ liệu', '### [FR-MGT-02] Quản lý phòng ban & danh mục')
    content = content.replace('### [FR-MGT-06] Tra soát nhật ký hệ thống (Audit Log / Activity Log)', '### [FR-MGT-03] Kiểm soát quyền truy cập & Audit Trail')
    content = content.replace('### [FR-MGT-07] Quản lý thời hạn lưu trữ (Data Retention)', '### [FR-MGT-04] Quản lý thời hạn lưu trữ')
    content = content.replace('### [FR-MGT-02] Dashboard tổng quan & Chỉ số KPI vận hành', '### [FR-MGT-05] Dashboard & thống kê quản trị')
    content = content.replace('### [FR-MGT-03] Báo cáo thời gian xử lý & Xu hướng nhóm vấn đề', '### [FR-MGT-06] Báo cáo, mức độ hài lòng & xuất dữ liệu')
    
    old_table = """| **FR-MGT-01** | Đăng nhập Quản lý | Xác thực tài khoản MANAGER/ADMIN. Dashboard tự động phân quyền dữ liệu theo vai trò. |
| **FR-MGT-02** | Dashboard KPI | Thẻ KPI: Tổng Ticket, Đang xử lý, Quá hạn SLA, CSAT TB. Biểu đồ tỷ lệ trạng thái + khối lượng theo phòng ban. |
| **FR-MGT-03** | Báo cáo & Phân tích | Thời gian xử lý TB, Top 5 nhóm vấn đề, báo cáo CSAT chi tiết. |
| **FR-MGT-04** | Quản lý tài khoản | Tạo/cập nhật/khóa tài khoản. Email + Mã định danh DUY NHẤT. |
| **FR-MGT-05** | Phân quyền RBAC | Gán Role (STUDENT/STAFF/MANAGER/ADMIN) + gán phòng ban. |
| **FR-MGT-06** | Audit Log | Bảng nhật ký: Thời gian, Tác nhân, Hành động, Chi tiết, IP. Cấm UPDATE/DELETE. |
| **FR-MGT-07** | Quản lý danh mục | CRUD Phòng ban/Danh mục. Không xóa cứng nếu đã có Ticket. Xuất dữ liệu báo cáo. |"""
    new_table = """| **FR-MGT-01** | Quản lý tài khoản, vai trò & RBAC | Tạo/sửa/khóa tài khoản, gán vai trò, kiểm soát quyền truy cập theo vai trò. |
| **FR-MGT-02** | Quản lý phòng ban & danh mục | Quản lý phòng ban, nhóm vấn đề/danh mục Ticket và dữ liệu cấu hình. |
| **FR-MGT-03** | Kiểm soát quyền truy cập & Audit Trail | Áp dụng kiểm soát truy cập, bảo vệ dữ liệu/file theo quyền và ghi nhận nhật ký thao tác. |
| **FR-MGT-04** | Quản lý thời hạn lưu trữ | Xác định thời hạn lưu trữ dữ liệu Ticket, file đính kèm, log. |
| **FR-MGT-05** | Dashboard & thống kê quản trị | Dashboard KPI, tổng số Ticket, Ticket đang xử lý, quá hạn, khối lượng theo phòng ban/nhân viên. |
| **FR-MGT-06** | Báo cáo, mức độ hài lòng & xuất dữ liệu | Báo cáo thời gian xử lý, xu hướng nhóm vấn đề, CSAT, phản hồi sinh viên và xuất dữ liệu. |"""
    content = content.replace(old_table, new_table)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

align_m01()
align_m02()
align_m03()
print("Aligned M01, M02, M03 PRDs with WP Resource Table.")
