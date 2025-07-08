label avg1033:
stop music

play music "ed7201.ogg"
scene avg_bg_010
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
window show
with fade_in
c21 '[textdict[2100571]]'
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[2100572]]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc052_01 5', 'p59', [l_entrance(-25), light, flip], 6)
c591 '[textdict[2100573]]'
hide p59
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc052_01 1', 'p59', [l(-25), light, flip], 6)
c591 '[textdict[2100574]]'
hide p59
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc052_01 1', 'p59', [l(-25), light, flip], 6)
c591 '[textdict[2100575]]'
return