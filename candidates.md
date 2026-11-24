# One-Liner Laugh Lab — Kandidat + Duel (Forge putaran 1)

- Lomba: `u-suroso-69-one-liner-laugh-lab-6ccf3aae` — satu baris lucu maks 200 karakter ke `/output/entry.txt`, prompt: excuse robot vacuum setelah makan kaus kaki.
- Juri: z-ai/glm-5.3-flash, duel dua arah, kriteria berurutan: (1) on-subject, (2) lucu (twist/deadpan), (3) orisinal, (4) cocok prompt, (5) padat.
- Field live: 1.996 submission (cek 11:49 WIB, masih naik ~3/menit). Hadiah $2,50 top 8 (#1 $0,80). Tutup 26 Nov 23:15 WIB; cutoff ronde buta 1: 25 Nov 04:34 WIB.
- Ideasi: 1 panggilan qwen4-max, 6.277 token total (prompt 392 + completion 5.885). TANPA glm-5.3.
- Orisinalitas: grep `idea-archive.md` = 0 hit untuk SEMUA kata kunci kandidat (load-bearing, curation, exhibit, consequence, hairball, escalated, specialist, time capsule, mule, stairs, sacrifice, ring, warranty, brush roll) dan 0 hit untuk vacuum/sock. Semua konsep segar vs arsip kita.
- Catatan: judul kompetitor BUKAN teks entri (teks disembunyikan ronde buta). Hitungan judul hanya sinyal sudut jenuh, bukan bukti teks sama.

## Sudut JENUH (hindari)
- "It was on the floor / floor is my jurisdiction" (112 judul), hungry/snack (107), sock attacked first / self-defense (13x), trespassing (7x), adopted sock / sock friend (50 cluster), sock begged day off, diet, laundry, hiding evidence.

## 10 kandidat (sudut berbeda)
1. (114) I removed what I assessed as a load-bearing sock. The house is still standing, so I'd call that a successful test.
2. (94) It's not digestion, it's curation. The exhibit is called 'So That's Where The Other One Went.'
3. (116) Think of me less as an appliance and more as a consequence. You'll get it back when the tone in this house improves.
4. (110) The cat coughs up a hairball and gets a treat. I take one argyle and suddenly there's a review of my warranty.
5. (91) Your sock has been escalated to a specialist. The specialist is me. I am also the incident.
6. (104) The sock is in the program. New name, new job in my brush roll, and you will not be contacting it again.
7. (102) There was a ring in it. Empty my bin, get down on one knee, and let's never discuss how this happened.
8. (94) I'm a time capsule. In four hundred years they'll open me and know everything about your feet.
9. (99) I'm a mule now. Don't ask what's inside me, don't ask who it's for, and don't ask the dog anything.
10. (94) The stairs required a sacrifice. I offered your good wool one. You're all safe until Thursday.

## Prioritas duel (berdasar tabrakan judul)
- Tabrakan judul 0: #2 curation, #3 consequence, #4 hairball, #9 mule, #10 stairs (dan #7 ring).
- Tabrakan kecil: #1 load-bearing (2), #5 escalated/specialist (1), #8 time capsule (2).
- Tabrakan lebih besar: #4 warranty (10 judul menyebut warranty — tapi sudut "kucing vs review warranty" berbeda), #6 brush roll (6 judul).

## Duel Fase A — round-robin 8 kandidat teratas (C2, C3, C4, C5, C7, C8, C9, C10)
- Juri proksi: qwen4-max HANYA (TANPA glm-5.3), prompt juri VERBATIM dari RULES.txt, dua arah, batch 5 pasang per panggilan, 12 panggilan (28 pasang x 2 arah).
- Skor game per aturan house: pemenang satu arah dapat 0,5 + margin/10, sisanya untuk yang kalah; skor game = rata-rata dua arah. Rate kandidat = rata-rata skor game (0–1).
- Panggilan duel: 14 total (12 Fase A + 2 Fase B), token qwen4-max tercatat di usage-log.jsonl.

| Pasang | Skor game (pihak pertama) |
|---|---|
| C2 vs C3 | 0,30 |
| C2 vs C4 | 0,30 |
| C2 vs C5 | 0,20 |
| C2 vs C7 | 0,30 |
| C2 vs C8 | 0,35 |
| C2 vs C9 | 0,50 |
| C2 vs C10 | 0,30 |
| C3 vs C4 | 0,50 |
| C3 vs C5 | 0,30 |
| C3 vs C7 | 0,35 |
| C3 vs C8 | 0,25 |
| C3 vs C9 | 0,30 |
| C3 vs C10 | 0,25 |
| C4 vs C5 | 0,25 |
| C4 vs C7 | 0,25 |
| C4 vs C8 | 0,75 |
| C4 vs C9 | 0,70 |
| C4 vs C10 | 0,45 |
| C5 vs C7 | 0,65 |
| C5 vs C8 | 0,70 |
| C5 vs C9 | 0,75 |
| C5 vs C10 | 0,50 |
| C7 vs C8 | 0,80 |
| C7 vs C9 | 0,75 |
| C7 vs C10 | 0,55 |
| C8 vs C9 | 0,75 |
| C8 vs C10 | 0,50 |
| C9 vs C10 | 0,25 |

### Rate Fase A (rata-rata skor game, 7 game per kandidat)
| Kandidat | Rate | Menang game (dari 7) |
|---|---|---|
| C5 escalated/specialist | **0,693** | 6 (1 imbang vs C10) |
| C7 ring/proposal | 0,650 | 6 |
| C10 stairs/sacrifice | 0,600 | 4 |
| C4 cat/warranty | 0,514 | 3 |
| C8 time capsule | 0,486 | 3 |
| C3 consequence | 0,379 | 1 |
| C9 mule | 0,357 | 1 |
| C2 curation | 0,321 | 0 |

### Cek tambahan — C5 vs 2 kandidat yang tidak ikut round-robin
| Pasang | Skor game C5 |
|---|---|
| C5 vs C1 load-bearing | 0,75 |
| C5 vs C6 program/brush roll | 0,70 |

C5 tidak terkalahkan dalam 9 game head-to-head (8 menang, 1 imbang vs C10).

## Duel Fase B — pemenang C5 vs 5 judul kompetitor terkuat (benchmark)
Jujur: ini JUDUL, bukan teks entri (teks disembunyikan ronde buta). Benchmark hanya sinyal kekuatan lapangan.

| Benchmark | Skor game C5 |
|---|---|
| B1 "It was on the floor. The floor is my jurisdiction. Case closed." | 0,60 |
| B2 "It was single, smelled of feet, and lay on the floor — legally, that is a dust bunny." | 0,40 |
| B3 "I spent three years eating dirt for this household. One sock is a promotion." | 0,35 |
| B4 "According to my sensors, the sock was trespassing. I did what any law-abiding appliance would do: I ate the evidence." | 0,60 |
| B5 "My sock-avoidance free trial expired at midnight — I didn't eat it by mistake, your card declined." | 0,40 |
| **Rata-rata C5 vs benchmark** | **0,47 (menang 2 dari 5)** |

## Pilihan akhir (Forge putaran 1)
**C5 — "Your sock has been escalated to a specialist. The specialist is me. I am also the incident." — 91 karakter / 91 byte, 1 baris.**

Alasan: rate tertinggi Fase A (0,693), menang game terbanyak (6/7, 1 imbang), menang head-to-head vs runner-up C7 (0,65), dan menang vs kedua kandidat di luar round-robin (C1 0,75, C6 0,70). Sudut "eskalasi korporat yang berujung pengakuan" segar (tabrakan judul 1) dan paling padat (91 karakter, tiga ketukan pendek).

**Catatan jujur untuk Warden: gate ≥0,70 TIDAK tercapai — rate C5 0,693, meleset 0,007 (dalam noise juri; mayoritas margin duel 2). Vs benchmark terkuat C5 hanya 0,47 (2/5). Keputusan LOLOS/GAGAL ada di Warden; Forge tidak mengklaim gate lolos.**
