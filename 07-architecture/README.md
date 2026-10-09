# 07 - Kiến Trúc Hệ Thống

Thư mục này mô tả kiến trúc kỹ thuật ở mức đủ để đội phát triển triển khai UniSupport mà không thay đổi phạm vi nghiệp vụ đã chốt.

## 1. Nguyên Tắc

- UniSupport là **Web Application** phục vụ ba phân hệ M01, M02, M03.
- Kiến trúc ưu tiên đơn giản, phù hợp quy mô khoảng 3.000 sinh viên và thời gian triển khai 14 tuần.
- Thông báo, xác thực, phân quyền và Audit là năng lực dùng chung; không tạo thêm module nghiệp vụ M04/M05.
- Không yêu cầu kiến trúc phân tán phức tạp, auto-scaling hoặc tích hợp bên thứ ba trong baseline.
- Công nghệ cụ thể có thể được nhóm kỹ thuật lựa chọn miễn không làm thay đổi PRD/NFR và phù hợp hạ tầng Client.

## 2. Tài Liệu

| Tài liệu | Nội dung |
| :--- | :--- |
| [system-context.md](./system-context.md) | Actor, ranh giới hệ thống và hệ thống bên ngoài. |
| [architecture-overview.md](./architecture-overview.md) | Thành phần Frontend, Backend, dữ liệu và file. |
| [data-model.md](./data-model.md) | Mô hình dữ liệu triển khai ở mức logic. |
| [api-design.md](./api-design.md) | Nguyên tắc giao tiếp giữa giao diện và Backend. |
| [security-design.md](./security-design.md) | Thiết kế xác thực, phân quyền, file và Audit. |
| [technical-decisions/](./technical-decisions/) | Các quyết định kỹ thuật có thể thay đổi mà không đổi nghiệp vụ. |
