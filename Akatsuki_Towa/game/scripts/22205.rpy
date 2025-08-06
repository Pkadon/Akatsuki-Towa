label avg22205:

play music "ed7151.ogg"
scene avg_bg_036
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1128594)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
c5621 '[convertstrid(1128595)]'
c5631 '[convertstrid(1128596)]'
c5621 '[convertstrid(1128597)]'
hide p1
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch17.ogg"
c23 '[convertstrid(1128598)]'
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li18.ogg"
c41 '[convertstrid(1128599)]'
hide p2
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1128600)]'
play music "ED6516.ogg"
hide p4
$ update_portrait('oc003_01 8', 'p3', [r(-6), dark], 5)
play sfx2 "other_7007.ogg"
c7201 '[convertstrid(1128601)]'
hide p3
$ update_portrait('oc001_01 20', 'p1', [r(-2), r_shake, light], 6)
c13 '[convertstrid(1128602)]'
$ update_portrait('oc001_01 20', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l_midback(-3), light, flip], 6)
c21 '[convertstrid(1128603)]'
hide p2
hide p1
$ update_narrator('c5631')
with fade
play sfx2 "other_7080.ogg"
c5631 '[convertstrid(1128604)]'
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1128605)]'
$ update_portrait('oc001_01 20', 'p1', [r(-2), dark], 5)
c5621 '[convertstrid(1128606)]'
$ update_portrait('oc001_01 9', 'p1', [r_midback(-2), light], 6)
play sfxvoice "bcv_oc001_com_01.ogg"
c13 '[convertstrid(1128607)]'
return