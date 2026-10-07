# Tài Liệu Đặc Tả Yêu Cầu Sản Phẩm - Phân Hệ Quản Lý (PRD - M03 Management Dashboard)

## 1. Tổng Quan Phân Hệ & Cơ Cấu Effort Theo Bảng Chi Phí Nội Bộ

Phân hệ **Quản lý / Quản lý (Management Dashboard)** phục vụ Ban Giám hiệu và Trưởng/Phó phòng ban trong việc theo dõi số liệu vận hành, xem báo cáo, quản trị tài khoản, vai trò, phòng ban, danh mục, phân quyền và tra soát hoạt động hệ thống.

### Bảng Phân Rã Chức Năng & Effort Đã Chốt (Tổng: 215h)

| Mã gói việc | Tên chức năng theo bảng chi phí | Tóm tắt scope nghiệp vụ | Effort kế hoạch |
| :--- | :--- | :--- | :---: |
| **WP-MGT-01** | Quản lý tài khoản, vai trò & RBAC | Tạo/sửa/khóa tài khoản, gán vai trò, kiểm soát quyền truy cập theo vai trò và phạm vi dữ liệu. | **64h** |
| **WP-MGT-02** | Quản lý phòng ban & danh mục | Quản lý phòng ban, nhóm vấn đề/danh mục Ticket và dữ liệu cấu hình phục vụ phân loại yêu cầu. | **26h** |
| **WP-MGT-03** | Kiểm soát quyền truy cập & Audit Trail | Áp dụng kiểm soát truy cập, bảo vệ dữ liệu/file theo quyền và ghi nhận nhật ký thao tác quan trọng. | **40h** |
| **WP-MGT-04** | Quản lý thời hạn lưu trữ | Xác định thời hạn lưu trữ dữ liệu Ticket, file đính kèm, log và dữ liệu báo cáo theo phạm vi dự án. | **15h** |
| **WP-MGT-05** | Dashboard & thống kê quản trị | Dashboard KPI, tổng số Ticket, Ticket đang xử lý, quá hạn, khối lượng theo phòng ban/nhân viên. | **33h** |
| **WP-MGT-06** | Báo cáo, mức độ hài lòng & xuất dữ liệu | Báo cáo thời gian xử lý, xu hướng nhóm vấn đề, CSAT, phản hồi sinh viên và xuất dữ liệu phục vụ quản lý. | **37h** |
| **TỔNG M3 - Quản lý** | | | **215h** |

---



### [FR-MGT-05] Dashboard & thống kê quản trị

**Mô tả**
Cung cấp màn hình Tổng quan hiển thị các thẻ chỉ số KPI cốt lõi và biểu đồ trực quan về tình hình xử lý phiếu hỗ trợ theo thời gian thực.

**Actor**
Quản lý / Quản trị viên.

**Preconditions**
- Người dùng đã đăng nhập tài khoản Quản lý thành công.

**Luồng chính**
1. Quản lý chọn mục **Dashboard Tổng quan**.
2. Hệ thống tải và hiển thị các thẻ chỉ số KPI (KPI Cards):
   - **Tổng số Ticket**: Tổng yêu cầu tiếp nhận trong khoảng thời gian đã chọn.
   - **Đang xử lý**: Số Ticket ở trạng thái `NEW`, `IN_PROGRESS`, `WAITING_STUDENT`.
   - **Quá hạn SLA**: Số Ticket chưa hoàn thành đã vượt quá mốc thời gian cam kết.
   - **Chỉ số CSAT trung bình**: Điểm đánh giá hài lòng trung bình từ sinh viên (Thang điểm 1-5 sao).
3. Hệ thống hiển thị các biểu đồ:
   - **Biểu đồ tỷ lệ trạng thái**: Tỷ lệ % Ticket theo các trạng thái.
   - **Biểu đồ khối lượng công việc theo phòng ban**: So sánh số Ticket giữa các Phòng ban.
4. Quản lý thay đổi Bộ lọc thời gian (Ví dụ: "Tuần này", "Tháng này").
5. Hệ thống tính toán và cập nhật lại toàn bộ chỉ số và biểu đồ theo khoảng thời gian mới.

