label avg12108:

play music "ed7101.ogg"
scene avg_bg_073
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with fade_in
play sfx2 "other_7020.ogg"
c11 '[convertstrid(1128038)]'
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
c9513 '[convertstrid(1128039)]'
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1128040)]'
hide p1
c0 '[convertstrid(1128041)]'
play sfx2 "other_7004.ogg"
c9513 '[convertstrid(1128042)]'
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1128043)]'
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
c9513 '[convertstrid(1128044)]'
hide p3
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na20.ogg"
c11 '[convertstrid(1128045)]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1128046)]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
c9513 '[convertstrid(1128047)]'
$ update_portrait('oc002_01 21', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1128048)]'
hide p2
$ update_portrait('oc001_01 9', 'p1', [l(-2), light, flip], 6)
play sfxvoice "bcv_oc001_c04_01.ogg"
c11 '[convertstrid(1128049)]' (what_size=(gui.text_size*1.2)) with shake
$ update_portrait('oc001_01 9', 'p1', [l(-2), dark, flip], 5)
c9513 '[convertstrid(1128050)]'
c9513 '[convertstrid(1128051)]'
c9513 '[convertstrid(1128052)]'
hide p1
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch11.ogg"
c21 '[convertstrid(1128053)]'
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
c9513 '[convertstrid(1128054)]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na05.ogg"
c11 '[convertstrid(1128055)]'
return