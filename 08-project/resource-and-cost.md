# Bảng Phân Bổ Nguồn Lực & Chi Phí (Resource Allocation & Cost)

## 1. Phân bổ Effort theo Phân hệ

### M1 – Student Portal
| Function | BA (h) | UI/UX (h) | TL (h) | FE1 (h) | FE2 (h) | BE1 (h) | BE2 (h) | QA (h) | Effort cơ sở (h) | Buffer (h) | Effort kế hoạch (h) | Key Risks / Issues |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| Tra cứu hướng dẫn & FAQ | 3 | 3 | 0 | 4 | 0 | 0 | 0 | 4 | 14 | 0 | 14 | |
| Tạo & gửi yêu cầu hỗ trợ | 5 | 5 | 1 | 10 | 1 | 6 | 1 | 5 | 34 | 3 | 37 | Quy tắc nghiệp vụ theo loại yêu cầu; liên kết form–Ticket; dependency giữa FE/BE |
| Xem & theo dõi yêu cầu | 4 | 3 | 1 | 8 | 3 | 5 | 3 | 5 | 32 | 1 | 33 | Đồng bộ trạng thái và lịch sử giữa Student/Staff; kiểm soát phạm vi dữ liệu |
| Nhận thông báo trạng thái | 3 | 1 | 0 | 4 | 0 | 4 | 4 | 3 | 19 | 0 | 19 | |
| Bổ sung thông tin & phản hồi | 3 | 1 | 0 | 5 | 3 | 5 | 3 | 5 | 25 | 0 | 25 | |
| **TỔNG M1 – Student** | **18** | **13** | **2** | **31** | **7** | **20** | **11** | **22** | **124** | **4** | **128** | Buffer tập trung cho form/workflow và đồng bộ trạng thái/lịch sử. |

### M2 – Staff Operations
| Function | BA (h) | UI/UX (h) | TL (h) | FE1 (h) | FE2 (h) | BE1 (h) | BE2 (h) | QA (h) | Effort cơ sở (h) | Buffer (h) | Effort kế hoạch (h) | Key Risks / Issues |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| Tiếp nhận, tìm kiếm & lọc yêu cầu | 3 | 3 | 1 | 4 | 5 | 8 | 3 | 6 | 33 | 0 | 33 | |
| Phân loại & phân công xử lý | 4 | 0 | 3 | 4 | 3 | 9 | 5 | 9 | 37 | 1 | 38 | Mapping Department/Staff và ownership Ticket; dữ liệu cấu hình ảnh hưởng phân công |
| Quản lý ưu tiên & thời hạn | 4 | 0 | 4 | 3 | 3 | 6 | 3 | 3 | 26 | 3 | 29 | Business rule về priority/deadline; ngày giờ và xử lý Ticket quá hạn |
| Xử lý & cập nhật yêu cầu | 4 | 1 | 1 | 4 | 4 | 9 | 4 | 9 | 36 | 3 | 39 | Workflow nhiều trạng thái; yêu cầu bổ sung và cập nhật phải đồng bộ xuyên Ticket lifecycle |
| Chuyển xử lý, Escalation & hoàn tất | 3 | 0 | 3 | 3 | 3 | 8 | 4 | 5 | 29 | 3 | 32 | Chuyển ownership, escalation và dependency giữa priority/deadline với workflow |
| Đóng & mở lại yêu cầu | 3 | 0 | 1 | 3 | 3 | 8 | 3 | 5 | 26 | 0 | 26 | |
| **TỔNG M2 – Staff** | **21** | **4** | **13** | **21** | **21** | **48** | **22** | **37** | **187** | **10** | **197** | Buffer tập trung cho phân công, priority/deadline, xử lý workflow và escalation. |

### M3 – Management Dashboard
| Function | BA (h) | UI/UX (h) | TL (h) | FE1 (h) | FE2 (h) | BE1 (h) | BE2 (h) | QA (h) | Effort cơ sở (h) | Buffer (h) | Effort kế hoạch (h) | Key Risks / Issues |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| Quản lý tài khoản, vai trò & RBAC | 5 | 3 | 6 | 3 | 8 | 13 | 9 | 13 | 60 | 4 | 64 | Authentication + RBAC; mapping Role/Permission; nguy cơ truy cập sai quyền |
| Quản lý phòng ban & danh mục | 4 | 1 | 3 | 0 | 4 | 5 | 5 | 4 | 26 | 0 | 26 | |
| Kiểm soát quyền truy cập & Audit Trail | 4 | 0 | 4 | 1 | 4 | 9 | 5 | 9 | 36 | 4 | 40 | Data access xuyên module và Audit Trail; yêu cầu nhất quán về quyền và logging |
| Quản lý thời hạn lưu trữ | 3 | 0 | 1 | 0 | 0 | 4 | 4 | 3 | 15 | 0 | 15 | |
| Dashboard & thống kê quản trị | 4 | 3 | 1 | 0 | 9 | 3 | 9 | 4 | 33 | 0 | 33 | |
| Báo cáo, mức độ hài lòng & xuất dữ liệu | 4 | 3 | 1 | 0 | 8 | 5 | 10 | 6 | 37 | 0 | 37 | |
| **TỔNG M3 – Quản lý** | **24** | **10** | **16** | **4** | **33** | **39** | **42** | **39** | **207** | **8** | **215** | Buffer tập trung cho RBAC và kiểm soát quyền/Audit; các chức năng quản trị còn lại giữ scope MVP. |

