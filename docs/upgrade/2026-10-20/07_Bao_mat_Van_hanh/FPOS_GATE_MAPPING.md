# Life Code OS Ánh xạ cổng phát hành FPOS

Ngày 20/10/2026. Giữ G01–G12 để truy vết; RG0–RG13 là gate workspace có authority. Mỗi dòng cần receipt riêng, mapping không đóng gate.

| FPOS | Gate cũ | Chủ trì dự kiến | Evidence bắt buộc |
|---|---|---|---|
| RG0 Source and baseline | G01 | Tech Lead | Path/remote/branch/full SHA/clean-tree; artifact digest; exact environment |
| RG1 Governance product and business | G04, G06, G12 | Founder + Product + Legal | Charter; requirement acceptance; Q decisions; rights; scope/budget/service entity |
| RG2 Architecture design and brand | G01, G06, G08 | Architect + UX + Founder | Approved ADRs; data flow; accessibility; brand and public claim review |
| RG3 AI system | G06, G08 | AI Lead + Method Lead + Security | Model/prompt/source versions; evals; ACL retrieval; costs; kill switch; human escalation |
| RG4 Infrastructure and environments | G01, G10 | Platform + SRE | Resource/account/region/bindings; isolation; secrets controls; backup; cost caps |
| RG5 Development and DevOps | G01, G11 | Tech Lead + QA | Protected branch; required checks; pinned build; artifact allowlist; no dirty deploy |
| RG6 Documentation | G04, G06, G12 | Product + Docs Owner | Authority/supersession; runbooks; API/schema; user/support docs; read coverage |
| RG7 Implementation data integration | G02, G03, G05, G06, G07, G09 | Backend + Data + QA | Object/tenant grants; method golden cases; migrations/reconciliation; payment and deletion |
| RG8 Verification and security | G02, G03, G08, G11 | Independent QA + Security | Unit/property/contract/browser/e2e; negative auth; pentest/retest; counts and skips |
| RG9 Staging and rehearsal | G01, G07, G09, G10 | Release Lead + SRE | Staging RC; auth/payment sandbox; load; restore/rollback; immutable rehearsal receipt |
| RG10 Production authorization | G01, G04, G12 | Founder + Release Authority | Exact RC and scope; functional approvals; authorized operator/change window |
| RG11 Post deploy verification | G01, G02, G03, G10 | SRE + QA | Provider deployment IDs map digest; domain routes; allowlisted smoke and failure paths |
| RG12 Cleanup and handoff | G05, G07, G12 | SRE + Support + Privacy | Temporary access removed; legacy disposition; support/escalation; cost/monitor/DR ownership |
| RG13 Founder domain sign off | G01, G04, G12 | Founder | Domain + exact release/capabilities + environment receipt + explicit decision |

Release hiện HOLD. Tất cả gate production trong bảng là NOT_CHECKED. Applicability hoặc waiver phải nêu scope, lý do, rủi ro, người duyệt và thời hạn; không kế thừa một approved gate sang capability mới.
