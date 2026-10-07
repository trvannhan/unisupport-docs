# Tổng Quan Sản Phẩm - UniSupport (Product Overview)

## 1. Tóm Tắt Dự Án (Executive Summary)

**UniSupport** là hệ thống Web Application hỗ trợ quản lý tập trung các yêu cầu hỗ trợ sinh viên tại **Aurora University**. Hệ thống hướng tới chuẩn hóa quy trình tiếp nhận, xử lý và theo dõi yêu cầu, giảm sự phụ thuộc vào các kênh rời rạc như email, biểu mẫu trực tuyến và tin nhắn.

Hệ thống phục vụ quy mô khoảng **3.000 sinh viên**, đồng thời hỗ trợ nhân viên các phòng ban và ban quản lý theo dõi, xử lý và giám sát tình hình hỗ trợ sinh viên.

---

## 2. Bài Toán Nghiệp Vụ (Problem Statement)

Hiện tại, yêu cầu hỗ trợ sinh viên được tiếp nhận qua nhiều kênh rời rạc và mỗi phòng ban có thể sử dụng cách quản lý riêng. Điều này dẫn đến các vấn đề chính:

- Yêu cầu bị phân tán, khó tra cứu lịch sử hỗ trợ thống nhất.
- Có nguy cơ bỏ sót hoặc xử lý trùng lặp.
- Sinh viên khó biết trạng thái và đơn vị/người đang phụ trách.
- Quy trình phân loại, chuyển tiếp và phản hồi giữa các phòng ban chưa đồng nhất.
- Ban quản lý thiếu số liệu tổng hợp để theo dõi và điều phối hoạt động.

UniSupport giải quyết các vấn đề này bằng cách tập trung yêu cầu trên một hệ thống Ticket, chuẩn hóa luồng xử lý và cung cấp dữ liệu phục vụ theo dõi, báo cáo.

---

## 3. Mục Tiêu Sản Phẩm (Product Goals)

### G-01: Tập trung hóa đầu mối tiếp nhận
Cung cấp một kênh thống nhất để sinh viên gửi yêu cầu hỗ trợ và theo dõi quá trình xử lý. Mỗi yêu cầu được tạo thành công có mã Ticket để phục vụ tra cứu.

### G-02: Minh bạch hóa tiến độ xử lý
Giúp sinh viên theo dõi trạng thái hiện tại, lịch sử cập nhật và đơn vị/người phụ trách xử lý yêu cầu.

### G-03: Chuẩn hóa quy trình vận hành
Hỗ trợ nhân viên phân loại, phân công/chuyển xử lý, cập nhật trạng thái, yêu cầu bổ sung và ghi nhận kết quả theo một quy trình thống nhất.

### G-04: Nâng cao năng lực giám sát
Cung cấp Dashboard và báo cáo để ban quản lý theo dõi khối lượng công việc, tình trạng xử lý, yêu cầu quá hạn, nhóm vấn đề thường gặp, thời gian xử lý và phản hồi sinh viên.

### G-05: Đảm bảo phân quyền và an toàn dữ liệu cơ bản
Đảm bảo người dùng chỉ xem và thao tác trong phạm vi quyền được cấp; file đính kèm chỉ người liên quan được truy cập và các thao tác quan trọng được ghi nhận để tra soát.

---

## 4. Các Phân Hệ Chính

UniSupport gồm **3 phân hệ chính**:

| Mã phân hệ | Tên phân hệ | Chức năng cốt lõi |
| :--- | :--- | :--- |
| **M01** | **Sinh viên (Student Portal)** | Đăng nhập, gửi yêu cầu hỗ trợ, đính kèm file ảnh/PDF, nhận mã Ticket, theo dõi tiến độ, bổ sung hồ sơ, nhận thông báo trạng thái, xem kết quả và đánh giá mức độ hài lòng. |
| **M02** | **Nhân viên (Staff Operations)** | Đăng nhập, xem danh sách yêu cầu mới/được giao, phân loại, xem xét mức độ ưu tiên, chuyển phòng ban/người phụ trách, cập nhật trạng thái, yêu cầu sinh viên bổ sung và ghi nhận kết quả xử lý. |
| **M03** | **Quản lý (Management Dashboard)** | Đăng nhập, theo dõi tổng quan tình hình xử lý, khối lượng công việc, báo cáo xu hướng/thời gian xử lý/phản hồi sinh viên và quản lý tài khoản/phân quyền. |

### Năng lực dùng chung

- **Thông báo trong hệ thống**: hỗ trợ người dùng nhận các thông tin liên quan đến quá trình xử lý Ticket.
- **Bảo mật & phân quyền**: xác thực người dùng, giới hạn quyền truy cập theo vai trò, bảo vệ file đính kèm và ghi nhận các thao tác quan trọng để tra soát.

---

## 5. Ngoài Phạm Vi (Non-Goals)

- Mobile App độc lập cho iOS/Android.
- Tích hợp bên thứ ba ngoài phạm vi đã thống nhất.
- Thiết lập sao lưu tự động, theo dõi vận hành máy chủ và hỗ trợ hạ tầng lâu dài.
- Phân quyền nhiều cấp và Audit Log nâng cao.
- Chat trực tiếp hoặc gọi thoại trong hệ thống.
- Tối ưu chịu tải lớn vượt quá quy mô khoảng 3.000 sinh viên.
- Chứng nhận bảo mật hoặc kiểm thử bảo mật chuyên sâu.

---

## 6. Hình Thức Triển Khai

- **Loại hình ứng dụng**: Web Application.
- **Thiết bị sử dụng**: Trình duyệt trên máy tính và thiết bị di động.
- **Ngôn ngữ giao diện**: Tiếng Việt và Tiếng Anh ở mức cơ bản.
- **Hạ tầng triển khai**: Sử dụng hạ tầng máy chủ và tên miền do Aurora University cung cấp.

---

## 7. Thông Số Dự Án

- **Quy mô phục vụ**: Khoảng 3.000 sinh viên.
- **Thời gian thực hiện**: 14 tuần.
- **Tổng kinh phí**: 300.000.000 VNĐ.
- **Thời gian nghiệm thu chính thức**: 10 ngày làm việc sau bàn giao.
- **Thời gian bảo hành kỹ thuật**: 30 ngày kể từ ngày nghiệm thu.
