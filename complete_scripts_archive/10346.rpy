label avg10346:

play music "ed7544.ogg"
scene avg_bg_031
$ update_narrator('c13')
window show
with fade_in
$ update_portrait('oc001_01 12', 'p1', [r_entrance(-2), light], 6)
play sfxvoice "avg_vocal_na21.ogg"
c13 '[convertstrid(1131270)]'
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch11.ogg"
c21 '[convertstrid(1131271)]'
hide p2
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1131272)]'
hide p4
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1131273)]'
hide p3
$ update_portrait('sc046_01 3', 'p1004', [l_midback(-5), light, flip], 6)
play sfx2 "fight_6024.ogg"
c10041 '[convertstrid(1131274)]' (what_size=(gui.text_size*1.2))
hide p1
$ update_portrait('sc046_01 3', 'p1004', [l(-5), dark, flip], 5)
play sfx2 "other_7085.ogg"
c10233 '[convertstrid(1131275)]'
c10243 '[convertstrid(1131276)]'
hide p1004
$ update_narrator('c13')
with fade
$ update_portrait('oc001_01 12', 'p1', [r_entrance(-2), r_shake, light], 6)
play sfxvoice "avg_vocal_na21.ogg"
c13 '[convertstrid(1131277)]' (what_size=(gui.text_size*1.2))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1131278)]'
hide p2
hide p1
$ update_narrator('c10253')
with fade
play sfx2 "other_7085.ogg"
c10253 '[convertstrid(1131279)]'
c10263 '[convertstrid(1131280)]' (what_size=(gui.text_size*1.4))
$ update_portrait('sc046_01 4', 'p1004', [l_midback(-5), light, flip], 6)
play sfx2 "other_7091.ogg"
c10041 '[convertstrid(1131281)]' (what_size=(gui.text_size*1.2))
return