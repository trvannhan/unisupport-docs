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
- Chọn nhóm vấn đề và cung cấp nội dung, tài liệu liên quan.
- Xem trạng thái, lịch sử cập nhật và đơn vị/người phụ trách.
- Bổ sung thông tin hoặc giấy tờ khi được yêu cầu.
- Nhận thông báo và xem kết quả xử lý.
- Phản hồi nếu kết quả chưa giải quyết được vấn đề.
- Đánh giá mức độ hài lòng sau khi yêu cầu được giải quyết.

**Phạm vi dữ liệu**
- Chỉ được truy cập các Ticket và dữ liệu thuộc chính tài khoản sinh viên đó.

### 2.2 Nhân viên (Staff)

**Mô tả**  
Nhân viên thuộc các phòng ban chịu trách nhiệm tiếp nhận và xử lý Ticket hỗ trợ sinh viên.

**Khả năng chính**
- Đăng nhập hệ thống.
- Xem, tìm kiếm và lọc các yêu cầu trong phạm vi được phép.
- Tiếp nhận và phân loại Ticket.
- Xử lý các Ticket được giao.
- Xác định mức độ ưu tiên và theo dõi thời hạn xử lý.
- Cập nhật trạng thái và ghi nhận hoạt động xử lý.
- Yêu cầu sinh viên bổ sung thông tin hoặc giấy tờ.
- Phân công hoặc chuyển Ticket sang người/phòng ban phù hợp khi được cấp quyền.
- Thực hiện escalation khi cần thiết.
- Ghi nhận kết quả và hoàn tất/đóng Ticket.
- Mở lại Ticket khi đáp ứng điều kiện nghiệp vụ đã quy định.

**Phạm vi dữ liệu**
- Chỉ được truy cập và thao tác trên Ticket trong phạm vi phòng ban, nhiệm vụ và quyền được cấp.

### 2.3 Quản lý (Management)

**Mô tả**  
Người dùng chịu trách nhiệm giám sát hoạt động hỗ trợ và thực hiện các chức năng quản lý/quản trị được cấp quyền.

**Khả năng chính**
- Đăng nhập hệ thống.
- Xem Dashboard và số liệu tổng hợp trong phạm vi được cấp.
- Theo dõi số lượng Ticket mới, đang xử lý, sắp quá hạn và đã quá hạn.
- Theo dõi khối lượng công việc theo phòng ban hoặc nhân viên.
- Xem báo cáo về loại yêu cầu, thời gian xử lý và mức độ hài lòng.
- Quản lý tài khoản, vai trò và quyền khi được cấp quyền quản trị.
- Quản lý phòng ban và danh mục Ticket.
- Tra soát Audit Trail và các thay đổi quan trọng.
- Quản lý thời hạn lưu trữ dữ liệu theo chính sách đã chốt.
- Xuất dữ liệu/báo cáo theo chức năng được cung cấp.

**Phạm vi dữ liệu**
- Truy cập dữ liệu và chức năng theo phạm vi quyền được cấp.
- Các chức năng quản trị chỉ được sử dụng bởi tài khoản Management có quyền phù hợp.

---

## 3. Bảng Tổng Hợp Quyền Theo Nhóm Người Dùng

| Chức năng / Hành động | Sinh viên | Nhân viên | Quản lý |
| :--- | :---: | :---: | :---: |
| Đăng nhập hệ thống | ✅ | ✅ | ✅ |
| Tra cứu FAQ/hướng dẫn | ✅ | ❌ | ❌ |
| Tạo Ticket hỗ trợ | ✅ | ❌ | ❌ |
| Xem Ticket theo phạm vi được cấp | Ticket của mình | ✅ | Theo quyền |
| Tiếp nhận / xử lý Ticket | ❌ | ✅ | Theo quyền |
| Phân loại / xác định ưu tiên | ❌ | ✅ | Theo quyền |
| Phân công / chuyển xử lý / escalation | ❌ | Theo quyền | Theo quyền |
| Yêu cầu sinh viên bổ sung | ❌ | ✅ | Theo quyền |
| Bổ sung thông tin theo yêu cầu | ✅ | ❌ | ❌ |
| Ghi nhận kết quả / đóng / mở lại Ticket | ❌ | ✅ | Theo quyền |
| Gửi đánh giá hài lòng | ✅ | ❌ | ❌ |
| Xem Dashboard / báo cáo | ❌ | ❌ | ✅ |
| Quản lý tài khoản / phân quyền | ❌ | ❌ | Theo quyền quản trị |
| Quản lý phòng ban / danh mục | ❌ | ❌ | Theo quyền quản trị |
| Xem Audit Trail / tra soát thay đổi | ❌ | ❌ | Theo quyền quản trị |
| Quản lý thời hạn lưu trữ dữ liệu | ❌ | ❌ | Theo quyền quản trị |
| Xuất báo cáo / dữ liệu | ❌ | ❌ | Theo quyền |

> Chi tiết quyền theo dữ liệu, trạng thái Ticket và từng hành động được đặc tả trong phần Domain, Functional Requirements, Workflows và Security.
