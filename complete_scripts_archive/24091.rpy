label avg24091:

play music "ed7105.ogg"
scene placeholderbackground
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
c23 '[textdict[1200329]]'
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
$ update_portrait('st026_01 1', 'p225', [l(-14), light, flip], 6)
c2251 '[textdict[1200330]]'
$ update_portrait('st026_01 1', 'p225', [l(-14), dark, flip], 6)
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 5)
c23 '[textdict[1200331]]'
return