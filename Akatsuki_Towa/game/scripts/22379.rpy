label avg22379:

$ play_music("ed7304.ogg")
scene avg_bg_218
$ update_narrator('c0')
window show
with fade_in
play sfx2 "other_7004.ogg"
c0 '[convertstrid(1133970)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1133971)]'
hide p1
play sfx2 "other_7080.ogg"
c0 '[convertstrid(1133972)]' with shake
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch11.ogg"
c21 '[convertstrid(1133973)]'
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1133974)]'
return