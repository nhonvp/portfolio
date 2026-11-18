# Deploy portfolio

Thư mục này gồm:

| File | Vai trò |
|---|---|
| `index.html` | Trang hoàn chỉnh, 1 file, đây là thứ đưa lên mạng |
| `source/portfolio.html` | Bản gốc để chỉnh sửa (link, giá, chữ) |
| `build.py` | Tạo lại `index.html` từ bản gốc: `python3 build.py` |
| `profile-vlance.md` | Chữ để dán vào hồ sơ vLance |

## Chỉnh nội dung rồi build lại
1. Mở `source/portfolio.html`, tìm khối `LINKS` và `PRICING` ở đầu thẻ `<script>` đầu tiên.
2. Điền link vLance, link app, giá. Ô để trống sẽ tự ẩn.
3. Chạy `python3 build.py` để cập nhật `index.html`.

## Đưa lên mạng (chọn một)
Trang chỉ cần `index.html`, không cần máy chủ hay bước build nào.

- **Netlify (nhanh nhất):** vào app.netlify.com/drop, kéo cả thư mục `Personal_CV` hoặc riêng `index.html` vào.
- **Vercel:** `npx vercel` trong thư mục này, hoặc kéo thả trên vercel.com/new.
- **GitHub Pages:** tạo repo, đẩy `index.html` lên nhánh `main`, bật Pages trong Settings.

Sau khi lên mạng, mở thử trên điện thoại thật, cả tiếng Việt lẫn tiếng Anh (nút VI/EN).

## Trang cần internet để tải
- Thư viện Three.js và GSAP từ cdnjs.cloudflare.com
- Font từ Google Fonts

Nếu các thư viện 3D không tải được, trang tự chuyển sang dạng danh sách dự án, vẫn đọc và bấm link bình thường.

## Cần biết
- Trang công khai số Zalo (0349177010) và email nhonpham13@gmail.com. Đổi hoặc bỏ trong khối `LINKS.contact` nếu không muốn.
- Các màn hình trên điện thoại 3D là minh họa tính năng, không phải ảnh chụp sản phẩm. Cuối trang có ghi chú rõ điều này.
