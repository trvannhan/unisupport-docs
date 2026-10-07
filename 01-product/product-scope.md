# Phạm Vi Sản Phẩm & Các Giả Định Dự Án (Product Scope & Assumptions)

## 1. Phạm Vi Chức Năng Sản Phẩm (Functional Scope)

UniSupport gồm **3 phân hệ chính** và một số năng lực dùng chung phục vụ toàn hệ thống.

### 1.1 Module Sinh viên (Student Portal)

- Đăng nhập hệ thống.
- Gửi yêu cầu hỗ trợ.
- Chọn nhóm vấn đề và nhập nội dung yêu cầu.
- Đính kèm file khi cần; phạm vi Proposal xác định loại file là ảnh/PDF.
- Nhận mã Ticket sau khi gửi thành công.
- Xem tiến độ xử lý và lịch sử cập nhật.
- Xem đơn vị/người phụ trách theo thông tin hệ thống cung cấp.
- Bổ sung thông tin hoặc giấy tờ khi nhân viên yêu cầu.
- Nhận thông báo và xem kết quả xử lý.
- Đánh giá mức độ hài lòng sau khi yêu cầu hoàn tất.

### 1.2 Module Nhân viên (Staff Operations)

- Đăng nhập hệ thống.
- Xem danh sách yêu cầu mới và các yêu cầu được giao.
- Phân loại yêu cầu theo nhóm vấn đề.
- Xem xét mức độ cần ưu tiên.
- Phân công hoặc chuyển yêu cầu sang đúng người/phòng ban khi cần.
- Cập nhật trạng thái xử lý.
- Yêu cầu sinh viên bổ sung thông tin hoặc giấy tờ.
- Ghi nhận kết quả và đóng yêu cầu sau khi hoàn thành.

### 1.3 Module Quản lý (Management Dashboard)

- Đăng nhập hệ thống.
- Xem số lượng yêu cầu mới, đang xử lý, sắp quá hạn hoặc đã quá hạn.
- Theo dõi tiến độ và khối lượng công việc theo phòng ban hoặc nhân viên.
- Xem xu hướng các nhóm yêu cầu.
- Xem thời gian xử lý trung bình.
- Xem tổng hợp phản hồi của sinh viên theo từng giai đoạn.
- Tạo/chỉnh sửa tài khoản và gán quyền phù hợp với từng vai trò.

### 1.4 Năng lực dùng chung

**Thông báo trong hệ thống**
- Cung cấp thông tin liên quan đến quá trình xử lý yêu cầu cho người dùng phù hợp.

**Bảo mật & phân quyền**
- Người dùng đăng nhập bằng tài khoản và mật khẩu riêng.
- Mỗi vai trò chỉ được xem và thao tác trong phạm vi quyền của mình.
- File đính kèm chỉ người liên quan được truy cập.
- Các thao tác quan trọng được ghi nhận để phục vụ tra soát.

> Các rule chi tiết như giới hạn dung lượng/số lượng file, thang điểm đánh giá, mức ưu tiên cụ thể, deadline/SLA và cơ chế thông báo chi tiết được đặc tả ở các phần liên quan khi đã có quyết định nghiệp vụ rõ ràng.

---

## 2. Các Hạng Mục Ngoài Phạm Vi (Out of Scope)

- Mobile App độc lập cho iOS/Android.
- Tích hợp bên thứ ba ngoài phạm vi đã thống nhất.
- Thiết lập sao lưu tự động, theo dõi vận hành máy chủ và hỗ trợ hạ tầng lâu dài.
- Phân quyền nhiều cấp và ghi lịch sử thao tác chi tiết ở mức nâng cao.
- Chat trực tiếp hoặc gọi thoại trong hệ thống.
- Tối ưu chịu tải lớn vượt quá quy mô khoảng 3.000 sinh viên.
- Chứng nhận bảo mật hoặc kiểm thử bảo mật chuyên sâu.

---

## 3. Giả Định Dự Án (Project Assumptions)

1. **Quy mô sử dụng**: Hệ thống phục vụ khoảng 3.000 sinh viên.
2. **Nền tảng**: Hệ thống được triển khai dưới dạng Web Application, không phải Mobile App độc lập.
3. **Ngôn ngữ**: Giao diện hỗ trợ Tiếng Việt và Tiếng Anh ở mức cơ bản.
4. **Hạ tầng**: Máy chủ và tên miền do Aurora University cung cấp; hiệu năng và tính ổn định phụ thuộc vào hạ tầng này.
5. **Tích hợp**: Không yêu cầu tích hợp bên thứ ba trong phạm vi hiện tại.
6. **Bảo mật**: Không yêu cầu chứng nhận bảo mật hoặc kiểm thử bảo mật chuyên sâu.
7. **Phản hồi/phê duyệt**: Thời gian chờ phản hồi hoặc phê duyệt từ phía Client không được tính vào thời gian triển khai theo kế hoạch.

---

## 4. Ràng Buộc Dự Án (Project Constraints)

- **Thời gian thực hiện**: 14 tuần.
- **Ngân sách**: 300.000.000 VNĐ.
- **Nghiệm thu chính thức**: 10 ngày làm việc kể từ khi bàn giao.
- **Bảo hành kỹ thuật**: 30 ngày kể từ ngày hai bên xác nhận nghiệm thu.
- **Thay đổi phạm vi**: Mọi điều chỉnh về phạm vi, chi phí hoặc tiến độ cần được hai bên xác nhận trước khi áp dụng.

---

## 5. Vị Trí Của Tài Liệu Chi Tiết

File này chỉ mô tả phạm vi sản phẩm ở mức cao. Chi tiết được tách sang các phần chuyên trách:

- `02-domain/`: trạng thái Ticket, lifecycle và business rules dùng chung.
- `03-modules/`: Functional Requirements, luồng chính, error flow và Acceptance Criteria.
- `04-workflows/`: các luồng nghiệp vụ xuyên nhiều chức năng/module.
- `05-non-functional-requirements/`: yêu cầu phi chức năng.
- `06-acceptance/`: traceability và test scenarios.
- `07-architecture/`: quyết định kỹ thuật và thiết kế triển khai.