### Tổng Hợp Toàn Dự Án

| Hạng mục | PM (h) | BA (h) | UI/UX (h) | TL (h) | FE1 (h) | FE2 (h) | BE1 (h) | BE2 (h) | QA (h) | DevOps (h) | Effort cơ sở (h) | Buffer (h) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Tổng toàn bộ Function | 0 | 63 | 27 | 31 | 56 | 61 | 107 | 75 | 98 | 0 | 518 | 22 |
| Quản lý dự án & điều phối | 70 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 70 | 0 |
| Môi trường, CI/CD, triển khai & bàn giao | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 30 | 30 | 0 |
| **TỔNG HOẠT ĐỘNG CẤP DỰ ÁN** | **70** | **0** | **0** | **0** | **0** | **0** | **0** | **0** | **0** | **30** | **100** | **0** |
| **TỔNG TOÀN DỰ ÁN** | **70** | **63** | **27** | **31** | **56** | **61** | **107** | **75** | **98** | **30** | **618** | **22** |

**Tổng Effort kế hoạch: 640h**

## 2. Bảng Chi Phí Nhân Sự Kế Hoạch

| STT | Nhân sự | Đơn giá / giờ | Thời gian làm việc (h) | Chi phí lương Gross phân bổ | Chi phí bảo hiểm 21,5% | Chi phí nhân sự nội bộ |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | Project Manager (PM) | 409,091 ₫ | 70 | 28,636,364 ₫ | 6,156,818 ₫ | 34,793,182 ₫ |
| 2 | Business Analyst (BA) | 236,364 ₫ | 63 | 14,890,909 ₫ | 3,201,545 ₫ | 18,092,455 ₫ |
| 3 | UI/UX Designer | 218,182 ₫ | 27 | 5,890,909 ₫ | 1,266,545 ₫ | 7,157,455 ₫ |
| 4 | Technical Lead (TL) | 454,545 ₫ | 31 | 14,090,909 ₫ | 3,029,545 ₫ | 17,120,455 ₫ |
| 5 | Frontend Developer 1 | 254,545 ₫ | 56 | 14,254,545 ₫ | 3,064,727 ₫ | 17,319,273 ₫ |
| 6 | Frontend Developer 2 | 181,818 ₫ | 61 | 11,090,909 ₫ | 2,384,545 ₫ | 13,475,455 ₫ |
| 7 | Backend Developer 1 | 254,545 ₫ | 107 | 27,236,364 ₫ | 5,855,818 ₫ | 33,092,182 ₫ |
| 8 | Backend Developer 2 | 181,818 ₫ | 75 | 13,636,364 ₫ | 2,931,818 ₫ | 16,568,182 ₫ |
| 9 | QA/QC Engineer | 181,818 ₫ | 98 | 17,818,182 ₫ | 3,830,909 ₫ | 21,649,091 ₫ |
| 10 | DevOps / Deployment Engineer | 200,000 ₫ | 30 | 6,000,000 ₫ | 1,290,000 ₫ | 7,290,000 ₫ |
| | **TỔNG** | | **618** | **153,545,455 ₫** | **33,012,273 ₫** | **186,557,727 ₫** |
| | **Chi phí dự phòng rủi ro** | | | | | **6,641,214 ₫** |

## 3. Tổng Chi Phí Nhân Sự Kế Hoạch

| Hạng mục | Giá trị |
| :--- | :--- |
| Tổng công sức cơ sở của Business Function | 518(h) |
| Hoạt động cấp dự án – PM & DevOps | 100(h) |
| Tổng công sức cơ sở toàn dự án | 618(h) |
| Chi phí lương Gross phân bổ | 153,545,455 ₫ |
| Chi phí bảo hiểm 21,5% | 33,012,273 ₫ |
| Chi phí nhân sự nội bộ cơ sở | 186,557,727 ₫ |
| Dự phòng rủi ro | 22(h) |
| Chi phí dự phòng rủi ro ước tính | 6,641,214 ₫ |
| Tổng công sức kế hoạch | 640(h) |
| **Tổng chi phí nhân sự kế hoạch nếu sử dụng toàn bộ dự phòng** | **193,198,941 ₫** |
