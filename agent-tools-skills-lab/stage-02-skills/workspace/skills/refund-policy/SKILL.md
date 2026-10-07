---
name: refund-policy
description: Kiểm tra điều kiện hoàn tiền, thời hạn và phí bằng tài liệu trong data/policies/, chọn chính sách theo ngày mua. Dùng khi người dùng hỏi về yêu cầu hoàn tiền hoặc muốn biết đơn hàng có đủ điều kiện hoàn tiền hay không.
---

# Refund policy

Đánh giá yêu cầu hoàn tiền dựa trên tài liệu chính sách trong workspace; không suy đoán dữ kiện còn thiếu.

## Quy trình

1. Kiểm tra người dùng đã cung cấp đủ **ngày mua**, **ngày yêu cầu hoàn tiền** và **trạng thái kích hoạt sản phẩm** hay chưa. Nếu thiếu bất kỳ thông tin nào, hỏi lại tất cả thông tin còn thiếu và dừng; không kết luận đủ hay không đủ điều kiện.
2. Đọc `skills/refund-policy/references/answer-template.md` bằng `read_file`.
3. Đọc các tài liệu chính sách trong `data/policies/` bằng `read_file`. Với workspace hiện tại, đọc cả `data/policies/policy-before-oct.md` và `data/policies/policy-from-oct.md`. Không đọc thư mục như thể đó là file, không tự đoán đường dẫn khác và không bỏ qua tài liệu ứng viên.
4. Đọc kỹ phạm vi hiệu lực trong từng tài liệu. Chọn chính sách theo **ngày mua**, không theo ngày yêu cầu hoàn tiền:
   - Ngày mua trước `2026-10-01`: `data/policies/policy-before-oct.md`.
   - Ngày mua từ `2026-10-01` trở đi, bao gồm ngày `2026-10-01`: `data/policies/policy-from-oct.md`.
   Nếu tài liệu không xác nhận rõ ngày mua thuộc phạm vi nào, hoặc các tài liệu mâu thuẫn, nêu rõ chưa thể xác định và không kết luận.
5. Tính số ngày lịch đã qua bằng ngày yêu cầu hoàn tiền trừ ngày mua; ngày mua là mốc bắt đầu, không tính thành một ngày đã qua. So sánh với hạn ghi trong chính sách được chọn. Nếu ngày yêu cầu trước ngày mua, hỏi người dùng xác nhận lại ngày tháng.
6. Đối chiếu các điều kiện khác đúng theo chính sách, bao gồm trạng thái kích hoạt. Chỉ kết luận đủ điều kiện khi tất cả điều kiện được nêu trong tài liệu đều thỏa mãn. Không tự đặt thêm điều kiện, ngoại lệ hoặc khoản phí.
7. Trả lời theo reference. Ghi đường dẫn tương đối chính xác của tài liệu làm căn cứ. Nếu không đọc được tài liệu hoặc không có tài liệu áp dụng, báo rõ trở ngại thay vì đưa ra kết luận không có căn cứ.

Chỉ dùng `read_file` và các công cụ sẵn có. Không yêu cầu Bash, lệnh terminal hoặc script.
