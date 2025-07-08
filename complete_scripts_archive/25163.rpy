label avg25163:
stop music

scene placeholderbackground
window show
with fade_in
play sfx2 "common_tag_2.ogg"
c0 '[textdict[1210534]]'
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 5)
play sfx2 "other_7079.ogg"
play sfxvoice "avg_vocal_na21.ogg"
c13 '[textdict[1210535]]'
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 5)
c23 '[textdict[1210536]]'
return