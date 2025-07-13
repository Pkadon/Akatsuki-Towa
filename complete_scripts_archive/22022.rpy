label avg22022:

play music "ed7105.ogg"
scene placeholderbackground
$ update_portrait('sc049_01 6', 'p56', [mid(-8), light], 5)
$ update_narrator('c563')
window show
with fade_in
play sfx2 "common_select.ogg"
c563 '[textdict[1120010]]'
hide p56
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
play sfx2 "fight_6024.ogg"
play sfxvoice "bcv_oc001_com_01.ogg"
c13 '[textdict[1120011]]'
return