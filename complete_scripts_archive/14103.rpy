label avg14103:

play music "ed7150.ogg"
scene avg_bg_023
$ update_portrait('oc002_01 17', 'p2', [r(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
play sfxvoice "avg_vocal_ch25.ogg"
c23 '[textdict[1202122]]'
$ update_portrait('oc002_01 17', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 2', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1202123]]'
hide p2
$ update_portrait('sc049_01 2', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 5)
c13 '[textdict[1202124]]'
$ update_portrait('oc001_01 22', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1202125]]'
$ update_portrait('sc049_01 10', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1202126]]'
hide p1
$ update_portrait('sc049_01 10', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 5)
play sfxvoice "avg_vocal_ch17.ogg"
c23 '[textdict[1202127]]'
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1202128]]'
return