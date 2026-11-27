# PRODUCTION BIBLE & STORYBOARD 79 KHUNG HÌNH — TẬP 01: ÔNG ÁP-RA-HAM

- **Kịch bản nguồn:** [01_ong_apraham_script.md](01_ong_apraham_script.md) (`6.111` từ · ước tính `~30–31` phút audio · `79` khung hình ≈ `~23–24` giây/khung hình)
- **Định hướng:** Phim tài liệu lịch sử Kinh Thánh điện ảnh live-action (`Cinematic photorealistic live-action biblical historical epic, 16:9 landscape`), giữ nhất quán nhận diện nhân vật xuyên suốt theo từng mốc tuổi, trang phục, đạo cụ và bối cảnh.
- **Cấu trúc thư mục ảnh:**
  - `images/refs_characters/` — Ảnh chuẩn nhân vật gốc & các phiên bản độ tuổi (dùng làm Image Reference khi tạo cảnh)
  - `images/refs_locations/` — 4 ảnh chuẩn bối cảnh lớn tái sử dụng (`Mamre`, `Ai Cập`, `Beersheba`, `Moriah`)
  - `images/scenes/` — 79 ảnh cảnh phim đặt tên chính xác `AB01-01.jpg` đến `AB18-03.jpg` (dùng trực tiếp cho `build_video.py`)
- **Lệnh dựng video MP4 1080p tự động** *(tự ưu tiên đọc `images/scenes/` nếu có)*:
  ```bash
  python ..\build_video.py 01_ong_apraham
  # Hoặc kèm nhạc nền không lời (-25 dB):
  python ..\build_video.py 01_ong_apraham --bgm path\to\ambient.mp3 --bgm-db -25
  ```

---

## 0. QUY TẮC TẠO ẢNH CỐ ĐỊNH (MASTER STYLE LOCK)

Gắn khối style prefix sau vào đầu mọi prompt để giữ đồng bộ 100% giữa tất cả 79 khung hình:

> **Master Style Prefix:**
> `Cinematic photorealistic live-action biblical historical epic film still, 16:9 widescreen, shot on 35mm anamorphic lens, natural motivated sunlight, authentic Bronze Age Ancient Near East costumes and architecture, realistic skin texture and weathered fabrics, rich cinematic color grading, dramatic storytelling composition, not 3D animation, not CGI cartoon, no text, no subtitles, no watermark.`

### Quy tắc bắt buộc xuyên suốt
1. **Nhân vật:** Dùng ảnh gốc trong `images/refs_characters/` làm reference. Không tạo lại khuôn mặt mới ở mỗi câu chuyện.
2. **Tuổi tác:** Luôn ghi rõ mã mốc tuổi (A1–A5 cho Abraham, S1–S4 cho Sarah, v.v.) trước khi tạo cảnh.
3. **Trang phục:** Mỗi nhân vật có bảng màu riêng cố định; chỉ thay đổi khi có lý do hợp lý (rời Ur sang Canaan, vào cung Ai Cập, tuổi già, hành quân).
4. **Bối cảnh:** Dùng 4 ảnh gốc trong `images/refs_locations/` làm reference cho các bối cảnh lặp lại.
5. **Tính lịch sử:** Chỉ dùng vật liệu, kiến trúc, vũ khí, trang phục thời Đồ Đồng Cận Đông cổ đại.
6. **Kể chuyện bằng hành động:** Mọi khung hình phải thể hiện hành động/cảm xúc rõ ràng, tránh dáng chân dung đứng nhìn thẳng camera.
7. **Thiên Chúa:** **Tuyệt đối không** tạo hình Thiên Chúa thành nhân vật có khuôn mặt/thân thể người cố định. Thể hiện qua ánh sáng từ ngoài khung hình, bầu trời, thiên nhiên, lò lửa tỏa khói và ngọn đuốc (St 15), hoặc phản ứng của Áp-ra-ham.
8. **Không chữ:** Không tiêu đề, không phụ đề, không watermark trên ảnh.

