# Technical Decisions

Thư mục này chỉ ghi các quyết định kỹ thuật **không làm thay đổi phạm vi nghiệp vụ**. Nếu một lựa chọn chưa được nhóm kỹ thuật chốt, tài liệu phải để ở trạng thái đề xuất thay vì coi là cam kết với Client.

| ADR | Nội dung | Trạng thái |
| :--- | :--- | :--- |
| [ADR-001](./ADR-001-ticket-id-generation.md) | Nguyên tắc mã Ticket duy nhất | Baseline constraint |
| [ADR-002](./ADR-002-role-based-access-control.md) | Thực thi phân quyền 3 nhóm người dùng | Baseline constraint |
| [ADR-003](./ADR-003-file-attachment-storage.md) | Bảo vệ file đính kèm | Baseline constraint |

Các quyết định về framework, database engine, token/session, container, cloud hoặc đường dẫn API có thể được nhóm kỹ thuật chốt sau, miễn tuân thủ PRD/NFR.
