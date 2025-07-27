label avg1085:

play music "ed7202.ogg"
scene avg_bg_079
$ update_portrait('oc004_01 5', 'p4', [l(-5), light, flip], 6)
$ update_narrator('c41')
window show
with fade_in
c41 '[convertstrid(2101857)]'
$ update_portrait('oc004_01 5', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[convertstrid(2101858)]'
$ update_portrait('oc001_01 5', 'p1', [r(-2), light], 5)
c13 '[convertstrid(2101859)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[convertstrid(2101860)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(2101861)]'
hide p4
hide p1
c0 '[convertstrid(2101862)]'
$ update_portrait('oc004_01 7', 'p4', [l_midback(-5), light, flip], 6)
play sfx2 "other_7007.ogg"
play sfxvoice "avg_vocal_li26.ogg"
c41 '[convertstrid(2101863)]'
stop music
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[convertstrid(2101864)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 12', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(2101865)]'
play music "ed7511.ogg"
$ update_portrait('oc004_01 12', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[convertstrid(2101866)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(2101867)]'
hide p4
play sfx2 "fight_6002.ogg"
c10871 '[convertstrid(2101868)]' with shake
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 5)
play sfxvoice "bcv_oc001_com_01.ogg"
c13 '[convertstrid(2101869)]'
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 16', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li23.ogg"
c41 '[convertstrid(2101870)]'
return