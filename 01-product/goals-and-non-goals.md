# Mục Tiêu Dự Án & Các Mục Nằm Ngoài Phạm Vi (Goals & Non-Goals)

## 1. Mục Tiêu Cốt Lõi (Core Goals)

### G-01: Tập trung hóa đầu mối tiếp nhận
- **Mục tiêu**: Cung cấp một kênh thống nhất để sinh viên gửi yêu cầu hỗ trợ và theo dõi quá trình xử lý.
- **Kết quả mong đợi**: Mỗi yêu cầu được tạo thành công trên hệ thống có mã Ticket để phục vụ tra cứu và theo dõi.

### G-02: Minh bạch hóa tiến độ xử lý
- **Mục tiêu**: Giúp sinh viên theo dõi trạng thái hiện tại và đơn vị/người phụ trách xử lý yêu cầu.
- **Kết quả mong đợi**: Sinh viên có thể xem tiến độ và lịch sử cập nhật trực tiếp trên hệ thống.

### G-03: Chuẩn hóa quy trình vận hành
- **Mục tiêu**: Hỗ trợ nhân viên phân loại, phân công/chuyển xử lý, cập nhật trạng thái, yêu cầu bổ sung và ghi nhận kết quả theo một quy trình thống nhất.
- **Kết quả mong đợi**: Giảm nguy cơ bỏ sót, xử lý trùng lặp và phản hồi không thống nhất giữa các phòng ban.

### G-04: Nâng cao năng lực giám sát
- **Mục tiêu**: Cung cấp Dashboard và báo cáo về khối lượng công việc, tình trạng xử lý, yêu cầu quá hạn, nhóm vấn đề thường gặp, thời gian xử lý và phản hồi sinh viên.
- **Kết quả mong đợi**: Ban quản lý có dữ liệu để theo dõi và hỗ trợ điều phối hoạt động.

### G-05: Đảm bảo phân quyền và an toàn dữ liệu cơ bản
- **Mục tiêu**: Đảm bảo người dùng chỉ xem và thao tác trong phạm vi quyền được cấp.
- **Kết quả mong đợi**: File đính kèm chỉ người liên quan được truy cập và các thao tác quan trọng được ghi nhận để tra soát.

---

## 2. Các Mục Nằm Ngoài Phạm Vi Hiện Tại (Out of Scope / Non-Goals)

| STT | Hạng mục ngoài phạm vi | Giải thích |
| :---: | :--- | :--- |
| **NG-01** | **Mobile App độc lập (iOS / Android)** | Hệ thống được triển khai dưới dạng Web Application, không xây dựng ứng dụng native riêng. |
| **NG-02** | **Tích hợp bên thứ ba ngoài phạm vi đã thống nhất** | Không triển khai các tích hợp với hệ thống bên ngoài nếu chưa nằm trong phạm vi đã xác nhận. |
| **NG-03** | **Sao lưu tự động và vận hành hạ tầng dài hạn** | Không bao gồm thiết lập backup tự động, theo dõi vận hành máy chủ và hỗ trợ hạ tầng lâu dài. |
| **NG-04** | **Phân quyền nhiều cấp và Audit Log nâng cao** | Chỉ triển khai phân quyền và ghi nhận thao tác ở mức cần thiết cho phạm vi hiện tại; không bao gồm mô hình phân quyền nhiều cấp phức tạp hoặc audit chi tiết nâng cao. |
| **NG-05** | **Chat trực tiếp / Gọi thoại** | Không triển khai live chat hoặc voice call trong hệ thống. |
| **NG-06** | **Tối ưu chịu tải lớn vượt quy mô dự án** | Hệ thống hướng tới quy mô khoảng 3.000 sinh viên, không bao gồm yêu cầu tối ưu cho quy mô lớn hơn đáng kể. |
| **NG-07** | **Chứng nhận hoặc kiểm thử bảo mật chuyên sâu** | Không bao gồm chứng nhận bảo mật hoặc kiểm thử bảo mật chuyên sâu bởi bên thứ ba. |
