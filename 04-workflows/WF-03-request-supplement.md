# WF-03 - Yêu Cầu Và Tiếp Nhận Bổ Sung

## 1. Mục Đích Và Phạm Vi

Mô tả luồng nhân viên yêu cầu sinh viên bổ sung thông tin/tài liệu và cách Ticket quay lại quá trình xử lý sau khi sinh viên phản hồi hợp lệ.

## 2. Vai Trò Và Điều Kiện Bắt Đầu

- **Vai trò:** Nhân viên phụ trách Ticket và Sinh viên sở hữu Ticket.
- Ticket đang ở `IN_PROGRESS`.
- Nhân viên hiện là người phụ trách hợp lệ.

## 3. Luồng Nghiệp Vụ Chính

1. Nhân viên mở Ticket và chọn **Yêu cầu bổ sung**.
2. Nhân viên nhập nội dung mô tả thông tin/tài liệu cần sinh viên cung cấp.
3. Hệ thống kiểm tra nội dung và trạng thái Ticket.
4. Hệ thống ghi nhận yêu cầu vào lịch sử và chuyển Ticket sang `WAITING_STUDENT`.
5. Đồng hồ thời hạn xử lý tạm dừng.
6. Sinh viên nhận thông báo và mở Ticket.
7. Sinh viên nhập nội dung bổ sung và/hoặc đính kèm file.
8. Sinh viên xác nhận gửi bổ sung.
9. Hệ thống kiểm tra dữ liệu/file, lưu nội dung bổ sung và ghi nhận lịch sử.
10. Ticket chuyển từ `WAITING_STUDENT` về `IN_PROGRESS`.
11. Đồng hồ thời hạn tiếp tục từ lượng thời gian còn lại.
12. Người phụ trách nhận thông báo và tiếp tục xử lý.

## 4. Luồng Ngoại Lệ

- Nội dung yêu cầu bổ sung của nhân viên không hợp lệ: không gửi yêu cầu.
- Sinh viên không nhập nội dung và cũng không có file: từ chối gửi bổ sung.
- File không đáp ứng quy tắc dùng chung: từ chối file không hợp lệ.
- Ticket không còn ở trạng thái phù hợp hoặc không thuộc sinh viên: từ chối thao tác.

## 5. Quy Tắc Nghiệp Vụ

- Nội dung yêu cầu bổ sung từ 10 đến 1.000 ký tự.
- Sinh viên phải cung cấp ít nhất nội dung hoặc file.
- File tuân thủ `BR-FILE-02`.
- Thời gian ở `WAITING_STUDENT` không tính vào thời gian xử lý.
- Yêu cầu và phản hồi bổ sung phải được bảo toàn trong lịch sử Ticket.

## 6. Tiêu Chí Nghiệm Thu

- Yêu cầu bổ sung hợp lệ chuyển `IN_PROGRESS → WAITING_STUDENT` và thông báo đúng sinh viên.
- Bổ sung hợp lệ chuyển `WAITING_STUDENT → IN_PROGRESS`.
- Thời hạn tạm dừng và tiếp tục đúng theo Business Rules.
- Người không có quyền không thể bổ sung hoặc xử lý Ticket ngoài phạm vi.

## 7. Tài Liệu Liên Quan

- M01: `FR-STU-04`, `FR-STU-05`.
- M02: `FR-STF-04`.
- Domain: `BR-SUP-01`, `BR-FILE-02`, `BR-DUE-02`.
