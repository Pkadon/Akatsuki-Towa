label avg22131:

$ play_music("ED6200.ogg")
scene avg_bg_036
$ update_narrator('c23')
$ update_portrait('oc002_01 3', 'p2', [r(-3), light], 6)
window show
with fade_in
$ update_portrait('oc002_01 3', 'p2', [r(-3), r_shake, light], 6)
c23 '[convertstrid(1128267)]'
$ update_portrait('oc002_01 3', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1128268)]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro13.ogg"
c33 '[convertstrid(1128269)]'
return