### 4 Điểm Kiểm Soát Bám Sát Kịch Bản (Script Fidelity)
- **Tuổi I-xa-ác (Isaac) tại núi Mô-ri-gia:** Kinh Thánh không ghi tuổi cụ thể; kịch bản mô tả chàng trai trẻ → thống nhất 1 ngoại hình thiếu niên/thanh niên (~16–19 tuổi), không khẳng định tuổi chính xác.
- **Quản gia đi tìm vợ cho I-xa-ác (St 24):** Kịch bản không xác nhận người quản gia ở St 24 chắc chắn là Ê-li-e-de (St 15) → tạo hình vị quản gia già trung tín nhất quán, không gán nhãn khẳng định hai người là một.
- **Ba vị khách tại Mam-rê & Hai vị đến Xơ-đôm:** Phải giữ cùng khuôn mặt và trang phục xuyên suốt chuỗi AB11–AB12.
- **Hai lần Ha-ga (Hagar) vào sa mạc:** Tách biệt hoàn toàn **St 16 (AB09)** — Ha-ga đang **mang thai** bỏ trốn một mình — với **St 21 (AB15)** — Ha-ga rời trại cùng **Ít-ma-ên thiếu niên (~15–16 tuổi)**, tuyệt đối không vẽ Ít-ma-ên là trẻ sơ sinh ở AB15.

---

## GIAI ĐOẠN 1 — CHỐT BỘ NHÂN VẬT CHUẨN (`images/refs_characters/`)

### A. 6 Nhân vật cốt lõi (tạo ảnh gốc trước khi tạo cảnh)

#### 1. Abraham / Áp-ra-ham (5 giai đoạn tuổi `A1` → `A5`)
- **Nhận diện cố định:** Đàn ông Trung Đông cổ đại, sống mũi cao thẳng, đôi mắt sâu trầm tĩnh, gò má rám nắng, râu dài dày tự nhiên.
- **Bảng màu trang phục:** Giai đoạn Ur (AB01): áo choàng dệt Lưỡng Hà màu nâu đất & xanh chàm đậm. Từ Haran/Canaan trở đi (AB02–AB18): áo dài lữ hành vải len thô màu be cát, áo khoác ngoài màu nâu sẫm / nâu ô-liu, khăn quấn đầu đơn giản.

| Mã | Độ tuổi | Ngoại hình | Dùng cho câu chuyện |
| :--- | :--- | :--- | :--- |
| `A1` | ~75 tuổi | Tóc và râu nâu sẫm điểm bạc, vóc dáng còn khỏe, bước đi vững | AB01, AB02, AB03, AB04, AB05, AB06 |
| `A2` | 85–86 tuổi | Tóc râu muối tiêu nhiều hơn, nếp nhăn sâu hơn, vẫn rắn rỏi | AB07, AB08, AB09 |
| `A3` | 99–100 tuổi | Râu bạc trắng rõ rệt, khuôn mặt hằn dấu thời gian, ánh mắt sâu sắc | AB10, AB11, AB12, AB13, AB14, AB15 |
| `A4` | Trên 100 tuổi | Giữ nguyên mặt A3, thêm nét khắc khổ và tóc râu bạc hơn | AB16, AB17 |
| `A5` | Đến 175 tuổi | Tóc và râu bạc trắng hoàn toàn, da nhăn sâu, dáng người già yếu bình an | AB18 |

- **Prompt mẫu tạo gốc `char_abraham_A1_75.jpg`:**
  `Cinematic photorealistic live-action biblical historical epic character sheet, 16:9 widescreen, 35mm film. Middle Eastern Bronze Age patriarch Abraham at age 75, weathered sun-tanned olive skin, strong aquiline nose, deep calm expressive dark eyes, full dark-brown beard streaked with silver-grey, hair streaked with silver. Wearing authentic textured coarse wool nomad robes in warm sand-beige and dark earthy umber brown cloak, simple woven headcloth. Neutral dusty Canaanite outdoor light, medium shot and profile reference, realistic skin pores, not 3D, no text, no watermark.`

#### 2. Sarah / Xa-ra (4 giai đoạn tuổi `S1` → `S4`)
- **Nhận diện cố định:** Phụ nữ Trung Đông cổ đại thanh tú, làn da ô-liu ấm, đôi mắt nâu sâu thông minh, dáng mặt trái xoan.
- **Bảng màu trang phục:** Vải lanh màu kem ấm, khăn choàng màu đất nung (terracotta) hoặc đỏ rượu trầm; tại Ur có họa tiết dệt Lưỡng Hà nhẹ; khi vào cung Ai Cập/Gerar khoác thêm choàng lụa/lanh sang hơn nhưng giữ nguyên khuôn mặt.
- **Mốc tuổi:** `S1` (65 tuổi: AB01–AB04) · `S2` (75 tuổi: AB09) · `S3` (89–90 tuổi: AB10–AB15) · `S4` (127 tuổi: AB17).
- **Prompt mẫu tạo gốc `char_sarah_S1_65.jpg`:**
  `Cinematic photorealistic live-action biblical historical epic character sheet, 16:9 widescreen, 35mm film. Middle Eastern Bronze Age woman Sarah at age 65, dignified mature beauty, warm olive skin with subtle natural lines, expressive dark brown eyes, dark hair subtly streaked with silver partially covered by a woven terracotta-red head scarf, wearing authentic coarse cream linen tunic and muted rust-red shawl. Natural warm daylight, realistic skin texture, not 3D, no text, no watermark.`

