# NFR-PERF - Hiệu Năng

## 1. Mục Tiêu

UniSupport phải đáp ứng ổn định các chức năng chính trong phạm vi quy mô khoảng **3.000 sinh viên** như Proposal, không đặt mục tiêu cho kiến trúc tải lớn hoặc lưu lượng vượt xa phạm vi này.

## 2. Yêu Cầu

- Các thao tác chính như đăng nhập, tạo/xem Ticket, cập nhật xử lý, xem Dashboard và báo cáo phải phản hồi ở mức sử dụng thực tế chấp nhận được trên hạ tầng do Aurora University cung cấp.
- Danh sách Ticket và báo cáo phải hỗ trợ lọc/tìm kiếm mà không làm thay đổi hoặc mất dữ liệu nghiệp vụ.
- File đính kèm tối đa **10 MB/file** theo Business Rules.
- Không đặt cam kết cố định về số người dùng đồng thời hoặc thời gian phản hồi API khi Proposal/Resource chưa chốt các chỉ số này.

## 3. Nghiệm Thu

- Các luồng chính của M01, M02, M03 hoạt động ổn định với bộ dữ liệu UAT đại diện cho phạm vi dự án.
- Không xuất hiện tình trạng treo chức năng hoặc lỗi làm gián đoạn luồng chính trong điều kiện UAT bình thường.
- Nếu hiệu năng phụ thuộc vào hạ tầng Client, kết quả phải được đánh giá cùng điều kiện môi trường thực tế.
