# CI và phát hành — đặc tả, không phải workflow tự triển khai

1. PR: lint/typecheck, contract validation, unit/property, method golden tests, negative auth tests, dependency/secret scans và source-rights checks.
2. Build public site bằng allowlist; kiểm tra nội dung artifact không chứa API source, worker source, fixture PI, `.env*` hoặc internal docs ngoài chủ đích.
3. Staging: fake accounts A/B, migrations, deletion, cache isolation, payment sandbox, duplicate queue, report render, a11y và restore tests.
4. Production: protected environment, người có quyền duyệt, clean exact SHA, artifact digest và deployment receipt riêng Pages/Worker. Không `--commit-dirty=true`, không `|| true` che lỗi thiết lập.
5. Postrelease: probe allowlist không PI, synthetic flow đã cho phép, log receipt và rollback nếu fail. Không tự rollback vào version đã bị revoked vì security.

Gói này không chứa secret và không có lệnh deploy tự chạy. Test reference green không thỏa gate staging/production.
