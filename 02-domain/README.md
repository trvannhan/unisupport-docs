# 02 - Domain

Thư mục này mô tả các khái niệm nghiệp vụ cốt lõi, mô hình Ticket, vòng đời xử lý và các quy tắc dùng chung trong hệ thống **UniSupport**.

Mục tiêu của phần Domain là giúp BA, Dev và QA hiểu thống nhất:
- Ticket là gì và gồm những thông tin nghiệp vụ nào.
- Các thuật ngữ được sử dụng trong hệ thống.
- Ticket thay đổi trạng thái như thế nào trong quá trình xử lý.
- Những quy tắc nghiệp vụ nào được áp dụng xuyên suốt các phân hệ.

## Tài liệu trong thư mục

| Tài liệu | Nội dung |
| :--- | :--- |
| [Domain Overview](./domain-overview.md) | Tổng quan miền nghiệp vụ, các khái niệm cốt lõi và luồng xử lý Ticket ở mức tổng quan. |
| [Terminology](./terminology.md) | Định nghĩa các thuật ngữ nghiệp vụ được sử dụng thống nhất trong toàn hệ thống. |
| [Ticket Model](./ticket-model.md) | Mô tả các thông tin nghiệp vụ chính của Ticket và các dữ liệu liên quan. |
| [Ticket Lifecycle](./ticket-lifecycle.md) | Mô tả các giai đoạn mà Ticket trải qua từ khi được tạo đến khi hoàn tất. |
| [State Transition](./state-transition.md) | Quy định các trạng thái Ticket và những chuyển đổi trạng thái hợp lệ. |
| [Business Rules](./business-rules.md) | Tổng hợp các quy tắc nghiệp vụ dùng chung như file đính kèm, phân công/chuyển xử lý, bổ sung thông tin, thời hạn xử lý, CSAT và Audit. |

## Thứ tự đọc đề xuất

1. [Domain Overview](./domain-overview.md)
2. [Terminology](./terminology.md)
3. [Ticket Model](./ticket-model.md)
4. [Ticket Lifecycle](./ticket-lifecycle.md)
5. [State Transition](./state-transition.md)
6. [Business Rules](./business-rules.md)

Sau khi hoàn thành phần Domain, tiếp tục với [03-modules](../03-modules/) để xem Functional Requirements và Acceptance Criteria của từng phân hệ.
