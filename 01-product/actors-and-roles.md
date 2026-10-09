# Các Vai Trò Trong Hệ Thống (Actors & Roles)

## 1. Danh Sách Vai Trò

UniSupport có **3 nhóm người dùng chính**, tương ứng với 3 phân hệ của sản phẩm:

```text
                    UNISUPPORT
                        |
        +---------------+---------------+
        |               |               |
        v               v               v
    SINH VIÊN       NHÂN VIÊN        QUẢN LÝ
     Student           Staff          Management
```

Các quyền quản trị hệ thống không tạo thành một nhóm người dùng thứ tư. Chúng là các quyền thuộc phân hệ **Management** và chỉ được cấp cho tài khoản Quản lý phù hợp.

---

## 2. Vai Trò & Trách Nhiệm Chính

### 2.1 Sinh viên (Student)

**Mô tả**  
Người dùng gửi yêu cầu hỗ trợ và theo dõi quá trình xử lý các yêu cầu của chính mình.

**Khả năng chính**
- Đăng nhập hệ thống.
- Tra cứu hướng dẫn/FAQ.
- Tạo và gửi Ticket hỗ trợ.
- Chọn nhóm vấn đề và nhập nội dung yêu cầu.
- Đính kèm file minh chứng theo rule đã chốt.
- Xem trạng thái, lịch sử cập nhật và đơn vị/người phụ trách.
- Bổ sung thông tin hoặc giấy tờ khi được yêu cầu.
- Nhận thông báo và xem kết quả xử lý.
- Phản hồi khi kết quả chưa giải quyết vấn đề theo lifecycle đã chốt.
- Đánh giá mức độ hài lòng sau khi yêu cầu được giải quyết theo rule CSAT đã chốt.

**Phạm vi dữ liệu**
- Chỉ được truy cập các Ticket và dữ liệu thuộc chính tài khoản sinh viên đó.

### 2.2 Nhân viên (Staff)

**Mô tả**  
Nhân viên thuộc các phòng ban chịu trách nhiệm tiếp nhận và xử lý Ticket hỗ trợ sinh viên.

**Khả năng chính**
- Đăng nhập hệ thống.
- Xem, tìm kiếm và lọc các yêu cầu trong phạm vi được phép.
- Tiếp nhận, phân loại và phân công Ticket theo quyền được cấp.
- Xác định mức độ ưu tiên và theo dõi thời hạn xử lý.
- Cập nhật tiến độ/trạng thái xử lý.
- Yêu cầu sinh viên bổ sung thông tin hoặc giấy tờ.
- Chuyển Ticket sang người/phòng ban phù hợp hoặc thực hiện escalation theo rule đã chốt.
- Ghi nhận kết quả xử lý.
- Đóng/mở lại Ticket theo điều kiện lifecycle đã chốt.

**Phạm vi dữ liệu**
- Chỉ được truy cập và thao tác trên Ticket trong phạm vi phòng ban, nhiệm vụ và quyền được cấp.

### 2.3 Quản lý (Management)

**Mô tả**  
Người dùng có trách nhiệm giám sát hoạt động hỗ trợ và thực hiện các chức năng quản lý/quản trị được cấp quyền.

**Khả năng chính**
- Đăng nhập hệ thống.
- Xem Dashboard và số liệu tổng hợp trong phạm vi được cấp.
- Theo dõi khối lượng công việc theo phòng ban hoặc nhân viên.
- Theo dõi Ticket sắp/quá hạn và các chỉ số thời gian xử lý.
- Xem báo cáo về xu hướng yêu cầu, hiệu quả xử lý và phản hồi/CSAT.
- Phân công hoặc điều phối công việc khi được cấp quyền.
- Tạo/chỉnh sửa/khóa tài khoản và gán quyền/phòng ban khi được cấp quyền quản trị.
- Quản lý phòng ban, danh mục và các cấu hình nghiệp vụ thuộc phạm vi được cấp.
- Tra soát các thao tác quan trọng và quản lý các chính sách hệ thống được giao.

**Phạm vi dữ liệu**
- Truy cập dữ liệu và chức năng theo phạm vi quyền được cấp.
- Một tài khoản Management không mặc định có toàn quyền; các quyền quản trị chỉ khả dụng khi được cấu hình/cấp quyền.

---

## 3. Ma Trận Quyền Ở Mức Sản Phẩm

| Chức năng / Hành động | Sinh viên | Nhân viên | Quản lý |
| :--- | :---: | :---: | :---: |
| Đăng nhập hệ thống | ✅ | ✅ | ✅ |
| Tra cứu FAQ/hướng dẫn | ✅ | ❌ | Theo quyền |
| Tạo Ticket hỗ trợ | ✅ | ❌ | ❌ |
| Xem Ticket của chính sinh viên | ✅ | Theo quyền | Theo quyền |
| Tiếp nhận / xử lý Ticket | ❌ | ✅ | Theo quyền |
| Phân loại / xác định ưu tiên | ❌ | ✅ | Theo quyền |
| Phân công / chuyển xử lý / escalation | ❌ | Theo quyền | Theo quyền |
| Yêu cầu sinh viên bổ sung | ❌ | ✅ | Theo quyền |
| Bổ sung thông tin theo yêu cầu | ✅ | ❌ | ❌ |
| Ghi nhận kết quả / đóng / mở lại Ticket | ❌ | Theo quyền | Theo quyền |
| Gửi đánh giá hài lòng | ✅ | ❌ | ❌ |
| Xem Dashboard / báo cáo | ❌ | ❌ | ✅ |
| Quản lý tài khoản / phân quyền | ❌ | ❌ | Theo quyền quản trị |
| Quản lý phòng ban / danh mục | ❌ | ❌ | Theo quyền quản trị |
| Tra soát thao tác quan trọng | ❌ | Theo quyền | Theo quyền quản trị |

> Chi tiết quyền theo dữ liệu, trạng thái Ticket và từng hành động được đặc tả trong phần Domain, Functional Requirements, Workflows và Security.
