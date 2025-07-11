label avg25803:

scene placeholderbackground
window show
with fade_in
play sfx2 "common_tag_2.ogg"
c0 '[textdict[1211254]]'
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[textdict[1211255]]'
hide p2
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 5)
c13 '[textdict[1211256]]'
hide p1
$ update_portrait('oc002_01 7', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch31.ogg"
c23 '[textdict[1211257]]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[textdict[1211258]]'
return