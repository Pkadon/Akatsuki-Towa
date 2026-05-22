label avg12107:

$ play_music("ed7150.ogg")
scene avg_bg_018
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with fade_in
c21 '[convertstrid(1128027)]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1128028)]'
hide p2
hide p1
play sfx2 "other_7004.ogg"
c0 '[convertstrid(1128029)]'
play sfx2 "other_7004.ogg"
c0 '[convertstrid(1128030)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1128031)]'
hide p1
play sfx2 "other_7004.ogg"
c0 '[convertstrid(1128032)]'
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1128034)]'
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
play sfxvoice "bcv_oc002_c02_01.ogg"
c21 '[convertstrid(1128035)]'
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na04_b.ogg"
c13 '[convertstrid(1128036)]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1128037)]'
return