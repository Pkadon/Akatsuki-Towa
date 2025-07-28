label avg12602:

play music "ED6200.ogg"
scene avg_bg_080
$ update_narrator('c21')
window show
with fade_in
$ update_portrait('oc002_01 17', 'p2', [l_entrance(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch19.ogg"
c21 '[convertstrid(1161132)]'
$ update_portrait('oc002_01 17', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r_entrance(-2), light], 6)
c13 '[convertstrid(1161133)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1161134)]'
hide p1
$ update_portrait('oc002_01 1', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1161135)]'
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 23', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1161136)]'
hide p2
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro12.ogg"
c31 '[convertstrid(1161137)]'
hide p4
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1161138)]'
hide p3
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1161139)]'
hide p2
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
play sfx2 "fight_6025.ogg"
c31 '[convertstrid(1161140)]'
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfx2 "fight_6024.ogg"
play sfxvoice "bcv_oc001_com_01.ogg"
c13 '[convertstrid(1161141)]'
return