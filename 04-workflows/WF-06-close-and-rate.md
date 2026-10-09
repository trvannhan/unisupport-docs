# WF-06 - Phản Hồi Kết Quả, Mở Lại, Đóng Và Đánh Giá

## 1. Mục Đích Và Phạm Vi

Mô tả toàn bộ hành vi sau khi Ticket ở `RESOLVED`: sinh viên chấp nhận kết quả hoặc yêu cầu mở lại; hệ thống tự đóng khi hết thời hạn; sau khi `CLOSED`, sinh viên có thể đánh giá mức độ hài lòng.

## 2. Vai Trò Và Điều Kiện Bắt Đầu

- **Vai trò:** Sinh viên, Nhân viên và Hệ thống.
- Ticket thuộc sinh viên và đang ở `RESOLVED` để phản hồi kết quả.
- Đánh giá chỉ áp dụng khi Ticket đã ở `CLOSED`.

## 3. Luồng Nghiệp Vụ Chính

**Luồng A — Sinh viên chấp nhận kết quả**
1. Sinh viên mở Ticket `RESOLVED` và xem kết quả.
2. Sinh viên xác nhận vấn đề đã được giải quyết.
3. Hệ thống chuyển Ticket sang `CLOSED`, ghi nhận thời điểm đóng và lịch sử.

**Luồng B — Sinh viên yêu cầu mở lại**
1. Sinh viên mở Ticket `RESOLVED` còn trong thời hạn 03 ngày làm việc.
2. Sinh viên chọn **Vấn đề chưa được giải quyết** và nhập lý do mở lại.
3. Hệ thống kiểm tra trạng thái, thời hạn và lý do.
4. Ticket chuyển từ `RESOLVED` về `IN_PROGRESS`.
5. Nếu người phụ trách cũ vẫn hoạt động và còn thuộc phòng ban hiện tại, Ticket tiếp tục được giao cho người đó và người đó nhận thông báo.
6. Nếu người phụ trách cũ không còn hợp lệ, Ticket được đưa về hàng chờ chưa có người phụ trách của phòng ban hiện tại.
7. Nhân viên tiếp tục xử lý theo M02; khi có kết quả mới, thực hiện lại WF-05.
8. Kết quả và lịch sử của vòng xử lý trước được giữ nguyên.

**Luồng C — Hệ thống tự động đóng**
1. Ticket ở `RESOLVED`.
2. Hết 03 ngày làm việc mà sinh viên không yêu cầu xử lý tiếp.
3. Hệ thống chuyển Ticket sang `CLOSED` và ghi nhận thời điểm đóng.

**Luồng D — Sinh viên đánh giá**
1. Ticket đã ở `CLOSED` và còn trong 07 ngày theo lịch kể từ thời điểm đóng.
2. Sinh viên chọn điểm 1–5 sao và nhập nhận xét nếu muốn.
3. Hệ thống kiểm tra Ticket chưa từng được đánh giá.
4. Hệ thống lưu đánh giá và không cho gửi đánh giá lần thứ hai.

## 4. Luồng Ngoại Lệ

- Ticket đã `CLOSED` hoặc hết thời hạn phản hồi: không cho mở lại.
- Lý do mở lại thiếu hoặc không hợp lệ: từ chối.
- Ticket không thuộc sinh viên: từ chối truy cập/thao tác.
- Ticket đã có đánh giá hoặc đã hết 07 ngày đánh giá: không nhận đánh giá mới.

## 5. Quy Tắc Nghiệp Vụ

- Reopen chỉ có chuyển đổi `RESOLVED → IN_PROGRESS`.
- Staff không có thao tác đóng hoặc mở lại độc lập.
- `CLOSED` là trạng thái kết thúc vòng đời; vấn đề mới phải tạo Ticket mới.
- Mỗi Ticket chỉ có tối đa một đánh giá 1–5 sao.
- Nhận xét CSAT là không bắt buộc.
- Mọi lần mở lại và đóng Ticket phải được ghi nhận trong lịch sử.

## 6. Tiêu Chí Nghiệm Thu

- Xác nhận kết quả hợp lệ chuyển `RESOLVED → CLOSED`.
- Reopen hợp lệ trong 03 ngày làm việc chuyển `RESOLVED → IN_PROGRESS`.
- Reopen giữ assignee cũ nếu hợp lệ; nếu không Ticket về đúng hàng chờ phòng ban.
- Ticket tự động đóng khi hết thời hạn phản hồi mà không có yêu cầu xử lý tiếp.
- CSAT chỉ nhận khi Ticket `CLOSED`, trong 07 ngày và tối đa một lần.

## 7. Tài Liệu Liên Quan

- M01: `FR-STU-06`, `FR-STU-07`.
- M02: `FR-STF-01`, `FR-STF-06`.
- Domain: `BR-LIFE-02`, `BR-LIFE-03`, `BR-CSAT-01`.
