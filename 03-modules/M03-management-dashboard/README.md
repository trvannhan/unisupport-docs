# Phân Hệ Quản Lý (M03 - Management Dashboard)

## 1. Tổng Quan Phân Hệ

Phân hệ **Quản lý (Management Dashboard)** là trung tâm điều hành dành riêng cho Ban Giám hiệu và Trưởng/Phó các Phòng ban chức năng tại **Aurora University**.

Phân hệ cung cấp các báo cáo số liệu trực quan theo thời gian thực về tình hình tiếp nhận và giải quyết yêu cầu hỗ trợ sinh viên, đo lường hiệu suất làm việc của từng phòng ban/nhân viên, đồng thời cung cấp công cụ quản trị tài khoản, phân quyền vai trò (RBAC) và tra soát lịch sử thao tác toàn hệ thống.

---

## 2. Mục Tiêu & Giá Trị Mang Lại

- **Giám sát thời gian thực (Real-time Monitoring)**: Theo dõi các chỉ số KPI vận hành cốt lõi (Tổng số Ticket, Số lượng quá hạn SLA, Thời gian xử lý trung bình, Chỉ số hài lòng CSAT).
- **Cơ sở điều phối nhân sự**: Giúp nhà trường nhận diện ngay phòng ban nào đang quá tải hoặc nhóm vấn đề nào phát sinh đột biến để kịp thời điều chỉnh quy trình/nhân sự.
- **Đánh giá chất lượng dịch vụ khách quan**: Tổng hợp phản hồi, điểm đánh giá sao và nhận xét của sinh viên sau khi yêu cầu được hoàn thành.
- **An toàn & Quản trị tập trung**: Quản lý vòng đời tài khoản người dùng, gán đúng vai trò/phòng ban và đảm bảo tính minh bạch nhờ nhật ký tra soát (Audit Log).

---

## 3. Danh Mục Yêu Cầu Chức Năng (Functional Requirements)

| Mã Yêu Cầu | Tên Chức Năng | Tóm Tắt Nghiệp Vụ |
| :--- | :--- | :--- |
| **FR-MGT-01** | Quản lý tài khoản, vai trò & RBAC | Tạo/sửa/khóa tài khoản, gán vai trò, kiểm soát quyền truy cập theo vai trò. |
| **FR-MGT-02** | Quản lý phòng ban & danh mục | Quản lý phòng ban, nhóm vấn đề/danh mục Ticket và dữ liệu cấu hình. |
| **FR-MGT-03** | Kiểm soát quyền truy cập & Audit Trail | Áp dụng kiểm soát truy cập, bảo vệ dữ liệu/file theo quyền và ghi nhận nhật ký thao tác. |
| **FR-MGT-04** | Quản lý thời hạn lưu trữ | Xác định thời hạn lưu trữ dữ liệu Ticket, file đính kèm, log. |
| **FR-MGT-05** | Dashboard & thống kê quản trị | Dashboard KPI, tổng số Ticket, Ticket đang xử lý, quá hạn. |
| **FR-MGT-06** | Báo cáo, mức độ hài lòng & xuất dữ liệu | Báo cáo thời gian xử lý, xu hướng nhóm vấn đề, CSAT, phản hồi sinh viên. |

### Effort Theo Bảng Chi Phí Nội Bộ Đã Chốt

| Gói việc | Effort |
| :--- | :---: |
| Quản lý tài khoản, vai trò & RBAC | **64h** |
| Quản lý phòng ban & danh mục | **26h** |
| Kiểm soát quyền truy cập & Audit Trail | **40h** |
| Quản lý thời hạn lưu trữ | **15h** |
| Dashboard & thống kê quản trị | **33h** |
| Báo cáo, mức độ hài lòng & xuất dữ liệu | **37h** |
| **Tổng M3 - Quản lý** | **215h** |

---

## 4. Sơ Đồ Luồng Tương Tác Của Quản Lý (Management Workflow)
```
[Đăng nhập (M05-Security)]
│
├───────────────────────────────┬───────────────────────────────┐
▼                               ▼                               ▼
[Dashboard KPI FR-MGT-05]     [Báo cáo & Xuất DL FR-MGT-06]   [Quản trị Hệ thống]
(Tổng Ticket, Overdue,         (Thời gian xử lý trung bình,      │
Chỉ số CSAT toàn trường)       Top xu hướng vấn đề)              ├──► [Tài khoản & RBAC FR-MGT-01]
                                                                 ├──► [Phòng ban & Danh mục FR-MGT-02]
                                                                 ├──► [Audit Trail FR-MGT-03]
                                                                 └──► [Thời hạn lưu trữ FR-MGT-04]
```

---

## 5. Quy Tắc Vận Hành & Thiết Kế Giao Diện (UI/UX Guidelines)

1. **Giao diện Trực quan (Data Visualization)**: Sử dụng các biểu đồ tròn (Pie chart) biểu diễn tỷ lệ trạng thái Ticket, biểu đồ cột (Bar chart) so sánh khối lượng công việc giữa các phòng ban, và biểu đồ đường (Line chart) thể hiện xu hướng theo thời gian.
2. **Bộ lọc Báo cáo linh hoạt (Filter Options)**: Cho phép lọc dữ liệu theo:
   - Khoảng thời gian (Hôm nay, Tuần này, Tháng này, Tùy chọn ngày).
   - Phòng ban chuyên trách.
   - Nhóm vấn đề (Category).
3. **Phân vùng dữ liệu xem (Data Scope)**:
   - **Trưởng phòng ban**: Chỉ xem được Báo cáo & KPI thuộc Phòng ban của mình phụ trách.
   - **Ban Giám hiệu / MANAGER**: Xem được Báo cáo & KPI toàn trường của tất cả phòng ban.
