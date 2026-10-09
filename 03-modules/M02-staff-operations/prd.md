# Phân Hệ Nhân Viên (M02 - Staff Operations)

## I. TỔNG QUAN PHÂN HỆ

Phân hệ **Staff Operations** cung cấp không gian làm việc để nhân viên Aurora University tiếp nhận, phân loại, phân công, xử lý, chuyển xử lý và ghi nhận kết quả các Ticket hỗ trợ sinh viên.

- **Actor chính:** Nhân viên (Staff).
- **Phạm vi dữ liệu:** Nhân viên chỉ được truy cập Ticket thuộc phòng ban hoặc phạm vi trách nhiệm được cấp.
- **Người phụ trách:** Một Ticket chỉ có một người phụ trách chính tại một thời điểm.
- **Phân công:** Các thao tác phân công/phân công lại chỉ dành cho người dùng có quyền phù hợp.
- **Phạm vi vòng đời:** M02 xử lý Ticket đến khi ghi nhận kết quả ở `RESOLVED`; việc đóng hoặc mở lại tuân theo vòng đời Ticket dùng chung.

---

## II. CHI TIẾT CÁC CHỨC NĂNG (FUNCTIONAL REQUIREMENTS)

### [FR-STF-00] Đăng nhập và truy cập Staff Operations

#### 1. Mô tả & Phạm vi
Cho phép nhân viên đăng nhập vào UniSupport và truy cập không gian làm việc phù hợp với phòng ban và quyền được cấp.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Nhân viên.
- **Preconditions:** Tài khoản tồn tại, đang hoạt động và được gắn với phạm vi phòng ban phù hợp.

#### 3. Quy tắc Dữ liệu & Validation
- **Tên đăng nhập:** bắt buộc, sử dụng tài khoản do nhà trường cấp.
- **Mật khẩu:** bắt buộc.
- Không chấp nhận dữ liệu chỉ chứa khoảng trắng.

#### 4. Luồng xử lý chi tiết
1. Nhân viên truy cập UniSupport.
2. Hệ thống yêu cầu đăng nhập nếu chưa có phiên hợp lệ.
3. Nhân viên nhập thông tin đăng nhập.
4. Hệ thống xác thực tài khoản, trạng thái hoạt động và phạm vi quyền.
5. Nếu hợp lệ, hệ thống cho phép truy cập Staff Operations và chỉ hiển thị dữ liệu thuộc phạm vi được cấp.

#### 5. Luồng ngoại lệ
- Thông tin đăng nhập không hợp lệ: từ chối truy cập.
- Tài khoản bị khóa hoặc vô hiệu hóa: không tạo phiên đăng nhập.
- Tài khoản chưa được gắn phạm vi phòng ban cần thiết: không cho phép truy cập dữ liệu Ticket của phòng ban.
- Phiên hết hạn: yêu cầu xác thực lại.

#### 6. Quy tắc nghiệp vụ
- Nhân viên không được truy cập Ticket ngoài phạm vi được cấp.
- Cơ chế xác thực và quản lý phiên được dùng chung với các phân hệ khác.

#### 7. Tiêu chí nghiệm thu
- **AC-00-01:** Tài khoản Staff hợp lệ truy cập được Staff Operations.
- **AC-00-02:** Nhân viên chỉ xem dữ liệu thuộc phạm vi phòng ban/quyền được cấp.
- **AC-00-03:** Tài khoản không hợp lệ hoặc bị vô hiệu hóa không truy cập được chức năng được bảo vệ.
- **AC-00-04:** Phiên hết hạn yêu cầu xác thực lại.

---

### [FR-STF-01] Xem hàng chờ, tìm kiếm và lọc Ticket

#### 1. Mô tả & Phạm vi
Cung cấp danh sách công việc để nhân viên xem Ticket mới, Ticket được giao và Ticket đang cần xử lý trong phạm vi của mình.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Nhân viên đã đăng nhập.
- **Preconditions:** Nhân viên có quyền truy cập ít nhất một phạm vi Ticket.

