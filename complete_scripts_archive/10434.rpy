label avg10434:

play music "ed7526.ogg"
scene placeholderbackground
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1141506)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1141507)]'
hide p2
$ update_portrait('oc004_01 11', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1141508)]'
play music "ed7511.ogg"
hide p4
hide p1
$ update_narrator('c10531')
with fade
play sfx2 "other_7080.ogg"
c10531 '[convertstrid(1141509)]' (what_size=(gui.text_size*1.2)) with shake
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
with fade
play sfxvoice "avg_vocal_ro02.ogg"
c31 '[convertstrid(1141510)]'
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 13', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li10.ogg"
c43 '[convertstrid(1141511)]'
hide p4
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
play sfxvoice "bcv_oc001_com_01.ogg"
c13 '[convertstrid(1141512)]'
hide p3
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l_midback(-3), light, flip], 6)
c21 '[convertstrid(1141513)]'
return