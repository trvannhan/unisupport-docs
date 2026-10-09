# Quy Tắc Nghiệp Vụ Cốt Lõi (Business Rules)

Tài liệu này quy định các Business Rules dùng chung cho **UniSupport**. Các quy tắc trong phần này được áp dụng nhất quán giữa Student Portal, Staff Operations và Management Dashboard, đồng thời là cơ sở để xây dựng Functional Requirements và Acceptance Criteria.

## 1. File Đính Kèm (`BR-FILE`)

### `BR-FILE-01` — Quyền truy cập file đính kèm

- File đính kèm của Ticket chỉ được truy cập bởi người dùng có liên quan và có quyền phù hợp.
- Sinh viên chỉ được xem file thuộc Ticket của chính mình.
- Nhân viên chỉ được xem file của Ticket thuộc phạm vi xử lý được phân quyền.
- Người dùng Management chỉ được truy cập file khi quyền được cấp cho phép phục vụ quản lý hoặc tra soát.
- Việc chuyển Ticket sang người/phòng ban khác không làm mất các file đã được ghi nhận trước đó.

### `BR-FILE-02` — Định dạng, dung lượng và số lượng file

- Định dạng được chấp nhận: **PDF, PNG, JPG/JPEG**.
- Dung lượng tối đa: **10 MB cho mỗi file**.
- Tối đa **03 file** cho mỗi lần tạo Ticket, mỗi lần bổ sung thông tin hoặc mỗi lần ghi nhận tài liệu kết quả.
- File không đáp ứng định dạng hoặc dung lượng cho phép phải bị từ chối trước khi được gắn vào Ticket.

---

## 2. Phân Công, Chuyển Xử Lý và Escalation (`BR-OWN`)

### `BR-OWN-01` — Phân công người phụ trách

- Ticket phải xác định được phòng ban phụ trách trong quá trình xử lý.
- Một Ticket chỉ có **01 người phụ trách chính tại một thời điểm**.
- Ticket có thể chưa có người phụ trách cụ thể khi vừa được tạo hoặc sau khi được chuyển sang phòng ban khác.
- Mọi thay đổi người phụ trách phải được ghi nhận trong lịch sử Ticket.

### `BR-OWN-02` — Chuyển xử lý

- Ticket được phép chuyển sang người phụ trách hoặc phòng ban khác khi yêu cầu không thuộc phạm vi hiện tại hoặc cần đơn vị phù hợp hơn xử lý.
- Người thực hiện chuyển phải nhập **lý do chuyển tối thiểu 10 ký tự**.
- Khi chuyển sang phòng ban khác, người phụ trách hiện tại được gỡ khỏi Ticket và phòng ban mới thực hiện phân công lại.
- Chuyển xử lý không làm mất nội dung, file đính kèm, kết quả trung gian hoặc lịch sử trước đó.
- Việc chuyển xử lý không tự tạo trạng thái vòng đời mới; Ticket tiếp tục ở trạng thái nghiệp vụ phù hợp.

### `BR-OWN-03` — Escalation

- Escalation được sử dụng khi Ticket vượt quá thẩm quyền xử lý hiện tại, cần hỗ trợ từ cấp phù hợp hơn hoặc có nguy cơ không đáp ứng thời hạn xử lý.
- Người thực hiện phải ghi nhận lý do escalation.
- Escalation phải giữ nguyên toàn bộ lịch sử xử lý và được ghi nhận như một sự kiện riêng trong Ticket.
- Escalation không tự động đóng Ticket và không làm mất trách nhiệm theo dõi cho đến khi phạm vi xử lý mới được xác lập.

---

## 3. Mức Độ Ưu Tiên và Thời Hạn Xử Lý (`BR-DUE`)

### `BR-DUE-01` — Mức độ ưu tiên và thời hạn mục tiêu

UniSupport sử dụng bốn mức độ ưu tiên:

| Mức độ | Thời hạn xử lý mục tiêu |
| :--- | :--- |
| **Thấp (LOW)** | 05 ngày làm việc |
| **Trung bình (MEDIUM)** | 03 ngày làm việc |
| **Cao (HIGH)** | 02 ngày làm việc |
| **Khẩn cấp (URGENT)** | 01 ngày làm việc |

- Ticket mới được áp dụng mức **Trung bình (MEDIUM)** mặc định cho đến khi được người có quyền điều chỉnh.
- Thời hạn xử lý ban đầu được xác định từ mức độ ưu tiên hiện tại của Ticket.
- Khi mức độ ưu tiên được thay đổi, thời hạn xử lý phải được tính lại theo mức mới nhưng vẫn giữ nguyên phần thời gian xử lý hợp lệ đã sử dụng trước đó.
- Việc thay đổi mức độ ưu tiên phải có quyền phù hợp và được ghi nhận trong lịch sử Ticket.

### `BR-DUE-02` — Cách tính ngày làm việc và tình trạng thời hạn

