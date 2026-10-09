# WF-05 - Ghi Nhận Kết Quả Và Chuyển Sang RESOLVED

## 1. Mục Đích Và Phạm Vi

Mô tả bước nhân viên ghi nhận kết quả xử lý chính thức và đưa Ticket từ `IN_PROGRESS` sang `RESOLVED`. Workflow này **không đóng Ticket**.

## 2. Vai Trò Và Điều Kiện Bắt Đầu

- **Vai trò chính:** Nhân viên phụ trách Ticket hoặc người có quyền ghi nhận kết quả.
- Ticket đang ở `IN_PROGRESS`.
- Kết quả xử lý đã sẵn sàng để phản hồi cho sinh viên.

## 3. Luồng Nghiệp Vụ Chính

1. Nhân viên mở Ticket đang xử lý.
2. Nhân viên chọn **Ghi nhận kết quả**.
3. Nhân viên nhập nội dung kết quả và đính kèm tài liệu kết quả nếu có.
4. Hệ thống kiểm tra quyền, trạng thái, nội dung và file.
5. Hệ thống lưu kết quả xử lý.
6. Ticket chuyển từ `IN_PROGRESS` sang `RESOLVED`.
7. Hệ thống ghi nhận thời điểm giải quyết và sự kiện thay đổi trạng thái.
8. Sinh viên nhận thông báo và có thể xem kết quả.
9. Ticket bắt đầu thời hạn 03 ngày làm việc để sinh viên chấp nhận kết quả hoặc yêu cầu mở lại.

## 4. Luồng Ngoại Lệ

- Thiếu nội dung kết quả hoặc nội dung không hợp lệ: không chuyển trạng thái.
- File kết quả không hợp lệ: từ chối file theo quy tắc dùng chung.
- Ticket không còn ở `IN_PROGRESS` hoặc người dùng không còn quyền: từ chối thao tác.

## 5. Quy Tắc Nghiệp Vụ

- Nội dung kết quả từ 20 đến 2.000 ký tự.
- Tài liệu kết quả: tối đa 03 file/lần, tối đa 10 MB/file, PDF/PNG/JPG/JPEG.
- `RESOLVED` chưa phải trạng thái kết thúc vòng đời.
- Kết quả và lịch sử trước đó phải được giữ nguyên.
- Việc đóng/mở lại sau `RESOLVED` thực hiện theo WF-06.

## 6. Tiêu Chí Nghiệm Thu

- Kết quả hợp lệ chuyển đúng `IN_PROGRESS → RESOLVED`.
- Sinh viên nhận thông báo và xem được kết quả/tài liệu được phép truy cập.
- Thiếu kết quả không làm Ticket đổi trạng thái.
- Workflow không tạo thao tác Staff đóng Ticket độc lập.

## 7. Tài Liệu Liên Quan

- M02: `FR-STF-06`.
- M01: `FR-STU-04`, `FR-STU-06`.
- Domain: `BR-LIFE-01`, `BR-FILE-01`, `BR-FILE-02`.