#### 3. Quy tắc Dữ liệu & Validation
- Tìm kiếm theo **Mã Ticket**.
- Bộ lọc hỗ trợ tối thiểu: **Trạng thái, Nhóm vấn đề, Mức độ ưu tiên, Người phụ trách**.
- Nhân viên chỉ nhận kết quả thuộc phạm vi dữ liệu được phép truy cập.
- Ticket được mở lại từ `RESOLVED` về `IN_PROGRESS` phải xuất hiện lại trong danh sách xử lý phù hợp.

#### 4. Luồng xử lý chi tiết
1. Nhân viên mở Staff Operations.
2. Hệ thống hiển thị hàng chờ Ticket thuộc phạm vi phòng ban/người dùng.
3. Nhân viên nhập Mã Ticket hoặc áp dụng một hay nhiều bộ lọc.
4. Hệ thống trả về danh sách Ticket phù hợp.
5. Nhân viên mở một Ticket để xem chi tiết trước khi tiếp nhận hoặc xử lý.
6. Hệ thống hiển thị thông tin Ticket, sinh viên gửi yêu cầu, Category, trạng thái, Priority, Deadline, người phụ trách, file được phép truy cập và lịch sử xử lý.

#### 5. Luồng ngoại lệ
- Không có Ticket phù hợp: hiển thị danh sách trống.
- Ticket ngoài phạm vi quyền: từ chối truy cập và không hiển thị dữ liệu.
- Mã Ticket không tồn tại: hiển thị trạng thái không tìm thấy.

#### 6. Quy tắc nghiệp vụ
- Kết quả tìm kiếm và lọc luôn phải tuân thủ phạm vi quyền của người dùng.
- Transfer hoặc phân công lại có thể làm Ticket không còn xuất hiện trong danh sách của người dùng cũ.
- Danh sách phải phản ánh trạng thái và người phụ trách hiện tại của Ticket.

#### 7. Tiêu chí nghiệm thu
- **AC-01-01:** Tìm kiếm bằng Mã Ticket hợp lệ trả về đúng Ticket nếu người dùng có quyền.
- **AC-01-02:** Bộ lọc chỉ trả về Ticket thỏa điều kiện đã chọn.
- **AC-01-03:** Ticket ngoài phạm vi không xuất hiện trong danh sách và không thể mở trực tiếp.
- **AC-01-04:** Ticket được mở lại xuất hiện lại trong danh sách xử lý phù hợp ở trạng thái `IN_PROGRESS`.

---

### [FR-STF-02] Phân loại, tiếp nhận và phân công Ticket

#### 1. Mô tả & Phạm vi
Cho phép nhân viên kiểm tra Category của Ticket, tiếp nhận Ticket chưa có người phụ trách và cho phép người dùng có quyền phân công hoặc phân công lại Ticket cho nhân viên phù hợp.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Nhân viên đã đăng nhập.
- **Actor bổ sung:** Người dùng có quyền phân công.
- **Preconditions:** Ticket thuộc phạm vi phòng ban được phép xử lý.

#### 3. Quy tắc Dữ liệu & Validation
- **Category:** phải là một giá trị đang hoạt động trong danh mục Category của hệ thống.
- Nếu Category hiện tại không phù hợp, người có quyền xử lý có thể chọn lại Category từ danh mục có sẵn.
- Nếu Category mới thuộc phòng ban khác, Ticket phải được xử lý theo luồng **Transfer** thay vì chỉ thay đổi phòng ban ngầm.
- **Người phụ trách:** phải là nhân viên hợp lệ thuộc phòng ban đang phụ trách Ticket.
- Một Ticket chỉ có **01 người phụ trách chính tại một thời điểm**.

#### 4. Luồng A — Tiếp nhận Ticket
1. Nhân viên mở Ticket chưa có người phụ trách trong hàng chờ phòng ban.
2. Hệ thống hiển thị nội dung yêu cầu và Category hiện tại.
3. Nhân viên kiểm tra Category và điều chỉnh nếu cần.
4. Nhân viên chọn **Tiếp nhận**.
5. Hệ thống kiểm tra Ticket vẫn chưa có người phụ trách và còn thuộc phạm vi của nhân viên.
6. Hệ thống ghi nhận nhân viên là người phụ trách chính.
7. Nếu Ticket đang ở `NEW`, hệ thống chuyển Ticket sang `IN_PROGRESS`.
8. Hệ thống ghi nhận sự kiện tiếp nhận/phân công vào lịch sử Ticket.