**Business Rules**
- Dữ liệu KPI được tổng hợp và làm mới tự động hoặc khi người dùng chọn Tải lại.
- Chỉ số quá hạn SLA chỉ tính trên các Ticket chưa ở trạng thái `RESOLVED` hoặc `CLOSED` mà mốc `sla_due_at` nhỏ hơn thời điểm hiện tại.

**Alternative / Error Flows**
- **Không có dữ liệu trong khoảng thời gian chọn**: Hệ thống hiển thị chỉ số = 0 và biểu đồ dạng trống (Empty chart state) kèm thông báo "Không có dữ liệu trong khoảng thời gian này".

**Acceptance Criteria**
- **AC-01**: Thẻ chỉ số hiển thị chính xác số lượng Ticket theo thời gian thực.
- **AC-02**: Thay đổi bộ lọc thời gian -> Các số liệu và biểu đồ tự động cập nhật tương ứng.
- **AC-03**: Nhấn vào thẻ "Quá hạn SLA" -> Hệ thống chuyển sang danh sách chi tiết các Ticket quá hạn.

**Ví dụ Edge Case**
Một Ticket hết hạn SLA lúc 10:00 AM. Quản lý xem Dashboard lúc 10:01 AM.
-> **Expected Result**: Thẻ chỉ số "Quá hạn SLA" tự động tăng thêm 1 đơn vị.

---

### [FR-MGT-06] Báo cáo, mức độ hài lòng & xuất dữ liệu

**Mô tả**
Cung cấp các báo cáo chi tiết về Thời gian xử lý trung bình (Average Resolution Time), xu hướng nhóm vấn đề phát sinh nhiều nhất và tổng hợp ý kiến phản hồi của sinh viên.

**Actor**
Quản lý / Quản trị viên.

**Preconditions**
- Người dùng đã đăng nhập tài khoản Quản lý.

**Luồng chính**
1. Quản lý truy cập mục **Báo cáo & Phân tích**.
2. Quản lý chọn loại báo cáo:
   - **Báo cáo Thời gian xử lý**: Hiển thị thời gian giải quyết trung bình (tính bằng giờ/ngày) theo từng Phòng ban hoặc từng Nhân viên.
   - **Báo cáo Xu hướng vấn đề**: Thống kê top 5 nhóm vấn đề (Category) sinh viên gặp phải nhiều nhất.
   - **Báo cáo Phản hồi CSAT**: Thống kê chi tiết danh sách đánh giá sao và nhận xét văn bản của sinh viên.
3. Quản lý chọn các tiêu chí lọc (Phòng ban, Ngày bắt đầu, Ngày kết thúc).
4. Hệ thống xuất ra giao diện báo cáo dạng bảng và biểu đồ tương ứng.

**Business Rules**
- Thời gian xử lý của 1 Ticket = `resolved_at` - `created_at` (đã trừ đi khoảng thời gian tạm dừng ở trạng thái `WAITING_STUDENT`).
- Báo cáo CSAT chỉ tính toán dựa trên các Ticket đã có đánh giá sao từ sinh viên.

**Alternative / Error Flows**
- **Khoảng thời gian chọn không hợp lệ (Ngày kết thúc trước Ngày bắt đầu)**: Hệ thống báo lỗi "Ngày kết thúc phải lớn hơn hoặc bằng Ngày bắt đầu".

**Acceptance Criteria**
- **AC-01**: Báo cáo thời gian xử lý trung bình hiển thị chính số giờ/ngày xử lý thực tế của phòng ban.
- **AC-02**: Danh sách Top nhóm vấn đề xếp theo thứ tự giảm dần số lượng Ticket phát sinh.
- **AC-03**: Hiển thị đầy đủ nhận xét và số sao đánh giá trong Báo cáo CSAT.

**Ví dụ Edge Case**
Trong tháng 10, Phòng Đào tạo nhận 100 Ticket, trong đó nhóm "Đăng ký tín chỉ" chiếm 60 Ticket.
-> **Expected Result**: Báo cáo Xu hướng vấn đề hiển thị "Đăng ký tín chỉ" đứng vị trí Top 1 với tỷ lệ 60%.