- **Ngày làm việc** là từ thứ Hai đến thứ Sáu, không bao gồm ngày nghỉ lễ hoặc ngày nghỉ chính thức của Aurora University.
- Thời hạn xử lý được tính từ thời điểm Ticket được tạo thành công theo số ngày làm việc tương ứng với mức độ ưu tiên.
- Khoảng thời gian Ticket ở trạng thái `WAITING_STUDENT` không được tính vào thời gian xử lý.
- Khi sinh viên bổ sung thông tin hợp lệ và Ticket quay lại `IN_PROGRESS`, thời gian xử lý tiếp tục được tính từ phần thời gian còn lại.
- Ticket được xem là **sắp quá hạn** khi đã sử dụng từ **80% thời gian xử lý mục tiêu** trở lên nhưng chưa vượt thời hạn.
- Ticket được xem là **quá hạn** khi vượt quá thời hạn xử lý và chưa chuyển sang `RESOLVED` hoặc `CLOSED`.

---

## 4. Yêu Cầu Bổ Sung Thông Tin (`BR-SUP`)

### `BR-SUP-01` — Chờ sinh viên bổ sung

- Nhân viên chỉ được yêu cầu bổ sung khi Ticket đang trong quá trình xử lý và thông tin hiện có chưa đủ để tiếp tục.
- Nội dung yêu cầu bổ sung phải nêu rõ thông tin hoặc tài liệu cần cung cấp.
- Sau khi yêu cầu bổ sung được gửi, Ticket chuyển sang `WAITING_STUDENT`.
- Trong thời gian `WAITING_STUDENT`, thời hạn xử lý được tạm dừng theo `BR-DUE-02`.
- Khi sinh viên bổ sung thông tin hoặc tài liệu hợp lệ, Ticket quay lại `IN_PROGRESS`.
- Yêu cầu bổ sung và phản hồi của sinh viên phải được ghi nhận trong lịch sử Ticket.

---

## 5. Hoàn Tất, Phản Hồi và Mở Lại Ticket (`BR-LIFE`)

### `BR-LIFE-01` — Chuyển sang RESOLVED

- Ticket chỉ được chuyển từ `IN_PROGRESS` sang `RESOLVED` khi đã có kết quả xử lý.
- Nội dung kết quả xử lý là thông tin bắt buộc trước khi Ticket được đánh dấu `RESOLVED`.
- Khi Ticket chuyển sang `RESOLVED`, sinh viên phải nhận được thông báo và có quyền xem kết quả.

### `BR-LIFE-02` — Thời hạn phản hồi và tự động đóng

- Sinh viên có **03 ngày làm việc** kể từ thời điểm Ticket chuyển sang `RESOLVED` để phản hồi kết quả.
- Nếu sinh viên chấp nhận kết quả, Ticket được chuyển sang `CLOSED`.
- Nếu hết **03 ngày làm việc** mà không có phản hồi yêu cầu xử lý tiếp, hệ thống chuyển Ticket sang `CLOSED`.
- Thời điểm đóng phải được ghi nhận trong lịch sử Ticket.

### `BR-LIFE-03` — Mở lại Ticket

- Mở lại chỉ được thực hiện khi Ticket đang ở trạng thái `RESOLVED` và còn trong thời hạn phản hồi.
- Sinh viên phải cung cấp lý do cho biết vấn đề chưa được giải quyết.
- Ticket hợp lệ được mở lại sẽ chuyển từ `RESOLVED` về `IN_PROGRESS`.
- Việc mở lại không xóa kết quả, thời điểm giải quyết hoặc lịch sử của vòng xử lý trước.
- Ticket đã chuyển sang `CLOSED` không được mở lại; nếu phát sinh nhu cầu hỗ trợ mới, sinh viên tạo Ticket mới.

---

## 6. Đánh Giá Mức Độ Hài Lòng (`BR-CSAT`)

### `BR-CSAT-01` — Điều kiện và thời hạn đánh giá

- Sinh viên được đánh giá khi Ticket đã ở trạng thái `CLOSED`.
- Mỗi Ticket chỉ được gửi **01 đánh giá**.
- Điểm đánh giá sử dụng thang **1 đến 5 sao**.
- Nội dung nhận xét bổ sung là không bắt buộc.
- Sinh viên có **07 ngày theo lịch** kể từ thời điểm Ticket chuyển sang `CLOSED` để gửi đánh giá.
- Sau thời hạn trên, Ticket vẫn được lưu phục vụ tra cứu nhưng không còn nhận đánh giá mới.

---

## 7. Lịch Sử Xử Lý và Tra Soát (`BR-AUD`)

### `BR-AUD-01` — Ghi nhận lịch sử Ticket

Các sự kiện quan trọng phải được ghi nhận trong lịch sử Ticket, tối thiểu gồm:

- Tạo Ticket.
- Phân loại và phân công.
- Thay đổi trạng thái.
- Thay đổi mức độ ưu tiên hoặc thời hạn xử lý.
- Yêu cầu và tiếp nhận thông tin bổ sung.
- Chuyển người/phòng ban xử lý.
- Escalation.
- Ghi nhận kết quả xử lý.
- Mở lại Ticket.
- Đóng Ticket.

Mỗi sự kiện phải xác định được nội dung thay đổi, người hoặc hệ thống thực hiện và thời điểm phát sinh.

### `BR-AUD-02` — Tính toàn vẹn của nhật ký tra soát

- Người dùng thông thường không được chỉnh sửa hoặc xóa các bản ghi lịch sử đã phát sinh.
- Các thao tác quản trị liên quan đến dữ liệu tra soát phải được kiểm soát theo quyền và không được làm mất dấu vết nghiệp vụ đã ghi nhận.
- Lịch sử Ticket phải được bảo toàn khi Ticket được phân công lại, chuyển xử lý, escalation, mở lại hoặc đóng.
