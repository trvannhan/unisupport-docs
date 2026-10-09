# 03 - Functional Modules

Thư mục `03-modules` đặc tả yêu cầu chức năng của **UniSupport** theo ba phân hệ nghiệp vụ chính. Nội dung tại đây được xây dựng trên các quy tắc và mô hình nghiệp vụ đã xác lập trong `02-domain`.

## Các Phân Hệ Nghiệp Vụ Chính

| Phân hệ | Phạm vi |
| :--- | :--- |
| [M01 - Student Portal](./M01-student-portal/) | Tra cứu hướng dẫn, tạo Ticket, theo dõi tiến độ, bổ sung thông tin, nhận kết quả và đánh giá mức độ hài lòng. |
| [M02 - Staff Operations](./M02-staff-operations/) | Tiếp nhận, phân loại, phân công, xử lý, chuyển/escalation, yêu cầu bổ sung, ghi nhận kết quả và quản lý vòng đời Ticket. |
| [M03 - Management Dashboard](./M03-management-dashboard/) | Giám sát hoạt động hỗ trợ, Dashboard/báo cáo và các chức năng quản trị được phân quyền. |

## Năng Lực Dùng Chung

Một số chức năng được áp dụng xuyên suốt các phân hệ và không được xem là phân hệ nghiệp vụ độc lập:

- **Notification:** tạo và hiển thị thông báo khi phát sinh các sự kiện Ticket liên quan.
- **Authentication, RBAC & Security:** xác thực, kiểm soát quyền truy cập và bảo vệ dữ liệu theo vai trò/phạm vi trách nhiệm.

Các thư mục hỗ trợ tương ứng có thể được sử dụng để đặc tả chi tiết kỹ thuật hoặc yêu cầu dùng chung, nhưng không làm thay đổi mô hình ba phân hệ nghiệp vụ của UniSupport.

## Cấu Trúc Đặc Tả

Mỗi phân hệ gồm:

- `README.md`: phạm vi, mục tiêu, work package và quan hệ với các phần còn lại.
- `prd.md`: Functional Requirements, điều kiện tiên quyết, luồng chính, luồng ngoại lệ, Business Rules và Acceptance Criteria.

Các trạng thái Ticket, thời hạn xử lý, quy tắc file đính kèm, mở lại Ticket và CSAT phải tuân thủ thống nhất theo [02-domain](../02-domain/).
