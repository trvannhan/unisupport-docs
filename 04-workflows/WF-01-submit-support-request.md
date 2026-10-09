# WF-01 - Gửi Yêu Cầu Hỗ Trợ

## 1. Mục Đích Và Phạm Vi

Mô tả luồng từ khi sinh viên tạo yêu cầu đến khi hệ thống tạo Ticket thành công, xác định phòng ban tiếp nhận và trả mã Ticket cho sinh viên.

## 2. Vai Trò Và Điều Kiện Bắt Đầu

- **Vai trò chính:** Sinh viên.
- Sinh viên đã đăng nhập bằng tài khoản hợp lệ.
- Danh mục **Nhóm vấn đề (Category)** đang hoạt động và mỗi Category có phòng ban tiếp nhận được cấu hình.

## 3. Luồng Nghiệp Vụ Chính

1. Sinh viên mở chức năng **Tạo yêu cầu**.
2. Hệ thống hiển thị danh sách Nhóm vấn đề đang hoạt động.
3. Sinh viên chọn một Nhóm vấn đề và nhập nội dung mô tả yêu cầu.
4. Sinh viên đính kèm tài liệu minh chứng nếu cần.
5. Sinh viên xác nhận gửi.
6. Hệ thống kiểm tra dữ liệu bắt buộc và file đính kèm.
7. Hệ thống xác định phòng ban tiếp nhận từ cấu hình của Nhóm vấn đề đã chọn.
8. Hệ thống tạo một Ticket, cấp mã Ticket duy nhất, đặt trạng thái `NEW`, mức độ ưu tiên mặc định `MEDIUM` và xác định thời hạn xử lý.
9. Hệ thống ghi nhận sự kiện tạo Ticket vào lịch sử.
10. Sinh viên nhận thông báo tạo thành công và xem được mã Ticket.

## 4. Luồng Ngoại Lệ

- Thiếu Nhóm vấn đề hoặc nội dung yêu cầu: không tạo Ticket.
- Nhóm vấn đề đã bị vô hiệu hóa trước thời điểm gửi: yêu cầu sinh viên chọn lại.
- File sai định dạng, vượt dung lượng hoặc vượt số lượng cho phép: từ chối file không hợp lệ.
- Thao tác gửi lặp từ cùng một lần xác nhận: không được tạo nhiều Ticket trùng nhau.

## 5. Quy Tắc Nghiệp Vụ

- Sinh viên chỉ chọn Category có sẵn, không tự nhập hoặc tạo Category mới.
- Nội dung yêu cầu từ 20 đến 2.000 ký tự và không được chỉ chứa khoảng trắng.
- Tối đa 03 file/lần, tối đa 10 MB/file, định dạng PDF/PNG/JPG/JPEG.
- Phòng ban tiếp nhận được xác định từ Category, sinh viên không tự chọn người phụ trách.
- Đồng hồ thời hạn bắt đầu khi Ticket được tạo thành công.

## 6. Tiêu Chí Nghiệm Thu

- Dữ liệu hợp lệ tạo đúng một Ticket ở `NEW`.
- Ticket có đúng sinh viên, Category, phòng ban tiếp nhận, mức `MEDIUM` và mã Ticket duy nhất.
- Dữ liệu hoặc file không hợp lệ không làm phát sinh Ticket.
- Sinh viên nhận được xác nhận và mã Ticket sau khi tạo thành công.

## 7. Tài Liệu Liên Quan

- M01: `FR-STU-02`, `FR-STU-04`.
- Domain: `BR-FILE-01`, `BR-FILE-02`, `BR-DUE-01`.