---

### [FR-MGT-01] Quản lý tài khoản, vai trò & RBAC

**Mô tả**
Cho phép Quản lý (Manager) khởi tạo tài khoản mới, cập nhật thông tin cá nhân và thực hiện Khóa/Mở khóa tài khoản người dùng trong hệ thống UniSupport.

**Actor**
Quản lý (Manager).

**Preconditions**
- Người dùng đăng nhập bằng tài khoản có vai trò `MANAGER`.

**Luồng chính**
1. Quản lý truy cập mục **Quản lý Tài khoản**.
2. Hệ thống hiển thị danh sách toàn bộ tài khoản người dùng (Sinh viên, Nhân viên, Quản lý).
3. **Thao tác 1 (Tạo tài khoản mới)**:
   - Quản lý nhấn **Tạo tài khoản**.
   - Quản lý nhập Email, Họ tên, Mã định danh (Mã SV / Mã NV), Mật khẩu khởi tạo và chọn Vai trò.
   - Quản lý nhấn **Lưu**.
4. **Thao tác 2 (Khóa / Mở khóa tài khoản)**:
   - Quản lý chọn tài khoản cần thao tác và chọn **Khóa tài khoản** (Disable) hoặc **Mở khóa** (Enable).
   - Quản lý nhập lý do thao tác.
   - Quản lý nhấn **Xác nhận**.
5. Hệ thống kiểm tra và cập nhật trạng thái tài khoản (`Active` hoặc `Inactive`).
6. Ghi nhận sự kiện vào Audit Log.

**Business Rules**
- Email và Mã sinh viên/Mã nhân viên là DUY NHẤT trong hệ thống.
- Tài khoản bị khóa (`Inactive`) sẽ lập tức bị hủy phiên đăng nhập hiện tại và không thể đăng nhập lại cho đến khi được mở khóa.
- Quản lý không thể tự khóa tài khoản của chính mình.

**Alternative / Error Flows**
- **Trùng Email hoặc Mã định danh**: Hệ thống báo lỗi "Email hoặc Mã định danh đã tồn tại trong hệ thống".

**Acceptance Criteria**
- **AC-01**: Quản lý tạo thành công tài khoản mới với đầy đủ thông tin hợp lệ.
- **AC-02**: Quản lý chọn khóa tài khoản người dùng A -> Tài khoản A chuyển sang `Inactive`, người dùng A bị kích ra khỏi hệ thống nếu đang làm việc.
- **AC-03**: Nhập trùng Email đã có -> Hệ thống hiển thị lỗi validation.

**Ví dụ Edge Case**
Quản lý thực hiện khóa tài khoản của Nhân viên B khi Nhân viên B đang đăng nhập xử lý Ticket.
-> **Expected Result**: Ngay thao tác gửi request tiếp theo của Nhân viên B, hệ thống từ chối và đẩy về màn hình Đăng nhập với thông báo "Tài khoản của bạn đã bị khóa".

---

#### Tích hợp: Phân quyền vai trò & Phòng ban

**Mô tả**
Cho phép Quản trị viên gán Vai trò hệ thống (`STUDENT`, `STAFF`, `MANAGER`) và gán Phòng ban chuyên trách cho tài khoản Nhân viên/Quản lý.

**Actor**
Quản lý (Manager).

**Preconditions**
- Người dùng có quyền `MANAGER`.

**Luồng chính**
1. Quản lý truy cập mục **Phân quyền & Phòng ban**.
2. Quản lý tìm kiếm và chọn tài khoản nhân viên cần cấu hình.
3. Quản lý chọn **Vai trò (Role)** tương ứng từ danh sách: `STAFF`, `MANAGER`.
4. Quản lý chọn **Phòng ban (Department)** phụ trách (Ví dụ: Phòng Đào tạo, Phòng CTHSSV...).
5. Quản lý nhấn **Lưu phân quyền**.
6. Hệ thống kiểm tra dữ liệu và cập nhật quyền hạn cho tài khoản.
7. Ghi vết thao tác vào Audit Log.

