label avg100103:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 5)
window show
with fade_in
play sfxvoice "avg_vocal_na15.ogg"
c13 '[textdict[1218015]]'
hide p1
$ update_portrait('sc001_01 1', 'p9', [mid(-11), light], 5)
c93 '[textdict[1218016]]'
$ update_portrait('sc001_01 2', 'p9', [mid(-11), light], 5)
c93 '[textdict[1218017]]'
$ update_portrait('sc001_01 1', 'p9', [mid(-11), light], 5)
c93 '[textdict[1218018]]'
hide p9
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na06.ogg"
c13 '[textdict[1218019]]'
return