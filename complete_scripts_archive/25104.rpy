label avg25104:
stop music

scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
window show
with fade_in
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[textdict[1210294]]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na06.ogg"
c13 '[textdict[1210295]]'
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 5)
play sfx2 "common_tag_2.ogg"
c13 '[textdict[1210296]]'
return