#### 5. Luồng B — Phân công hoặc phân công lại
1. Người dùng có quyền phân công mở Ticket.
2. Hệ thống hiển thị danh sách nhân viên hợp lệ thuộc phòng ban đang phụ trách Ticket.
3. Người dùng chọn một nhân viên.
4. Hệ thống kiểm tra quyền và phạm vi phòng ban.
5. Hệ thống cập nhật người phụ trách chính.
6. Nếu Ticket đang ở `NEW`, Ticket chuyển sang `IN_PROGRESS`.
7. Hệ thống ghi nhận người phụ trách trước, người phụ trách mới và người thực hiện thao tác vào lịch sử.

#### 6. Luồng ngoại lệ
- Hai nhân viên cùng tiếp nhận một Ticket: chỉ một người được trở thành người phụ trách chính; người còn lại nhận thông báo Ticket đã được tiếp nhận.
- Phân công cho người không thuộc phòng ban hiện tại: từ chối thao tác.
- Ticket đã được Transfer sang phòng ban khác trước khi thao tác hoàn tất: từ chối và hiển thị dữ liệu mới nhất.

#### 7. Quy tắc nghiệp vụ
- Tuân thủ `BR-OWN-01`.
- Phân loại và phân công phải được ghi nhận trong lịch sử Ticket.
- Nhân viên không được tự tạo Category mới trong luồng xử lý Ticket.

#### 8. Tiêu chí nghiệm thu
- **AC-02-01:** Tiếp nhận Ticket `NEW` hợp lệ gán đúng người phụ trách và chuyển sang `IN_PROGRESS`.
- **AC-02-02:** Không thể có hai người phụ trách chính đồng thời cho cùng một Ticket.
- **AC-02-03:** Phân công chỉ chấp nhận nhân viên hợp lệ thuộc phòng ban đang xử lý.
- **AC-02-04:** Thay đổi Category hợp lệ được ghi nhận trong lịch sử.
- **AC-02-05:** Category dẫn đến phòng ban khác phải sử dụng Transfer.

---

### [FR-STF-03] Quản lý mức độ ưu tiên và thời hạn xử lý

#### 1. Mô tả & Phạm vi
Cho phép người dùng có quyền thiết lập mức độ ưu tiên của Ticket và theo dõi thời hạn xử lý tương ứng.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Nhân viên hoặc người dùng có quyền điều chỉnh Priority.
- **Preconditions:** Ticket thuộc phạm vi xử lý của người dùng.

#### 3. Quy tắc Dữ liệu & Validation
- Priority chỉ nhận một trong bốn giá trị: `LOW`, `MEDIUM`, `HIGH`, `URGENT`.
- Ticket mới có Priority mặc định `MEDIUM`.
- Thời hạn mục tiêu:
  - `LOW`: 05 ngày làm việc.
  - `MEDIUM`: 03 ngày làm việc.
  - `HIGH`: 02 ngày làm việc.
  - `URGENT`: 01 ngày làm việc.
- Ticket được xem là sắp quá hạn khi đã sử dụng từ 80% thời gian xử lý mục tiêu trở lên.

#### 4. Luồng xử lý chi tiết
1. Người dùng mở Ticket thuộc phạm vi xử lý.
2. Hệ thống hiển thị Priority và Deadline hiện tại.
3. Người dùng chọn Priority phù hợp.
4. Hệ thống kiểm tra quyền thực hiện.
5. Hệ thống lưu Priority mới và tính lại Deadline theo quy tắc dùng chung.
6. Hệ thống ghi nhận thay đổi Priority/Deadline vào lịch sử Ticket.
7. Danh sách công việc phản ánh trạng thái sắp quá hạn hoặc quá hạn tương ứng.

