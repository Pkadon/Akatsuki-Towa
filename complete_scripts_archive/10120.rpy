label avg10120:

play music "ed7561.ogg"
scene avg_bg_012
$ update_narrator('c0')
window show
with fade_in
play sfx2 "other_7022.ogg"
c0 '[textdict[1123036]]'
play sfx2 "other_7022.ogg"
c7143 '[textdict[1006641]]'
$ update_portrait('st051_01 3', 'p258', [l(-9), light, flip], 6)
play sfx2 "other_7023.ogg"
c2581 '[textdict[1006642]]'
hide p258
play sfx2 "other_7022.ogg"
c0 '[textdict[1123037]]'
scene avg_bg_033
$ update_narrator('c6753')
with fade
play sfx2 "other_7022.ogg"
c6753 '[textdict[1006643]]'
play sfx2 "other_7023.ogg"
c7131 '[textdict[1006644]]'
$ update_portrait('st034_01 2', 'p233', [r(12), light], 5)
c2333 '[textdict[1006645]]'
$ update_portrait('st034_01 2', 'p233', [r(12), dark], 5)
c6771 '[textdict[1006646]]'
hide p233
$ update_portrait('st027_01 5', 'p226', [r(5), light], 5)
play sfx2 "other_7022.ogg"
c2263 '[textdict[1006647]]'
return