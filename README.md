# Tài Liệu Dự Án UniSupport

Kho tài liệu này mô tả phạm vi, nghiệp vụ, yêu cầu chức năng, workflow, yêu cầu phi chức năng, nghiệm thu, kiến trúc và các ràng buộc dự án của **UniSupport – Student Support Management System** tại Aurora University.

Tài liệu được tổ chức theo hướng: **Proposal/Resource → Product → Domain → PRD → Workflow → NFR → Acceptance/RTM → Architecture → Project**.

## Cấu Trúc Tài Liệu

```text
unisupport-docs/
├── README.md
├── 01-product/
│   ├── README.md
│   ├── product-overview.md
│   ├── actors-and-roles.md
│   └── product-scope.md
├── 02-domain/
│   ├── README.md
│   ├── domain-overview.md
│   ├── terminology.md
│   ├── ticket-model.md
│   ├── ticket-lifecycle.md
│   ├── state-transition.md
│   └── business-rules.md
├── 03-modules/
│   ├── README.md
│   ├── M01-student-portal/
│   ├── M02-staff-operations/
│   └── M03-management-dashboard/
├── 04-workflows/
│   ├── README.md
│   ├── WF-01-submit-support-request.md
│   ├── WF-02-claim-and-triage.md
│   ├── WF-03-request-supplement.md
│   ├── WF-04-transfer-department.md
│   ├── WF-05-complete-and-resolve.md
│   ├── WF-06-close-and-rate.md
│   └── WF-07-escalation.md
├── 05-non-functional-requirements/
│   ├── README.md
│   ├── performance.md
│   ├── reliability.md
│   ├── security.md
│   ├── usability.md
│   ├── deployment.md
│   └── observability.md
├── 06-acceptance/
│   ├── README.md
│   ├── traceability-matrix.md
│   └── test-scenarios.md
├── 07-architecture/
│   ├── README.md
│   ├── system-context.md
│   ├── architecture-overview.md
│   ├── data-model.md
│   ├── api-design.md
│   ├── security-design.md
│   └── technical-decisions/
└── 08-project/
    ├── assumptions.md
    ├── constraints.md
    ├── milestones-and-timeline.md
    ├── open-questions.md
    └── glossary.md
```

## Phạm Vi Nghiệp Vụ Chính

UniSupport có đúng **03 phân hệ nghiệp vụ**:

| Mã | Phân hệ | Người dùng chính |
| :--- | :--- | :--- |
| **M01** | Student Portal | Sinh viên |
| **M02** | Staff Operations | Nhân viên |
| **M03** | Management Dashboard | Quản lý |

Thông báo, xác thực, phân quyền, bảo mật file và Audit là **năng lực dùng chung**, không phải phân hệ M04/M05 độc lập.

## Nguồn Baseline

Các tài liệu trong repository phải bám theo hai baseline của nhóm:

- Project Proposal đã chốt với Aurora University.
- Bảng Resource/chi phí nội bộ đã chốt của nhóm.

Khi PRD phân rã một Work Package thành nhiều FR hoặc Flow, tổng effort của Work Package vẫn giữ nguyên theo Resource. Quan hệ này được theo dõi tại [Requirements Traceability Matrix](./06-acceptance/traceability-matrix.md).

## Quy Tắc Tài Liệu

- Product/Domain/PRD mô tả **hành vi nghiệp vụ**, không gắn cứng vào API, database hoặc framework.
- Workflow sử dụng Mermaid để mô tả luồng xuyên chức năng/phân hệ.
- NFR chỉ cam kết các yêu cầu chất lượng phù hợp Proposal và phạm vi dự án.
- Architecture có thể lựa chọn giải pháp kỹ thuật nhưng không được thay đổi Business Rules hoặc mở rộng scope.
- Project documents giữ nguyên các ràng buộc đã chốt về thời gian, chi phí và effort.