#### 5. Luồng ngoại lệ
- Người dùng không có quyền thay đổi Priority: từ chối thao tác.
- Ticket đã chuyển sang phạm vi khác trước khi lưu: từ chối và yêu cầu tải lại dữ liệu.
- Giá trị Priority không thuộc danh sách cho phép: không chấp nhận.

#### 6. Quy tắc nghiệp vụ
- Tuân thủ `BR-DUE-01` và `BR-DUE-02`.
- Thời gian Ticket ở `WAITING_STUDENT` không tính vào thời gian xử lý.
- Khi Priority thay đổi, Deadline được tính lại theo mức mới nhưng vẫn giữ phần thời gian xử lý hợp lệ đã sử dụng.

#### 7. Tiêu chí nghiệm thu
- **AC-03-01:** Mỗi Priority tạo ra Deadline đúng theo Business Rules.
- **AC-03-02:** Thay đổi Priority hợp lệ cập nhật Deadline và lịch sử Ticket.
- **AC-03-03:** Ticket đạt ngưỡng 80% được nhận diện là sắp quá hạn.
- **AC-03-04:** Ticket vượt Deadline và chưa `RESOLVED`/`CLOSED` được nhận diện là quá hạn.
- **AC-03-05:** Khoảng thời gian `WAITING_STUDENT` không làm tiêu hao thời gian xử lý còn lại.

---

### [FR-STF-04] Xử lý Ticket và yêu cầu sinh viên bổ sung

#### 1. Mô tả & Phạm vi
Cho phép nhân viên xử lý Ticket đang phụ trách, ghi nhận tiến độ và yêu cầu sinh viên bổ sung thông tin hoặc tài liệu khi dữ liệu hiện có chưa đủ để tiếp tục xử lý.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Nhân viên phụ trách Ticket.
- **Preconditions:** Ticket đang ở `IN_PROGRESS` và thuộc phạm vi của nhân viên.

#### 3. Quy tắc Dữ liệu & Validation
- Nội dung cập nhật tiến độ: nếu được ghi nhận, không được chỉ chứa khoảng trắng.
- Yêu cầu bổ sung: bắt buộc có nội dung mô tả rõ thông tin hoặc tài liệu cần cung cấp.
- Nội dung yêu cầu bổ sung: từ **10 đến 1.000 ký tự**.
- Nhân viên chỉ được yêu cầu bổ sung khi Ticket đang ở `IN_PROGRESS`.

#### 4. Luồng A — Cập nhật tiến độ
1. Nhân viên mở Ticket đang phụ trách.
2. Nhân viên ghi nhận nội dung tiến độ xử lý khi cần.
3. Hệ thống lưu cập nhật vào lịch sử Ticket.
4. Ticket tiếp tục ở `IN_PROGRESS`.

#### 5. Luồng B — Yêu cầu bổ sung
1. Nhân viên mở Ticket đang phụ trách.
2. Nhân viên chọn **Yêu cầu bổ sung**.
3. Nhân viên nhập nội dung cần sinh viên cung cấp.
4. Hệ thống kiểm tra dữ liệu và trạng thái hiện tại.
5. Hệ thống lưu yêu cầu bổ sung vào lịch sử.
6. Ticket chuyển từ `IN_PROGRESS` sang `WAITING_STUDENT`.
7. Thời gian xử lý được tạm dừng.
8. Hệ thống tạo thông báo trong hệ thống cho sinh viên.

#### 6. Luồng ngoại lệ
- Nội dung yêu cầu bổ sung không hợp lệ: không gửi yêu cầu.
- Ticket không còn ở `IN_PROGRESS`: từ chối thao tác.
- Nhân viên không còn là người phụ trách hoặc không còn quyền xử lý: từ chối cập nhật.

#### 7. Quy tắc nghiệp vụ
- Tuân thủ `BR-SUP-01` và `BR-DUE-02`.
- Yêu cầu bổ sung và phản hồi sau đó của sinh viên phải được bảo toàn trong lịch sử Ticket.
- Khi sinh viên bổ sung hợp lệ, Ticket quay về `IN_PROGRESS`.