#### 3. Lot / Lót (`L1` trẻ ~30s → `L2` trung niên ~40s–50s)
- **Nhận diện cố định:** Cháu trai Áp-ra-ham, nét mặt trẻ hơn, râu ngắn gọn, ánh mắt lanh lợi nhưng dễ dao động.
- **Bảng màu trang phục:** Áo dài màu xanh xám đá (slate blue-grey) và thắt lưng da nâu.
- **Prompt mẫu tạo gốc `char_lot_L1.jpg`:**
  `Cinematic photorealistic live-action biblical historical epic character sheet, 16:9 widescreen, 35mm film. Bronze Age Middle Eastern man Lot in his early 30s, nephew of Abraham, tanned olive skin, short neatly kept dark beard, alert dark eyes, wearing dusty slate-blue woven wool tunic and brown leather belt, simple travel cloak. Natural warm daylight, realistic skin texture, not 3D, no text, no watermark.`

#### 4. Hagar / Ha-ga (`H1` mang thai St 16 · `H2` khắc khổ St 21)
- **Nhận diện cố định:** Phụ nữ Ai Cập cổ đại, da đồng sẫm, tóc đen bện gọn, đôi mắt kiên cường pha nét buồn.
- **Bảng màu trang phục:** Áo lanh Ai Cập đơn giản màu vàng đất nhạt / nâu tro, hơi sờn cũ phù hợp thân phận nữ tỳ.
- **Prompt mẫu tạo gốc `char_hagar_H1.jpg`:**
  `Cinematic photorealistic live-action biblical historical epic character sheet, 16:9 widescreen, 35mm film. Ancient Egyptian maidservant Hagar in her late 20s, warm bronze-brown Egyptian skin, dark braided hair under a simple worn linen headwrap, resilient dark eyes, wearing humble weathered ochre-linen dress and simple faded wrap. Natural sunlight, realistic skin texture, not 3D, no text, no watermark.`

#### 5. Ishmael / Ít-ma-ên (`IM1` sơ sinh → `IM2` 13 tuổi → `IM3` thiếu niên ~15–16 tuổi → `IM4` trưởng thành)
- **Nhận diện cố định:** Mang nét lai giữa Áp-ra-ham và Ha-ga, da nâu rám nắng hoang mạc, vóc dáng cao nhanh nhẹn, ánh mắt sắc.
- **Bảng màu trang phục:** Nâu đất hoang mạc, áo không tay hoặc áo ngắn lữ hành, sau này mang cung tên.

#### 6. Isaac / I-xa-ác (`IS1` sơ sinh → `IS2` trẻ nhỏ dứt sữa ~3 tuổi → `IS3` thanh niên tại Moriah ~16–19 tuổi → `IS4` trưởng thành ~40–75 tuổi)
- **Nhận diện cố định:** Mang nét điềm đạm của Áp-ra-ham và đôi mắt hiền của Xa-ra, dáng thư sinh nhưng khỏe khoắn.
- **Bảng màu trang phục:** Kem sáng, nâu nhạt, xanh ô-liu dịu.

