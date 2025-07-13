label avg14105:

play music "ed7150.ogg"
scene avg_bg_023
$ update_portrait('sc053_01 4', 'p60', [l(-32), light, flip], 6)
$ update_narrator('c601')
window show
with fade_in
c601 '[textdict[1202141]]'
$ update_portrait('sc053_01 4', 'p60', [l(-32), dark, flip], 6)
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 5)
c23 '[textdict[1202142]]'
$ update_portrait('oc002_01 9', 'p2', [r(-3), dark], 5)
$ update_portrait('sc053_01 1', 'p60', [l(-32), light, flip], 6)
c601 '[textdict[1202143]]'
hide p60
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1202144]]'
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1202145]]'
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 5)
play sfxvoice "avg_vocal_ch08.ogg"
c23 '[textdict[1202146]]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na02.ogg"
c13 '[textdict[1202147]]'
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1202148]]'
return