#### 8. Tiêu chí nghiệm thu
- **AC-04-01:** Cập nhật tiến độ hợp lệ được lưu vào đúng Ticket.
- **AC-04-02:** Yêu cầu bổ sung hợp lệ chuyển Ticket sang `WAITING_STUDENT`.
- **AC-04-03:** Sinh viên nhận được thông báo và xem được nội dung cần bổ sung.
- **AC-04-04:** Thời gian xử lý tạm dừng trong `WAITING_STUDENT` và tiếp tục khi Ticket quay về `IN_PROGRESS`.
- **AC-04-05:** Ticket ngoài `IN_PROGRESS` không thể phát sinh yêu cầu bổ sung mới.

---

### [FR-STF-05] Chuyển xử lý và Escalation

#### 1. Mô tả & Phạm vi
Cho phép chuyển Ticket sang người/phòng ban phù hợp khác hoặc thực hiện Escalation khi Ticket cần phạm vi xử lý cao hơn, cần hỗ trợ hoặc có nguy cơ không đáp ứng thời hạn.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Nhân viên có quyền xử lý Ticket.
- **Preconditions:** Ticket thuộc phạm vi xử lý hiện tại và chưa ở `CLOSED`.

#### 3. Quy tắc Dữ liệu & Validation
- **Transfer sang phòng ban khác:** bắt buộc chọn phòng ban đích khác phòng ban hiện tại.
- **Lý do Transfer:** bắt buộc, tối thiểu 10 ký tự.
- **Escalation:** bắt buộc có lý do mô tả nguyên nhân cần chuyển cấp xử lý.
- Transfer và Escalation không tạo trạng thái Ticket mới.

#### 4. Luồng A — Transfer
1. Nhân viên mở Ticket.
2. Nhân viên chọn **Chuyển xử lý**.
3. Hệ thống hiển thị các phòng ban đích hợp lệ.
4. Nhân viên chọn phòng ban và nhập lý do.
5. Hệ thống kiểm tra quyền, trạng thái và dữ liệu.
6. Hệ thống thay đổi phòng ban phụ trách.
7. Người phụ trách hiện tại được gỡ khỏi Ticket nếu không còn thuộc phạm vi phù hợp.
8. Ticket giữ trạng thái nghiệp vụ hiện tại phù hợp và xuất hiện trong hàng chờ của phòng ban mới.
9. Hệ thống ghi nhận phòng ban trước, phòng ban sau, lý do và người thực hiện vào lịch sử.

#### 5. Luồng B — Escalation
1. Nhân viên xác định Ticket vượt thẩm quyền hiện tại, cần hỗ trợ hoặc có nguy cơ quá hạn.
2. Nhân viên chọn **Escalation** và nhập lý do.
3. Hệ thống kiểm tra quyền và dữ liệu.
4. Hệ thống ghi nhận sự kiện Escalation và chuyển Ticket đến phạm vi xử lý phù hợp theo quyền được cấu hình.
5. Ticket giữ trạng thái nghiệp vụ phù hợp.
6. Các bên liên quan nhận thông báo trong hệ thống.

#### 6. Luồng ngoại lệ
- Transfer không có lý do hoặc lý do dưới 10 ký tự: từ chối.
- Chọn chính phòng ban hiện tại làm đích Transfer: từ chối.
- Người dùng không đủ quyền: từ chối thao tác.
- Ticket đã thay đổi phạm vi/trạng thái không còn phù hợp trước khi xác nhận: từ chối và hiển thị dữ liệu mới nhất.

#### 7. Quy tắc nghiệp vụ
- Tuân thủ `BR-OWN-02` và `BR-OWN-03`.
- Transfer/Escalation phải giữ nguyên mã Ticket, nội dung, file và lịch sử đã có.
- Transfer/Escalation không tự động chuyển Ticket sang `RESOLVED` hoặc `CLOSED`.

#### 8. Tiêu chí nghiệm thu
- **AC-05-01:** Transfer hợp lệ đưa Ticket vào phạm vi phòng ban mới mà không thay đổi mã Ticket.
- **AC-05-02:** Người phụ trách cũ được gỡ khi không còn phù hợp với phòng ban mới.
- **AC-05-03:** Transfer không tạo state `TRANSFERRED`.
- **AC-05-04:** Escalation hợp lệ được ghi nhận thành sự kiện riêng trong lịch sử.
- **AC-05-05:** Lịch sử trước Transfer/Escalation được giữ nguyên.

