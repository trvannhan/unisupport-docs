# NFR-SEC - Bảo Mật Và Phân Quyền

## 1. Phạm Vi

UniSupport áp dụng mức bảo mật phù hợp phạm vi dự án. Proposal không yêu cầu chứng nhận bảo mật hoặc kiểm thử bảo mật chuyên sâu.

## 2. Yêu Cầu

- Người dùng đăng nhập bằng tài khoản và mật khẩu riêng.
- Hệ thống có ba nhóm người dùng chính: Sinh viên, Nhân viên và Quản lý.
- Sinh viên chỉ truy cập Ticket của chính mình.
- Nhân viên chỉ truy cập Ticket thuộc phạm vi phòng ban/quyền được cấp.
- Quản lý chỉ truy cập dữ liệu và chức năng trong phạm vi quản lý/quyền được cấp.
- File đính kèm chỉ được xem bởi người dùng có liên quan và có quyền phù hợp.
- Mật khẩu không được lưu hoặc hiển thị ở dạng có thể đọc trực tiếp.
- Các thao tác quan trọng phải được ghi nhận để tra soát theo `BR-AUD`.
- Nhật ký tra soát không được sửa/xóa bằng chức năng thông thường của ứng dụng.

## 3. Giới Hạn Phạm Vi

- Không bao gồm penetration testing chuyên sâu hoặc chứng nhận bảo mật quốc tế.
- Cơ chế token/session, thuật toán hash và middleware cụ thể là quyết định kỹ thuật tại `07-architecture`.

## 4. Nghiệm Thu

- Người dùng không thể truy cập Ticket/file ngoài phạm vi quyền.
- Tài khoản bị khóa không đăng nhập được.
- Các sự kiện Audit bắt buộc được ghi nhận đúng tác nhân, thời điểm và nội dung thay đổi cần thiết.
