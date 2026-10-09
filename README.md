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

Thông báo, xác thực, phân quyền, bảo mật file và Audit được triển khai như **các năng lực dùng chung** xuyên suốt ba phân hệ nghiệp vụ.

## Project Baseline

| Baseline | Vai trò |
| :--- | :--- |
| **UniSupport Project Proposal** | Xác định mục tiêu, phạm vi bàn giao, giả định, ràng buộc và tiêu chí nghiệm thu cấp dự án. |
| **Internal Resource & Cost Plan** | Xác định Work Package, effort kế hoạch và cơ sở lập tiến độ nguồn lực. |

Việc phân rã Work Package thành nhiều Functional Requirement hoặc workflow không làm thay đổi effort kế hoạch của Work Package. Quan hệ truy xuất được quản lý tại [Requirements Traceability Matrix](./06-acceptance/traceability-matrix.md).

## Documentation Conventions

- **Product, Domain và PRD** là nguồn mô tả hành vi nghiệp vụ và không phụ thuộc vào công nghệ triển khai.
- **Workflows** thể hiện luồng phối hợp giữa các chức năng và phân hệ bằng Mermaid.
- **Non-Functional Requirements** xác định các thuộc tính chất lượng áp dụng toàn hệ thống.
- **Architecture** mô tả giải pháp kỹ thuật phục vụ các yêu cầu đã xác định và không thay đổi Business Rules.
- **Acceptance & RTM** duy trì truy xuất từ Work Package đến yêu cầu, workflow và kịch bản UAT.
- **Project documents** quản lý các giả định, ràng buộc, tiến độ và quyết định cấp dự án.
