# ADR-001 - Mã Ticket Duy Nhất

## Bối Cảnh

Proposal yêu cầu sinh viên nhận mã Ticket để theo dõi. Domain yêu cầu mã Ticket duy nhất trong hệ thống.

## Quyết Định Baseline

- Mỗi Ticket phải có **một mã Ticket duy nhất**, hiển thị được cho Sinh viên/Staff/Management khi có quyền.
- Mã phải ổn định trong suốt vòng đời Ticket và không thay đổi khi Transfer, reopen hoặc đóng Ticket.
- Định dạng hiển thị và loại khóa chính trong database là quyết định triển khai kỹ thuật, không phải requirement nghiệp vụ.

## Hệ Quả

Đội phát triển phải bảo đảm tính duy nhất nhưng không bị khóa vào một format mã cụ thể trước khi thiết kế kỹ thuật được chốt.
