# WF-07 - Chuyển Cấp Hỗ Trợ (Escalation)

## 1. Mục Đích Và Phạm Vi

Mô tả cách nhân viên yêu cầu hỗ trợ từ Quản lý khi Ticket vượt thẩm quyền hiện tại, cần hỗ trợ điều phối hoặc có nguy cơ không đáp ứng thời hạn. Escalation không thay thế Transfer.

## 2. Vai Trò Và Điều Kiện Bắt Đầu

- **Vai trò chính:** Nhân viên có quyền Escalation.
- **Vai trò nhận:** Quản lý có quyền tiếp nhận Escalation trong phạm vi liên quan.
- Ticket đang ở `NEW`, `IN_PROGRESS` hoặc `WAITING_STUDENT`.

## 3. Luồng Nghiệp Vụ Chính

1. Nhân viên mở Ticket và chọn **Chuyển cấp hỗ trợ**.
2. Hệ thống hiển thị các tài khoản Quản lý hợp lệ trong phạm vi liên quan.
3. Nhân viên chọn người nhận và nhập lý do.
4. Hệ thống kiểm tra quyền, trạng thái, người nhận và nội dung lý do.
5. Hệ thống ghi nhận người gửi, người nhận, lý do và thời điểm Escalation.
6. Category, phòng ban, người phụ trách chính và trạng thái Ticket được giữ nguyên.
7. Người phụ trách hiện tại tiếp tục chịu trách nhiệm xử lý Ticket.
8. Người nhận Quản lý và người phụ trách hiện tại nhận thông báo trong hệ thống.
9. Sinh viên không nhận thông báo chỉ vì sự kiện Escalation nội bộ.

## 4. Luồng Ngoại Lệ

- Không có người nhận Quản lý hợp lệ: không thực hiện Escalation.
- Lý do dưới 10 ký tự, trên 1.000 ký tự hoặc chỉ chứa khoảng trắng: từ chối.
- Người dùng không có quyền hoặc Ticket không còn trong trạng thái cho phép: từ chối.

## 5. Quy Tắc Nghiệp Vụ

- Escalation không thay đổi Category, phòng ban, assignee hoặc trạng thái Ticket.
- Escalation không làm mất lịch sử, nội dung hoặc file.
- Nếu cần đổi phòng ban, phải thực hiện WF-04 riêng.
- Nếu cần đổi người phụ trách trong cùng phòng ban, thực hiện luồng phân công lại của M02.

## 6. Tiêu Chí Nghiệm Thu

- Escalation hợp lệ được gửi tới đúng tài khoản Quản lý đã chọn.
- Ticket giữ nguyên Category, phòng ban, người phụ trách và trạng thái.
- Lịch sử ghi đúng người gửi, người nhận, lý do và thời điểm.
- Quản lý nhận Escalation và người phụ trách hiện tại nhận thông báo; sinh viên không nhận thông báo chỉ từ sự kiện này.

## 7. Tài Liệu Liên Quan

- M02: `FR-STF-05`.
- M03: phạm vi Quản lý và kiểm soát quyền liên quan.
- Domain: `BR-OWN-03`.
