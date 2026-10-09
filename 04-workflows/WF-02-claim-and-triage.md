# WF-02 - Tiếp Nhận, Phân Loại Và Phân Công

## 1. Mục Đích Và Phạm Vi

Mô tả cách Ticket mới trong hàng chờ phòng ban được kiểm tra Nhóm vấn đề, tiếp nhận hoặc phân công cho một nhân viên và bắt đầu quá trình xử lý.

## 2. Vai Trò Và Điều Kiện Bắt Đầu

- **Vai trò chính:** Nhân viên.
- **Vai trò bổ sung:** Nhân viên/Quản lý có quyền phân công.
- Ticket thuộc phạm vi phòng ban và đang ở `NEW` hoặc chưa có người phụ trách.

## 3. Luồng Nghiệp Vụ Chính

1. Nhân viên mở hàng chờ Ticket của phòng ban.
2. Hệ thống hiển thị Ticket mới/chưa có người phụ trách.
3. Nhân viên mở Ticket và kiểm tra nội dung, file và Category hiện tại.
4. Nếu Category chưa phù hợp, nhân viên chọn lại một Category đang hoạt động.
5. Nếu Category mới vẫn thuộc phòng ban hiện tại, hệ thống lưu thay đổi Category và lịch sử tương ứng.
6. Nhân viên chọn **Tiếp nhận**, hoặc người có quyền chọn một nhân viên hợp lệ để **Phân công**.
7. Hệ thống kiểm tra Ticket chưa bị người khác tiếp nhận/chuyển xử lý và nhân viên được chọn còn hợp lệ.
8. Hệ thống ghi nhận tối đa một người phụ trách chính.
9. Nếu Ticket đang ở `NEW`, hệ thống chuyển Ticket sang `IN_PROGRESS`.
10. Hệ thống ghi nhận việc phân loại/phân công vào lịch sử và Ticket xuất hiện trong danh sách xử lý của người phụ trách.

Nếu Category mới thuộc phòng ban khác, việc thay đổi chỉ được hoàn tất thông qua **WF-04 - Chuyển xử lý sang phòng ban khác**.

## 4. Luồng Ngoại Lệ

- Hai nhân viên cùng tiếp nhận: chỉ một người được trở thành người phụ trách chính; người còn lại nhận dữ liệu mới nhất.
- Nhân viên được chọn không còn hoạt động hoặc không thuộc phòng ban hiện tại: từ chối phân công.
- Ticket đã được chuyển sang phòng ban khác: không cho hoàn tất thao tác theo dữ liệu cũ.
- Category mới thuộc phòng ban khác: chuyển sang WF-04 thay vì lưu Category riêng lẻ.

## 5. Quy Tắc Nghiệp Vụ

- Một Ticket có tối đa một người phụ trách chính tại một thời điểm.
- Ticket có thể chưa có người phụ trách trước khi tiếp nhận/phân công.
- Category phải lấy từ danh mục đang hoạt động.
- Việc thay đổi Category, người phụ trách và trạng thái phải được ghi nhận trong lịch sử.
- Mức độ ưu tiên và thời hạn tuân theo `BR-DUE-01` và `BR-DUE-02`.

## 6. Tiêu Chí Nghiệm Thu

- Tiếp nhận Ticket `NEW` hợp lệ gán đúng người phụ trách và chuyển sang `IN_PROGRESS`.
- Không thể có hai người phụ trách chính đồng thời.
- Phân công chỉ chấp nhận nhân viên hợp lệ thuộc phòng ban hiện tại.
- Category thuộc phòng ban khác không được lưu nếu WF-04 chưa hoàn tất.

## 7. Tài Liệu Liên Quan

- M02: `FR-STF-01`, `FR-STF-02`, `FR-STF-03`.
- Domain: `BR-OWN-01`, `BR-DUE-01`, `BR-DUE-02`.
