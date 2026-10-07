# Phân Hệ Nhân Viên (M02 - Staff Operations)

## 1. Tổng Quan Phân Hệ

Phân hệ **Nhân viên (Staff Operations)** là không gian làm việc chính dành cho cán bộ, chuyên viên thuộc các Phòng ban chức năng tại **Aurora University** (Phòng Đào tạo, Phòng CTHSSV, Phòng Tài chính - Kế toán, Trung tâm CNTT, Thư viện...). 

Phân hệ này cung cấp các công cụ vận hành giúp nhân viên tiếp nhận, phân loại, phân công, điều phối liên phòng ban, trao đổi với sinh viên và ghi nhận kết quả xử lý các phiếu hỗ trợ (Ticket) một cách chuyên nghiệp, tránh bỏ sót hoặc xử lý trùng lặp.

---

## 2. Mục Tiêu & Giá Trị Mang Lại

- **Hòm thư công việc tập trung (Centralized Inbox)**: Gom toàn bộ yêu cầu của sinh viên về một nơi, chia theo Phòng ban và Cá nhân phụ trách.
- **Phân công & Phối hợp rõ ràng**: Loại bỏ tình trạng đùn đẩy công việc nhờ cơ chế Tiếp nhận (Claim), Phân công (Assign) và Chuyển phòng ban (Transfer) minh bạch.
- **Kiểm soát tiến độ & SLA**: Theo dõi mức độ ưu tiên và thời hạn cam kết xử lý (SLA), hạn chế tối đa các yêu cầu bị trễ hạn.
- **Lưu vết toàn bộ quá trình**: Mọi ghi chú nội bộ, yêu cầu bổ sung thông tin hay cập nhật kết quả đều được ghi nhận vào nhật ký tra soát (Audit Trail).

---

## 3. Danh Mục Yêu Cầu Chức Năng (Functional Requirements)

| Mã Yêu Cầu | Tên Chức Năng | Tóm Tắt Nghiệp Vụ |
| :--- | :--- | :--- |
| **FR-STF-01** | Tiếp nhận, tìm kiếm & lọc yêu cầu | Xem danh sách yêu cầu mới/được giao, tìm kiếm, lọc theo trạng thái, phòng ban, mức ưu tiên. |
| **FR-STF-02** | Phân loại & phân công xử lý | Claim Ticket chưa có chủ hoặc Assign cho nhân viên, chuẩn hóa nhóm vấn đề. |
| **FR-STF-03** | Quản lý ưu tiên & thời hạn | Thiết lập mức ưu tiên, tính/hiển thị SLA, cảnh báo quá hạn. |
| **FR-STF-04** | Xử lý & cập nhật yêu cầu | Ghi nhận tiến độ, trao đổi với sinh viên, yêu cầu bổ sung thông tin/hồ sơ. |
| **FR-STF-05** | Chuyển xử lý, Escalation & hoàn tất | Chuyển phòng ban/người phụ trách khi cần, escalation các trường hợp khó. |
| **FR-STF-06** | Đóng & mở lại yêu cầu | Đóng yêu cầu sau khi hoàn tất hoặc mở lại khi sinh viên phản hồi/chưa hài lòng. |

### Effort Theo Bảng Chi Phí Nội Bộ Đã Chốt

| Gói việc | Effort |
| :--- | :---: |
| Tiếp nhận, tìm kiếm & lọc yêu cầu | **33h** |
| Phân loại & phân công xử lý | **38h** |
| Quản lý ưu tiên & thời hạn | **29h** |
| Xử lý & cập nhật yêu cầu | **39h** |
| Chuyển xử lý, Escalation & hoàn tất | **32h** |
| Đóng & mở lại yêu cầu | **26h** |
| **Tổng M2 - Staff** | **197h** |

---

## 4. Sơ Đồ Luồng Tương Tác Của Nhân Viên (Staff Workflow)
```
[Đăng nhập (M05-Security)] ──► [Hòm thư Phòng ban / Inbox]
                                 │
                                 ▼
                [Tiếp nhận & Lọc FR-STF-01]
                                 │
                                 ▼
                [Phân loại & Phân công FR-STF-02]
                                 │
                                 ▼
                    [Ưu tiên & SLA FR-STF-03]
                                 │
┌────────────────────────────────┼────────────────────────────────┐
▼                                ▼                                ▼
[Chuyển PB/Escalation FR-STF-05] [Xử lý & Bổ sung FR-STF-04] [Xử lý nghiệp vụ]
│                                │                                │
▼                                ▼                                │
(Chờ PB mới Claim)      (Tạm dừng đếm SLA)                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┤
                                                                  ▼
                                                    [Đóng & mở lại FR-STF-06]
                                                                  │
                                                                  ▼
                                                    [Chuyển trạng thái RESOLVED]
```

---

## 5. Quy Tắc Vận Hành & Giao Diện (Operational & UI Guidelines)

1. **Bộ lọc danh sách công việc (Inbox Filters)**:
   - **Ticket Mới (Department New)**: Các Ticket gửi đến phòng ban chưa có người tiếp nhận.
   - **Việc của tôi (My Assigned)**: Các Ticket do cá nhân nhân viên đang thụ lý.
   - **Chờ sinh viên bổ sung (Pending Student)**: Các Ticket đang chờ phản hồi từ sinh viên.
   - **Cảnh báo Quá hạn (Overdue / High Priority)**: Các Ticket sắp hoặc đã vượt thời gian SLA.
2. **Phân biệt Ghi chú Nội bộ vs Phản hồi Công khai**:
   - **Internal Note (Vàng)**: Trao đổi nội bộ giữa các nhân viên/quản lý, sinh viên **KHÔNG** nhìn thấy.
   - **Public Response (Trắng/Xanh)**: Phản hồi chính thức gửi tới sinh viên.
3. **An toàn bảo mật**: Nhân viên chỉ được xem file đính kèm của các Ticket thuộc Phòng ban mình phụ trách.
