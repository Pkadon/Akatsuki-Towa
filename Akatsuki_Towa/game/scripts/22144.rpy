label avg22144:

play music "ed7565.ogg"
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with fade_in
play sfxvoice "avg_vocal_na17.ogg"
c11 '[convertstrid(1128332)]'
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc007_01 6', 'p7', [r(-24), light], 6)
c73 '[convertstrid(1128333)]'
hide p1
$ update_portrait('oc007_01 6', 'p7', [r(-24), dark], 5)
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1128334)]'
$ update_portrait('oc002_01 1', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc007_01 1', 'p7', [r(-24), light], 6)
c73 '[convertstrid(1128335)]'
$ update_portrait('oc007_01 5', 'p7', [r(-24), light], 6)
play sfxvoice "avg_vocal_ar05.ogg"
c73 '[convertstrid(1128336)]'
hide p2
$ update_portrait('oc007_01 5', 'p7', [r(-24), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1128337)]'
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc007_01 2', 'p7', [r(-24), light], 6)
c73 '[convertstrid(1128338)]'
hide p4
$ update_portrait('oc007_01 2', 'p7', [r(-24), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1128339)]'
$ update_portrait('oc003_01 14', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1128340)]'
$ update_portrait('oc003_01 14', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc007_01 2', 'p7', [r(-24), r_shake, light], 6)
play sfxvoice "avg_vocal_ar06.ogg"
c73 '[convertstrid(1128341)]'
$ update_portrait('oc007_01 3', 'p7', [r(-24), light], 6)
c73 '[convertstrid(1128342)]'
hide p3
$ update_portrait('oc007_01 3', 'p7', [r(-24), dark], 5)
$ update_portrait('oc004_01 5', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li07.ogg"
c41 '[convertstrid(1128343)]'
hide p7
$ update_portrait('oc004_01 5', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 6', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro03.ogg"
c33 '[convertstrid(1128344)]'
hide p4
$ update_portrait('oc003_01 6', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 21', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[convertstrid(1128345)]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1128346)]'
hide p3
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc007_01 5', 'p7', [r(-24), light], 6)
c73 '[convertstrid(1128347)]'
$ update_portrait('oc007_01 1', 'p7', [r(-24), light], 6)
c73 '[convertstrid(1128348)]'
$ update_portrait('oc007_01 5', 'p7', [r(-24), light], 6)
play sfxvoice "avg_vocal_ar07.ogg"
c73 '[convertstrid(1128349)]'
hide p1
$ update_portrait('oc007_01 5', 'p7', [r(-24), dark], 5)
$ update_portrait('oc002_01 14', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch08.ogg"
c21 '[convertstrid(1128350)]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1128351)]'
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc007_01 1', 'p7', [r(-24), light], 6)
c73 '[convertstrid(1128352)]'
$ update_portrait('oc007_01 5', 'p7', [r_exit(-24), light], 6)
play sfx2 "other_7020.ogg"
c73 '[convertstrid(1128353)]'
hide p7
hide p1
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch05.ogg"
c21 '[convertstrid(1128354)]'
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r_entrance(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[convertstrid(1128355)]'
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1128356)]'
return