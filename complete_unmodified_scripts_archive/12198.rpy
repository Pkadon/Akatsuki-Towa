label avg12198:

$ play_music("ED6104.ogg")
scene avg_bg_023
$ update_portrait('st009_01 1', 'p209', [l(-22), light, flip], 6)
$ update_narrator('c2091')
window show
with fade_in
c2091 '[convertstrid(1120590)]'
$ update_portrait('st009_01 1', 'p209', [l(-22), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1120591)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('st009_01 1', 'p209', [l(-22), light, flip], 6)
c2091 '[convertstrid(1120592)]'
hide p1
$ update_portrait('st009_01 1', 'p209', [l(-22), dark, flip], 5)
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch08.ogg"
c23 '[convertstrid(1120593)]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), r_shake, light], 6)
c13 '[convertstrid(1120594)]'
hide p209
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1120595)]'
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1120596)]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('st009_01 4', 'p209', [l(-22), light, flip], 6)
c2091 '[convertstrid(1120597)]'
$ update_portrait('st009_01 1', 'p209', [l(-22), light, flip], 6)
c2091 '[convertstrid(1120598)]'
return