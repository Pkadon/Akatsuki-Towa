label avg20086:

play music "ed7106.ogg"
scene avg_bg_013
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
window show
with fade_in
c21 '[textdict[1004469]]'
$ update_portrait('oc002_01 1', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('sc052_01 1', 'p59', [r_entrance(-25), light], 5)
c593 '[textdict[1004470]]'
$ update_portrait('sc052_01 1', 'p59', [r(-25), dark], 5)
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch05.ogg"
c21 '[textdict[1004471]]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1004472]]'
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1004473]]'
hide p59
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('sc053_01 1', 'p60', [r(-32), light], 5)
c603 '[textdict[1004474]]'
hide p60
$ update_portrait('sc052_01 1', 'p59', [r(-25), light], 5)
c593 '[textdict[1004475]]'
$ update_portrait('sc052_01 1', 'p59', [r(-25), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na20.ogg"
c11 '[textdict[1004476]]'
hide p59
$ update_portrait('oc001_01 10', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('sc053_01 5', 'p60', [r(-32), light], 5)
c603 '[textdict[1004477]]'
$ update_portrait('sc053_01 5', 'p60', [r(-32), dark], 5)
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1004478]]'
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('sc053_01 4', 'p60', [r(-32), light], 5)
c603 '[textdict[1004479]]'
hide p1
$ update_portrait('sc053_01 4', 'p60', [r(-32), dark], 5)
$ update_portrait('sc052_01 4', 'p59', [l(-25), light, flip], 6)
c591 '[textdict[1004480]]'
hide p60
$ update_portrait('sc052_01 4', 'p59', [l(-25), dark, flip], 6)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[textdict[1004481]]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('sc052_01 4', 'p59', [l(-25), light, flip], 6)
c591 '[textdict[1004482]]'
$ update_portrait('sc052_01 4', 'p59', [l(-25), light, flip], 6)
c591 '[textdict[1004483]]'
hide p2
$ update_portrait('sc052_01 4', 'p59', [l(-25), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1004484]]'
return