### B. 12 Nhân vật phụ & Quần chúng
| Nhân vật phụ | Xuất hiện | Ghi chú tạo hình |
| :--- | :--- | :--- |
| **Terah (Te-rác)** — cha Abraham | AB01 | Cụ già Lưỡng Hà râu bạc dài, áo choàng len dày màu nâu đỏ sẫm |
| **Pharaoh Ai Cập** | AB03 | Vương triều Trung Cổ Ai Cập (Middle Kingdom), vải lanh trắng mịn, vòng cổ vàng xanh ngọc |
| **Vua Sodom (Xơ-đôm)** | AB06 | Trang phục thành bang Canaan lộng lẫy nhưng kiêu ngạo, đối lập với Men-ki-xê-đê |
| **Melchizedek (Men-ki-xê-đê)** | AB06 | Vua kiêm tư tế uy nghi, khiêm tốn, áo lễ vải lanh trắng ngà & đai dệt vàng nhạt |
| **Ba đồng minh (Aner, Eshcol, Mamre)** | AB05 | Thủ lĩnh bộ tộc Amorite/Canaan vũ trang giáo đồng, áo choàng da thú |
| **Quản gia già (Eliezer / Quản gia St 24)** | AB07, AB17 | Ông lão trung tín, tóc bạc, áo màu nâu xám — không mặc định hai người là một |
| **Ba vị khách tại Mamre** | AB11, AB12 | 3 người đàn ông trang phục lữ khách vải lanh sáng giản dị, thần thái thanh cao — giữ y hệt sang AB12 |
| **Thiên sứ** | AB09, AB15, AB16 | Hình dáng trang nghiêm trong ánh sáng dịu tự nhiên (không cánh sặc sỡ giả tạo) |
| **Abimelech (A-bi-me-léc)** | AB13 | Vua thành bang Gerar (Canaan/Philistine), khác hoàn toàn Pharaoh Ai Cập |
| **Ephron (Ép-rôn)** | AB17 | Quý tộc người Khết (Hittite) tại Hếp-rôn, trang phục dệt sọc cổ |
| **Rebecca (Rê-bê-ca)** | AB17 | Thiếu nữ Mê-xô-pô-ta-mi trẻ trung, đoan trang, bình nước gốm trên vai |
| **Keturah (Cơ-tu-ra)** | AB18 | Người phụ nữ trung niên điềm đạm bên Áp-ra-ham những năm cuối đời |
| **Quần chúng** | Xuyên suốt | Người hầu, mục tử, 318 gia nhân vũ trang, thương nhân Ur, quan Ai Cập, trưởng lão Hittite |

---

## GIAI ĐOẠN 2 — 4 BỐI CẢNH CHUẨN TÁI SỬ DỤNG (`images/refs_locations/`)

1. **`loc_mamre_hebron.jpg` (Trại Mam-rê – Hếp-rôn)** — Dùng cho AB04, AB05, AB07, AB08, AB09, AB10, AB11, AB14, AB17, AB18:
   `Cinematic photorealistic live-action biblical historical epic establishing shot, 16:9 widescreen. Ancient Bronze Age nomad encampment of Abraham at Mamre near Hebron in Canaan: dark woven goat-hair tents pitched beneath massive ancient gnarled oak trees on low rocky limestone hills, dry golden grass, rough unhewn stone altar nearby, grazing sheep in distance, warm Mediterranean sunlight, not 3D, no text, no watermark.`
2. **`loc_egypt_nile.jpg` (Ai Cập – Trung Cổ Vương Triều)** — Dùng cho AB03 *(tuyệt đối không dùng lại cho Gerar AB13)*:
   `Cinematic photorealistic live-action biblical historical epic establishing shot, 16:9 widescreen. Ancient Middle Kingdom Egypt along the Nile river: monumental sandstone palace columns with subtle carved reliefs, date palms, mudbrick city walls, fertile green riverbanks contrasting with golden desert beyond, warm amber afternoon sunlight, not 3D, no text, no watermark.`
3. **`loc_beersheba_desert.jpg` (Hoang mạc Bơ-e Se-va)** — Dùng cho AB15:
   `Cinematic photorealistic live-action biblical historical epic establishing shot, 16:9 widescreen. Arid stony Negev wilderness near Beersheba: cracked pale ochre desert earth, scattered limestone rocks, sparse thorny acacia shrubs, harsh blazing midday sunlight, vast empty horizon with shimmering heat haze, not 3D, no text, no watermark.`
4. **`loc_mount_moriah.jpg` (Núi Mô-ri-gia)** — Dùng xuyên suốt chuỗi AB16 (10 ảnh đồng nhất địa hình đá vôi khô cằn, không rừng xanh):
   `Cinematic photorealistic live-action biblical historical epic establishing shot, 16:9 widescreen. Rugged rocky limestone ridge of Mount Moriah in ancient Judea: steep dusty gravel trail winding up pale grey-ochre stone slopes, sparse dry scrub and thorny bushes, vast quiet mountain horizon under cool early morning light, authentic Bronze Age wilderness, not 3D, no text, no watermark.`

---

## GIAI ĐOẠN 3 — DANH SÁCH 18 CÂU CHUYỆN & 79 KHUNG HÌNH (`images/scenes/`)

