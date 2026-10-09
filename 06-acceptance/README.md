# 06 - Nghiệm Thu Và Truy Xuất Yêu Cầu

Thư mục này dùng để đối chiếu phạm vi đã cam kết, Resource nội bộ, Functional Requirements và kịch bản UAT của UniSupport.

## 1. Tài Liệu

| Tài liệu | Mục đích |
| :--- | :--- |
| [traceability-matrix.md](./traceability-matrix.md) | Liên kết Resource WP → FR/Flow → Workflow → UAT. |
| [test-scenarios.md](./test-scenarios.md) | Các kịch bản UAT đại diện cho ba phân hệ và năng lực dùng chung. |

## 2. Nguyên Tắc Nghiệm Thu

- Aurora University có **10 ngày làm việc sau bàn giao chính thức** để thực hiện nghiệm thu theo Proposal.
- Các luồng chính của M01, M02, M03 phải hoạt động đúng.
- Phân quyền phải đúng theo vai trò và phạm vi dữ liệu.
- Không còn lỗi làm gián đoạn chức năng chính.
- Tài liệu bàn giao phải đầy đủ theo cam kết.
- Lỗi kỹ thuật không ảnh hưởng chức năng chính được ghi nhận và có kế hoạch khắc phục, không tự động trở thành điều kiện từ chối nghiệm thu.

## 3. Nguyên Tắc Truy Xuất

- Không thay đổi effort hoặc các dòng Resource đã chốt.
- Một Work Package có thể ánh xạ tới nhiều FR/Flow.
- Đăng nhập/xác thực là năng lực dùng chung; không nhân đôi effort chỉ vì mỗi phân hệ đều có FR truy cập.
- Nhãn **M3 – Admin** trong Resource là tên nhóm công việc quản trị, không tạo vai trò `ADMIN` thứ tư.
