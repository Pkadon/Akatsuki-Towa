label avg25083:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 20', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "fight_6024.ogg"
play sfxvoice "bcv_oc001_com_01.ogg"
c13 '[textdict[1210244]]'
return