### Câu chuyện 01 — Cuộc sống tại Ur và hành trình tới Haran *(St 11 · `AB01-01` → `AB01-04`)*
- **Nhân vật:** Terah, Abram (`A1` tiền 75), Sarai (`S1`), Lot (`L1`) · **Trang phục:** Ảnh hưởng Lưỡng Hà (chưa mặc đồ lữ hành Canaan).
- **Prompt chi tiết sẵn dùng (ưu tiên sản xuất trước & kiểm tra đồng bộ):**
  - **`AB01-01.jpg`** *(Toàn cảnh thành Ur phồn thịnh bên sông Euphrates)*:
    `Cinematic photorealistic live-action biblical historical epic wide establishing shot, 16:9 widescreen, 35mm film. Thriving ancient Bronze Age Mesopotamian city of Ur of the Chaldeans beside the Euphrates river at golden morning light: towering stepped mudbrick ziggurat temple in the background, bustling clay-brick houses, narrow merchant alleys, loaded donkey caravans and traders along the canal, warm dusty atmospheric haze, not 3D, no text, no watermark.`
  - **`AB01-02.jpg`** *(Gia đình Terah trong sân nhà tại Ur trước khi di cư)*:
    `Cinematic photorealistic live-action biblical historical epic medium-wide shot, 16:9 widescreen, 35mm film. Inside a sunlit mudbrick courtyard home in ancient Ur of the Chaldeans: elderly bearded father Terah seated beside pottery and woven carpets; Abraham (A1, age ~70, dark beard streaked with silver, Mesopotamian earth-brown and indigo woven robe) standing beside his dignified wife Sarah (S1, warm cream and terracotta wrap) and young nephew Lot (L1, slate-blue tunic), quiet family conversation before departure, natural warm courtyard light, not 3D, no text, no watermark.`
  - **`AB01-03.jpg`** *(Terah dẫn gia đình rời cổng thành Ur)*:
    `Cinematic photorealistic live-action biblical historical epic cinematic tracking wide shot, 16:9 widescreen, 35mm film. Elderly Terah leading his family caravan—Abraham (A1), Sarah (S1), young Lot (L1), servants, loaded donkeys, and flocks of sheep—walking out through the massive mudbrick city gates of ancient Ur onto an open dusty road, the great ziggurat and bustling city receding behind them in warm afternoon dust, not 3D, no text, no watermark.`
  - **`AB01-04.jpg`** *(Đoàn định cư tại Haran, Terah già yếu)*:
    `Cinematic photorealistic live-action biblical historical epic medium-wide shot, 16:9 widescreen, 35mm film. Nomad camp settled on the semi-arid plains of ancient Haran at late afternoon: dark woven goat-hair tents pitched near low mudbrick outposts; Abraham (A1) and Sarah (S1) standing quietly together outside a tent watching over the aged frail father Terah resting on woven rugs in the shaded entrance, quiet contemplative mood, warm golden sunset light, not 3D, no text, no watermark.`

---

### Bảng tổng hợp 75 khung hình còn lại (`AB02-01` → `AB18-03`)

