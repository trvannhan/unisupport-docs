# ADR-002 - Thực Thi Phân Quyền

## Bối Cảnh

UniSupport có ba nhóm người dùng chính: Sinh viên, Nhân viên và Quản lý. Resource dành effort riêng cho tài khoản/RBAC và kiểm soát quyền/Audit.

## Quyết Định Baseline

- Hệ thống phải kiểm tra cả **quyền chức năng** và **phạm vi dữ liệu**.
- Sinh viên bị giới hạn theo Ticket của chính mình.
- Nhân viên bị giới hạn theo phòng ban/quyền và trách nhiệm xử lý.
- Quản lý bị giới hạn theo phạm vi toàn trường hoặc phòng ban cùng quyền được cấp.
- Việc thực thi bằng session/token, middleware hoặc cơ chế tương đương do đội kỹ thuật lựa chọn.

## Hệ Quả

Kiến trúc không được hardcode theo cách làm mất khả năng gán quyền/phạm vi đã được M03 định nghĩa.
