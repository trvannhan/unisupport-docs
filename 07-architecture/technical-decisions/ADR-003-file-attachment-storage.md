# ADR-003 - Bảo Vệ File Đính Kèm

## Bối Cảnh

Proposal yêu cầu file chỉ người liên quan mới xem được. File có thể chứa tài liệu của sinh viên nên không được bỏ qua kiểm tra quyền.

## Quyết Định Baseline

- Mỗi file phải liên kết với Ticket và ngữ cảnh nghiệp vụ tương ứng.
- Trước khi cho phép xem/tải file, Backend phải xác định người dùng có quyền đối với Ticket/file.
- Cách lưu file vật lý có thể là local storage hoặc phương án phù hợp hạ tầng Client; lựa chọn này không thay đổi quy tắc quyền.
- Không yêu cầu tích hợp dịch vụ lưu trữ bên thứ ba trong baseline.

## Hệ Quả

Có thể thay đổi cơ chế lưu trữ khi triển khai mà không phải sửa PRD, miễn quyền truy cập và giới hạn file vẫn đúng.