| Câu chuyện | Kinh Thánh | Mã ảnh | Nội dung khung hình | Nhân vật / Lưu ý đồng bộ |
| :--- | :--- | :--- | :--- | :--- |
| **02. Tiếng gọi rời quê hương** | St 12:1–9 | `AB02-01` | Abram đứng một mình ngoài lều lúc bình minh lắng nghe tiếng Chúa gọi, khuôn mặt suy tư | `A1` (75t) — từ đây cố định bộ đồ lữ hành Canaan |
| | | `AB02-02` | Abram dẫn Sarai, Lot, gia nhân và gia súc rời Haran tiến về vùng đất xa lạ | `A1`, `S1`, `L1`, đoàn người |
| | | `AB02-03` | Đoàn đến Shechem, bên cây sồi Moreh; phía xa có khu định cư dân Canaan | `A1`, `S1`, `L1` |
| | | `AB02-04` | Abram dựng bàn thờ đá thô thờ phượng Thiên Chúa dưới nắng chiều đồi Canaan | `A1` |
| **03. Nạn đói & Ai Cập** | St 12:10–20 | `AB03-01` | Nạn đói tại Canaan, đồng cỏ khô nứt nẻ, gia súc gầy yếu; Abram nhìn lo lắng | `A1` |
| | | `AB03-02` | Abram và Sarai trên đường xuống Ai Cập, Abram nói chuyện riêng đầy bất an | `A1`, `S1` |
| | | `AB03-03` | Sarai được quan Ai Cập đưa vào cung Pharaoh, nổi bật giữa kiến trúc Ai Cập | `S1`, `loc_egypt_nile` — giữ nhận diện Sarai |
| | | `AB03-04` | Pharaoh ngồi trên ngai chất vấn Abram tại đại sảnh; Sarai đứng bên, căng thẳng | `A1`, `S1`, Pharaoh |
| **04. Abram & Lot chia đất** | St 13 | `AB04-01` | Người chăn gia súc hai bên cãi vã bên nguồn nước vì thiếu đồng cỏ | Quần chúng mục tử |
| | | `AB04-02` | Abram và Lot trên sườn đồi cao nhìn ra hai hướng; Abram nhường quyền chọn | `A1`, `L1` |
| | | `AB04-03` | Lot dẫn gia đình, lều và gia súc xuống đồng bằng Jordan xanh tươi về phía Sodom | `L1` |
| | | `AB04-04` | Abram ở lại vùng đồi Mamre gần Hebron, dựng lều và bàn thờ dưới cây sồi cổ thụ | `A1`, `loc_mamre_hebron` |
| **05. Chiến tranh 4 vua & cứu Lot** | St 14:1–16 | `AB05-01` | Chiến trường Siddim: chiến binh tháo chạy giữa hố nhựa đường, khói bụi, chiến xa cổ | Quần chúng quân lính |
| | | `AB05-02` | Lot và người nhà bị quân thắng trận áp giải đi, tài sản bị cướp, thành phố hỗn loạn | `L2` |
| | | `AB05-03` | Người sống sót chạy đến trại Mamre báo tin; Abram đứng bật dậy khẩn trương | `A1`, `loc_mamre_hebron` |
| | | `AB05-04` | Abram chỉ huy 318 gia nhân & đồng minh tập kích doanh trại địch ban đêm dưới ánh đuốc | `A1` (vẫn 75–85t, không trẻ hóa cơ bắp) |
| | | `AB05-05` | Abram gặp lại Lot sau giải cứu, phía sau là người được cứu và tài sản thu hồi | `A1`, `L2` |
| **06. Melchizedek chúc phước** | St 14:17–24 | `AB06-01` | Melchizedek trong lễ phục vua-tư tế đón Abram, mang bánh và rượu chúc phước | `A1`, Melchizedek |
| | | `AB06-02` | Abram kính cẩn dâng một phần mười chiến lợi phẩm cho Melchizedek | `A1`, Melchizedek |
| | | `AB06-03` | Vua Sodom đề nghị trao của cải nhưng Abram đứng thẳng giơ tay từ chối | `A1`, Vua Sodom |
| **07. Lời hứa dưới trời sao** | St 15:1–6 | `AB07-01` | Abram ngồi cô độc trong căn lều tối dưới ánh đèn dầu, trăn trở chưa có con | `A2` (85t), có thể có Eliezer thoáng xa |
| | | `AB07-02` | Abram bước ra ngoài lều, ngước nhìn bầu trời đêm đầy sao vô tận *(ảnh biểu tượng)* | `A2`, `loc_mamre_hebron` |
| | | `AB07-03` | Cận cảnh Abram dưới trời sao, đôi mắt vừa kinh ngạc vừa bừng hy vọng | `A2` |
| **08. Giao ước con vật chia đôi** | St 15:7–21 | `AB08-01` | Abram đặt các phần lễ vật đối diện nhau trên nền đất (trang nghiêm, không máu me) | `A2` |
| | | `AB08-02` | Abram xua chim săn mồi lao xuống lễ vật trong ánh chiều tà | `A2` |
| | | `AB08-03` | Trong đêm, lò lửa tỏa khói và ngọn đuốc cháy đi qua lối giữa lễ vật; Abram quan sát | `A2` — **không vẽ thân thể người cho Thiên Chúa** |
| **09. Hagar & Ishmael ra đời** | St 16 | `AB09-01` | Sarai trò chuyện với Abram trong lều đề nghị chuyện Hagar; Hagar đứng xa phía cửa | `A2`, `S2`, `H1` |
| | | `AB09-02` | Hagar mang thai, Sarai tức giận, Abram đứng giữa khó xử | `A2`, `S2`, `H1` (mang thai) |
| | | `AB09-03` | Hagar mang thai một mình rời trại đi vào hoang mạc nắng gắt | `H1` (mang thai — không bế trẻ!) |
| | | `AB09-04` | Hagar ngồi kiệt sức bên suối, thiên sứ hiện ra trong ánh sáng dịu | `H1`, Thiên sứ |
| | | `AB09-05` | Hagar sinh Ishmael; Abram 86 tuổi bế con sơ sinh, Hagar nằm nghỉ trong lều | `A2`, `H1`, `IM1` |
| **10. Đổi tên & Giao ước cắt bì** | St 17 | `AB10-01` | Abram 99t sấp mình trước ánh sáng từ ngoài khung hình, nhận tên mới Abraham | `A3` (99t) |
| | | `AB10-02` | Abraham kinh ngạc xen lẫn nụ cười khi nghe Sarah sẽ sinh con | `A3` |
| | | `AB10-03` | Abraham tập hợp Ishmael 13 tuổi cùng người nam trong gia tộc công bố giao ước | `A3`, `IM2` (13t) — không mô tả thủ thuật |
| **11. Ba vị khách tại Mamre** | St 18:1–15 | `AB11-01` | Abraham ngồi trước cửa lều giữa trưa nắng, bất ngờ thấy ba vị khách đứng trước mặt | `A3`, 3 vị khách, `loc_mamre_hebron` |
| | | `AB11-02` | Abraham cung kính tiếp đón ba vị khách dưới tán sồi lớn, chuẩn bị nước rửa chân | `A3`, 3 vị khách |
| | | `AB11-03` | Sarah nhào bột làm bánh trong lều, người hầu chế biến bê non bên ngoài | `S3` (89t), người hầu |
| | | `AB11-04` | Ba vị khách ăn dưới bóng cây, Abraham đứng hầu; Sarah kín đáo nghe sau cửa lều | `A3`, `S3`, 3 vị khách |
| | | `AB11-05` | Cận cảnh Sarah hé nhìn sau cửa lều, đưa tay che nụ cười nghi ngờ | `S3` |
| **12. Cầu xin cho Sodom** | St 18:16–33; 19:27–29 | `AB12-01` | Abraham cùng ba vị khách đứng trên sườn đồi nhìn xuống vùng đồng bằng hai thành phố | `A3`, 3 vị khách (đồng bộ AB11) |
| | | `AB12-02` | Hai vị khách đi về hướng Sodom; Abraham ở lại bước tới cầu xin Thiên Chúa | `A3`, 2 vị khách |
| | | `AB12-03` | Cận cảnh Abraham tha thiết cầu thay, gương mặt lo lắng cho người vô tội | `A3` |
| | | `AB12-04` | Sáng hôm sau, Abraham đứng một mình trên mỏm đồi nhìn cột khói dày đặc từ đồng bằng | `A3` *(không thêm cảnh vợ Lot hóa muối)* |
| **13. Tại Gerar** | St 20 | `AB13-01` | Abraham và Sarah đến thành bang Gerar, đi qua cổng thành cùng người hầu | `A3`, `S3` — kiến trúc Canaan, khác Ai Cập |
| | | `AB13-02` | Sarah được đưa vào triều đình Abimelech trong cung điện địa phương | `S3`, Abimelech |
| | | `AB13-03` | Abimelech giật mình tỉnh giấc hoảng sợ sau giấc mộng cảnh báo trong phòng tối | Abimelech |
| | | `AB13-04` | Abraham đứng trước Abimelech giải thích chuyện em gái rồi cầu nguyện cho nhà vua | `A3`, Abimelech |
| **14. Isaac ra đời** | St 21:1–8 | `AB14-01` | Sarah 90t bế Isaac sơ sinh trên giường, Abraham 100t đứng cạnh đầy xúc động | `A3`, `S3`, `IS1` — ánh sáng vàng ấm |
| | | `AB14-02` | Cận cảnh Sarah ôm Isaac, nụ cười hạnh phúc trên gương mặt già nua | `S3`, `IS1` |
| | | `AB14-03` | Tiệc mừng Isaac dứt sữa dưới lều trại, gia đình vui mừng | `A3`, `S3`, `IS2` |
| **15. Hagar & Ishmael vào sa mạc** | St 21:9–21 | `AB15-01` | Sarah thấy Ishmael thiếu niên đùa giỡn/trêu Isaac trong tiệc, gương mặt căng thẳng | `S3`, `IM3` (~15–16t), `IS2` |
| | | `AB15-02` | Sarah yêu cầu đưa hai mẹ con đi; Abraham đau buồn đứng giữa hai phía | `A3`, `S3` |
| | | `AB15-03` | Sáng sớm, Abraham trao bánh và bầu nước cho Hagar; Ishmael thiếu niên đứng cạnh mẹ | `A3`, `H2`, `IM3` |
| | | `AB15-04` | Hagar và Ishmael bước qua hoang mạc Beersheba khô hạn, bầu nước gần cạn | `H2`, `IM3`, `loc_beersheba_desert` |
| | | `AB15-05` | Ishmael kiệt sức nằm dưới bóng bụi cây; Hagar ngồi cách xa khóc tuyệt vọng | `H2`, `IM3` — **không vẽ Ishmael sơ sinh** |
| | | `AB15-06` | Hagar phát hiện giếng nước sau lời thiên sứ, chạy tới múc nước cứu con | `H2`, `IM3`, Thiên sứ |
| **16. Núi Moriah (Cao trào)** | St 22:1–19 | `AB16-01` | Abraham tỉnh giấc trước bình minh, ngồi trầm tư ngoài lều sau mệnh lệnh của Chúa | `A4` (>100t) |
| | | `AB16-02` | Abraham chẻ củi, thắng yên lừa lúc tảng sáng; Isaac và hai đầy tớ đứng bên | `A4`, `IS3` (thanh niên), 2 đầy tớ, con lừa |
| | | `AB16-03` | Đoàn 4 người và con lừa đi trên đường đất đá hướng về vùng núi khô cằn | `A4`, `IS3`, `loc_mount_moriah` |
| | | `AB16-04` | Ngày thứ ba: Abraham và Isaac nhìn thấy núi Moriah từ xa; hai đầy tớ đứng cạnh lừa | `A4`, `IS3`, 2 đầy tớ |
| | | `AB16-05` | Hai đầy tớ ở lại chân núi; Abraham cầm lửa và dao, Isaac vác bó củi bắt đầu leo dốc | `A4`, `IS3` — khóa đạo cụ (củi, lửa, dao) |
| | | `AB16-06` | Giữa dốc núi: Isaac quay hỏi cha về con chiên; Abraham nhìn con xúc động nhưng điềm tĩnh | `A4`, `IS3` |
| | | `AB16-07` | Trên đỉnh núi đá, Abraham dựng bàn thờ đá và xếp củi lên; Isaac ở gần bên | `A4`, `IS3`, `loc_mount_moriah` |
| | | `AB16-08` | Isaac trên bàn thờ; Abraham giơ dao nhưng dừng lại khi nghe tiếng thiên sứ *(không máu)* | `A4`, `IS3`, ánh sáng/thiên sứ |
| | | `AB16-09` | Abraham quay nhìn bụi cây thấy con chiên đực mắc sừng; Isaac phía sau đã được giải thoát | `A4`, `IS3`, con chiên đực |
| | | `AB16-10` | Abraham dâng con chiên thay Isaac; hai cha con bước xuống chân núi trong nắng chiều ấm | `A4`, `IS3` |
| **17. Sarah qua đời & Cưới Rebecca** | St 23–24 | `AB17-01` | Abraham già nua ngồi đau buồn bên Sarah vừa qua đời trong lều ở Hebron | `A4`, `S4` (127t) |
| | | `AB17-02` | Abraham thương lượng mua hang Machpelah với Ephron trước các trưởng lão Hittite | `A4`, Ephron, trưởng lão |
| | | `AB17-03` | Abraham đứng lặng trước cửa hang đá Machpelah trong ánh chiều tĩnh lặng | `A4` |
| | | `AB17-04` | Abraham giao nhiệm vụ cho người quản gia già trung tín đi tìm vợ cho Isaac | `A4`, Quản gia già |
| | | `AB17-05` | Rebecca gặp người quản gia bên giếng nước cạnh đàn lạc đà tại Mesopotamia | Rebecca, Quản gia già |
| | | `AB17-06` | Isaac trưởng thành gặp Rebecca khi nàng đến Canaan lúc chiều muộn bên lều trại | `IS4`, Rebecca |
| **18. Cuối đời & An táng** | St 25:1–11 | `AB18-01` | Abraham những năm cuối đời bên Keturah và các con trong khu trại mở rộng | `A5`, Keturah |
| | | `AB18-02` | Abraham 175 tuổi nằm nghỉ bình an trong lều, ánh chiều chiếu lên gương mặt già nua | `A5` (175t) |
| | | `AB18-03` | Isaac và Ishmael trưởng thành đứng cạnh nhau trước hang Machpelah an táng cha | `IS4`, `IM4` *(có thể nối cảnh hoàng hôn Canaan làm kết phim)* |

---

## TRÌNH TỰ SẢN XUẤT ĐỀ XUẤT

1. **Bước 1:** Tạo & chốt 6 ảnh gốc nhân vật cốt lõi trong `images/refs_characters/` (`Abraham A1` → phát triển `A2..A5`, `Sarah S1` → `S2..S4`, `Lot`, `Hagar`, `Ishmael`, `Isaac`).
2. **Bước 2:** Tạo 4 ảnh bối cảnh chuẩn trong `images/refs_locations/`.
3. **Bước 3:** Tạo ảnh từng câu chuyện một, lưu vào `images/scenes/` đúng mã `AB01-01.jpg` → `AB18-03.jpg`. Kiểm tra đồng bộ sau mỗi câu chuyện rồi mới qua câu chuyện tiếp theo.
4. **Bước 4:** Chạy `python ..\build_video.py 01_ong_apraham` để tự động ghép 79 khung hình với file `01_ong_apraham.mp3` thành video YouTube 1080p hoàn chỉnh.