**Business Rules**
- Một tài khoản Nhân viên (`STAFF`) bắt buộc phải thuộc về **ít nhất 01 Phòng ban**.
- Quyền hạn mới có hiệu lực ngay lập tức sau khi lưu.

**Alternative / Error Flows**
- **Gán vai trò STAFF nhưng không chọn Phòng ban**: Hệ thống dừng thao tác và báo lỗi "Tài khoản Nhân viên bắt buộc phải thuộc về ít nhất một Phòng ban".

**Acceptance Criteria**
- **AC-01**: Gán vai trò `STAFF` và gán Phòng Đào tạo cho nhân viên A -> Nhân viên A đăng nhập thấy đúng Hòm thư Phòng Đào tạo.
- **AC-02**: Đổi vai trò nhân viên A từ `STAFF` lên `MANAGER` -> Nhân viên A truy cập được thêm các Báo cáo của phòng ban đó.

**Ví dụ Edge Case**
Quản lý chuyển Nhân viên C từ Phòng Đào tạo sang Phòng CTHSSV.
-> **Expected Result**: Nhân viên C lập tức không còn thấy danh sách Ticket của Phòng Đào tạo mà chuyển sang thấy Ticket của Phòng CTHSSV.

---

### [FR-MGT-03] Kiểm soát quyền truy cập & Audit Trail

**Mô tả**
Cho phép Quản trị viên xem nhật ký lưu vết toàn bộ các hành động quan trọng diễn ra trên hệ thống để phục vụ tra soát khi có khiếu nại hoặc sự cố.

**Actor**
Quản lý (Manager).

**Preconditions**
- Người dùng đăng nhập bằng tài khoản `MANAGER`.

**Luồng chính**
1. Quản lý truy cập mục **Nhật ký tra soát (Audit Log)**.
2. Hệ thống hiển thị bảng danh sách các bản ghi nhật ký sắp xếp theo thời gian mới nhất.
3. Mỗi bản ghi hiển thị:
   - **Thời gian**: Mốc thời gian thực hiện (UTC/Local time).
   - **Tác nhân**: Tên & Email người thực hiện thao tác.
   - **Hành động**: Loại hành động (Ví dụ: `TICKET_STATUS_CHANGE`, `DEPARTMENT_TRANSFER`, `USER_LOCKED`...).
   - **Chi tiết**: Mô tả sự thay đổi dữ liệu (Giá trị cũ -> Giá trị mới).
   - **Địa chỉ IP**: Địa chỉ IP client thực hiện.
4. Quản lý có thể lọc log theo Khoảng thời gian, Tác nhân hoặc Mã Ticket.

**Business Rules**
- Nhật ký hệ thống tuân thủ quy tắc `BR-AUD-01` (Chỉ ghi - Append-only, tuyệt đối không được sửa hoặc xóa).
- Mọi thao tác thay đổi trạng thái Ticket, Chuyển phòng ban, Khóa tài khoản đều phải bắt buộc ghi log.

**Alternative / Error Flows**
- **Không tìm thấy bản ghi theo điều kiện lọc**: Hiển thị bảng trống kèm thông báo "Không tìm thấy nhật ký phù hợp".

**Acceptance Criteria**
- **AC-01**: Mọi hành động quan trọng do bất kỳ người dùng nào thực hiện đều sinh ra 01 bản ghi Audit Log tương ứng ngay lập tức.
- **AC-02**: Dữ liệu Audit Log chỉ ở dạng xem (Read-only), không có nút Sửa hoặc Xóa trên giao diện.
- **AC-03**: Lọc theo Mã Ticket `TK-20261004-001` -> Hiển thị toàn bộ lịch sử biến đổi của Ticket đó từ lúc tạo đến lúc đóng.

**Ví dụ Edge Case**
Nhân viên A chuyển Ticket sang Phòng ban khác lúc 14:30. Quản lý mở trang Audit Log lúc 14:31.
-> **Expected Result**: Dòng log ghi nhận hành động `DEPARTMENT_TRANSFER` của Nhân viên A hiển thị ngay ở đầu danh sách.

