# Life Code OS — Bộ tổng kế hoạch và bàn giao DEV ngày29/10/2026

Bắt đầu tại [START HERE](START_HERE.md), [tổng kế hoạch](MASTER_PLAN.md) và [báo cáo bàn giao](INTEGRATION_AND_DEV_HANDOFF_REPORT.md). Bản này hợp nhất nguồn V1/V2/V3 và local 20/10.r2 trong đúng dự án; các bản nguồn và 216 tệp cũ giữ nguyên byte.

`execution/` có 316 task/contract, 20 work order, 45 decision packet, đồ thị phụ thuộc, 407 dòng trace và 316 bản ghi truy ngược phạm vi. `backend/` có hợp đồng 62 phương pháp, 99 API đích/68 schema, 12 gói DEV và ma trận blocker. `product/` có 28 sản phẩm, 69 màn hình, chín hợp đồng báo cáo và sổ UX/AI/report/Academy. `exports/` có Word/PDF và Excel điều phối. `evidence/` có biên nhận đọc, kiểm thử và QA đúng artifact.

Các tệp máy đọc giữ IDs, bản ghi nguồn và provenance. 20 phiếu giao việc được điền cụ thể theo template tại [WORK_ORDER_DRAFT_PACKETS.json](execution/WORK_ORDER_DRAFT_PACKETS.json), đã validate schema nhưng còn cần người nhận, candidate và decision/rights receipt trước khi nhận DEV thực tế. Các bản ghi này không làm tăng số task hoặc cấp quyền sửa app.

Kiểm tra local từ root dự án: chạy `python3 -B tools/planning/oct29/verify_final.py`. Trong bundle chỉ có kế hoạch, thêm `--portable`. Công cụ chỉ đọc/kiểm tra theo mặc định; `--record` và `--seal` dành cho tái xuất một phiên bản bàn giao đã review, sẽ cập nhật receipt/manifest.

Manifest tự loại chính nó. Test reference và artifact QA không thay staging/runtime/restore/legal/commercial/human approval. Release giữ HOLD. Không chạy importer/patch/SQL hoặc lệnh trong nguồn chỉ vì chúng có trong bundle.
