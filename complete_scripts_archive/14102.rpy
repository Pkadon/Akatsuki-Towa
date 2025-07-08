label avg14102:
stop music

play music "ed7150.ogg"
scene avg_bg_023
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
window show
with fade_in
c561 '[textdict[1202113]]'
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 5)
play sfxvoice "bcv_oc002_com_01.ogg"
c23 '[textdict[1202114]]'
hide p2
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1202115]]'
hide p56
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1202116]]'
hide p1
$ update_portrait('sc049_01 5', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 5)
play sfxvoice "avg_vocal_ch25.ogg"
c23 '[textdict[1202117]]'
hide p56
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 4', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1202118]]'
hide p2
$ update_portrait('sc049_01 4', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na04.ogg"
c13 '[textdict[1202119]]'
hide p56
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1202120]]'
return