---

### [FR-STF-06] Ghi nhận kết quả và hoàn tất phần xử lý

#### 1. Mô tả & Phạm vi
Cho phép nhân viên ghi nhận kết quả xử lý chính thức của Ticket và chuyển Ticket sang `RESOLVED` để sinh viên xem và phản hồi.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Nhân viên phụ trách Ticket hoặc người dùng có quyền hoàn tất xử lý.
- **Preconditions:** Ticket đang ở `IN_PROGRESS` và đã đáp ứng điều kiện nghiệp vụ để có thể ghi nhận kết quả.

#### 3. Quy tắc Dữ liệu & Validation
- **Nội dung kết quả xử lý:** bắt buộc, từ **20 đến 2.000 ký tự**, không chấp nhận nội dung chỉ chứa khoảng trắng.
- **Tài liệu kết quả:** không bắt buộc; nếu có phải tuân thủ quy tắc file dùng chung.
- Chỉ Ticket ở `IN_PROGRESS` mới được chuyển sang `RESOLVED` theo luồng này.

#### 4. Luồng xử lý chi tiết
1. Nhân viên mở Ticket đang xử lý.
2. Nhân viên chọn **Ghi nhận kết quả**.
3. Nhân viên nhập nội dung kết quả và đính kèm tài liệu nếu có.
4. Hệ thống kiểm tra quyền, trạng thái và dữ liệu.
5. Hệ thống lưu kết quả xử lý.
6. Ticket chuyển từ `IN_PROGRESS` sang `RESOLVED`.
7. Hệ thống ghi nhận thời điểm giải quyết.
8. Kết quả và sự kiện thay đổi trạng thái được ghi vào lịch sử Ticket.
9. Hệ thống gửi thông báo trong hệ thống cho sinh viên.

#### 5. Luồng ngoại lệ
- Thiếu nội dung kết quả hoặc nội dung không hợp lệ: không cho phép hoàn tất.
- File kết quả không đáp ứng quy tắc file: từ chối file không hợp lệ.
- Ticket không còn ở `IN_PROGRESS`: từ chối thao tác.
- Người dùng không có quyền hoàn tất Ticket: từ chối.

#### 6. Quy tắc nghiệp vụ
- Tuân thủ `BR-LIFE-01`, `BR-FILE-01` và `BR-FILE-02`.
- `RESOLVED` chưa phải trạng thái kết thúc vòng đời.
- Sinh viên có 03 ngày làm việc để chấp nhận kết quả hoặc yêu cầu mở lại.
- M02 không tự mở form CSAT tại `RESOLVED`; CSAT chỉ áp dụng khi Ticket đã `CLOSED`.
- Nếu Ticket được mở lại hợp lệ, Ticket quay về `IN_PROGRESS` và tiếp tục quá trình xử lý.

#### 7. Tiêu chí nghiệm thu
- **AC-06-01:** Kết quả hợp lệ chuyển Ticket từ `IN_PROGRESS` sang `RESOLVED`.
- **AC-06-02:** Sinh viên nhận thông báo và xem được nội dung/tài liệu kết quả thuộc Ticket của mình.
- **AC-06-03:** Thiếu nội dung kết quả không làm Ticket chuyển trạng thái.
- **AC-06-04:** Ghi nhận kết quả không làm mất lịch sử xử lý trước đó.
- **AC-06-05:** Ticket được mở lại hợp lệ quay về `IN_PROGRESS` và xuất hiện lại trong phạm vi xử lý phù hợp.

---

## III. QUY TẮC THAM CHIẾU

Các Functional Requirements của M02 phải tuân thủ thống nhất với:

- [Ticket Lifecycle](../../02-domain/ticket-lifecycle.md)
- [State Transition](../../02-domain/state-transition.md)
- [Business Rules](../../02-domain/business-rules.md)
