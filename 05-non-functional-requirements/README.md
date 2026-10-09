# 05 - Yêu Cầu Phi Chức Năng

Thư mục này mô tả các yêu cầu chất lượng dùng chung cho UniSupport. Nội dung bám theo Proposal, phạm vi 3 phân hệ và quy mô khoảng 3.000 sinh viên; không tự mở rộng thành các cam kết kỹ thuật hoặc hạ tầng chưa được thống nhất.

## 1. Danh Sách Tài Liệu

| Tài liệu | Phạm vi |
| :--- | :--- |
| [performance.md](./performance.md) | Hiệu năng phù hợp quy mô dự án. |
| [reliability.md](./reliability.md) | Tính ổn định và toàn vẹn dữ liệu nghiệp vụ. |
| [security.md](./security.md) | Xác thực, phân quyền, bảo vệ file và tra soát. |
| [usability.md](./usability.md) | Web responsive và hỗ trợ Việt/Anh ở mức cơ bản. |
| [deployment.md](./deployment.md) | Điều kiện triển khai và bàn giao trên hạ tầng Client. |
| [observability.md](./observability.md) | Ghi log kỹ thuật cơ bản và nhật ký tra soát nghiệp vụ. |

## 2. Nguyên Tắc

- NFR không tạo thêm phân hệ nghiệp vụ ngoài M01, M02, M03.
- Các giới hạn nghiệp vụ như file 10 MB, trạng thái Ticket, quyền truy cập và Audit phải nhất quán với Domain/PRD.
- Proposal không cam kết chỉ số tải lớn, chứng nhận bảo mật hoặc kiểm thử bảo mật chuyên sâu; tài liệu này không tự tạo các cam kết đó.
- Công nghệ triển khai cụ thể thuộc `07-architecture`, không phải yêu cầu sản phẩm.