---

### [FR-MGT-04] Quản lý thời hạn lưu trữ

**Mô tả**
Cho phép Quản lý thiết lập và kiểm soát thời hạn lưu trữ (retention policy) đối với Ticket đã đóng, file đính kèm và Audit Log để tối ưu dung lượng hệ thống theo chính sách của nhà trường.

**Actor**
Quản lý (Manager).

**Preconditions**
- Người dùng đăng nhập bằng tài khoản có vai trò `MANAGER`.

**Luồng chính**
1. Quản lý truy cập mục **Cấu hình lưu trữ**.
2. Quản lý xem các mức thiết lập lưu trữ hiện tại (vd: Ticket lưu 3 năm, File lưu 1 năm, Log lưu 6 tháng).
3. Quản lý điều chỉnh các mốc thời gian lưu trữ theo cấu hình cho phép.
4. Quản lý nhấn **Lưu cấu hình**.
5. Hệ thống cập nhật thời hạn lưu trữ và ghi nhận Audit Log.

**Business Rules**
- Chỉ tài khoản có thẩm quyền Quản lý hệ thống mới có thể chỉnh sửa cấu hình này.
- Các quy định xóa dữ liệu tự động định kỳ (cron job) sẽ dựa trên cấu hình lưu trữ này.

---

### [FR-MGT-02] Quản lý phòng ban & danh mục

**Mô tả**
Cho phép Quản lý quản lý các dữ liệu cấu hình phục vụ vận hành hệ thống, bao gồm Phòng ban, Nhóm vấn đề/Danh mục Ticket và thao tác xuất dữ liệu báo cáo theo phạm vi đã chốt trong bảng chi phí nội bộ.

**Actor**
Quản lý (Manager).

**Preconditions**
- Người dùng đăng nhập bằng tài khoản có vai trò `MANAGER`.

**Luồng chính**
1. Quản lý truy cập mục **Cấu hình hệ thống**.
2. Quản lý xem danh sách Phòng ban và Nhóm vấn đề/Danh mục Ticket.
3. Quản lý tạo mới hoặc cập nhật thông tin cấu hình cần thiết.
4. Quản lý cấu hình thời hạn lưu trữ dữ liệu theo chính sách của dự án.
5. Quản lý truy cập báo cáo và chọn **Xuất dữ liệu** theo bộ lọc thời gian/phòng ban.
6. Hệ thống tạo file xuất dữ liệu và ghi nhận thao tác vào Audit Log.

**Business Rules**
- Không được xóa cứng Phòng ban/Danh mục đã phát sinh Ticket; chỉ cho phép chuyển trạng thái ngừng sử dụng để bảo toàn lịch sử dữ liệu.
- File xuất dữ liệu chỉ bao gồm dữ liệu nằm trong phạm vi quyền của người dùng.
- Việc xuất dữ liệu phải ghi nhận người thực hiện, thời điểm, bộ lọc và loại báo cáo vào Audit Log.

**Alternative / Error Flows**
- **Tên phòng ban hoặc mã danh mục bị trùng**: Hệ thống không lưu và hiển thị lỗi validation.
- **Không có dữ liệu theo bộ lọc xuất báo cáo**: Hệ thống thông báo không có dữ liệu phù hợp và không tạo file rỗng gây hiểu nhầm.

**Acceptance Criteria**
- **AC-01**: Quản lý tạo mới Phòng ban hoặc Nhóm vấn đề hợp lệ -> Dữ liệu xuất hiện trong danh sách lựa chọn khi tạo/phân loại Ticket.
- **AC-02**: Quản lý vô hiệu hóa một danh mục đã có Ticket lịch sử -> Ticket cũ vẫn xem được dữ liệu danh mục, nhưng danh mục không còn xuất hiện cho Ticket mới.
- **AC-03**: Quản lý xuất báo cáo theo khoảng thời gian -> Hệ thống tạo file dữ liệu đúng bộ lọc và ghi Audit Log.
