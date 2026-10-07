# Hiện Trạng & Bài Toán Nghiệp Vụ (Problem Statement)

## 1. Hiện Trạng Tiếp Nhận Yêu Cầu Tại Aurora University

Hiện tại, sinh viên có thể gửi yêu cầu hỗ trợ qua nhiều kênh khác nhau như email, điện thoại, biểu mẫu trực tuyến, tin nhắn mạng xã hội, trao đổi trực tiếp hoặc nhờ người khác chuyển tiếp. Mỗi phòng ban có thể sử dụng cách quản lý riêng, khiến dữ liệu hỗ trợ bị phân tán và khó theo dõi thống nhất.

---

## 2. Các Điểm Nghẽn & Khó Khăn Chính (Key Pain Points)

### 2.1 Thiếu đầu mối tập trung
- Yêu cầu của sinh viên nằm ở nhiều kênh khác nhau.
- Khó tra cứu lại lịch sử hỗ trợ một cách thống nhất.

### 2.2 Nguy cơ bỏ sót hoặc xử lý trùng lặp
- Yêu cầu có thể bị bỏ sót khi nằm trong email, tin nhắn hoặc bảng theo dõi riêng.
- Nhiều người có thể cùng xử lý một yêu cầu nếu không có cơ chế phân công rõ ràng.

### 2.3 Sinh viên khó theo dõi tiến độ
- Sinh viên khó biết yêu cầu đang ở trạng thái nào.
- Không phải lúc nào sinh viên cũng biết đơn vị hoặc người đang phụ trách xử lý.

### 2.4 Quy trình xử lý giữa các phòng ban chưa thống nhất
- Việc phân loại, chuyển tiếp và cập nhật kết quả có thể khác nhau giữa các đơn vị.
- Phản hồi dành cho sinh viên có nguy cơ thiếu nhất quán.

### 2.5 Ban quản lý thiếu số liệu tổng hợp
Ban quản lý cần có khả năng theo dõi:
- Số lượng yêu cầu mới, đang xử lý, sắp quá hạn hoặc đã quá hạn.
- Khối lượng công việc theo phòng ban hoặc nhân viên.
- Nhóm vấn đề phát sinh nhiều và xu hướng tăng/giảm.
- Thời gian xử lý trung bình.
- Phản hồi và mức độ hài lòng của sinh viên.

---

## 3. Tác Động Nghiệp Vụ

```text
Kênh tiếp nhận phân tán
        |
        +--> Nguy cơ bỏ sót yêu cầu
        |
        +--> Xử lý trùng lặp / phản hồi không thống nhất
        |
        +--> Sinh viên khó theo dõi tiến độ
        |
        +--> Quản lý thiếu dữ liệu để giám sát và điều phối
```

---

## 4. Hướng Giải Quyết Của UniSupport

UniSupport hướng tới giải quyết các vấn đề trên bằng cách:

1. **Tập trung hóa tiếp nhận**: Cung cấp một Web Application thống nhất để sinh viên gửi yêu cầu hỗ trợ.
2. **Quản lý bằng Ticket**: Mỗi yêu cầu được tạo thành công có mã Ticket để theo dõi.
3. **Minh bạch tiến độ**: Sinh viên xem được trạng thái hiện tại, lịch sử cập nhật và đơn vị/người phụ trách theo thông tin hệ thống cung cấp.
4. **Chuẩn hóa xử lý**: Hỗ trợ nhân viên phân loại, phân công/chuyển xử lý, cập nhật trạng thái, yêu cầu bổ sung và ghi nhận kết quả.
5. **Hỗ trợ quản lý**: Cung cấp Dashboard và báo cáo phục vụ theo dõi tình hình xử lý và điều phối nguồn lực.
