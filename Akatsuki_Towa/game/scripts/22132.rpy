label avg22132:

$ play_music("ED6200.ogg")
scene avg_bg_036
$ update_narrator('c23')
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
window show
with fade_in
$ update_portrait('oc002_01 6', 'p2', [r(-3), r_shake, light], 6)
play sfx2 "other_7034.ogg"
play sfxvoice "avg_vocal_ch08.ogg"
c23 '[convertstrid(1128270)]'
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 6', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1128271)]'
return