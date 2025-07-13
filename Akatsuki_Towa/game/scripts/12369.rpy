label avg12369:

play music "ed7124.ogg"
scene avg_bg_059
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
c23 '[textdict[1133845]]'
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
c10961 '[textdict[1133846]]'
hide p2
$ update_portrait('oc001_01 6', 'p1', [r(-2), light], 5)
c13 '[textdict[1133847]]'
hide p1
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 5)
c23 '[textdict[1133848]]'
$ update_portrait('oc002_01 1', 'p2', [r(-3), dark], 5)
c10961 '[textdict[1133849]]'
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1133850]]'
return