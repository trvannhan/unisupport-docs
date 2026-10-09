# WF-04 - Chuyển Xử Lý Sang Phòng Ban Khác

## 1. Mục Đích Và Phạm Vi

Mô tả cách Ticket được chuyển sang **phòng ban khác** khi nội dung thực tế thuộc phạm vi xử lý khác. Đổi người phụ trách trong cùng phòng ban không dùng Workflow này mà thực hiện bằng phân công lại.

## 2. Vai Trò Và Điều Kiện Bắt Đầu

- **Vai trò:** Nhân viên hoặc Quản lý có quyền chuyển xử lý.
- Ticket thuộc phạm vi được phép thao tác.
- Ticket đang ở `NEW`, `IN_PROGRESS` hoặc `WAITING_STUDENT`.

## 3. Luồng Nghiệp Vụ Chính

1. Người dùng mở Ticket và chọn **Chuyển xử lý**.
2. Hệ thống hiển thị các Category đang hoạt động cùng phòng ban được cấu hình.
3. Người dùng chọn **Category đích** và nhập lý do chuyển.
4. Hệ thống xác định phòng ban đích từ Category đã chọn.
5. Hệ thống kiểm tra Category đích thuộc phòng ban khác phòng ban hiện tại và dữ liệu chuyển hợp lệ.
6. Hệ thống cập nhật **Category và phòng ban** trong cùng một thao tác.
7. Hệ thống gỡ người phụ trách hiện tại.
8. Ticket giữ nguyên trạng thái nghiệp vụ hiện tại phù hợp.
9. Ticket xuất hiện trong hàng chờ của phòng ban mới để được tiếp nhận/phân công.
10. Hệ thống ghi nhận Category trước/sau, phòng ban trước/sau, lý do và người thực hiện.
11. Sinh viên và phạm vi phòng ban mới nhận thông báo trong hệ thống.

## 4. Luồng Ngoại Lệ

- Category đích không hoạt động hoặc vẫn thuộc phòng ban hiện tại: từ chối.
- Lý do chuyển không hợp lệ: từ chối.
- Ticket đã thay đổi phạm vi/trạng thái trước khi xác nhận: từ chối và hiển thị dữ liệu mới nhất.
- Người dùng không có quyền chuyển xử lý: từ chối.

## 5. Quy Tắc Nghiệp Vụ

- Lý do chuyển từ 10 đến 1.000 ký tự.
- Transfer không tạo trạng thái mới và không tự chuyển Ticket về `NEW`.
- Category và phòng ban phải được cập nhật nhất quán; không lưu trạng thái trung gian không khớp.
- Transfer thành công luôn gỡ người phụ trách hiện tại.
- Nội dung, file, kết quả trung gian và lịch sử trước đó được giữ nguyên.

## 6. Tiêu Chí Nghiệm Thu

- Transfer hợp lệ cập nhật đúng Category/phòng ban và giữ nguyên mã Ticket.
- Người phụ trách cũ được gỡ và Ticket xuất hiện trong hàng chờ phòng ban mới.
- Trạng thái nghiệp vụ hiện tại không bị đổi chỉ vì Transfer.
- Lịch sử và thông báo được ghi/gửi đúng đối tượng.

## 7. Tài Liệu Liên Quan

- M02: `FR-STF-05`.
- Domain: `BR-OWN-02`.
