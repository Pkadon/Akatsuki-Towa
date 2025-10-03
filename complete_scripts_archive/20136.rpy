label avg20136:

$ play_music("ED6516.ogg")
scene avg_bg_071
$ update_narrator('c7013')
window show
with fade_in
play sfx2 "other_7072.ogg"
play sfxvoice "avg_vocal_ji03.ogg"
c7013 '[convertstrid(1006700)]'
c7013 '[convertstrid(1006701)]'
$ update_portrait('sc044_01 4', 'p51', [l(-7), light, flip], 6)
c511 '[convertstrid(1006702)]'
$ update_portrait('sc044_01 4', 'p51', [l(-7), dark, flip], 5)
c7013 '[convertstrid(1006703)]'
hide p51
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1006704)]'
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1006705)]'
hide p2
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1006706)]'
hide p3
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
c7013 '[convertstrid(1006707)]'
hide p1
$ update_portrait('sc044_01 2', 'p51', [l(-7), light, flip], 6)
c511 '[convertstrid(1006708)]'
$ update_portrait('sc044_01 2', 'p51', [l(-7), dark, flip], 5)
c7013 '[convertstrid(1006709)]'
hide p51
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1006710)]'
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li14.ogg"
c43 '[convertstrid(1006711)]'
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1006712)]'
hide p4
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1006713)]'
hide p1
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('sc044_01 4', 'p51', [l(-7), light, flip], 6)
c511 '[convertstrid(1006714)]'
hide p2
$ update_portrait('sc044_01 4', 'p51', [l(-7), dark, flip], 5)
c7013 '[convertstrid(1006715)]'
play sfxvoice "avg_vocal_ji05.ogg"
c7013 '[convertstrid(1006716)]'
hide p51
$ update_portrait('oc002_01 14', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1006717)]'
$ update_portrait('oc002_01 14', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na18.ogg"
c13 '[convertstrid(1006718)]'
return