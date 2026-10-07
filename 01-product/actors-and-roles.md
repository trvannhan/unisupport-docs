# Các Vai Trò Trong Hệ Thống (Actors & Roles)

## 1. Danh Sách Vai Trò

UniSupport có **3 vai trò chính**:

```text
                    UNISUPPORT
                        |
        +---------------+---------------+
        |               |               |
        v               v               v
    SINH VIÊN       NHÂN VIÊN        QUẢN LÝ
     Student           Staff          Management
```

---

## 2. Vai Trò & Trách Nhiệm Chính

### 2.1 Sinh viên (Student)

**Mô tả**  
Người dùng gửi yêu cầu hỗ trợ và theo dõi quá trình xử lý yêu cầu của mình.

**Khả năng chính**
- Đăng nhập hệ thống.
- Tạo và gửi Ticket hỗ trợ.
- Chọn nhóm vấn đề và nhập nội dung yêu cầu.
- Đính kèm file ảnh/PDF khi cần.
- Xem trạng thái, lịch sử cập nhật và đơn vị/người phụ trách.
- Bổ sung thông tin hoặc giấy tờ khi được yêu cầu.
- Xem kết quả xử lý và các thông báo liên quan.
- Đánh giá mức độ hài lòng sau khi yêu cầu hoàn tất.

**Phạm vi dữ liệu**
- Chỉ được truy cập các Ticket thuộc chính tài khoản sinh viên đó.

### 2.2 Nhân viên (Staff)

**Mô tả**  
Nhân viên thuộc các phòng ban chịu trách nhiệm tiếp nhận và xử lý Ticket hỗ trợ sinh viên.

**Khả năng chính**
- Đăng nhập hệ thống.
- Xem các yêu cầu mới và các yêu cầu được giao trong phạm vi được phép.
- Phân loại Ticket và xem xét mức độ ưu tiên.
- Phân công hoặc chuyển Ticket sang đúng người/phòng ban khi cần.
- Cập nhật trạng thái xử lý.
- Yêu cầu sinh viên bổ sung thông tin hoặc giấy tờ.
- Ghi nhận kết quả và đóng yêu cầu sau khi hoàn thành.

**Phạm vi dữ liệu**
- Chỉ được truy cập và thao tác trên Ticket trong phạm vi quyền được cấp.

### 2.3 Quản lý (Management)

**Mô tả**  
Người dùng có trách nhiệm theo dõi tình hình vận hành, xem báo cáo và quản lý tài khoản/phân quyền.

**Khả năng chính**
- Đăng nhập hệ thống.
- Xem Dashboard tổng quan.
- Theo dõi khối lượng công việc theo phòng ban hoặc nhân viên.
- Xem báo cáo về xu hướng yêu cầu, thời gian xử lý và phản hồi sinh viên.
- Tạo/chỉnh sửa tài khoản.
- Gán quyền phù hợp với từng vai trò.
- Tra soát các thao tác quan trọng khi cần.

**Phạm vi dữ liệu**
- Truy cập dữ liệu và chức năng quản lý theo phạm vi quyền được cấp.

---

## 3. Ma Trận Quyền Ở Mức Sản Phẩm

| Chức năng / Hành động | Sinh viên | Nhân viên | Quản lý |
| :--- | :---: | :---: | :---: |
| Đăng nhập hệ thống | ✅ | ✅ | ✅ |
| Tạo Ticket hỗ trợ | ✅ | ❌ | ❌ |
| Xem Ticket của chính sinh viên | ✅ | Theo quyền | Theo quyền |
| Tiếp nhận / xử lý Ticket | ❌ | ✅ | Theo quyền |
| Chuyển phòng ban / người phụ trách | ❌ | ✅ | Theo quyền |
| Yêu cầu sinh viên bổ sung | ❌ | ✅ | Theo quyền |
| Bổ sung thông tin theo yêu cầu | ✅ | ❌ | ❌ |
| Ghi nhận kết quả / đóng Ticket | ❌ | ✅ | Theo quyền |
| Gửi đánh giá hài lòng | ✅ | ❌ | ❌ |
| Xem Dashboard / báo cáo | ❌ | ❌ | ✅ |
| Quản lý tài khoản / phân quyền | ❌ | ❌ | ✅ |
| Tra soát thao tác quan trọng | ❌ | Theo quyền | ✅ |

> Chi tiết quyền theo dữ liệu, trạng thái Ticket và từng hành động được đặc tả trong phần Domain, Functional Requirements và Security.
